---
name: Incidencias sobre validación SHACL en DCAT-AP-ES
about: Reportar un problema, inconsistencia o propuesta de mejora en las formas SHACL
  del modelo de datos DCAT-AP-ES
title: 'SHACL - '
labels: DCAT-AP-ES, documentation, SHACL
assignees: dportoles, mjanez

---

## Tipo de incidencia
> *Marca con una `[x]` la opción que corresponda*
- [ ] Error en la definición de una forma SHACL
- [ ] Inconsistencia respecto al modelo DCAT-AP-ES
- [ ] Problemas de compatibilidad con DCAT-AP/SHACL estándar
- [ ] Ambigüedad en la interpretación de reglas
- [ ] Problemas de implementación/validación
- [ ] Otro (*especificar*)

## Elemento SHACL afectado
> *Indica la forma, clase, propiedad o componente del modelo DCAT-AP-ES/SHACL donde se encuentra el problema.*
- ***Forma/Clase/Propiedad SHACL**: Ej: `DatasetShape`, `dcat:Dataset`, `dct:publisher`, etc.*
- ***Ubicación en el perfil o regla**:  Referencia a la sección específica de la documentación de las formas SHACL, ej: 
  - Modelo DCAT-AP-ES: [`dct:LicenseDocument`->`dct:type`](https://datosgobes.github.io/DCAT-AP-ES/#nota-dct_licensedocument-dct_type)
  - SHACL: [`dcatapes:LicenceTypeRestriction`](https://github.com/datosgobes/DCAT-AP-ES/blob/ff08443345c5c5468979dd929ed6ab1edde45969/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl#L126-L137)

### Situación actual (SHACL/DCAT-AP-ES)
> *Describe cómo está definida o implementada actualmente la forma o regla.*

### Problema detectado
> *Explica el problema, error o limitación y por qué constituye una incidencia relevante*

## Evidencia
> *Proporciona ejemplos concretos del problema, preferiblemente en SHACL (`Turtle`), RDF (`Turtle`, `RDF/XML`, `JSON-LD`) o informe de validación*

```turtle
# Ejemplo que muestra el problema
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .

ex:DatasetShape
    a sh:NodeShape ;
    sh:targetClass dcat:Dataset ;
    # Código que ilustra el problema
    .
```

## Posible Solución
> *Si tienes una propuesta, describe los cambios en la forma/regla o en el modelo para resolver el problema.*

### Ejemplo de Implementación Correcta
> *Proporciona un ejemplo de cómo debería ser la solución en SHACL/RDF.*

```turtle
# Ejemplo de implementación correcta
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .

ex:DatasetShape
    a sh:NodeShape ;
    sh:targetClass dcat:Dataset ;
    # Código con la solución propuesta
    .
```

## Información Adicional
> *Cualquier información, enlaces o referencias útiles para entender el problema o la solución*

>[!NOTE]
> Por favor, proporciona toda la información posible para facilitar la evaluación y resolución de la incidencia.
