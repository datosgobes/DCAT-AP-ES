---
name: Incidencias sobre el perfil DCAT-AP-ES
about: Reportar un problema o inconsistencia en el modelo de datos DCAT-AP-ES
title: 'Modelo - '
labels: DCAT-AP-ES, documentation
assignees: dportoles, mjanez

---

## Tipo de incidencia
> *Marca con una `[x]` la opción que corresponda*
- [ ] Error en la definición de una propiedad
- [ ] Inconsistencia en el modelo de datos
- [ ] Problema de compatibilidad con DCAT-AP
- [ ] Ambigüedad en la interpretación
- [ ] Problema de implementación
- [ ] Otro (*especificar*)

## Elemento afectado
> *Indica la clase, propiedad o componente del modelo DCAT-AP-ES donde se encuentra el problema.*
- ***Clase/Propiedad**: Ej: `dcat:Dataset`, `dct:publisher`, etc.*
- ***Ubicación en el perfil**:  Referencia a la sección específica del documento, ej: https://datosgobes.github.io/DCAT-AP-ES/#nota-dcat_distribution-dcat_accessurl*

### Situación actual en DCAT-AP-ES
> *Describe cómo funciona o está definido actualmente el elemento.*

### Problema detectado
> *Explica el problema o error identificado y por qué constituye una incidencia*

## Evidencia
> *Proporciona ejemplos concretos del problema, preferiblemente en RDF (`Turtle`, `RDF/XML`, `JSON-LD`)*

```turtle
# Ejemplo que muestra el problema
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .

<http://ejemplo.org/dataset/123> 
    a dcat:Dataset ;
    # Código que ilustra el problema
    .
```

## Posible Solución
> *Si tienes una propuesta de solución, describe claramente qué cambios deberían hacerse en el modelo.*

### Ejemplo de Implementación Correcta
> *Proporciona un ejemplo de cómo debería ser la solución.*

```turtle
# Ejemplo de implementación correcta
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .

<http://ejemplo.org/dataset/123> 
    a dcat:Dataset ;
    # Código con la solución propuesta
    .
```

## Información Adicional
> *Cualquier información adicional, enlaces o referencias que ayuden a entender el problema*

>[!NOTE]
> Por favor, proporciona toda la información posible para facilitar la evaluación y resolución de la incidencia.
