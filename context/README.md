# DCAT-AP-ES JSON-LD Context

Este directorio contiene el contexto JSON-LD de [DCAT-AP-ES](https://datosgobes.github.io/DCAT-AP-ES/), que consolida la especificación del modelo con los metadatos del perfil de aplicación.

## Archivo principal

- `dcat-ap-es-context.jsonld`: contexto completo con todas las entidades, propiedades y restricciones.

## Propósito

El archivo actúa como fuente única de verdad y reúne:

1. Modelo base (entidades y propiedades)
2. Restricciones SHACL (cardinalidad y tipos)
3. Niveles de aplicabilidad (RFC 2119)
4. Variantes de contexto (HVD, NSIP/ERPD)
5. Referencias a las convenciones vigentes

## Estructura

### Namespaces declarados

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "adms": "http://www.w3.org/ns/adms#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "eli": "http://data.europa.eu/eli/ontology#",
    "spdx": "http://spdx.org/rdf/terms#",
    "prov": "http://www.w3.org/ns/prov#",
    "time": "http://www.w3.org/2006/time#",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "sh": "http://www.w3.org/ns/shacl#",
    "dcatapes": "http://datos.gob.es/def/dcat-ap-es#",
    "dcatapesconv": "http://datos.gob.es/def/dcat-ap-es/convenciones#"
  }
}
```

### Entidades incluidas

El contexto incluye las 11 entidades principales de DCAT-AP-ES:

1. **Catalog** - Catálogo de datos
2. **CatalogRecord** - Registro de catálogo
3. **DataService** - Servicio de datos
4. **Dataset** - Conjunto de datos
5. **Distribution** - Distribución
6. **Agent** - Agente (organización o persona)
7. **Identifier** - Identificador
8. **Location** - Ubicación
9. **PeriodOfTime** - Periodo de tiempo
10. **Checksum** - Suma de verificación
11. **Relationship** - Relación cualificada

### Propiedades por entidad

Cada propiedad está definida con:

#### Propiedades estándar JSON-LD

- **`@id`**: URI completa de la propiedad RDF
- **`@type`**: Tipo JSON-LD (por ejemplo, `@id` para referencias a recursos)
- **`@container`**: Contenedor JSON-LD (`@set` para arrays sin orden)

#### Propiedades SHACL (W3C estándar)

- **`sh:minCount`**: Cardinalidad mínima (obligatoria si ≥ 1)
- **`sh:maxCount`**: Cardinalidad máxima (restricción si < ∞)
- **`sh:class`**: Clase RDF esperada para valores que son recursos
- **`sh:datatype`**: Tipo de dato esperado para valores literales
- **`sh:or`**: Lista de clases alternativas permitidas

#### Propiedades DCAT-AP-ES específicas

- **`dcatapes:applicabilityLevel`**: Nivel de obligatoriedad según RFC 2119
  - `dcatapes:Mandatory` - DEBE (MUST)
  - `dcatapes:Recommended` - DEBERÍA (SHOULD)
  - `dcatapes:Optional` - PUEDE (MAY)

- **`dcatapes:contextVariants`**: Array de variantes según el contexto
  - Cada variante incluye:
    - `dcatapes:context`: Identificador del contexto (ej: `dcatapes:HVD`)
    - `dcatapes:applicabilityLevel`: Nivel modificado en ese contexto
    - `sh:minCount`, `sh:maxCount`: Cardinalidad modificada

- **`dcatapes:conventions`**: Array de URIs de convenciones que aplican
  - Ejemplo: `["dcatapes:Conv11", "dcatapes:Conv12"]`

## Ejemplo de propiedad

```json
"hvdCategory": {
  "@id": "dcatap:hvdCategory",
  "@container": "@set",
  "@type": "@id",
  "sh:class": "skos:Concept",
  "dcatapes:applicabilityLevel": "dcatapes:Optional",
  "dcatapes:contextVariants": [
    {
      "dcatapes:context": "dcatapes:HVD",
      "dcatapes:applicabilityLevel": "dcatapes:Mandatory",
      "sh:minCount": 1
    }
  ],
  "dcatapes:conventions": ["dcatapesconv:convencion-11"]
}
```

### Interpretación

1. **Propiedad base**: `dcatap:hvdCategory` (categoría HVD)
2. **Tipo**: Referencia a un `skos:Concept`
3. **Aplicabilidad**: Opcional en contexto general
4. **Variante HVD**: 
   - En contexto HVD (High Value Datasets)
   - Se vuelve OBLIGATORIA (`Mandatory`)
   - Requiere al menos 1 valor (`sh:minCount: 1`)
5. **Convenciones**: Afectada por la Convención 11
   - URI expandida: `https://datosgobes.github.io/DCAT-AP-ES/conventions/#convencion-11`

## Interpretación de cardinalidad

### Ejemplos de cardinalidades SHACL:

| Cardinalidad original | `sh:minCount` | `sh:maxCount` | Interpretación |
|----------------------|---------------|---------------|----------------|
| `1..1` | `1` | `1` | Exactamente 1 (obligatorio) |
| `1..n` | `1` | - | Al menos 1 (obligatorio, múltiple) |
| `0..1` | - | `1` | Máximo 1 (opcional, singular) |
| `0..n` | - | - | Sin restricción (opcional, múltiple) |
| `1..3` | `1` | `3` | Entre 1 y 3 valores |

**Nota:** la ausencia de `sh:minCount` implica mínimo 0 (opcional) y la ausencia de `sh:maxCount` implica cardinalidad sin límite.

## Convenciones

Las convenciones son reglas que modifican o extienden el perfil base de DCAT-AP-ES. Se referencian usando el prefijo `dcatapesconv:`.

### Prefijo de convenciones

```json
"dcatapesconv": "https://datosgobes.github.io/DCAT-AP-ES/conventions/#convencion-"
```

### Formato de referencias

Las convenciones se referencian en el array `dcatapes:conventions` de cada propiedad:

```json
"dcatapes:conventions": ["dcatapesconv:convencion-11", "dcatapesconv:convencion-12"]
```

### URIs expandidas

| Referencia | URI expandida |
|------------|---------------|
| `dcatapesconv:convencion-11` | `https://datosgobes.github.io/DCAT-AP-ES/conventions/#convencion-11` |
| `dcatapesconv:convencion-12` | `https://datosgobes.github.io/DCAT-AP-ES/conventions/#convencion-12` |

### Convenciones principales

- **Conv. 11**: Requisitos para conjuntos de datos de alto valor (HVD)
- **Conv. 12**: Todo Dataset HVD debe tener al menos un DataService
- **Conv. 25-27**: Requisitos para NSIP/ERPD (Data Governance Act)

### Futuro: Ontología formal

Actualmente, las URIs apuntan a fragmentos HTML en la documentación. Se está considerando crear una **ontología formal RDF** de convenciones que permita:

- Dereferenciación con content negotiation (HTML para humanos, RDF para máquinas)
- Definiciones estructuradas de cada convención
- Metadatos: contextos aplicables, entidades afectadas, tipos de modificación
- Integración con validación SHACL

Ver propuesta completa en: [`docs/conventions-ontology-proposal.md`](../docs/conventions-ontology-proposal.md)

## Contextos de aplicación

### Contexto base (DCAT-AP-ES general)

Todas las propiedades tienen sus valores base definidos directamente en la raíz de cada propiedad.

### Contexto HVD (High Value Datasets)

Según el Reglamento de Ejecución (UE) 2023/138, los conjuntos de datos de alto valor tienen requisitos adicionales:

- `dcatapes:context`: `"dcatapes:HVD"`
- Propiedades que cambian: `hvdCategory`, `applicableLegislation`, `distribution`, `contactPoint`, `page`, `servesDataset`
- Generalmente: Opcional → Obligatorio, cardinalidad aumentada

### Contexto NSIP/ERPD (futuro)

Para puntos de información únicos (SNIEP) y proveedores registrados (ERPD) según Reglamento (UE) 2022/868:

- `dcatapes:context`: `"dcatapes:NSIP"` o `"dcatapes:ERPD"`
- Definido en Convenciones 25, 26 y 27

## Relación con otros archivos

### `docs/index.md`

El contexto JSON-LD debe estar sincronizado con las tablas de propiedades en `index.md`. Un script de validación puede comparar ambos para detectar inconsistencias.

### `docs/conventions.md`

Las convenciones referenciadas en `dcatapes:conventions` están documentadas aquí. Cada convención especifica modificaciones al modelo base.

### `shacl/1.0.0/*.ttl`

Los shapes SHACL deben implementar las restricciones definidas en este contexto. La validación puede verificar que:
- Las cardinalidades SHACL coincidan con `sh:minCount`/`sh:maxCount` del contexto
- Los rangos SHACL coincidan con `sh:class`/`sh:datatype` del contexto
- Las severidades SHACL reflejen los niveles de aplicabilidad

## Uso programático

### Validar contra el contexto

```python
import json

# Cargar el contexto
with open('context/dcat-ap-es-context.jsonld') as f:
    context = json.load(f)

# Acceder a las definiciones
catalog_props = context['@context']['Catalog']['@context']
title_def = catalog_props['title']

print(f"Título obligatorio: {title_def['sh:minCount'] >= 1}")
print(f"Tipo de dato: {title_def['sh:datatype']}")
print(f"Nivel: {title_def['dcatapes:applicabilityLevel']}")
```

### Generar documentación

El contexto puede ser usado para generar automáticamente:
- Tablas de propiedades en Markdown
- Documentación AsciiDoc
- Esquemas de validación
- Plantillas de ejemplo

### Generar SHACL shapes

Las propiedades SHACL del contexto pueden ser transformadas directamente a shapes Turtle para validación.

## Referencias

- **SHACL**: [W3C Shapes Constraint Language](https://www.w3.org/TR/shacl/)
- **JSON-LD**: [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
- **DCAT-AP**: [DCAT Application Profile for data portals in Europe](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/dcat-application-profile-data-portals-europe)
- **RFC 2119**: [Key words for use in RFCs to Indicate Requirement Levels](https://www.rfc-editor.org/rfc/rfc2119)
- **HVD Regulation**: [Implementing Regulation (EU) 2023/138](https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj)
- **DGA Regulation**: [Regulation (EU) 2022/868](https://eur-lex.europa.eu/eli/reg/2022/868/oj)

## Mantenimiento

Al actualizar el modelo DCAT-AP-ES:

1. Actualizar el contexto JSON-LD con los cambios
2. Sincronizar `docs/index.md`
3. Ejecutar el script de validación
4. Ajustar los shapes SHACL en `shacl/1.0.0/` cuando proceda
5. Revisar `docs/conventions.md`
6. Ejecutar los tests de validación

---

**Versión:** 1.0.0  
**Última actualización:** diciembre de 2025  
**Mantenedor:** Dirección General de Gobernanza Pública y Transformación Digital
