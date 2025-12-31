# Ontología formal de DCAT-AP-ES

## Objetivo

Definir una ontología RDF que describa de manera formal el perfil de aplicación [DCAT-AP-ES](https://datosgobes.github.io/DCAT-AP-ES/) y sus [convenciones](https://datosgobes.github.io/DCAT-AP-ES/convenciones/). La ontología debe aportar:

- URIs dereferenciables que ofrezcan RDF y HTML mediante negociación de contenido.
- Metadatos homogéneos sobre contexto, entidades, propiedades y normativa.
- Reglas procesables por máquinas para validación y trazabilidad.

## Propuestas

### Namespaces

```turtle
@prefix dcatapes: <http://datos.gob.es/def/dcat-ap-es#> .
@prefix dcatapesconv: <https://datos.gob.es/def/dcat-ap-es/convenciones#> .
```

## Ontología base [DCAT-AP-ES](https://datosgobes.github.io/DCAT-AP-ES/)
**TODO**

## Ontología de [convenciones](https://datosgobes.github.io/DCAT-AP-ES/convenciones/)
### Clase principal: Convention

```turtle
dcatapesconv:Convention a owl:Class ;
    rdfs:label "Convención DCAT-AP-ES"@es ;
    rdfs:label "DCAT-AP-ES Convention"@en ;
    rdfs:comment "Una convención que modifica o extiende el perfil base DCAT-AP-ES"@es ;
    rdfs:comment "A convention that modifies or extends the base DCAT-AP-ES profile"@en ;
    dct:conformsTo <https://datosgobes.github.io/DCAT-AP-ES/conventions/> ;
```

### Propiedades

```turtle
# Identificador numérico
dcatapesconv:conventionNumber a owl:DatatypeProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range xsd:integer .

# Título
dcatapesconv:title a owl:DatatypeProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range rdfs:Literal .

# Descripción
dcatapesconv:description a owl:DatatypeProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range rdfs:Literal .

# Contexto de aplicación (HVD, NSIP/ERPD, Geo, Stat, etc.)
dcatapesconv:appliesInContext a owl:ObjectProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range dcatapesconv:ApplicationContext .

# Entidades afectadas
dcatapesconv:affectsEntity a owl:ObjectProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range rdfs:Class .

# Propiedades afectadas
dcatapesconv:affectsProperty a owl:ObjectProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range rdf:Property .

# Tipo de modificación
dcatapesconv:modificationType a owl:ObjectProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range dcatapesconv:ModificationType .

# Normativa de referencia
dcatap:applicableLegislation eli:LegalResource .

# Estado
adms:status a owl:ObjectProperty ;
    rdfs:domain dcatapesconv:Convention ;
    rdfs:range skos:Concept .  # COMPLETED, DEPRECATED, DRAFT
```

### Tipos de modificación

```turtle
dcatapesconv:ModificationType a owl:Class ;
    rdfs:label "Tipo de modificación"@es .

dcatapesconv:CardinalityChange a dcatapesconv:ModificationType ;
    rdfs:label "Cambio de cardinalidad"@es .

dcatapesconv:ApplicabilityChange a dcatapesconv:ModificationType ;
    rdfs:label "Cambio de aplicabilidad"@es .

dcatapesconv:RangeRestriction a dcatapesconv:ModificationType ;
    rdfs:label "Restricción de rango"@es .

dcatapesconv:NewProperty a dcatapesconv:ModificationType ;
    rdfs:label "Nueva propiedad"@es .

dcatapesconv:RelationalConstraint a dcatapesconv:ModificationType ;
    rdfs:label "Restricción relacional"@es .
```

### Contextos de aplicación

```turtle
dcatapesconv:ApplicationContext a owl:Class ;
    rdfs:label "Contexto de aplicación"@es .

dcatapesconv:BaseContext a dcatapesconv:ApplicationContext ;
    rdfs:label "Contexto base"@es .

dcatapesconv:HVDContext a dcatapesconv:ApplicationContext ;
    rdfs:label "High Value Datasets (HVD)"@es ;
    dcatap:applicableLegislation <http://data.europa.eu/eli/reg_impl/2023/138/oj> .

dcatapesconv:NSIPContext a dcatapesconv:ApplicationContext ;
    rdfs:label "Single Information Point (NSIP)"@es ;
    dcatap:applicableLegislation <http://data.europa.eu/eli/reg/2022/868/oj> .
```

## Ejemplo: Convención 11 (HVD)

```turtle
@prefix dcatapesconv: <https://datos.gob.es/def/dcat-ap-es/conventions#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcatap: <http://data.europa.eu/r5r/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix eli: <http://data.europa.eu/eli/ontology#> .

dcatapesconv:convencion-11 a dcatapesconv:Convention ;
    dcatapesconv:conventionNumber 11 ;
    dct:title "Conjunto de datos de alto valor (HVD)"@es ;
    dct:title "High Value Dataset (HVD)"@en ;
    dct:description """Los conjuntos de datos catalogados como de alto valor deben incluir 
        propiedades adicionales obligatorias según el Reglamento 2023/138."""@es ;
    dcatapesconv:appliesInContext dcatapesconv:HVDContext ;
    dcatap:applicableLegislation <http://data.europa.eu/eli/reg_impl/2023/138/oj> ;
    adms:status <http://publications.europa.eu/resource/authority/distribution-status/COMPLETED> ;
    
    # Afecta a Dataset
    dcatapesconv:affectsEntity dcat:Dataset ;
    dcatapesconv:affectsProperty dcatap:hvdCategory ;
    dcatapesconv:affectsProperty dcatap:applicableLegislation ;
    dcatapesconv:affectsProperty dcat:distribution ;
    
    # Afecta a Distribution
    dcatapesconv:affectsEntity dcat:Distribution ;
    dcatapesconv:affectsProperty dcatap:applicableLegislation ;
    dcatapesconv:affectsProperty dcat:accessURL ;
    dcatapesconv:affectsProperty dcat:downloadURL ;
    
    # Afecta a DataService
    dcatapesconv:affectsEntity dcat:DataService ;
    dcatapesconv:affectsProperty dcatap:hvdCategory ;
    dcatapesconv:affectsProperty dcatap:applicableLegislation ;
    
    # Tipos de modificaciones aplicadas
    dcatapesconv:modificationType dcatapesconv:ApplicabilityChange ;
    dcatapesconv:modificationType dcatapesconv:CardinalityChange .
```

## Ejemplo: Convención 12 (HVD - DataService)

```turtle
dcatapesconv:convencion-12 a dcatapesconv:Convention ;
    dcatapesconv:conventionNumber 12 ;
    dct:title "Servicio de datos para HVD"@es ;
    dct:description """Todo Dataset HVD debe tener al menos un DataService asociado 
        que permita el acceso a sus Distributions."""@es ;
    dcatapesconv:appliesInContext dcatapesconv:HVDContext ;
    dcatap:applicableLegislation <http://data.europa.eu/eli/reg_impl/2023/138/oj> ;
    adms:status <http://publications.europa.eu/resource/authority/distribution-status/COMPLETED> ;
    
    # Es una restricción relacional
    dcatapesconv:modificationType dcatapesconv:RelationalConstraint ;
    
    # Afecta a las relaciones entre entidades
    dcatapesconv:affectsEntity dcat:Dataset ;
    dcatapesconv:affectsEntity dcat:DataService ;
    dcatapesconv:affectsProperty dcat:servesDataset ;
    
    # Expresada como regla SHACL (opcional)
    dcatapesconv:shaclRule """
        @prefix sh: <http://www.w3.org/ns/shacl#> .
        @prefix dcat: <http://www.w3.org/ns/dcat#> .
        
        # Todo Dataset HVD debe tener al menos un DataService
        [] a sh:NodeShape ;
            sh:targetClass dcat:Dataset ;
            sh:condition [
                sh:property [
                    sh:path dcatap:hvdCategory ;
                    sh:minCount 1 ;
                ]
            ] ;
            sh:property [
                sh:path [ sh:inversePath dcat:servesDataset ] ;
                sh:minCount 1 ;
                sh:class dcat:DataService ;
            ] .
    """^^sh:SPARQLRule .
```