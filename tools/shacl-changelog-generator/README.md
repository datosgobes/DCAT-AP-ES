# SHACL Changelog Generator

Genera y mantiene automáticamente un CHANGELOG de los archivos SHACL del proyecto DCAT-AP-ES basándose en el historial de Git.

## Uso

```bash
# Generar CHANGELOG completo
python3 tools/shacl-changelog-generator/generate_shacl_changelog.py --output shacl/CHANGELOG.md

# Actualizar desde un commit específico
python3 tools/shacl-changelog-generator/generate_shacl_changelog.py --since <hash>
```

**Opciones:**
- `--output, -o`: Archivo de salida (default: `shacl/CHANGELOG.md`)
- `--since`: Hash del commit desde el cual actualizar
- `--repo-path`: Ruta al repositorio (default: directorio actual)

## Características

- Categorización automática según Conventional Commits (`feat:`, `fix:`, `refactor:`, etc.)
- Agrupación por mes/año
- Detección de referencias a convenciones (Convención 25, 26, etc.)
- Enlaces a commits y perfiles de GitHub (@usuario)
- Integración con GitHub Actions (automático en PRs a `main`)

## Ejemplo de salida

```markdown
## Febrero 2026
### Features
- Implementar SHACL con Convención 30 (Convención 30) - `shacl_dataset_shape.ttl` ([`f23b81b`](../../commit/f23b81b)) - @mjanez
```
