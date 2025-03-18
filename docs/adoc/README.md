# Directorio `docs/adoc`

Este directorio contiene los archivos AsciiDoc (`.adoc`) generados a partir de la conversión de documentos MkDocs. Estos archivos están listos para ser procesados y generar la documentación final en formato PDF.

## Cabecera de los archivos AsciiDoc

Cada archivo AsciiDoc incluye una [cabecera que define metadatos y opciones de configuración para la generación del documento](https://docs.asciidoctor.org/asciidoc/latest/document/header/). A continuación, se detalla el significado de cada atributo en la cabecera de ejemplo:

```adoc
= Convenciones técnicas, semánticas y organizativas de la aplicación de DCAT-AP-ES en el catálogo de datos.gob.es
Equipo Asesoramiento <soporte@datos.gob.es>
v1: DCAT-AP-ES Convenciones
:version-label:
:description: "Este documento establece las convenciones para la implementación del perfil DCAT-AP-ES en el catálogo nacional datos.gob.es, adaptando el estándar europeo DCAT-AP 2.1.1 y la extensión HVD 2.2.0 a las necesidades españolas. Define reglas técnicas, semánticas y organizativas para asegurar la interoperabilidad entre los distintos proveedores de datos abiertos, incluyendo administraciones autonómicas y locales. El documento está dirigido a desarrolladores y mantenedores de portales de datos abiertos, estableciendo directrices obligatorias y recomendadas según la terminología RFC2119."
:keywords: dcat-ap-es, dcat-ap, hvd, open-data, interoperability, metadata, standards, rdf, linked-data, semantic-web, data-gob-es, spain
:sectanchors:
:url-repo: https://github.com/datosgobes/DCAT-AP-ES
:sectnums:
:toc:
:toc-title: Índice
:source-highlighter: rouge
:rouge-style: github
:autofit-option:
:icons: font
:imagesdir: .
:front-cover-image: image::img/cover-dcat-ap-es-conventions.es.png[]
:pdf-theme: datosgobes-theme.yml
```

### Explicación de los atributos

*   **`= Título del documento`**: Define el título principal del documento.
*   **`Autor <email>`**: Especifica el autor del documento y su dirección de correo electrónico.
*   **`v1: DCAT-AP-ES Convenciones`**: Define la versión del documento y un identificador.
*   **`:version-label:`**: Permite personalizar la etiqueta de la versión.
*   **`:description:`**: Una breve descripción del contenido del documento.
*   **`:keywords:`**: Palabras clave asociadas al documento para facilitar la búsqueda.
*   **`:sectanchors:`**: Activa la generación de anclas para las secciones, permitiendo enlaces directos.
*   **`:url-repo:`**: URL del repositorio del proyecto.
*   **`:sectnums:`**: Activa la numeración automática de las secciones.
*   **`:toc:`**: Habilita la tabla de contenidos (TOC).
*   **`:toc-title:`**: Define el título de la tabla de contenidos.
*   **`:source-highlighter: rouge`**: Especifica el resaltador de sintaxis para el código fuente (en este caso, Rouge).
*   **`:rouge-style: github`**: Define el estilo de resaltado de Rouge (en este caso, el estilo de GitHub).
*   **`:autofit-option:`**:  Configura el ajuste automático de contenido.
*   **`:icons: font`**: Utiliza iconos de [Font Awesome](https://fontawesome.com/v4/icons/).
*   **`:imagesdir: .`**: Define el directorio donde se encuentran las imágenes (en este caso, el directorio actual).
*   **`:front-cover-image:`**: Especifica la imagen de la portada del documento.
*   **`:pdf-theme: datosgobes-theme.yml`**: Define el tema PDF a utilizar para la generación del documento.

Para más detalles sobre las opciones de configuración y personalización, se recomienda consultar la [documentación oficial de Asciidoctor](https://asciidoctor.org/docs/).
