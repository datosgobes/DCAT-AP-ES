# Introduction

This document presents a detailed specification of the metadata used to describe catalogs and reusable data resources.

The metadata is described based on the Semantic Web paradigm, which implements resource description using the standard model for data exchange on the Web, RDF (Resource Description Framework). This approach allows different data cataloging systems to interact and exchange information effectively and consistently, achieving semantic interoperability to facilitate the discovery and findability of data resources, thus significantly increasing their value for reuse.

The application profile, hereinafter referred to as DCAT-AP-ES, is the metadata model included in the new version of the Public Sector Information Resources Interoperability Technical Standard ([NTI-RISP](https://datos.gob.es/en/doc-tags/nti-risp)), which is currently under administrative processing. The model adopts the guidelines of the European metadata exchange schema DCAT-AP with some additional restrictions and adjustments. This application profile is in turn based on the DCAT specification, an RDF vocabulary created with the objective of improving interoperability among online data catalogs, developed by the [Data Exchange Working Group](https://www.w3.org/2017/dxwg/) since it was published as a W3C Recommendation in 2014. The European profile version used as a reference for the preparation of DCAT-AP-ES is [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211), together with the elements described in the extension [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) to incorporate the modeling of [High Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir).

As is known, an open data catalog may consist solely of datasets or data services, although it is common to have both datasets and services represented by instances of the classes and properties specified in this model.

In this document, the main classes of the application profile are detailed: Catalog, Dataset, Distribution, and Data Service, as well as other classes relevant for providing comprehensive descriptive information about the reusable resources cataloged according to the DCAT-AP-ES model. The set of controlled vocabularies that must be used to harmonize the properties describing the cataloged elements is also specified.

!!! warning "Conventions Guide"
    As additional material to this technical guide, the [**datos.gob.es Conventions**](./conventions) are included. These establish **specific conventions** where **additional rules** are defined to address practical, semantic, or technical needs in the application of DCAT-AP-ES that complement this formal specification.

# High Value Datasets

In response to the growing importance of data in society and the economy, the European Commission adopted the [**European Commission Implementing Regulation (EU) 2023/138**](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138) (*High Value Datasets Implementing Regulation, HVD IR*) on December 21, 2022. This regulation establishes clear guidelines for public bodies regarding the availability of high value datasets and aims to improve the quality, accessibility, and use of a specific set of key data within the public sector. To achieve this, the HVD regulation sets specific requirements for the metadata associated with the published datasets.

!!! note "Relationship between the specification and data-specific regulations"
    
    The **DCAT-AP-ES application profile represents the minimum core metadata** applied to all entities in the model. However, **compliance with the specification does not exempt compliance with the specific regulations applicable** in each sector, as is the case with the HVD regulation. In particular, datasets that meet the HVD criteria may include additional metadata or restrictions that are not covered by DCAT-AP-ES but are required by law.

# DCAT-AP-ES Metadata Model {#dcat-ap-es-model}

The fundamental elements of the model are detailed below, beginning with the UML diagram, the class relationships, the namespace used in the specification, and the set of controlled vocabularies.

## Model Diagram {#uml}

The DCAT-AP-ES model is presented below as a UML diagram that illustrates the specification described in this document. To facilitate interpretation, details included in the description of each metadata element have been omitted. In essence, the key classes and some relevant supporting ones are included.

![](img/uml/dcat-ap-es.drawio "Illustration. UML diagram of the DCAT-AP-ES metadata model"){ align=center width="100%"}

## DCAT-AP-ES Application Profile Classes {#dcat-ap-es-entities}

The most relevant classes used in the model are listed below:

* [**Catalog**](#catalog_-_class_dcatcatalog_-_mandatory). The **`dcat:Catalog`** class represents a catalog, which is a collection of data where each individual element is a metadata record describing some resource. The content of a catalog consists of collections of metadata about datasets, data services, or other types of resources, including other catalogs. It functions as a unified access point that facilitates the search and reuse of data resources.
* [**Catalog Record**](#catalog_record_-_class_dcatcatalogrecord_-_optional). The Catalog Record class (**`dcat:CatalogRecord`**) describes individual entries within a data catalog, each being a specific metadata record. A catalog record references an entity in the catalog, which can be a dataset or a data service. It is mainly used to explicitly collect provenance information about the entries in a catalog.
* [**Data Service**](#data_service_-_class_dcatdataservice_-_optional). The Data Service class (**`dcat:DataService`**) represents a collection of operations accessible through an interface (API) that provides access to one or more datasets or data processing functions. Its use allows the cataloging of various types of data services, facilitating the implementation of functionalities for the programmatic handling and/or exploitation of data.
* **[Dataset](#dataset_-_class_dcatdataset_-_mandatory)**. The Dataset class (**`dcat:Dataset`**) represents a conceptualization of a collection of information published by a single identifiable agent. The notion of a dataset is broad, intending to accommodate the types of resources that arise from a publication context, which can be represented in many forms, including numbers, text, images, sound, and other media or types, any of which could be collected in a dataset.
* [**Distribution**](#distribution_-_class_dcatdistribution_-_recommended). The Distribution class of a dataset (**`dcat:Distribution`**) represents an accessible and reusable form of a dataset, such as a downloadable file.
* [**Agent**](#agent_-_class_foafagent_-_mandatory). The Agent class (**`foaf:Agent`**) is used to represent any organization or person that has the competence to perform actions on a catalog and the cataloged resources. Its main function is to provide concrete references about the different actors who can intervene with different roles in the management of a data catalog.
* [**Identifier**](#note-dcat_dataset-dct_identifier). The Identifier class of a dataset (**`dct:Identifier`**) is used to express the unique reference assigned to a dataset within the context of a specific identifier scheme.
* [**Location**](#location_-_class_dctlocation_-_optional). The Location class (**`dct:Location`**) is used to identify a geographic region or place. It can be represented using a controlled vocabulary or by expressing geographic coordinates that delimit a specific area.
* [**Period of Time**](#period_of_time_-_class_dctperiodoftime_-_optional). The Period of Time class (**`dct:PeriodOfTime`**) is used to define a time interval that is delimited by a start date and an end date.
* [**Checksum**](#checksum_-_class_spdxchecksum_-_optional). The Checksum class (**`spdx:Checksum`**) is used to specify the method implemented and the result obtained to ensure the integrity of dataset distributions, i.e., that their content has not been altered.
* [**Relationship**](#relationship_between_resources_-_class_dcatrelationship_-_optional). The Relationship class between resources (**`dcat:Relationship`**) is used to specify additional information regarding a relationship between resources or agents, providing context on how these resources are interrelated.

## Namespaces Used in the Model {#dcat-ap-es-namespaces}

Each property of a class that describes an attribute of the catalog, catalog record, data service, dataset, distribution, etc., reuses terms from other existing vocabularies. They are specified via a URI determined by the combination of the corresponding vocabulary’s prefix (referenced in the DCAT-AP-ES model’s namespace) and the name of the class or property. For example, the property `dct:issued` of the Catalog class is expressed equivalently in its abbreviated and extended forms as follows:

!!! info "Note on Namespaces"

    `dct:issued` is equivalent to `http://purl.org/dc/terms/issued`

Below, generic vocabularies that configure the namespaces reused in the implementation of the DCAT-AP-ES model are listed:

| **Vocabulary** | **Prefix** | **URI** |
| --- | --- | --- |
| Asset Description Metadata Schema | `adms:` | `http://www.w3.org/ns/adms#` |
| Dataset Catalog (dcat) | `dcat:` | `http://www.w3.org/ns/dcat#` |
| DCAT Application profile for data portals | `dcatap:` | `http://data.europa.eu/r5r/` |
| Dublin Core Terms | `dct:` | `http://purl.org/dc/terms/` |
| Friend Of A Friend (FOAF) | `foaf:` | `http://xmlns.com/foaf/0.1/` |
| Location Core Vocabulary | `locn:` | `http://www.w3.org/ns/locn#` |
| Web Ontology Document | `owl:` | `http://www.w3.org/2002/07/owl#` |
| Open Digital Rights Language | `odrl:` | `http://www.w3.org/ns/odrl/2/` |
| Prov Family of Documents | `prov:` | `http://www.w3.org/ns/prov#` |
| Resource Description Framework | `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| Resource Description Framework Schema | `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| Simple Knowledge Organization System (SKOS) | `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| Software Package Data Exchange | `spdx:` | `http://spdx.org/rdf/terms#` |
| W3C Time Ontology | `time:` | `http://www.w3.org/2006/time#` |
| vCard Ontology | `vcard:` | `http://www.w3.org/2006/vcard/ns#` |
| XML Schema | `xsd:` | `http://www.w3.org/2001/XMLSchema#` |

## Controlled Vocabularies used in the model {#dcat-ap-es-vocabularies}

The following is a list of properties that must be adjusted using the controlled vocabularies indicated in the table below, in order to guarantee a minimum level of interoperability.

| **Property** | **Entity** | **Vocabulary** | **Vocabulary URI** |
| --- | --- | --- | --- |
| **dcatap:availability** | Distribution | [Planned availability](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/planned-availability) | `http://publications.europa.eu/resource/authority/planned-availability` |
| **dct:accessRights** | Dataset<br>DataService | [Access right](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/access-right) | `http://publications.europa.eu/resource/authority/access-right` |
| **dct:accrualPeriodicity** | Dataset | [Frequency](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/frequency) | `http://publications.europa.eu/resource/authority/frequency` |
| **dct:format** | Distribution | [File type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type) | `http://publications.europa.eu/resource/authority/file-type` |
| **dcatap:hvdCategory** | Dataset<br>DataService | [HVD Category](https://op.europa.eu/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/bna/asd487ae75) | `http://data.europa.eu/bna/asd487ae75` |
| **dct:language** | Catalog<br>Dataset<br>CatalogRecord<br>Distribution | [Language](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/language) | `http://publications.europa.eu/resource/authority/language` |
| **dct:license** | Catalog<br>DataService<br>Distribution | [Licence](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/licence) | `http://publications.europa.eu/resource/authority/licence` |
| **dcat:mediaType** | Distribution | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| **dct:spatial** | Catalog<br>Dataset | <ul><li>[NTI-RISP Territory Taxonomy](https://datos.gob.es/es/recurso/sector-publico/territorio)</li><li> [Continent](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/continent)</li><li>[Countries and territories](http://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/country)</li><li>[Administrative territorial unit](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/atu)</li><li>[Place](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/place)</li><li>[Geonames](http://www.geonames.org/)</li></ul> | <ul><li>`http://datos.gob.es/es/recurso/sector-publico/territorio`</li><li>`http://publications.europa.eu/resource/authority/continent`</li><li>`http://publications.europa.eu/resource/authority/country`</li><li>`http://publications.europa.eu/resource/authority/atu`</li><li>`http://publications.europa.eu/resource/authority/place`</li><li>`http://sws.geonames.org/`</li></ul> |
| **dcat:theme** | Dataset | <ul><li>[Taxonomy of primary sectors NTI-RISP](http://datos.gob.es/kos/sector-publico/sector)</li><li> [DCAT-AP Data Theme)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[INSPIRE Register Themes](http://inspire.ec.europa.eu/theme)</li></ul>  | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| **dcat:themeTaxonomy** | Catalog | <ul><li>[Taxonomy of primary sectors NTI-RISP](http://datos.gob.es/kos/sector-publico/sector)</li><li> [DCAT-AP Data Theme)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[INSPIRE Register Themes](http://inspire.ec.europa.eu/theme)</li></ul> | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| **dct:type** | Agent | [ADMS publisher type vocabulary](http://purl.org/adms/publishertype/1.0) | `http://purl.org/adms/publishertype/1.0` |
| **dct:type** | Dataset | [Dataset type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/dataset-type) | `http://publications.europa.eu/resource/authority/dataset-type` |
| **adms:status** | Distribution | [Distribution status](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/distribution-status) | `http://publications.europa.eu/resource/authority/distribution-status` |
