!!! tip "Ejemplos prácticos de implementación"

    Aquí encontrarás prototipos listos para usar que demuestran cómo implementar el [modelo de metadatos DCAT-AP-ES](/#dcat-ap-es-model) en diferentes formatos: [`RDF/XML`](https://www.w3.org/TR/rdf-syntax-grammar/) y [Turtle `(TTL)`](https://www.w3.org/TR/turtle/). 
    
    Estos ejemplos te guiarán en el uso de [propiedades obligatorias, recomendadas y opcionales](/#relacion_de_metadatos_del_modelo_dcat-ap-es) para describir las entidades principales del modelo.

!!! example "Convenciones para la especificación de ejemplos"

    Se establece las siguientes convenciones de nombrado para su uso en todos los ejemplos definidos: 

    * Base de la URIs: `http://dcat-ap-es.ejemplo.org `
    * URI catálogo: `http://dcat-ap-es.ejemplo.org/catalogo` 
    * URI dataservice: `http://dcat-ap-es.ejemplo.org/dataservice/dataservice-ejemplo-1 `
    * URI dataset: `http://dcat-ap-es.ejemplo.org/dataset/dataset-ejemplo-1` 
    * URI distribución: `http://dcat-ap-es.ejemplo.org/resource/distribucion-ejemplo-1` 
    * URI organismo: `http://datos.gob.es/recurso/sector-publico/org/Organismo/Identificador-Organismo`


# Catálogo - Clase: [`dcat:Catalog`](/#catalogo_-_clase_dcatcatalog_-_obligatorio)
## Catálogo - Propiedades obligatorias

Este ejemplo muestra cómo declarar un catálogo de datos utilizando **únicamente las propiedades obligatorias** según el perfil DCAT-AP-ES. Incluye metadatos esenciales como: Título, Descripción, Página web, Publicador, Licencia, Taxonomía de temas, Fecha de creación, Fecha de actualización e Idioma.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E1_Catalogo_solo_obligatorias.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E1_Catalogo_solo_obligatorias.ttl"
    ```

## Catálogo - Propiedades obligatorias y recomendadas

Este ejemplo amplía el anterior, incluyendo tanto las **propiedades obligatorias como las recomendadas** para la descripción de un catálogo DCAT-AP-ES. Además de los metadatos esenciales, se añaden propiedades como la cobertura geográfica (`dct:spatial`) e incluyendo la descripción básica de un conjunto de datos (`dcat:dataset`) y servicios de datos (`dcat:service`).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E2_Catalogo_obligatorias_recomendadas.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E2_Catalogo_obligatorias_recomendadas.ttl"
    ```

## Catálogo - Propiedades obligatorias, recomendadas y opcionales

Este ejemplo presenta una descripción completa de un catálogo DCAT-AP-ES, utilizando **propiedades obligatorias, recomendadas y opcionales**. Se incluyen metadatos adicionales como el creador del catálogo como una organización (`dct:creator`) y la declaración de derechos de acceso ligados al uso de los datos del catálogo (`dct:rights`). Se detalla además que el catálogo tiene un subcatálogo vinculado (`dct:hasPart`).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E3_Catalogo_obligatorias_recomendadas_opcionales.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E3_Catalogo_obligatorias_recomendadas_opcionales.ttl"
    ```

## Catálogo - Concreción del publicador

Este ejemplo muestra cómo **detallar la información del publicador de un catálogo, utilizando propiedades** para especificar:

*   Identificador persistente (`dct:identifier`)
*   Nombre (`foaf:name`)
*   Correo electrónico (`foaf:mbox`)
*   Tipo de organización dentro de la estructura del Estado (`dct:type`)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E4_Catalogo_publisher_organizacion.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E4_Catalogo_publisher_organizacion.ttl"
    ```

## Catálogo - Migración desde NTI-RISP a DCAT-AP-ES {#catalogo_-_nti_dcatapes}

Este ejemplo muestra cómo migrar un catálogo modelado originalmente según NTI-RISP (2013) al perfil DCAT-AP-ES. Facilitando la interoperabilidad y enriqueciendo los metadatos del catálogo, permitiendo su integración en portales nacionales y europeos. El proceso consiste en mapear las propiedades clave de NTI-RISP a DCAT-AP-ES, añadiendo vocabularios y elementos recomendados por el nuevo perfil.

El catálogo `http://dcat-ap-es.ejemplo.org/catalogo` incluye información esencial como título, descripción, publicador, fechas clave, página web, temáticas, idiomas, términos de uso y referencia a datasets. Además, incorpora elementos recomendados por DCAT-AP-ES, como los temas, el punto de contacto y la legislación aplicable. Como normal general se alinean los vocabularios europeos, así como se incluye la descripción de los nuevos Servicios de Datos (`dcat:DataService`)

!!! tip "Ejemplo original NTI 2013"

    El ejemplo original de catálogo NTI-RISP 2013 está disponible en:
    [Catálogo NTI-RISP a DCAT-AP-ES](https://datosgobes.github.io/NTI-RISP/examples/#ejemplo_de_migracion_catalogo_nti-risp_a_dcat-ap-es)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/1.0.0/E_DCAT-AP-ES_Catalog.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/1.0.0/E_DCAT-AP-ES_Catalog.ttl"
    ```

## Catálogo HVD - Migración desde NTI-RISP a DCAT-AP-ES HVD {#catalogo_-_nti_dcatapes_hvd}

Este ejemplo ilustra cómo adaptar un catálogo NTI-RISP para cumplir con los requisitos HVD. La motivación es asegurar que los datos de alto valor estén disponibles mediante APIs y cumplan con la normativa europea, añadiendo propiedades específicas como la categoría HVD, legislación aplicable y más detalles de los servicios de datos.

El catálogo `http://dcat-ap-es.ejemplo.org/catalogo` se enriquece con información sobre servicios de datos (APIs), datasets HVD, contacto, legislación y disponibilidad, siguiendo el reglamento HVD. Así, se facilita la transición y el cumplimiento normativo para la publicación de datos de alto valor.

!!! tip "Ejemplo original NTI 2013"

    El ejemplo original de catálogo NTI-RISP 2013 está disponible en:
    [Catálogo NTI-RISP a DCAT-AP-ES](https://datosgobes.github.io/NTI-RISP/examples/#ejemplo_de_migracion_catalogo_nti-risp_a_dcat-ap-es)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/1.0.0/E_DCAT-AP-ES_Catalog_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/1.0.0/E_DCAT-AP-ES_Catalog_HVD.ttl"
    ```

# Servicio de datos - Clase: [`dcat:DataService`](/#servicio_de_datos_-_clase_dcatdataservice_-_opcional)
## Servicio de datos - Especificación de servicios de acceso a datos

El ejemplo describe **un catálogo que contiene el registro de un único servicio de datos que proporciona el acceso a un servicio CSW** sin especificar qué datasets sirve. El servicio de datos CSW cumple con el IR HVD e INSPIRE, está descrito como un servicio de descubrimiento, está disponible bajo derechos de acceso público, es compatible con el estándar CSW de OGC, cuenta con una licencia de reutilización CC-BY 4.0, el ámbito territorial cubierto por el dataset está delimitado por un rectangular para la que se especifican sus coordenadas y detalla un punto de contacto para trasladar cuestiones relativas al servicio mediante un formulario web o un correo electrónico.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E10_Data_Service_CSW_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E10_Data_Service_CSW_HVD.ttl"
    ```

## Servicio de datos - *DataService* HVD

Este ejemplo ilustra cómo especificar *datasets* accesibles a través de **servicios de datos (APIs), cumpliendo con el [Reglamento HVD (High-Value Datasets)](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138)**.

De acuerdo con el reglamento, los HVD deben estar disponibles a través de APIs. Para ello, el publicador debe disponer de una API implementada en una plataforma, a través de la cual los reutilizadores tendrán acceso a los datos en tiempo real. Esta plataforma API sirve varios conjuntos de datos (`dataset-HVD-ejemplo-1` y `dataset-ejemplo-1`).

Dado que la API sirve al menos un HVD, se aplican los requisitos de implementación según el reglamento HVD. Por tanto, el publicador de la API debe asegurar que el `dcat:endpointURL` declarado sea persistente, es decir, estable en el tiempo (por ejemplo, la implementación de una nueva plataforma API o el cambio de nombre del publicador no deben afectar la URL del punto final).

Además, se proporciona información sobre el uso de la API, mediante:

*   Documentación técnica basada en el [estándar OpenAPI](https://swagger.io/specification/)
*   Un SLA (*Service Level Agreement*) para documentar la calidad del servicio

Por último, se añade la propiedad obligatoria que informa sobre los canales de contacto habilitados por el publicador.

Para simplificar la presentación del ejemplo, se obvia la especificación de las propiedades del catálogo.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E9_Data_Service_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E9_Data_Service_HVD.ttl"
    ```

# Conjunto de datos - Clase: [`dcat:Dataset`](/#conjunto_de_datos_-_clase_dcatdataset_-_obligatorio)
## Conjunto de datos - *Datasets* HVD y no HVD

Este ejemplo describe **un catálogo que contiene dos conjuntos de datos HVD y no HVD:**:

*   **`dataset-HVD-ejemplo-1`**: Un conjunto de datos que **sí** está dentro del alcance del [Reglamento HVD (High-Value Datasets)](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138).
*   **`dataset-ejemplo-1`**: Un conjunto de datos que **no** está dentro del alcance del Reglamento HVD.

Ambos conjuntos de datos están dentro del alcance de la [Directiva INSPIRE](http://data.europa.eu/eli/dir/2007/2/oj).

El catálogo especifica detalles sobre:

*   El publicador (`dct:publisher`)
*   El creador (`dct:creator`)
*   Los derechos de acceso (`dct:rights`)
*   La referencia a otro catálogo vinculado (`dct:hasPart`)

El conjunto de datos `dataset-HVD-ejemplo-1` también está etiquetado con la categoría HVD adecuada, utilizando el concepto más granular [`Preservación de la naturaleza y biodiversidad`](http://data.europa.eu/bna/c_b7f6a4f3).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E6_Dataset_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E6_Dataset_HVD.ttl"
    ```

## Conjunto de datos - Distribuciones de *datasets* HVD

El reglamento de implementación HVD requiere que los datasets HVD puedan ser descargables (*bulk download*) siempre que resulte pertinente. Los datasets se pueden descargar en diferentes formatos y niveles de detalle. En este ejemplo, las **distribuciones están disponibles en dos formatos: RDF y formato shapefile (SHP)** de ESRI. De acuerdo con el reglamento HVD, estos datasets de ejemplo están disponibles como mínimo en descarga masiva con una granularidad de 5 metros y con una frecuencia de actualización mensual. En función de estos requisitos, el publicador del dataset decide indicar que la distribución SHP es una descarga masiva HVD.

Además, se describe el modelo de datos asociado a la distribución proporcionando documentación detallada del esquema de datos mediante el metadato dct:conformsTo.

Se especifican también las condiciones de reutilización mediante una licencia tipo (`CC-BY 4.0`) y se indica que el estado de disponibilidad de ambas distribuciones es estable, describiendo de esta forma, que los datos permanecerán disponibles a largo plazo.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E7_Distribuciones_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E7_Distribuciones_HVD.ttl"
    ```