# Docker Image: DCAT-AP-ES SHACL Validator

Imagen Docker con pySHACL, rapper y herramientas de validación DCAT-AP-ES.

## Construcción

```bash
cd tools/docker-pyshacl
docker build -t dcat-ap-es/shacl-validation:latest .
```

## Uso

Usar el script `tests/validate-local.sh` que gestiona automáticamente la imagen Docker:

```bash
# Desde la raíz del repositorio
./tests/validate-local.sh all
```

Ver [tests/README.md](../../tests/README.md) para documentación completa del sistema de validación.

## Contenido de la Imagen

- **pySHACL**: Validador SHACL (Python)
- **Raptor rapper**: Parser RDF para validación sintáctica
- **Python scripts**: Validadores personalizados DCAT-AP-ES
- **Alpine Linux**: Base ligera (~150 MB)

## Herramientas Disponibles

```bash
# Validador unificado (recomendado)
docker run --rm -v "$PWD:/workspace" dcat-ap-es/shacl-validation:latest validate all

# Herramientas individuales
docker run --rm -v "$PWD:/workspace" dcat-ap-es/shacl-validation:latest pyshacl --help
docker run --rm -v "$PWD:/workspace" dcat-ap-es/shacl-validation:latest rapper --help
docker run --rm -v "$PWD:/workspace" dcat-ap-es/shacl-validation:latest compare-model-shacl
```
```
