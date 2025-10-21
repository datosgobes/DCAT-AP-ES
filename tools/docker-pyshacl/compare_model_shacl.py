#!/usr/bin/env python3
"""
Compare model properties in docs/index.md against SHACL shapes.
Generates tests/validation-reports/model-vs-shacl-report.md (Markdown table)

Improvements (A, B, C):
 A) Robust Markdown table parser for index.md (accurate Aplicabilidad/Cardinalidad extraction)
 B) Map shapes by sh:targetClass to match entity scopes (separate HVD vs non-HVD checks)
 C) HVD-specific validation: verify minCount>=1 + severity=Violation for HVD-mandatory properties

Checks performed:
 1. Property presence in SHACL shapes (by sh:path + targetClass context)
 2. Severity alignment: Obligatorio → sh:Violation, Recomendado → sh:Warning
 3. Cardinality alignment: documented (1..n, 0..n, 1..1) vs sh:minCount/sh:maxCount
 4. nodeKind extraction (sh:IRI, sh:Literal, sh:BlankNode)
 5. Datatype/class constraints (sh:datatype, sh:class)
 6. HVD compliance: HVD-mandatory properties must have minCount>=1 + severity=Violation

Usage: run from repo root:
  python tools/compare_model_shacl.py

"""
import re
import os
import sys
from collections import defaultdict
from configparser import ConfigParser
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

# Detect if running in Docker (workspace mounted at /workspace) or locally
if os.path.exists('/workspace/docs/index.md'):
    REPO_ROOT = '/workspace'
else:
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DOC_INDEX = os.path.join(REPO_ROOT, 'docs', 'index.md')
SHACL_DIR = os.path.join(REPO_ROOT, 'shacl', '1.0.0')
SHACL_HVD_DIR = os.path.join(REPO_ROOT, 'shacl', '1.0.0', 'hvd')
TEST_INI = os.path.join(REPO_ROOT, 'tests', 'test.ini')
OUT_REPORT = os.path.join(REPO_ROOT, 'tests', 'validation-reports', 'model-vs-shacl-report.md')

SH = Namespace('http://www.w3.org/ns/shacl#')
DCAT = Namespace('http://www.w3.org/ns/dcat#')
DCT = Namespace('http://purl.org/dc/terms/')
FOAF = Namespace('http://xmlns.com/foaf/0.1/')
SPDX = Namespace('http://spdx.org/rdf/terms#')
VCARD = Namespace('http://www.w3.org/2006/vcard/ns#')
ADMS = Namespace('http://www.w3.org/ns/adms#')
PROV = Namespace('http://www.w3.org/ns/prov#')
DCATAP = Namespace('http://data.europa.eu/r5r/')
ODRL = Namespace('http://www.w3.org/ns/odrl/2/')
LOCN = Namespace('http://www.w3.org/ns/locn#')
TIME = Namespace('http://www.w3.org/2006/time#')

# Global configuration dictionaries (loaded from test.ini)
PREFIX_MAP = {}
ENTITY_CLASS_MAP = {}
ENTITY_TO_REUSABLE_SHAPE = {}


def load_config(ini_path):
    """
    Load configuration from test.ini:
    - [prefixes]: namespace prefix to URI mapping
    - [entity_classes]: entity name to RDF class URI mapping
    - [reusable_shapes]: entity URI to reusable shape URI mapping
    """
    global PREFIX_MAP, ENTITY_CLASS_MAP, ENTITY_TO_REUSABLE_SHAPE
    
    # Use RawConfigParser to preserve case sensitivity
    config = ConfigParser()
    config.optionxform = str  # Preserve case for keys
    config.read(ini_path, encoding='utf-8')
    
    # Load prefix mappings
    if config.has_section('prefixes'):
        PREFIX_MAP = dict(config.items('prefixes'))
    
    # Load entity class mappings (convert underscore back to colon)
    if config.has_section('entity_classes'):
        for key, value in config.items('entity_classes'):
            # Convert dcat_Catalog -> dcat:Catalog
            original_key = key.replace('_', ':', 1)
            ENTITY_CLASS_MAP[original_key] = value
    
    # Load reusable shape mappings (entity URI -> list of shape URIs)
    # Format: entitykey = entity_uri | shape_uri1, shape_uri2, ...
    if config.has_section('reusable_shapes'):
        for key, value in config.items('reusable_shapes'):
            if '|' in value:
                parts = value.split('|', 1)
                entity_uri = parts[0].strip()
                shape_uris = [s.strip() for s in parts[1].split(',')]
                ENTITY_TO_REUSABLE_SHAPE[entity_uri] = shape_uris

    print(f"Configuración cargada desde {ini_path}:")
    print(f"  - {len(PREFIX_MAP)} prefijos")
    print(f"  - {len(ENTITY_CLASS_MAP)} clases de entidad")
    print(f"  - {len(ENTITY_TO_REUSABLE_SHAPE)} mapeos de forma reutilizable")


def expand_prefixed(s):
    """Convert prefix:local to full URI."""
    s = s.strip()
    if s.startswith('http://') or s.startswith('https://'):
        return s
    if ':' in s:
        p, local = s.split(':', 1)
        if p in PREFIX_MAP:
            return PREFIX_MAP[p] + local
    return s


def parse_index_md(path):
    """
    Parse docs/index.md to extract properties by entity from detail tables.
    
    Detail tables format:
    | [`dcat:Dataset`](#Dataset) | [`dct:type`](http://purl.org/dc/terms/type) |
    | --- | --- |
    | **Metadato** | **Tipo** |
    | **Descripción** | Categorización del conjunto de datos. |
    | **Propiedad** | [**dct:type**](http://purl.org/dc/terms/type) |
    | **Aplicabilidad** | **Opcional** |
    | **Cardinalidad** | **0..1** |
    | **Rango** | ... |
    
    Returns dict: entity -> list of property dicts
    {prop, metadato, applicability, cardinality, hvd_applicability, hvd_cardinality}
    """
    content = open(path, encoding='utf-8').read()
    lines = content.splitlines()
    entities = defaultdict(list)
    
    current_entity = None
    in_table = False
    
    print(f"Parseando {path}...")
    print(f"Total de líneas: {len(lines)}")
    print(f"Entidades a buscar: {list(ENTITY_CLASS_MAP.keys())}")
    
    for i, line in enumerate(lines):
        # Detect detail table header: | [Entity](#Entity) | [dct:property](URI) |
        # Example: | [`dcat:Dataset`](#Dataset) | [`dct:type`](http://purl.org/dc/terms/type) |
        # Must have exactly 2 data columns to avoid matching vocabulary reference tables (which have 4 columns)
        pipe_count = line.count('|')
        
        # Property detail tables have format: | data | data | (3 pipes)
        # Vocabulary tables have: | data | data | data | data | (5 pipes)
        if pipe_count == 3:
            m_detail_header = re.search(r'\|\s*\[`?([a-zA-Z0-9_:]+)`?\]\(#([a-zA-Z0-9_:]+)\)\s*\|\s*\[`?([a-zA-Z0-9_:]+)`?\]\((http[^\)]+)\)\s*\|', line)
        else:
            m_detail_header = None
        
        if m_detail_header:
            entity_from_link = m_detail_header.group(1)  # Get namespace:Entity format
            prop_uri = m_detail_header.group(4)
            
            if entity_from_link in ENTITY_CLASS_MAP:
                current_entity = entity_from_link
                in_table = True
                
                # Extract applicability and cardinality from next lines in the table
                applicability = None
                cardinality = None
                hvd_applicability = None
                hvd_cardinality = None
                
                # Look ahead for Aplicabilidad and Cardinalidad rows
                for j in range(i+1, min(i+10, len(lines))):
                    future_line = lines[j]
                    
                    # Stop if we hit another table header (starts with | [ and has link format)
                    if future_line.strip().startswith('| ['):
                        break
                    
                    # Stop at blank line or new section
                    if future_line.strip() == '' or future_line.startswith('## ') or future_line.startswith('!!!'):
                        break
                    
                    # Extract Aplicabilidad (handles "Recomendado - Sí es HVD: Obligatorio")
                    if '**Aplicabilidad**' in future_line:
                        # Check for HVD-specific format first (look for " - " separator followed by HVD indicator)
                        if ' - ' in future_line and 'HVD' in future_line:
                            # Format: "Recomendado - Sí es HVD: Obligatorio"
                            # Split on " - " to get base part
                            parts = future_line.split(' - ', 1)
                            if len(parts) == 2:
                                # Base applicability (before " - ")
                                base_part = parts[0]
                                if 'Obligatorio' in base_part:
                                    applicability = 'Obligatorio'
                                elif 'Recomendado' in base_part:
                                    applicability = 'Recomendado'
                                elif 'Opcional' in base_part:
                                    applicability = 'Opcional'
                                
                                # HVD applicability (after "Sí es HVD:" or "HVD:")
                                hvd_part = parts[1]
                                # Look for the colon after HVD indicator
                                if ':' in hvd_part:
                                    hvd_text = hvd_part.split(':', 1)[-1]
                                    if 'Obligatorio' in hvd_text:
                                        hvd_applicability = 'Obligatorio'
                                    elif 'Recomendado' in hvd_text:
                                        hvd_applicability = 'Recomendado'
                                    elif 'Opcional' in hvd_text:
                                        hvd_applicability = 'Opcional'
                        else:
                            # Standard format (no HVD distinction)
                            if 'Obligatorio' in future_line:
                                applicability = 'Obligatorio'
                            elif 'Recomendado' in future_line:
                                applicability = 'Recomendado'
                            elif 'Opcional' in future_line:
                                applicability = 'Opcional'
                    
                    # Extract Cardinalidad (handles "0..n - Sí es HVD: 1..n")
                    if '**Cardinalidad**' in future_line:
                        # Check for HVD-specific format first
                        if ' - ' in future_line and 'HVD' in future_line:
                            # Format: "0..n - Sí es HVD: 1..n"
                            parts = future_line.split(' - ', 1)
                            if len(parts) == 2:
                                # Base cardinality
                                m_card = re.search(r'([\d]+\.\.[\dn]+)', parts[0])
                                if m_card:
                                    cardinality = m_card.group(1)
                                
                                # HVD cardinality
                                hvd_part = parts[1]
                                if ':' in hvd_part:
                                    hvd_text = hvd_part.split(':', 1)[-1]
                                    m_hvd_card = re.search(r'([\d]+\.\.[\dn]+)', hvd_text)
                                    if m_hvd_card:
                                        hvd_cardinality = m_hvd_card.group(1)
                        else:
                            # Standard format (no HVD distinction)
                            m_card = re.search(r'([\d]+\.\.[\dn]+)', future_line)
                            if m_card:
                                cardinality = m_card.group(1)
                
                # Extract property name from URI (last part after # or /)
                prop_name = prop_uri.split('/')[-1].split('#')[-1]
                
                entities[current_entity].append({
                    'prop': prop_uri,
                    'metadato': prop_name,
                    'applicability': applicability,
                    'cardinality': cardinality,
                    'hvd_applicability': hvd_applicability,
                    'hvd_cardinality': hvd_cardinality,
                })
    
    # Print summary of parsed properties
    total_props = sum(len(props) for props in entities.values())
    print(f"Propiedades encontradas por entidad:")
    for entity, props in entities.items():
        print(f"  {entity}: {len(props)} propiedades")
    print(f"Total de propiedades parseadas: {total_props}")
    
    return entities


def index_shacl_shapes(shacl_dir, hvd_dir):
    """
    Load SHACL graphs and index property shapes by targetClass and path.
    Improved (B): map shapes by sh:targetClass to distinguish entity scopes and HVD vs non-HVD.
    Improved (D): detect reusable shapes (no targetClass) and index them separately
    
    Returns: (base_index, hvd_index, reusable_shapes)
      base_index[target_class][prop_path] -> list of shape entries
      hvd_index[target_class][prop_path] -> list of shape entries
      reusable_shapes[shape_uri][prop_path] -> list of shape entries (for sh:node references)
    """
    def index_dir(d, is_hvd=False):
        idx = defaultdict(lambda: defaultdict(list))
        reusable_idx = defaultdict(lambda: defaultdict(list))
        if not os.path.isdir(d):
            return idx, reusable_idx
        
        files = [os.path.join(d, fn) for fn in os.listdir(d) if fn.endswith('.ttl') or fn.endswith('.shacl')]
        g = Graph()
        for f in files:
            try:
                g.parse(f, format='turtle')
            except Exception as e:
                try:
                    g.parse(f, format='n3')
                except Exception:
                    print(f"Advertencia: no se pudo analizar {f}: {e}", file=sys.stderr)
                    continue
        
        # Map NodeShapes by targetClass
        node_shapes_map = {}
        reusable_shapes = {}  # Shapes without targetClass but with properties (e.g., Agent_Shape)
        for ns in g.subjects(RDF.type, SH.NodeShape):
            has_target = False
            for tc in g.objects(ns, SH.targetClass):
                tc_uri = str(tc)
                node_shapes_map[str(ns)] = tc_uri
                has_target = True
            
            # If no targetClass but has sh:property, it's a reusable shape (e.g., Agent_Shape)
            if not has_target:
                for _ in g.objects(ns, SH.property):
                    reusable_shapes[str(ns)] = True
                    break
        
        def extract_path(o):
            if isinstance(o, URIRef):
                return str(o)
            try:
                for first_o in g.objects(o, RDF.first):
                    return str(first_o) if isinstance(first_o, URIRef) else str(first_o)
            except Exception:
                pass
            return str(o)
        
        def build_entry(shape, file_path):
            entry = {'shape': str(shape), 'file': os.path.basename(file_path), 'is_hvd': is_hvd}
            sev = None
            # Try both sh:severity and sh:resultSeverity
            for o in g.objects(shape, SH.severity):
                sev = str(o)
                break
            if not sev:
                for o in g.objects(shape, SH.resultSeverity):
                    sev = str(o)
                    break
            entry['severity'] = sev
            minc = None
            for o in g.objects(shape, SH.minCount):
                try:
                    minc = int(str(o))
                except Exception:
                    pass
            maxc = None
            for o in g.objects(shape, SH.maxCount):
                try:
                    maxc = int(str(o))
                except Exception:
                    pass
            entry['minCount'] = minc
            entry['maxCount'] = maxc
            nk = None
            for o in g.objects(shape, SH.nodeKind):
                nk = str(o)
            entry['nodeKind'] = nk
            dt = None
            for o in g.objects(shape, SH.datatype):
                dt = str(o)
            clz = None
            for o in g.objects(shape, SH['class']):
                clz = str(o)
            entry['datatype'] = dt
            entry['class'] = clz
            return entry
        
        # 1) Explicit PropertyShape nodes
        for ps in g.subjects(RDF.type, SH.PropertyShape):
            path = None
            for o in g.objects(ps, SH.path):
                path = extract_path(o)
                break
            if not path:
                continue
            
            target_class = 'UNKNOWN'
            for parent in g.subjects(SH.property, ps):
                if str(parent) in node_shapes_map:
                    target_class = node_shapes_map[str(parent)]
                    break
            
            entry = build_entry(ps, f)
            idx[target_class][path].append(entry)
        
        # 2) NodeShapes with sh:property
        for ns in g.subjects(RDF.type, SH.NodeShape):
            tc = 'UNKNOWN'
            has_target = False
            for tc_obj in g.objects(ns, SH.targetClass):
                tc = str(tc_obj)
                has_target = True
                break
            
            for prop in g.objects(ns, SH.property):
                path = None
                for o in g.objects(prop, SH.path):
                    path = extract_path(o)
                    break
                if not path:
                    continue
                
                entry = build_entry(prop, f)
                # If severity not on prop, check ns
                if not entry['severity']:
                    for o in g.objects(ns, SH.resultSeverity):
                        entry['severity'] = str(o)
                
                # If has targetClass, index by targetClass
                if has_target:
                    idx[tc][path].append(entry)
                else:
                    # If no targetClass, it's a reusable shape - index by shape URI
                    reusable_idx[str(ns)][path].append(entry)
        
        return idx, reusable_idx
    
    base_idx, base_reusable = index_dir(shacl_dir, is_hvd=False)
    hvd_idx, hvd_reusable = index_dir(hvd_dir, is_hvd=True)
    
    # Merge reusable shapes
    all_reusable = {}
    all_reusable.update(base_reusable)
    all_reusable.update(hvd_reusable)
    
    return base_idx, hvd_idx, all_reusable


def merge_shape_entries(shapes):
    """
    Merge multiple SHACL property shape entries for the same property.
    Takes the best values from all shapes (e.g., if one has minCount and another has severity).
    
    IMPORTANT: For cardinality constraints (minCount/maxCount), we preserve
    the severity from the shape that defines that specific constraint.
    """
    if not shapes:
        return None
    if len(shapes) == 1:
        return shapes[0]
    
    merged = dict(shapes[0])
    
    # Track severity associated with cardinality constraints
    mincount_severity = merged.get('severity') if merged.get('minCount') is not None else None
    maxcount_severity = merged.get('severity') if merged.get('maxCount') is not None else None
    
    # Merge attributes from remaining shapes
    for shape in shapes[1:]:
        # Keep non-None values; if first entry has None, take from next
        if not merged.get('severity') and shape.get('severity'):
            merged['severity'] = shape.get('severity')
        
        # Track severity from the shape that provides minCount
        if merged.get('minCount') is None and shape.get('minCount') is not None:
            merged['minCount'] = shape.get('minCount')
            mincount_severity = shape.get('severity')
        
        # Track severity from the shape that provides maxCount
        if merged.get('maxCount') is None and shape.get('maxCount') is not None:
            merged['maxCount'] = shape.get('maxCount')
            maxcount_severity = shape.get('severity')
            
        if not merged.get('nodeKind') and shape.get('nodeKind'):
            merged['nodeKind'] = shape.get('nodeKind')
        if not merged.get('datatype') and shape.get('datatype'):
            merged['datatype'] = shape.get('datatype')
        if not merged.get('class') and shape.get('class'):
            merged['class'] = shape.get('class')
    
    # Store cardinality-specific severities for later comparison
    if mincount_severity:
        merged['minCount_severity'] = mincount_severity
    if maxcount_severity:
        merged['maxCount_severity'] = maxcount_severity
    
    return merged


def compare_properties(model, base_idx, hvd_idx, reusable_shapes):
    """
    Compare model properties against SHACL shapes.
    Improved (C): HVD-specific checks for compliance.
    Improved (D): Check reusable shapes (e.g., Agent_Shape for foaf:Agent properties)
    
    Returns list of comparison results (dict per property).
    
    Note: ENTITY_TO_REUSABLE_SHAPE is loaded from test.ini [reusable_shapes] section
    """
    results = []
    
    for entity, props in model.items():
        entity_uri = ENTITY_CLASS_MAP.get(entity)
        if not entity_uri:
            continue
        
        for p in props:
            prop_uri = p['prop']
            applicability = (p.get('applicability') or '').strip()
            cardinality = (p.get('cardinality') or '').strip()
            hvd_applicability = (p.get('hvd_applicability') or '').strip()
            hvd_cardinality = (p.get('hvd_cardinality') or '').strip()
            
            # Search in base shapes
            base_shapes = base_idx.get(entity_uri, {}).get(prop_uri, [])
            # Search in HVD shapes
            hvd_shapes = hvd_idx.get(entity_uri, {}).get(prop_uri, [])
            
            # If not found in targetClass-based shapes, check reusable shapes
            if not base_shapes and not hvd_shapes:
                potential_shape_uris = ENTITY_TO_REUSABLE_SHAPE.get(entity_uri, [])
                for shape_uri in potential_shape_uris:
                    if shape_uri in reusable_shapes:
                        reusable_props = reusable_shapes[shape_uri].get(prop_uri, [])
                        if reusable_props:
                            base_shapes = reusable_props
                            break
            
            result = {
                'entity': entity,
                'entity_uri': entity_uri,
                'prop': prop_uri,
                'metadato': p.get('metadato', ''),
                'doc_applicability': applicability,
                'doc_cardinality': cardinality,
                'hvd_applicability': hvd_applicability,
                'hvd_cardinality': hvd_cardinality,
                'base_shapes': base_shapes,
                'hvd_shapes': hvd_shapes,
                'issues': [],
                'status': 'OK',
            }
            
            # Check 1: Property presence
            if not base_shapes and not hvd_shapes:
                result['status'] = 'MISSING'
                result['issues'].append('Propiedad sin forma SHACL')
                # Mark as CRITICAL only if it's Obligatorio (mandatory)
                if applicability and 'oblig' in applicability.lower():
                    result['status'] = 'CRITICAL'
                    result['issues'][0] = 'CRITICAL: Propiedad OBLIGATORIA sin forma SHACL'
                results.append(result)
                continue
            
            # Analyze base shape: merge multiple entries if they exist
            shape = merge_shape_entries(base_shapes)
            hvd_shape = merge_shape_entries(hvd_shapes)
            
            if shape:
                # Check 2: Severity alignment for BASE (non-HVD)
                # Use minCount_severity if available, otherwise general severity
                severity = shape.get('minCount_severity') if shape.get('minCount') is not None else shape.get('severity', '')
                
                if applicability:
                    app_lower = applicability.lower()
                    if 'oblig' in app_lower or 'mandatory' in app_lower:
                        if not severity or 'Violation' not in severity:
                            result['issues'].append(f"Doc base: Obligatorio, pero severidad SHACL base es {severity or 'not set'}")
                            result['status'] = 'WARN'
                    elif 'recomend' in app_lower or 'recommend' in app_lower:
                        # For Recomendado: Warning is correct, Violation would be inconsistent
                        # But only check if we have a minCount (cardinality constraint)
                        if shape.get('minCount') is not None:
                            if severity and 'Violation' in severity:
                                result['issues'].append(f"Doc base: Recomendado, pero severidad SHACL base es Violation")
                                result['status'] = 'WARN'
                
                # Check 3: Cardinality alignment for BASE (non-HVD)
                min_count = shape.get('minCount')
                max_count = shape.get('maxCount')
                if cardinality:
                    # Extract min from cardinality (e.g., "0..n" -> 0, "1..1" -> 1)
                    card_min = int(cardinality.split('..')[0]) if '..' in cardinality else None
                    card_max_str = cardinality.split('..')[-1] if '..' in cardinality else None
                    card_max = int(card_max_str) if card_max_str and card_max_str.isdigit() else None
                    
                    # Only validate if both have values
                    if card_min is not None and min_count is not None:
                        if card_min != min_count:
                            result['issues'].append(f"Doc base: cardinalidad min={card_min}, pero SHACL base minCount={min_count}")
                            result['status'] = 'WARN'
                    
                    if card_max is not None and max_count is not None:
                        if card_max != max_count:
                            result['issues'].append(f"Doc base: cardinalidad max={card_max}, pero SHACL base maxCount={max_count}")
                            result['status'] = 'WARN'
            
            # Check C: HVD compliance (informational, not blocking)
            if hvd_applicability or hvd_cardinality:
                if hvd_applicability:
                    hvd_app_lower = hvd_applicability.lower()
                    if 'oblig' in hvd_app_lower or 'mandatory' in hvd_app_lower:
                        # HVD-mandatory: SHOULD have HVD shape with minCount>=1 and severity=Violation
                        if not hvd_shape:
                            result['issues'].append('INFO: Doc HVD obligatorio pero no hay forma SHACL HVD')
                            if result['status'] == 'OK':
                                result['status'] = 'INFO'
                        else:
                            hvd_sev = hvd_shape.get('severity', '')
                            hvd_min = hvd_shape.get('minCount')
                            if not hvd_sev or 'Violation' not in hvd_sev:
                                result['issues'].append(f'INFO: Doc HVD obligatorio pero severidad SHACL HVD es {hvd_sev or "not set"}')
                                if result['status'] == 'OK':
                                    result['status'] = 'INFO'
                            if not hvd_min or hvd_min < 1:
                                result['issues'].append(f'INFO: Doc HVD obligatorio pero SHACL HVD minCount={hvd_min}')
                                if result['status'] == 'OK':
                                    result['status'] = 'INFO'
                    elif 'recomend' in hvd_app_lower or 'recommend' in hvd_app_lower:
                        if hvd_shape:
                            hvd_sev = hvd_shape.get('severity', '')
                            if hvd_sev and 'Violation' in hvd_sev:
                                result['issues'].append(f'INFO: Doc HVD recomendado pero severidad SHACL HVD es Violation')
                                if result['status'] == 'OK':
                                    result['status'] = 'INFO'
                
                # HVD Cardinality check
                if hvd_cardinality and hvd_shape:
                    hvd_min = hvd_shape.get('minCount')
                    hvd_max = hvd_shape.get('maxCount')
                    
                    # Extract min/max from HVD cardinality
                    hvd_card_min = int(hvd_cardinality.split('..')[0]) if '..' in hvd_cardinality else None
                    hvd_card_max_str = hvd_cardinality.split('..')[-1] if '..' in hvd_cardinality else None
                    hvd_card_max = int(hvd_card_max_str) if hvd_card_max_str and hvd_card_max_str.isdigit() else None
                    
                    if hvd_card_min is not None and hvd_min is not None:
                        if hvd_card_min != hvd_min:
                            result['issues'].append(f'INFO: Doc HVD cardinalidad min={hvd_card_min}, pero SHACL HVD minCount={hvd_min}')
                            if result['status'] == 'OK':
                                result['status'] = 'INFO'
                    
                    if hvd_card_max is not None and hvd_max is not None:
                        if hvd_card_max != hvd_max:
                            result['issues'].append(f'INFO: Doc HVD cardinalidad max={hvd_card_max}, pero SHACL HVD maxCount={hvd_max}')
                            if result['status'] == 'OK':
                                result['status'] = 'INFO'
            
            results.append(result)
    
    return results


def generate_markdown_report(results, output_file):
    """Generate Markdown table report with summary by entity."""
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    total = len(results)
    ok = sum(1 for r in results if r['status'] == 'OK')
    warn = sum(1 for r in results if r['status'] == 'WARN')
    missing = sum(1 for r in results if r['status'] == 'MISSING')
    info = sum(1 for r in results if r['status'] == 'INFO')
    critical = sum(1 for r in results if r['status'] == 'CRITICAL')
    
    with open(output_file, 'w', encoding='utf-8') as fh:
        fh.write('# Modelo vs SHACL - Informe de Comparación\n\n')
        fh.write(f'Generado: `{os.path.basename(__file__)}`\n\n')
        fh.write('## Resumen Ejecutivo\n\n')
        fh.write(f'- **Total propiedades analizadas**: {total}\n')
        fh.write(f'- ✅ **OK**: {ok}\n')
        fh.write(f'- ⚠️ **WARN**: {warn} (no bloqueante)\n')
        fh.write(f'- ❔ **MISSING**: {missing}\n')
        fh.write(f'- ℹ️ **INFO**: {info} (HVD - no bloqueante)\n')
        fh.write(f'- ❌ **CRITICAL**: {critical} (Propiedades OBLIGATORIAS sin SHACL)\n\n')
        
        if critical > 0:
            fh.write('❌ **ERROR BLOQUEANTE**: Propiedades OBLIGATORIAS del modelo no tienen formas SHACL correspondientes.\n\n')
        else:
            fh.write('✅ **Validación exitosa**: Todas las propiedades OBLIGATORIAS tienen formas SHACL.\n\n')
        
        # Group by entity
        by_entity = defaultdict(list)
        for r in results:
            by_entity[r['entity']].append(r)
        
        for entity in sorted(by_entity.keys()):
            fh.write(f'## {entity}\n\n')
            fh.write('| Propiedad | Doc App Base | Doc Card Base | Doc App HVD | Doc Card HVD | SHACL Sev Base | SHACL minC Base | SHACL maxC Base | SHACL Sev HVD | SHACL minC HVD | SHACL maxC HVD | Status | Notas |\n')
            fh.write('|-----------|--------------|---------------|-------------|--------------|----------------|-----------------|-----------------|---------------|----------------|----------------|--------|-------|\n')
            
            for r in sorted(by_entity[entity], key=lambda x: x['prop']):
                prop_short = r['prop'].replace('http://purl.org/dc/terms/', 'dct:') \
                    .replace('http://www.w3.org/ns/dcat#', 'dcat:') \
                    .replace('http://xmlns.com/foaf/0.1/', 'foaf:') \
                    .replace('http://www.w3.org/2006/vcard/ns#', 'vcard:') \
                    .replace('http://www.w3.org/ns/adms#', 'adms:') \
                    .replace('http://spdx.org/rdf/terms#', 'spdx:') \
                    .replace('http://data.europa.eu/r5r/', 'dcatap:') \
                    .replace('http://www.w3.org/ns/prov#', 'prov:') \
                    .replace('http://www.w3.org/ns/odrl/2/', 'odrl:') \
                    .replace('http://www.w3.org/ns/locn#', 'locn:') \
                    .replace('http://www.w3.org/2006/time#', 'time:')
                
                # Base documentation
                doc_app_base = r['doc_applicability'] or '-'
                doc_card_base = r['doc_cardinality'] or '-'
                
                # HVD documentation
                doc_app_hvd = r['hvd_applicability'] or '-'
                doc_card_hvd = r['hvd_cardinality'] or '-'
                
                # Base SHACL
                base_shape = merge_shape_entries(r['base_shapes']) if r['base_shapes'] else None
                # Use minCount_severity if available (for cardinality constraints), otherwise general severity
                if base_shape and base_shape.get('minCount') is not None and base_shape.get('minCount_severity'):
                    shacl_sev_base = base_shape['minCount_severity'].replace('http://www.w3.org/ns/shacl#', 'sh:')
                else:
                    shacl_sev_base = base_shape['severity'].replace('http://www.w3.org/ns/shacl#', 'sh:') if base_shape and base_shape.get('severity') else '-'
                shacl_min_base = str(base_shape['minCount']) if base_shape and base_shape.get('minCount') is not None else '-'
                shacl_max_base = str(base_shape['maxCount']) if base_shape and base_shape.get('maxCount') is not None else '-'
                
                # HVD SHACL
                hvd_shape = merge_shape_entries(r['hvd_shapes']) if r['hvd_shapes'] else None
                # Use minCount_severity if available (for cardinality constraints), otherwise general severity
                if hvd_shape and hvd_shape.get('minCount') is not None and hvd_shape.get('minCount_severity'):
                    shacl_sev_hvd = hvd_shape['minCount_severity'].replace('http://www.w3.org/ns/shacl#', 'sh:')
                else:
                    shacl_sev_hvd = hvd_shape['severity'].replace('http://www.w3.org/ns/shacl#', 'sh:') if hvd_shape and hvd_shape.get('severity') else '-'
                shacl_min_hvd = str(hvd_shape['minCount']) if hvd_shape and hvd_shape.get('minCount') is not None else '-'
                shacl_max_hvd = str(hvd_shape['maxCount']) if hvd_shape and hvd_shape.get('maxCount') is not None else '-'
                
                status_icon = {
                    'OK': '✅',
                    'WARN': '⚠️',
                    'MISSING': '❌',
                    'INFO': 'ℹ️',
                    'CRITICAL': '🚨'
                }.get(r['status'], '')
                
                issues_str = '; '.join(r['issues']) if r['issues'] else ''
                
                fh.write(f'| `{prop_short}` | {doc_app_base} | {doc_card_base} | {doc_app_hvd} | {doc_card_hvd} | {shacl_sev_base} | {shacl_min_base} | {shacl_max_base} | {shacl_sev_hvd} | {shacl_min_hvd} | {shacl_max_hvd} | {status_icon} {r["status"]} | {issues_str} |\n')
            
            fh.write('\n')
        
        # Critical issues section (only mandatory properties missing SHACL)
        if critical > 0:
            fh.write('## 🚨 Propiedades OBLIGATORIAS sin SHACL (Bloqueante)\n\n')
            for r in results:
                if r['status'] == 'CRITICAL':
                    fh.write(f'### {r["entity"]} - `{r["prop"]}`\n\n')
                    fh.write(f'- **Metadato**: {r["metadato"]}\n')
                    fh.write(f'- **Aplicabilidad**: {r["doc_applicability"]}\n')
                    fh.write(f'- **Cardinalidad**: {r["doc_cardinality"]}\n')
                    for issue in r['issues']:
                        fh.write(f'- {issue}\n')
                    fh.write('\n')
        
        # HVD informational issues
        hvd_issues = [r for r in results if r['status'] == 'INFO']
        if hvd_issues:
            fh.write('## ℹ️ Recomendaciones HVD (No bloqueante)\n\n')
            fh.write('Las siguientes propiedades HVD-mandatory deberían tener constraints específicos en shapes HVD:\n\n')
            for r in hvd_issues:
                fh.write(f'- **{r["entity"]}** - `{r["prop"]}`: {"; ".join(r["issues"])}\n')
    
    print(f'Generado informe Markdown: {output_file}')


def main():
    print('Cargando configuración del test.ini...')
    load_config(TEST_INI)
    
    print('Parseando docs/index.md...')
    model = parse_index_md(DOC_INDEX)

    print('Indexando formas SHACL (base + HVD)...')
    base_idx, hvd_idx, reusable_shapes = index_shacl_shapes(SHACL_DIR, SHACL_HVD_DIR)

    print('Comparando propiedades...')
    results = compare_properties(model, base_idx, hvd_idx, reusable_shapes)

    print('Generando informes...')
    generate_markdown_report(results, OUT_REPORT)
    
    # Note: Summary is generated by validate-local.sh as part of Phase 3 (all phases combined)
    
    # Exit code: 0 if no CRITICAL (mandatory properties missing SHACL), 1 otherwise
    critical = sum(1 for r in results if r['status'] == 'CRITICAL')
    warn = sum(1 for r in results if r['status'] == 'WARN')
    info = sum(1 for r in results if r['status'] == 'INFO')
    
    if critical > 0:
        print(f'\n🚨 ERROR: {critical} propiedades OBLIGATORIAS sin formas SHACL')
        print(f'ℹ️  Advertencias: {warn} WARN, {info} INFO (no bloqueantes)')
        sys.exit(1)
    else:
        print('\n✅ Validación exitosa: todas las propiedades OBLIGATORIAS tienen SHACL')
        if warn > 0 or info > 0:
            print(f'ℹ️  Advertencias informativas: {warn} WARN, {info} INFO (no bloqueantes)')
        sys.exit(0)


if __name__ == '__main__':
    main()
