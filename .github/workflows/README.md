# Workflows

Automatizaciones de CI/CD para DCAT-AP-ES. Todos los workflows se ejecutan en GitHub Actions.

## Activos

### [`mkdocs.yml`](./mkdocs.yml)
Despliega la documentación MkDocs a GitHub Pages cuando hay cambios en `main`.

**Trigger**: Push a `main` o ejecución manual  
**Salida**: https://datosgobes.github.io/DCAT-AP-ES/  
**Nota**: Instala todas las dependencias de MkDocs y publica en rama `gh-pages`

---

### [`validate-shacl.yml`](./validate-shacl.yml)
Valida archivos SHACL y ejemplos RDF/TTL en PRs y pushes a `main`/`develop`.

**Trigger**: Cambios en `shacl/**/*.ttl`, `examples/**/*.{rdf,ttl}` o archivos de configuración  
**Ejecución**: Docker con pyshacl (ver `tests/validate-local.sh`)  
**Artefactos**: Reportes de validación (30 días)  
**Nota**: Comenta resumen en PRs automáticamente

---

### [`update-shacl-changelog.yml`](./update-shacl-changelog.yml)
Mantiene actualizado [`shacl/CHANGELOG.md`](../../shacl/CHANGELOG.md) cuando cambian archivos SHACL.

**Trigger**: Cambios en `shacl/**/*.ttl` en `develop`  
**Funcionamiento**: 
1. Detecta commits nuevos desde la última actualización
2. Categoriza según Conventional Commits
3. Crea PR automática para revisión (requiere 1 aprobación)

**Protecciones**:
- Evita bucles (detecta commits del bot)
- Solo crea PR si hay cambios reales
- No ejecuta en paralelo (concurrency)

**Manual**: Actions → Update SHACL Changelog → Run workflow

---

### [`asciidocpdf.yml`](./asciidocpdf.yml)
Genera PDFs desde archivos AsciiDoc cuando se modifican en `docs/adoc/`.

**Trigger**: Cambios en `docs/adoc/**` o ejecución manual (con opción de conversión MD→AsciiDoc)  
**Salida**: PDFs en `refs/dcat-ap-es/pdf/`  
**Flujo**: 
1. Genera PDFs con Docker Compose
2. Compara hashes con versión en `main`
3. Crea PR si hay cambios reales

**Manual**: Actions → `Generate PDFs from AsciiDoc` files (checkbox "Convert Markdown to AsciiDoc" si aplica)

---

## En desarrollo

### [`changelog.yml`](./changelog.yml)
Genera CHANGELOG.md y release notes cuando se publica un tag de versión.

**Trigger**: Tags `v*.*.*` (ej: `v1.0.0`)  
**Acciones**:
- Genera CHANGELOG.md automáticamente
- Crea GitHub Release con notas
- Categoriza commits por tipo (feat, fix, docs, etc.)

**Formato**: Sigue [Keep a Changelog](https://keepachangelog.com/es/)

---

### [`documentation.yml`](./documentation.yml)
Build alternativo de documentación con Poetry (actualmente manual), para versionar.

**Trigger**: Solo manual  
**Diferencia con mkdocs.yml**: Usa Poetry para gestión de dependencias, incluye Playwright para rendering  
**TODO**: Añadir versionado con [mike](https://github.com/jimporter/mike)

---