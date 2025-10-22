# DCAT-AP-ES: Pruebas y Validación
[![ES](https://img.shields.io/badge/lang-ES-yellow.svg)](README.md) [![EN](https://img.shields.io/badge/lang-EN-blue.svg)](README.en.md)

Sistema automatizado de validación DCAT-AP-ES con 3 fases: comparación modelo-SHACL, validación sintáctica y conformidad semántica.

## Uso Rápido

```bash
# Validar todo (recomendado)
./tests/validate-local.sh all

# Validar fases individuales
./tests/validate-local.sh model-only    # Fase 0 solamente
./tests/validate-local.sh syntax-only   # Fase 1 solamente
./tests/validate-local.sh shacl-only    # Fase 2 solamente
```

**Requisito**: Docker instalado

**Informes generados**: `tests/validation-reports/SUMMARY.md`

## Fases de Validación

### Fase 0: Comparación Modelo-SHACL
Verifica que todas las propiedades OBLIGATORIAS del modelo (`docs/index.md`) tengan formas SHACL correspondientes.

**Tecnología**: Python + rdflib  
**Resultado**: `model-vs-shacl-report.md` y `.csv`

### Fase 1: Validación Sintáctica
Valida sintaxis Turtle de archivos SHACL definidos en `test.ini`.

**Tecnología**: Raptor rapper  
**Archivos**: Listados en `tests/test.ini` bajo `[shacl_shapes]`

**Ejemplo de error**:
```
rapper: Error - URI file:///workspace/shacl/1.0.0/file.ttl:123 - syntax error
```
El número `:123` indica la línea exacta del error.

### Fase 2: Validación Semántica
Valida ejemplos RDF contra formas SHACL usando pySHACL.

**Tecnología**: pySHACL  
**Casos de prueba**: Definidos en `tests/test.ini` bajo `[tests]`

| Caso de Prueba | Descripción |
|---------------|-------------|
| `E_DCAT-AP-ES_minimal.ttl` | Solo propiedades obligatorias |
| `E_DCAT-AP-ES_full.ttl` | Obligatorias + recomendadas |
| `E_DCAT-AP-ES_Catalog_HVD.ttl` | HVD mínimo |
| `E_DCAT-AP-ES_Catalog_HVD_full.ttl` | HVD completo |

## Archivo test.ini

Define qué archivos SHACL y casos de prueba se validan:

```ini
[shacl_shapes]
# Archivos SHACL a validar sintácticamente (Fase 1)
shacl_catalog_shape.ttl
shacl_dataset_shape.ttl
hvd/shacl_dataset_hvd_shape.ttl

[tests]
# Casos de prueba semánticos (Fase 2)
dcatapes_minimal = E_DCAT-AP-ES_minimal.ttl
dcatapes_full = E_DCAT-AP-ES_full.ttl
```

**Shapes base** (cargados automáticamente):
- `shacl_mdr-vocabularies.shape.ttl` - Vocabularios controlados
- `shacl_common_shapes.ttl` - Shapes reutilizables

## GitHub Actions

El workflow `.github/workflows/validate-shacl.yml` ejecuta automáticamente `validate-local.sh all` en:
- Pull Requests que modifiquen archivos `shacl/**/*.ttl`, `examples/**/*.{rdf,ttl}` o el workflow
- Push a ramas `main` y `develop`

**Artefactos**: Los informes se suben como artefactos (retención 30 días)  
**Comentarios PR**: El contenido de `SUMMARY.md` se publica automáticamente

## Troubleshooting

**Error sintáctico con número de línea**:
```sh
[ERROR] ✗ shacl_mdr-vocabularies.shape.ttl
  rapper: Parsing URI file:///workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl with parser turtle
  rapper: Error - URI file:///workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl:139 - syntax error, unexpected a
  rapper: Failed to parse file /workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl turtle content
  rapper: Parsing returned 93 triples
```
→ Revisar línea 139 del archivo (URIs, comas, puntos, literales)

**Violación SHACL**:
```
sh:resultMessage "Missing required property dcat:distribution"
```
→ Añadir propiedad obligatoria o verificar su referencia

**Clase no reconocida**:
```
sh:resultMessage "Value does not have class Y"
```
→ Verificar declaración `rdf:type` explícita

## Ejecutar Pruebas Localmente

### Requisitos Previos

El script `validate-local.sh` se encarga de todo automáticamente:
- Verifica instalación de Docker
- Construye la imagen Docker de validación si no existe
- Ejecuta todas las fases de validación
- Genera informes en `tests/validation-reports/`

**Requisito único**: Docker instalado
```bash
# Instalar Docker
# Seguir instrucciones en: https://docs.docker.com/get-docker/
```

### Script de Validación Unificado

```bash
# Ejecutar todas las fases (recomendado)
./tests/validate-local.sh all

# O ejecutar fases específicas
./tests/validate-local.sh model-only      # Fase 0: Comparación Modelo-SHACL
./tests/validate-local.sh syntax-only     # Fase 1: Validación sintáctica SHACL
./tests/validate-local.sh shacl-only      # Fase 2: Validación semántica

# Sin argumentos = 'all'
./tests/validate-local.sh
```

**Ubicación de informes**: `tests/validation-reports/`
- `SUMMARY.md` - Resumen ejecutivo de todas las fases
- `model-vs-shacl-report.md` - Comparación detallada Modelo-SHACL
- `*-report.ttl` - Informes SHACL en formato Turtle

## Comprender Resultados de Validación

### Niveles de Severidad SHACL

- **Violación** (`sh:Violation`): Restricción obligatoria fallida → **La construcción falla**
- **Advertencia** (`sh:Warning`): Propiedad recomendada ausente → **La construcción pasa con advertencias**
- **Información** (`sh:Info`): Propiedad opcional ausente → **La construcción pasa**

### Resultados Esperados

```md
### Fase 0: Comparación Modelo-SHACL
**Propósito:** Verificar que el modelo de documentación tiene definiciones SHACL correspondientes

- **Estado:** ✅ CORRECTO
- **Problemas CRÍTICOS:** 0
- **Advertencias informativas:** 29 WARN, 0 INFO (no bloqueantes)

---

### Fase 1: Validación Sintáctica (Formas SHACL)
**Propósito:** Verificar que los archivos de formas SHACL son RDF/Turtle sintácticamente válidos

- **Errores de sintaxis:** 1
- **Estado:** ❌ ERROR

---

### Fase 2: Validación Semántica (Ejemplos RDF contra SHACL)
**Propósito:** Validar archivos de ejemplo RDF contra las restricciones de las formas SHACL

| Caso de Prueba | Esperado | Estado |
|----------------|----------|--------|
| DCAT-AP-ES Minimal Example | Avisos permitidos | ✅ CORRECTO |
| DCAT-AP-ES Full Example | Conformidad completa | ✅ CORRECTO |
| DCAT-AP-ES HVD Minimal Example | Avisos permitidos | ✅ CORRECTO |
| DCAT-AP-ES HVD Full Example | Conformidad completa | ✅ CORRECTO |

## Estadísticas

- **Fase 0 (Modelo-SHACL):** Problemas CRÍTICOS: 0
- **Fase 1 (Sintaxis):** Errores: 1
- **Fase 2 (Semántica):** Fallos en pruebas: 0
```

## Integración Continua

El flujo de trabajo de GitHub Actions se ejecuta automáticamente en:

- **Solicitudes de extracción (Pull Requests)** (para evitar duplicación, se ejecuta solo una vez por actualización de PR):
  - Cuando apuntan a las ramas `main` o `develop`
  - Solo si se modifican estas rutas:
    - `shacl/**/*.ttl` - Definiciones de formas SHACL
    - `examples/**/*.rdf` - Ejemplos RDF
    - `examples/**/*.ttl` - Ejemplos Turtle
    - `docs/index.md` - Modelo de documentación
    - `tools/docker-pyshacl/**` - Scripts de validación
    - `tests/test.ini` - Configuración de tests
    - `.github/workflows/validate-shacl.yml` - El propio workflow

- **Pushes directos a main/develop** (fuera de PRs):
  - Mismos filtros de rutas que arriba
  - Solo se ejecuta si no hay un PR asociado (evita duplicación)

> **Nota**: El workflow incluye una comprobación de deduplicación para evitar ejecutarse dos veces cuando ocurren eventos `pull_request` y `push` simultáneamente (ej: al hacer push a una rama de PR).

### Artefactos del Flujo de Trabajo

Los informes de validación se cargan como artefactos:
- Retención: 30 días
- Nombre: `shacl-validation-reports`
- Contenidos:
  - `minimal-report.ttl`
  - `full-report.ttl`
  - `hvd-report.txt`
  - `hvd-full-report.ttl`
  - `SUMMARY.md`

### Comentarios en Solicitudes de Extracción

El flujo de trabajo comenta automáticamente en PRs con:
- Tabla resumen de resultados de pruebas
- Indicadores de aprobado/advertencia/fallo
- Enlace a informes de artefactos detallados

## Referencias

- **DCAT-AP-ES**: https://datosgobes.github.io/DCAT-AP-ES/
- **SHACL Spec**: https://www.w3.org/TR/shacl/

