Con el propósito de verificar si el intercambio de metadatos cumple técnicamente con [DCAT-AP-ES](/), se pueden utilizar los grafos de [formas SHACL disponibles en el repositorio](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/). El Lenguaje de Restricción de Formas (*Shapes Constraint Language* - SHACL), es una [recomendación del W3C](https://www.w3.org/TR/shacl/) para expresar restricciones en un grafo de conocimiento RDF. 

La siguiente ilustración muestra de forma esquemática las etapas principales del proceso de validación SHACL aplicadas a los metadatos, desde la preparación de los datos hasta la obtención de los resultados de conformidad.

![](img/dge_shacl.es.drawio "Ilustración . Descripción de los pasos de validación SHACL")

Las formas SHACL permiten comprobar si un catálogo expresado en una serialización RDF es válido. Dado que debería ser posible transformar el intercambio de datos en RDF para la conformidad con DCAT-AP-ES, estas formas SHACL pueden utilizarse en cualquier contexto de intercambio de datos. Sin embargo las formas SHACL proporcionadas son solo un punto de partida para los implementadores.

Al utilizar estas plantillas es posible identificar y corregir posibles desviaciones respecto a la especificación, mejorando la calidad de los metadatos producidos. Además, existen herramientas interactivas, como el [Banco de Pruebas de Interoperabilidad de la Comisión Europea](https://www.itb.ec.europa.eu/shacl/any/upload) [^1] o [SHACL playground](https://shacl-playground.zazuko.com/) [^2], que ofrece un servicio en línea donde es posible cargar y validar archivos RDF contra las formas SHACL de DCAT-AP-ES., que facilitan la validación de archivos DCAT-AP utilizando SHACL. ​

!!! info "Más información"

    - **✅ Cómo usar los validadores SHACL en diferentes stacks tecnológicos**: [github.com/datosgobes/DCAT-AP-ES/.../shacl/README.md](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/README.md)

    - Más información sobre la validación y las formas SHACL en [SHACL, un lenguaje para validar grafos RDF](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf).

    
# Formas SHACL de DCAT-AP-ES
Todas las versiones de los ficheros de formas de DCAT-AP-ES se encuentran en el repositorio de código [`shacl/{version}/`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/): 

- `shacl_common_shapes.ttl`: Restricciones comunes para todas las entidades.
- `shacl_catalog_shape.ttl:` Restricciones para catálogos.
- `shacl_dataservice_shape.ttl`: Restricciones para servicios de datos.
- `shacl_dataset_shape.ttl`: Restricciones para conjuntos de datos.
- `shacl_distribution_shape.ttl`: Restricciones para distribuciones.
- `shacl_dataservice_shape.ttl`: Restricciones para servicios de datos.
- `shacl_mdr-vocabularies.shape.ttl`: Vocabularios controlados y sus restricciones.
- `shacl_imports.ttl`: Definiciones de importación para ontologías externas.
- `shacl_mdr_imports.ttl`: Definiciones de importación para vocabularios MDR.

**`hvd/`**: Subdirectorio con restricciones adicionales para conjuntos de datos de alto valor (HVD):

- `shacl_common_hvd_shapes.ttl`: Restricciones comunes para todas las entidades HVD.
- `shacl_catalog_shape.ttl:` Restricciones para catálogos HVD.
- `shacl_dataservice_hvd_shape.ttl`: Restricciones para servicios de datos HVD.
- `shacl_dataset_hvd_shape.ttl`: Restricciones para conjuntos de datos HVD.
- `shacl_distribution_hvd_shape.ttl`: Restricciones para distribuciones HVD.

# Casos de Uso
*Sección no normativa*

Los diferentes casos de validación para DCAT-AP-ES se basan en el nivel de completitud de las comprobaciones y en la incorporación de conocimiento de fondo (vocabularios). Cada caso está diseñado para un escenario específico de intercambio de datos.

!!! tip "Consejo. Caso de uso."

    Para la mayoría de los casos de uso, se recomienda el [`Caso 1: DCAT-AP-ES completo`](/validation/#case_1_dcat_ap_es_full). Proporciona una validación completa de la coherencia básica y conformidad con vocabularios estándar.
    Si tu catálogo contiene conjuntos de datos de alto valor (HVD), considera utilizar el [`Caso 2: DCAT-AP-ES completo (HVD)`](/validation/#case_1_dcat_ap_es_full_hvd) para una validación que incluya los requerimientos del [Reglamento de ejecución (UE) 2023/138 de la Comisión Europea](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138).

    La elección del caso de validación adecuado depende de tus necesidades específicas y del contexto de intercambio de datos.

A continuación, se describe cada caso con las formas para la versión `DCAT-AP-ES 1.0.0` y se recomienda cuál utilizar para un catálogo:

## **Caso 1: DCAT-AP-ES completo** {#case_1_dcat_ap_es_full}
Incluye todas las restricciones necesarias para la coherencia técnica de las distintas entidades del modelo, incluyendo las restricciones de pertenencia a clases de rango y todos los vocabularios utilizados en DCAT-AP-ES.

*Formas SHACL*:

- *Estándar*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr-vocabularies.shape.ttl)

## **Caso 2: DCAT-AP-ES completo (HVD)** {#case_2_dcat_ap_es_full_hvd}
Incluye todas las restricciones anteriormente mencionadas, además de aquellas que permiten describir adecuadamente los conjuntos de datos de alto valor ([HVD](/#conjuntos_de_datos_de_alto_valor_high_value_datasets)).

*Formas SHACL*:

- *Estándar: Entidades principales y vocabularios controlados*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr-vocabularies.shape.ttl)

- *HVD: Restricciones específicas de conjuntos de alto valor*
  - [`shacl_common_hvd_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_dataservice_hvd_shape.ttl)
  - [`shacl_dataset_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_dataset_hvd_shape.ttl)
  - [`shacl_distribution_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_distribution_hvd_shape.ttl)

## **Caso 3: DCAT-AP-ES completo (con conocimiento de fondo)** {#case_3_dcat_ap_es_full_imports}
Extiende el [Caso 1](validation/#case_1_dcat_ap_es_full) con conocimiento de fondo, añadiendo conformidad con estándares externos.

*Formas SHACL*:

- *Estándar: Entidades principales y vocabularios controlados*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr-vocabularies.shape.ttl)

- *Importaciones*
  - [`shacl_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr_imports.ttl)

!!! info "¿Qué es el conocimiento de fondo?"
    El conocimiento de fondo (*background knowledge*) consiste en la importación de ontologías y vocabularios externos que complementan la validación. Estos archivos de importación (`shacl_imports.ttl` y `shacl_mdr_imports.ttl`) contienen definiciones de clases, propiedades y relaciones jerárquicas de los estándares utilizados en DCAT-AP-ES.
    
    Utilizar este conocimiento de fondo permite:
    
    1. *Validaciones semánticamente más ricas*: Al conocer la estructura completa de las ontologías.
    2. *Inferencia de tipos*: Permite detectar inconsistencias en la jerarquía de clases.
    3. *Validación de propiedades derivadas*: Comprueba relaciones que podrían no estar explícitas en los datos.
    
    Sin embargo, incluir este conocimiento de fondo puede hacer que la validación sea más lenta y consuma más recursos.

## **Caso 4: DCAT-AP-ES completo (HVD con conocimiento de fondo)** {#case_4_dcat_ap_es_full_hvd_imports}
Extiende el [Caso 1](validation/#case_1_dcat_ap_es_full) con conocimiento de fondo conformidad con estándares externos. También incluye las formas que permiten describir adecuadamente los conjuntos de datos de alto valor ([HVD](#conjuntos_de_datos_de_alto_valor_high_value_datasets)).

*Formas SHACL*:

- *Estándar: Entidades principales y vocabularios controlados*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr-vocabularies.shape.ttl)

- *HVD: Restricciones específicas de conjuntos de alto valor*
  - [`shacl_common_hvd_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_dataservice_hvd_shape.ttl)
  - [`shacl_dataset_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_dataset_hvd_shape.ttl)
  - [`shacl_distribution_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/hvd/shacl_distribution_hvd_shape.ttl)

- *Importaciones*
  - [`shacl_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/shacl_mdr_imports.ttl)

[^1]: SHACL validator: [github.com/ISAITB/shacl-validator](https://github.com/ISAITB/shacl-validator). Interoperability Test Bed, Interoperable Europe Unit, DIGIT, European Commission.
[^2]: Zazuko SHACL Playground: [github.com/zazuko/shacl-playground](https://github.com/zazuko/shacl-playground). Zazuko GmbH.