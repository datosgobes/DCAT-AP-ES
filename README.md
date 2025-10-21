# Repositorio DCAT-AP-ES
[![ES](https://img.shields.io/badge/lang-ES-yellow.svg)](README.md) [![EN](https://img.shields.io/badge/lang-EN-blue.svg)](README.en.md) [![Validación formas SHACL](https://github.com/datosgobes/DCAT-AP-ES/actions/workflows/validate-shacl.yml/badge.svg)](https://github.com/datosgobes/DCAT-AP-ES/actions/workflows/validate-shacl.yml)

Este proyecto proporciona una serie de recursos para la [implementación técnica de DCAT-AP-ES](https://datos.gob.es/es/documentacion/etiquetas/normativas-3836), un perfil de aplicación del vocabulario de catálogo de datos ([DCAT-AP](https://datos.gob.es/es/documentacion/dcat-ap-perfil-de-aplicacion-de-dcat-para-portales-open-data-europeos)) para España.

> [!TIP]
> La documentación disponible en [DCAT-AP-ES Online](https://datosgobes.github.io/DCAT-AP-ES/) está diseñada para servir como referencia tanto para publicadores como para usuarios de datos abiertos. En ella se detallan los principios y directrices para estructurar y describir conjuntos de datos de acuerdo con el perfil de aplicación DCAT-AP-ES, facilitando su interoperabilidad y reutilización. Además, incluye esquemas de metadatos, ejemplos prácticos, y guías de implementación que ayudan a garantizar una correcta adopción del perfil.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `.devcontainer`: Configuración para [Dev Containers](https://containers.dev/implementors/spec/), una funcionalidad que permite desarrollar en un entorno preconfigurado dentro de un contenedor [Docker](https://docs.docker.com/).
- `.github/workflows/`: Contiene los flujos de trabajo de [GitHub Actions](https://docs.github.com/es/actions) para la generación de la documentación online y pruebas automatizadas para las formas SHACL.
- `docs/`: Documentación principal del proyecto en formato [`Markdown`](https://daringfireball.net/projects/markdown/syntax) para [MKDocs](https://www.mkdocs.org/getting-started/).
- `overrides`: [Plantillas personalizadas](https://squidfunk.github.io/mkdocs-material/customization/) para la documentación online.
- `examples/`: Ejemplos de uso de `DCAT-AP-ES` en formato RDF/XML y Turtle.
- `shacl/`: Archivos de validación SHACL para `DCAT-AP-ES` y extensión HVD.
- `tests/`: Scripts y documentación para validación local de SHACL. [Más información](./tests/README.md)
- `refs/`: Referencias adicionales y documentación relacionada.
- `tools/`: Herramientas y software útil para la gestión del proyecto. [Más información](#herramientas-adicionales-del-repositorio)

## Testing y Validación

Este repositorio incluye un sistema completo de validación SHACL automatizado mediante GitHub Actions. Para más información sobre cómo ejecutar tests localmente y entender los resultados de validación, consulta [tests/README.md](./tests/README.md).

### Validación Local

Para validar cambios antes de hacer commit:

```bash
# Ejecutar todas las validaciones
./tests/validate-local.sh

# Solo validación sintáctica
./tests/validate-local.sh --syntax-only

# Solo validación semántica SHACL
./tests/validate-local.sh --shacl-only
```

El script validará:
- Coherencia entre el modelo DCAT-AP-ES y las formas SHACL.
- Sintaxis de archivos SHACL (Turtle)
- Conformidad de ejemplos RDF con las shapes SHACL

> [!WARNING]
> **Requisitos**: [Docker](https://docs.docker.com/get-started/get-docker/)

## Contribución

Si deseas contribuir a este proyecto, por ejemplo arreglando algún [fichero de validación SHACL](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf) de `DCAT-AP-ES`, por favor sigue estos pasos:

1. Bifurca el repositorio [`datosgobes/DCAT-AP-ES`](https://github.com/datosgobes/DCAT-AP-ES).

    ```sh
    git clone https://github.com/datosgobes/DCAT-AP-ES.git
    ```

2. Crea una nueva rama con tu correción

    ```sh
    git checkout -b fix/shacl-property-x
    ```

3. **Valida tus cambios localmente** antes de hacer commit

    ```sh
    ./tests/validate-local.sh
    ```

4. Realiza tus cambios y haz commit 

    ```sh
    git commit -am 'Corregido rango de propiedad x'
    ```

5. Sube tus cambios 

    ```sh
    git push origin fix/shacl-property-x
    ```

6. Abre una [Solicitud de extracción (*Pull Request*)](https://github.com/datosgobes/DCAT-AP-ES/pulls) para confirmar el cambio en la rama principal.

> [!TIP]
> El workflow de GitHub Actions ejecutará automáticamente las validaciones SHACL en tu Pull Request y comentará los resultados. Asegúrate de que todas las validaciones pasen antes de solicitar revisión.

## Desarrollo

Para previsualizar la documentación con MkDocs y lanzarlo en modo depuración, revisa la siguiente documentación: [información sobre MKDocs](./refs/dev/mkdocs.md) 

### Traducción de la documentación

Esta documentación usa [`mkdocs-static-i18n`](https://ultrabug.github.io/mkdocs-static-i18n/) para ser multilingüe, con ese objetivo se adopta la estructura de sufijos: 

```bash
├── assets
│   ├── css
│   └── js
├── img
├── conventions.en.md
├── conventions.md
├── examples.en.md
├── examples.md
├── index.md
└── robots.txt
```

> [!NOTE] 
> Usando la estructura de sufijo en los archivos de documentación (por defecto), debes agregar el sufijo `.<idioma>.<extensión>` a tus archivos (por ejemplo, `index.en.md`).  
> Más información en: [Documentación del plugin MkDocs static i18n](https://ultrabug.github.io/mkdocs-static-i18n/getting-started/quick-start/)

### Herramientas adicionales del repositorio
1. **Python hook ([`dcat_ap_es.py`](./tools/mkdocs-hooks/dcat_ap_es.py))**: 
   - Es un [*hook* para MkDocs](https://www.mkdocs.org/user-guide/configuration/#hooks) que se ejecuta después de la construcción del sitio
   - Se encarga de copiar archivos `PDF` desde un directorio de origen a un directorio de destino en el sitio generado

2. **Imagen personalizada para Asciidoctor** ([`Dockerfile`](./tools/asciidoctor/Dockerfile)):
   - Basado en la imagen [`asciidoctor/docker-asciidoctor`](https://github.com/asciidoctor/docker-asciidoctor)
   - Se utiliza para generar documentos `PDF` maquetados a partir de archivos `AsciiDoc`

3. **Imagen personalizada para md2adoc** ([`Dockerfile`](./tools/md2adoc/Dockerfile)):
   - Basado en la imagen [`ruby`](https://github.com/docker-library/ruby)
   - Se utiliza para convertir documentos Markdown a formato `AsciiDoc`

Estos tres componentes forman parte de un pipeline de documentación que:
1. Convierte archivos Markdown a AsciiDoc (usando el contenedor md2adoc)
2. Genera `PDF` a partir de los archivos AsciiDoc (usando el contenedor asciidoctor)
3. Copia los `PDF` generados al sitio web final durante la construcción de MkDocs (usando el hook de Python)

## Licencia

Todo el material de este repositorio se publica bajo la licencia `CC-BY 4.0`, a menos que se mencione explícitamente lo contrario. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

## Contacto

Para cualquier consulta o sugerencia, por favor abre [una incidencia (*Issue*) en el repositorio](https://github.com/datosgobes/DCAT-AP-ES/issues) o contacta a los mantenedores del proyecto.