!!! tip "Practical implementation examples"

    Here you will find ready-to-use prototypes that demonstrate how to implement the [DCAT-AP-ES metadata model](index.md#dcat-ap-es-model) in different formats: [`RDF/XML`](https://www.w3.org/TR/rdf-syntax-grammar/) and [Turtle `(TTL)`](https://www.w3.org/TR/turtle/). 
    
    These examples will guide you in using [mandatory, recommended and optional properties](index.md#dcat-ap-es-model-relations) to describe the main entities of the model.

!!! Success "Migrate your catalog"
    ^^Specific examples are included if you already have an RDF catalog compliant with NTI-RISP (2013)^^ and want to update it: 

    - [**Migrate to DCAT-AP-ES**](#catalogo_-_nti_dcatapes) <span style="color:#00bfa5"><b>:material-arrow-up-right:</b></span> 
    - [**Migrate to DCAT-AP-ES HVD**](#catalogo_-_nti_dcatapes_hvd) <span style="color:#00bfa5"><b>:material-arrow-up-right:</b></span> 

!!! example "Conventions for example specification"

    The following naming conventions are established for use in all defined examples: 

    * URI base: `http://dcat-ap-es.ejemplo.org `
    * Catalog URI: `http://dcat-ap-es.ejemplo.org/catalogo` 
    * Dataservice URI: `http://dcat-ap-es.ejemplo.org/dataservice/dataservice-ejemplo-1 `
    * Dataset URI: `http://dcat-ap-es.ejemplo.org/dataset/dataset-ejemplo-1` 
    * Distribution URI: `http://dcat-ap-es.ejemplo.org/resource/distribucion-ejemplo-1` 
    * Organization URI: `http://datos.gob.es/recurso/sector-publico/org/Organismo/Identificador-Organismo`

# Templates

## DCAT-AP-ES minimum metadata core {#dcatapes_minimal}

This template provides an implementation of **[the minimum mandatory metadata core](index.md#dcat-ap-es-detailed-model)** according to the DCAT-AP-ES profile, aligned with the Technical Interoperability Standard for Reuse of Public Sector Information Resources (NTI-RISP) and the technical conventions of datos.gob.es.

It includes only the **mandatory entities and properties** to describe an open data catalog according to the current formal specification. It is the basic reference for publication and federation of interoperable metadata in the national catalog, and can be used as an example or starting point for automatic generation of DCAT-AP-ES compliant catalogs.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/1.0.0/E_DCAT-AP-ES_minimal.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/1.0.0/E_DCAT-AP-ES_minimal.ttl"
    ```

## Complete DCAT-AP-ES template {#dcatapes_full_optional}

This template provides a comprehensive implementation of the DCAT-AP-ES profile, showing **all available properties** at all applicability levels: mandatory, recommended and optional. 

Through this complete serialization, you can explore how to enrich the description of catalogs, datasets, distributions and data services with advanced metadata. It constitutes a comprehensive reference template to maximize the interoperability and quality of metadata, facilitating its integration into national and international open data ecosystems according to current technical specifications.

=== "RDF/XML"
    [`RDF/XML`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/examples/rdf/1.0.0/E_DCAT-AP-ES_full_optional.rdf) <span style="color:#00bfa5"><b>:material-arrow-up-right:</b></span>

=== "TTL"
    [`Turtle (TTL)`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/examples/ttl/1.0.0/E_DCAT-AP-ES_full_optional.ttl) <span style="color:#00bfa5"><b>:material-arrow-up-right:</b></span>

## Migration from NTI-RISP to DCAT-AP-ES {#catalogo_-_nti_dcatapes}

This example shows how to migrate a catalog originally modeled according to NTI-RISP (2013) to the DCAT-AP-ES profile. Facilitating interoperability and enriching the catalog metadata, allowing its integration into national and European portals. The process consists of mapping the key properties of NTI-RISP to DCAT-AP-ES, adding vocabularies and elements recommended by the new profile.

The catalog `http://dcat-ap-es.ejemplo.org/catalogo` includes essential information such as title, description, publisher, key dates, web page, themes, languages, terms of use and reference to datasets. In addition, it incorporates elements recommended by DCAT-AP-ES, such as themes, contact point and applicable legislation. As a general rule, European vocabularies are aligned, and the description of the new Data Services (`dcat:DataService`) is included.

!!! tip "Original NTI 2013 example"

    The original NTI-RISP (2013) catalog example is available at:
    [NTI-RISP Catalog to DCAT-AP-ES](https://datosgobes.github.io/NTI-RISP/examples/#catalogo_-_nti_dcatapes)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/1.0.0/E_DCAT-AP-ES_Catalog.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/1.0.0/E_DCAT-AP-ES_Catalog.ttl"
    ```

## Migration from NTI-RISP to DCAT-AP-ES HVD {#catalogo_-_nti_dcatapes_hvd}

This example illustrates how to adapt an NTI-RISP catalog to meet HVD requirements. The motivation is to ensure that high-value data is available through APIs and complies with European regulations, adding specific properties such as HVD category, applicable legislation and more details about data services.

The catalog `http://dcat-ap-es.ejemplo.org/catalogo` is enriched with information about data services (APIs), HVD datasets, contact, legislation and availability, following the HVD regulation. Thus, the transition and regulatory compliance for the publication of high-value data is facilitated.

!!! tip "Original NTI 2013 example"

    The original NTI-RISP (2013) catalog example is available at:
    [NTI-RISP Catalog to DCAT-AP-ES](https://datosgobes.github.io/NTI-RISP/examples/#catalogo_-_nti_dcatapes)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/1.0.0/E_DCAT-AP-ES_Catalog_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/1.0.0/E_DCAT-AP-ES_Catalog_HVD.ttl"
    ```

# Catalog - Class: [`dcat:Catalog`](index.md#Catalog)
## Catalog - Mandatory properties

This example shows how to declare a data catalog using **only mandatory properties** according to the DCAT-AP-ES profile. It includes essential metadata such as: Title, Description, Web page, Publisher, License, Theme taxonomy, Creation date, Modification date and Language.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E1_Catalogo_solo_obligatorias.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E1_Catalogo_solo_obligatorias.ttl"
    ```

## Catalog - Mandatory and recommended properties

This example extends the previous one, including both **mandatory and recommended properties** for the description of a DCAT-AP-ES catalog. In addition to essential metadata, properties such as geographic coverage (`dct:spatial`) are added, including the basic description of a dataset (`dcat:dataset`) and data services (`dcat:service`).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E2_Catalogo_obligatorias_recomendadas.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E2_Catalogo_obligatorias_recomendadas.ttl"
    ```

## Catalog - Mandatory, recommended and optional properties

This example presents a complete description of a DCAT-AP-ES catalog, using **mandatory, recommended and optional properties**. Additional metadata is included such as the catalog creator as an organization (`dct:creator`) and the declaration of access rights linked to the use of catalog data (`dct:rights`). It is also detailed that the catalog has a linked sub-catalog (`dct:hasPart`).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E3_Catalogo_obligatorias_recomendadas_opcionales.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E3_Catalogo_obligatorias_recomendadas_opcionales.ttl"
    ```

## Catalog - Publisher specification

This example shows how to **detail the information of a catalog publisher, using properties** to specify:

*   Persistent identifier (`dct:identifier`)
*   Name (`foaf:name`)
*   Email (`foaf:mbox`)
*   Type of organization within the State structure (`dct:type`)

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E4_Catalogo_publisher_organizacion.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E4_Catalogo_publisher_organizacion.ttl"
    ```


# Data Service - Class: [`dcat:DataService`](index.md#DataService)
## Data Service - Specification of data access services

The example describes **a catalog that contains the record of a single data service that provides access to a CSW service** without specifying which datasets it serves. The CSW data service complies with the IR HVD and INSPIRE, is described as a discovery service, is available under public access rights, is compatible with the OGC CSW standard, has a CC-BY 4.0 reuse license, the territorial scope covered by the dataset is delimited by a rectangle for which its coordinates are specified and details a contact point to transfer questions regarding the service through a web form or email.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E10_Data_Service_CSW_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E10_Data_Service_CSW_HVD.ttl"
    ```

## Data Service - HVD *DataService*

This example illustrates how to specify *datasets* accessible through **data services (APIs), complying with the [HVD Regulation (High-Value Datasets)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0138)**.

According to the regulation, HVDs must be available through APIs. For this, the publisher must have an API implemented on a platform, through which reusers will have access to data in real time. This API platform serves several datasets (`dataset-HVD-ejemplo-1` and `dataset-ejemplo-1`).

Since the API serves at least one HVD, implementation requirements apply according to the HVD regulation. Therefore, the API publisher must ensure that the declared `dcat:endpointURL` is persistent, that is, stable over time (for example, the implementation of a new API platform or the publisher's name change should not affect the endpoint URL).

In addition, information about API usage is provided through:

*   Technical documentation based on the [OpenAPI standard](https://swagger.io/specification/)
*   An SLA (*Service Level Agreement*) to document service quality

Finally, the mandatory property that informs about the contact channels enabled by the publisher is added.

To simplify the presentation of the example, the specification of catalog properties is omitted.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E9_Data_Service_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E9_Data_Service_HVD.ttl"
    ```

# Dataset - Class: [`dcat:Dataset`](index.md#Dataset)
## Dataset - HVD and non-HVD *Datasets*

This example describes **a catalog containing two HVD and non-HVD datasets:**:

*   **`dataset-HVD-ejemplo-1`**: A dataset that **is** within the scope of the [HVD Regulation (High-Value Datasets)](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0138).
*   **`dataset-ejemplo-1`**: A dataset that **is not** within the scope of the HVD Regulation.

Both datasets are within the scope of the [INSPIRE Directive](http://data.europa.eu/eli/dir/2007/2/oj).

The catalog specifies details about:

*   The publisher (`dct:publisher`)
*   The creator (`dct:creator`)
*   Access rights (`dct:rights`)
*   The reference to another linked catalog (`dct:hasPart`)

The dataset `dataset-HVD-ejemplo-1` is also tagged with the appropriate HVD category, using the most granular concept [`Nature and biodiversity preservation`](http://data.europa.eu/bna/c_b7f6a4f3).

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E6_Dataset_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E6_Dataset_HVD.ttl"
    ```

## Dataset - HVD *dataset* distributions

The HVD implementation regulation requires that HVD datasets be downloadable (*bulk download*) whenever relevant. Datasets can be downloaded in different formats and levels of detail. In this example, **distributions are available in two formats: RDF and ESRI shapefile (SHP) format**. According to the HVD regulation, these example datasets are available at least in bulk download with a granularity of 5 meters and with a monthly update frequency. Based on these requirements, the dataset publisher decides to indicate that the SHP distribution is an HVD bulk download.

In addition, the data model associated with the distribution is described by providing detailed documentation of the data schema through the dct:conformsTo metadata.

The reuse conditions are also specified through a standard license (`CC-BY 4.0`) and it is indicated that the availability status of both distributions is stable, thus describing that the data will remain available in the long term.

=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/E7_Distribuciones_HVD.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/E7_Distribuciones_HVD.ttl"
    ```
