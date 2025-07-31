Esta sección recopila las preguntas más frecuentes sobre DCAT-AP-ES, su implementación y uso. El objetivo es proporcionar respuestas claras y concisas para facilitar la comprensión y adopción de este perfil de aplicación.

Secciones:

* [Sobre DCAT-AP-ES](#dcat-ap-es): Aborda preguntas comunes sobre el perfil de aplicación.
* [Modelo de datos](#model): Explica dudas y conceptos fundamentales del modelo de datos.
* [Federación](#federation): Responde a dudas sobre la implementación técnica y la federación con el [catálogo nacional](https://datos.gob.es/).
* [Repositorio](#repository): Introduce el repositorio [`datosgobes/DCAT-AP-ES`](https://github.com/datosgobes/DCAT-AP-ES) y su propósito.
* [Perfiles de aplicación relacionados](#application-profile): Contextualiza las especificaciones relacionadas con DCAT-AP-ES.


!!! warning "Relación con las preguntas frecuentes de datos.gob.es"

    Este documento se centra en cuestiones específicas sobre la especificación DCAT-AP-ES y su implementación técnica. Para consultas generales sobre el catálogo nacional, recomendamos visitar las [preguntas frecuentes de datos.gob.es](https://datos.gob.es/faq-page).


---

## **Sobre DCAT-AP-ES** { .faq-h #dcat-ap-es}

<div class="grid cards" markdown>
-   :boostrap-spain:{ .lg .middle .grid-emoji } **DCAT-AP-ES**{ .grid-title #vocab-dcat-ap-es }

    ---

    Adaptación de DCAT-AP que incorpora especificaciones propias del contexto español y la extensión HVD.

    [:octicons-arrow-right-24: Ver más](/)


-   :fontawesome-solid-plus:{ .lg .middle .grid-emoji } **¿Principales novedades de DCAT-AP-ES?**{ .grid-title #novedades }

    ---

    Se alinea con el perfil europeo DCAT-AP, incorpora servicios de datos (`dcat:DataService`), el modelado de conjuntos de alto valor (HVD) y mejoras en la descripción de la calidad de metadatos.

    [:octicons-arrow-right-24: Clases](/DCAT-AP-ES/#dcat-ap-es-entities)

-   :material-connection:{ .lg .middle .grid-emoji } **¿Relación con otros estándares?**{ .grid-title #relacion }

    ---

    DCAT-AP-ES implementa DCAT-AP y su extensión HVD, garantizando la compatibilidad con el ecosistema europeo de datos abiertos.

    [:octicons-arrow-right-24: UML](/DCAT-AP-ES/#uml)

-   :material-calendar:{ .lg .middle .grid-emoji } **¿Cuándo entra en vigor?**{ .grid-title #vigencia }

    ---

    DCAT-AP-ES está previsto que entre en vigor en 2025, tras la aprobación de la nueva NTI-RISP, el día siguiente a su publicación en el BOE.

    [:octicons-arrow-right-24: NTI-RISP](https://www.boe.es/eli/es/res/2013/02/19/(4))

-   :material-clock-fast:{ .lg .middle .grid-emoji } **¿Qué plazo hay para migrar?**{ .grid-title #migracion }

    ---

    Los publicadores disponen de un periodo de adaptación desde la entrada en vigor de la NTI-RISP.

    [:octicons-arrow-right-24: Cambios](/DCAT-AP-ES/#annex-1-nti-risp-to-dcat-ap-es)

</div>

## **Modelo de datos** { .faq-h #model}

<div class="grid cards grid-2col" markdown>

-   :fontawesome-solid-diagram-project:{ .lg .middle .grid-emoji } **¿Cómo se relacionan los elementos de DCAT-AP-ES?**{ .grid-title #relaciones-modelo }

    ---

    El modelo DCAT-AP-ES funciona como una red donde los elementos se conectan entre sí:

    - Un **catálogo** (`dcat:Catalog`) funciona como un contenedor principal que aloja conjuntos de datos y servicios

    - Los **servicios de datos** (`dcat:DataService`) proporcionan acceso a los conjuntos de datos

    - Cada **conjunto de datos** (`dcat:Dataset`) puede tener múltiples distribuciones (formatos)

    - Las **distribuciones** (`dcat:Distribution`) pueden accederse a través de servicios específicos

    ```mermaid
    graph LR
        %% Definición de nodos
        Catalog((dcat:Catalog)):::main
        Dataset[dcat:Dataset]:::entity
        DataService[dcat:DataService]:::entity
        Distribution[dcat:Distribution]:::entity

        %% Relaciones con etiquetas
        Catalog -->|dcat:dataset| Dataset
        Catalog -->|dcat:service| DataService
        DataService -->|dcat:servesDataset| Dataset
        Dataset -->|dcat:distribution| Distribution
        Distribution -->|dcat:accessService| DataService

        %% Estilos con bordes redondeados
        classDef main fill:#B8C2CC,stroke:none,font-size:24px,color:#00a99d,font-weight:bold;
        classDef entity fill:#e6f3ff,stroke:none,font-size:20px,color:#154481 !important,rx:10,ry:10,font-weight:bold;

        %% Estilos de línea
        linkStyle default stroke:#154481,stroke-width:1px,stroke-dasharray:3;
    ```

    [:octicons-arrow-right-24: Relaciones](/DCAT-AP-ES/#dcat-ap-es-model-relations)

-   :material-update:{ .lg .middle .grid-emoji } **¿ Cómo evoluciono desde un catálogo NTI-RISP?**{ .grid-title #migracion-nti }

    ---

    Si ya tienes un catálogo conforme al modelo de metadatos NTI-RISP 2013, para evolucionar a DCAT-AP-ES puedes:

    1. **Identificar cambios**: Revisar las diferencias entre ambos modelos según el [Anexo 1 - Cambios respecto a la NTI-RISP](/DCAT-AP-ES/#annex-1-nti-risp-to-dcat-ap-es) e incorporar nuevos metadatos obligatorios.

    2. **Adaptar vocabularios controlados**: Utilizar los [vocabularios actualizados del modelo](/DCAT-AP-ES/#dcat-ap-es-vocabularies) en vez de literales.

    3. **Añadir soporte a servicios**: Incorporar la clase [`dcat:DataService`](/DCAT-AP-ES/#servicio_de_datos_-_clase_dcatdataservice_-_opcional) si ofreces APIs o servicios.

    4. **Validar el catálogo**: Comprobar la conformidad utilizando las [herramientas de validación](/DCAT-AP-ES/validacion/)

    [:octicons-arrow-right-24: Migración](/DCAT-AP-ES/#annex-1-nti-risp-to-dcat-ap-es)

-   :material-compare:{ .lg .middle .grid-emoji } **¿ Diferencias entre DCAT-AP-ES y DCAT-AP?**{ .grid-title #diferencias-dcat }

    ---

    DCAT-AP-ES añade varias restricciones y extiende el modelo europeo:

    - **Obligatoriedad ampliada**: Establece más propiedades obligatorias para garantizar la interoperabilidad.

    - **Contexto español**: Añade taxonomías y vocabularios controlados propios del sector público español.

    - **Integración HVD**: Incorpora completamente el modelo de datos de alto valor.

    - **Cardinalidad adaptada**: Limita algunas cardinalidades para descripciones más precisas.

    [:octicons-arrow-right-24: Diferencias](/DCAT-AP-ES/#annex-3-dcat-ap-to-dcat-ap-es)

</div>


---

## **Federación** { .faq-h #federation}

<div class="grid cards" markdown>

-   :fontawesome-solid-laptop-code:{ .lg .middle .grid-emoji } **¿Dónde encontrar ejemplos de DCAT-AP-ES?**{ .grid-title #implementacion-ejemplos }

    ---

    Disponibles en la guía online y en el directorio `examples/` del repositorio, organizados por entidades y casos de uso específicos.

    [:octicons-arrow-right-24: Ejemplos](/DCAT-AP-ES/examples)

-   :fontawesome-solid-file-code:{ .lg .middle .grid-emoji } **¿Qué formato debe tener el catálogo?**{ .grid-title #implementacion-formatos }

    ---

    El fichero de catálogo que va a federarse debe describirse conforme a la sintaxis XML para RDF denominada `RDF/XML`

    [:octicons-arrow-right-24: Sintaxis](https://www.w3.org/TR/rdf-syntax-grammar/)

</div>

---

## **Repositorio** { .faq-h #repository}

<div class="grid cards" markdown>

-   :material-source-repository:{ .lg .middle .grid-emoji } **¿Qué es el repositorio DCAT-AP-ES?**{ .grid-title #repository-que-es }

    ---

    Repositorio de código y seguimiento sobre la implementación de la NTI de acuerdo con el perfil de aplicación DCAT-AP-ES.

    [:octicons-arrow-right-24: Repositorio](https://github.com/datosgobes/DCAT-AP-ES "Repositorio de código fuente con todo el material de DCAT-AP-ES" )

-   :fontawesome-brands-readme:{ .lg .middle .grid-emoji } **¿Qué encontrar en el repositorio DCAT-AP-ES?**{ .grid-title #repository-readme }

    ---

    La evolución de la especificación DCAT-AP-ES con documentación técnica, guías, ejemplos y la retroalimentación de los usuarios.

    [:octicons-arrow-right-24: Léeme](https://github.com/datosgobes/DCAT-AP-ES#guía-para-dcat-ap-es "README del repositorio DCAT-AP-ES con indicaciones sobre contenido y contribución" )

-   :fontawesome-solid-folder-open:{ .lg .middle .grid-emoji } **¿Hay materiales de apoyo?**{ .grid-title #repository-materiales }

    ---

    Existen guías de aplicación e implementación técnica, convenciones, modelos de datos, vocabularios, ejemplos, ficheros de validación SHACL, etc.

    [:octicons-arrow-right-24: Guía](/DCAT-AP-ES/)

-   :fontawesome-solid-code-pull-request:{ .lg .middle .grid-emoji } **Pensado para contribuir**{ .grid-title #repository-contribuir }

    ---

    Pensado para que la comunidad pueda proponer mejoras y participar en la evolución del perfil DCAT-AP-ES.

    [:octicons-arrow-right-24: Contribuir](https://github.com/datosgobes/DCAT-AP-ES?tab=readme-ov-file#contribución "Informa acerca de incidencias o mejoras del perfil DCAT-AP-ES")

-   :fontawesome-brands-creative-commons:{ .lg .middle .grid-emoji } **Código abierto, CC-BY 4.0**{ .grid-title #repository-license }

    ---

    Todo el material esta licenciado con la licencia abierta *Creative Commons Attribution 4.0 International*.

    [:octicons-arrow-right-24: Licencia](https://github.com/datosgobes/DCAT-AP-ES#CC-BY-4.0-1-ov-file "Licencia de uso libre que permite compartir, copiar, distribuir y modificar una obra, incluso con fines comerciales, con la única condición de reconocer la autoría original")

</div>

---

## **Perfiles de aplicación relacionados** { .faq-h #application-profile}

<div class="grid cards" markdown>

-   :simple-semanticweb:{ .lg .middle .grid-emoji } **DCAT**{ .grid-title{ .grid-title #vocab-dcat }

    ---

    Es el vocabulario fundamental para describir catálogos y recursos de datos en la web desarrollado por el W3C.

    [:octicons-arrow-right-24: Ver más](https://www.w3.org/TR/vocab-dcat/)

-   :simple-europeanunion:{ .lg .middle .grid-emoji } **DCAT-AP**{ .grid-title #vocab-dcat-ap }

    ---

    Es el perfil europeo basado en DCAT que define normas comunes para catálogos de datos abiertos, facilitando la interoperabilidad.

    [:octicons-arrow-right-24: Ver más](https://op.europa.eu/es/web/eu-vocabularies/dcat-ap)

-   :fontawesome-solid-star:{ .lg .middle .grid-emoji } **DCAT-AP HVD**{ .grid-title #vocab-dcat-ap-hvd}

    ---

    Extensión de DCAT-AP para describir y catalogar conjuntos de datos de alto valor en cumplimiento del Reglamento de Implementación HVD.

    [:octicons-arrow-right-24: Ver más](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-ap-hvd)

</div>

---
