# Introduction

This document presents a detailed specification of the metadata that allows the description of catalogs and reusable data resources.

The metadata is described based on the Semantic Web paradigm, which implements resource description using the standard model for data exchange on the Web, RDF (Resource Description Framework). This approach allows different data cataloging systems to interact and exchange information effectively and consistently, achieving semantic interoperability to facilitate the search and discoverability of data resources, considerably improving their value for reuse.

The application profile, hereinafter DCAT-AP-ES, is the metadata model included in the new version of the Technical Interoperability Standard for Public Sector Information Resources ([NTI-RISP](https://datos.gob.es/es/doc-tags/nti-risp)), which is currently undergoing administrative processing. The model adopts the guidelines of the European metadata exchange schema DCAT-AP with some additional restrictions and adjustments, an application profile which in turn is based on the DCAT specification, an RDF vocabulary created with the aim of improving interoperability between online data catalogs that has been developed by the [Dataset Exchange Working Group](https://www.w3.org/2017/dxwg/) since it was published as a W3C recommendation in 2014. The version of the European profile taken as a reference for the development of DCAT-AP-ES is [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) together with the elements described in the [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) extension to incorporate the modeling of [High Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) (*High Value Datasets*).

!!! info "Profile Conformance (SEMIC)"
    [DCAT-AP-ES has been evaluated according to **SEMIC guidelines for DCAT-AP reuse**](#semic-reuse-guidelines), achieving an **overall conformance of approximately 94%**, with **three non-critical improvement actions**.

As is well known, an open data catalog can consist solely of datasets or data services, although it is usual for it to have both datasets and services and is represented by instances of the classes and properties specified in this model.

This document details the main classes of the application profile: Catalog, Dataset, Distribution and Data Service, as well as other relevant classes for complete descriptive information of the reusable elements cataloged according to the DCAT-AP-ES model. It also specifies the set of controlled vocabularies that must be used to adjust the properties that describe the cataloged elements.

!!! warning "Conventions Guide"
    As additional material to this technical guide, the [**datos.gob.es Conventions**](conventions.md) are included, which establish **specific conventions** where **additional rules** are defined to address practical, semantic or technical needs of the DCAT-AP-ES application that complement this formal specification.

In response to the growing importance of data in society and the economy, the European Commission adopted the [**Commission Implementing Regulation (EU) 2023/138**](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0138) (*High Value Datasets Implementing Regulation, HVD IR*) on December 21, 2022. This regulation establishes clear guidelines for public bodies in the availability of high-value datasets and aims to improve the quality, accessibility and use of a specific set of key data within the public sector. To achieve this, the HVD regulation establishes specific requirements for the metadata associated with published datasets.


!!! note "Relationship between specification and specific data legislation"

    The **DCAT-AP-ES application profile is the minimum metadata core** that applies to all entities in the model. However, **conformance with the specification does not exempt compliance with applicable specific regulations** in each sector, as is the case with the HVD regulation. In particular, datasets that meet HVD criteria may include additional metadata or restrictions that are not covered by DCAT-AP-ES but are covered by legislation.

# DCAT-AP-ES Metadata Model {#dcat-ap-es-model}

The following details the fundamental elements of the model, beginning with the UML diagram, the list of classes, the namespace used in the specification, and the list of controlled vocabularies.

!!! info "Priority of Spanish version over other language versions"
    If several versions of the document exist in different languages, **the Spanish version will prevail** as the primary reference for interpretation and application.

## Model Diagram {#uml}

The DCAT-AP-ES model is represented below as a UML diagram that illustrates the specification described in this document. To facilitate its interpretation, details that are included in the description of each metadata item in this document are omitted. Fundamentally, key classes and some relevant ones that support the former are included.

![](img/uml/dcat-ap-es.drawio "Illustration. UML schema of the DCAT-AP-ES metadata model"){ align=center width="100%"}

!!! info "Priority of formal specification over diagram"
    Although the UML diagram facilitates visual understanding, **the DCAT-AP-ES model described in this document prevails over any graphical interpretation**. In case of discrepancy, the formal definitions and restrictions of the model must be followed.

## DCAT-AP-ES Application Profile Classes {#dcat-ap-es-entities}

The most relevant classes used in the model are listed below:

* [**Catalog**](#Catalog). The [**`dcat:Catalog`**](http://www.w3.org/ns/dcat#Catalog) class represents a catalog, which is a dataset in which each individual element is a metadata record describing some resource. The content of a catalog consists of collections of metadata about datasets, data services, or other types of resources, including other catalogs. It functions as a unified access point that facilitates the search and reuse of data resources.
* [**Catalog Record**](#CatalogRecord). The Catalog Record class ([**`dcat:CatalogRecord`**](http://www.w3.org/ns/dcat#CatalogRecord)) describes individual entries within a data catalog, each one being a specific metadata record. A catalog record references an entity in the catalog which can be a dataset or a data service. It is primarily used to explicitly collect provenance information about entries in a catalog.
* [**Data Service**](#DataService). The Data Service class ([**`dcat:DataService`**](http://www.w3.org/ns/dcat#DataService)) represents a collection of operations accessible through an interface (API) that provides access to one or more datasets or data processing functions. Its use enables the cataloging of various types of data services, facilitating the implementation of functionalities for the programmatic handling and/or exploitation of data.
* [**Dataset**](#Dataset). The Dataset class ([**`dcat:Dataset`**](http://www.w3.org/ns/dcat#Dataset)) represents a conceptualization of a collection of information published by a single identifiable agent. The notion of dataset is broad with the intention of accommodating the types of resources that arise from a publication context and can be represented in many forms, including numbers, text, images, sound, and other media or types, any of which could be compiled into a dataset.
* [**Distribution**](#Distribution). The Distribution of a dataset class ([**`dcat:Distribution`**](http://www.w3.org/ns/dcat#Distribution)) represents an accessible and reusable form of a dataset, such as a downloadable file.
* [**Agent**](#Agent). The Agent class ([**`foaf:Agent`**](http://xmlns.com/foaf/0.1/Agent)) is used to represent any organization or person who has competencies to perform actions on a catalog and the cataloged resources. Its main function is to provide concrete references about the different actors who can intervene with different roles in the management of a data catalog.
* [**Identifier**](#Identifier). The (alternative) Identifier class of a dataset ([**`adms:Identifier`**](https://www.w3.org/TR/vocab-adms/#identifier)) is used to express the exclusive reference assigned to a dataset in the context of a given identifier scheme.
* [**Location**](#Location). The Location class ([**`dct:Location`**](http://purl.org/dc/terms/Location)) is used to identify a geographical region or place. It can be represented using a controlled vocabulary or through the expression of geographical coordinates that delimit a specific area.
* [**Period of Time**](#PeriodOfTime). The Validity or Temporal Period class ([**`dct:PeriodOfTime`**](http://purl.org/dc/terms/PeriodOfTime)) is used to define a time interval that is delimited by a start date and an end date.
* [**Checksum**](#Checksum). The Resource Control and Verification class ([**`spdx:Checksum`**](http://spdx.org/rdf/terms#Checksum)) is used to specify the method that is implemented and the result obtained to guarantee the integrity of dataset distributions, that is, that their content has not been altered.
* [**Relationship**](#Relationship). The Relationship between resources class ([**`dcat:Relationship`**](http://www.w3.org/ns/dcat#Relationship)) is used to specify additional information relating to a relationship between resources or agents, providing contextualization about how said resources are interrelated.

## Namespaces Used in the Model {#dcat-ap-es-namespaces}

Each property of a class that describes some attribute of the elements of the catalog, catalog record, data service, dataset, distribution, etc., reuses terms from other existing vocabularies. They are specified by a URI determined by the composition of the prefix of the corresponding vocabulary referenced in the namespace of the DCAT-AP-ES model and the name of the class or property. For example, the [`dct:issued`](http://purl.org/dc/terms/issued) property of the Catalog class is expressed equivalently in its abbreviated and extended form as follows:

!!! info "Note on Namespaces"

    [`dct:issued`](http://purl.org/dc/terms/issued) is equivalent to `http://purl.org/dc/terms/issued`

The generic vocabularies that make up the namespace reused in the implementation of the DCAT-AP-ES model are listed below:

| **Vocabulario** | **Prefijo** | **URI** |
| --- | --- | --- |
| Asset Description Metadata Schema | [`adms:`](http://www.w3.org/ns/adms#) | `http://www.w3.org/ns/adms#` |
| Data Catalog Vocabulary | [`dcat:`](http://www.w3.org/ns/dcat#) | `http://www.w3.org/ns/dcat#` |
| DCAT Application profile for data portals | [`dcatap:`](http://data.europa.eu/r5r/) | `http://data.europa.eu/r5r/` |
| Dublin Core Terms | [`dct:`](http://purl.org/dc/terms/) | `http://purl.org/dc/terms/` |
| Friend Of A Friend | [`foaf:`](http://xmlns.com/foaf/0.1/) | `http://xmlns.com/foaf/0.1/` |
| Location Core Vocabulary | [`locn:`](http://www.w3.org/ns/locn#) | `http://www.w3.org/ns/locn#` |
| Web Ontology Document | [`owl:`](http://www.w3.org/2002/07/owl#) | `http://www.w3.org/2002/07/owl#` |
| Open Digital Rights Language | [`odrl:`](http://www.w3.org/ns/odrl/2/) | `http://www.w3.org/ns/odrl/2/` |
| Open Data Rights Statement Vocabulary | [`odrs:`](http://schema.theodi.org/odrs#) | `http://schema.theodi.org/odrs#` |
| Prov Family of Documents | [`prov:`](http://www.w3.org/ns/prov#) | `http://www.w3.org/ns/prov#` |
| Resource Description Framework | [`rdf:`](http://www.w3.org/1999/02/22-rdf-syntax-ns#) | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| Resource Description Framework Schema | [`rdfs:`](http://www.w3.org/2000/01/rdf-schema#) | `http://www.w3.org/2000/01/rdf-schema#` |
| Simple Knowledge Organization System | [`skos:`](http://www.w3.org/2004/02/skos/core#) | `http://www.w3.org/2004/02/skos/core#` |
| Software Package Data Exchange | [`spdx:`](http://spdx.org/rdf/terms#) | `http://spdx.org/rdf/terms#` |
| W3C Time Ontology | [`time:`](http://www.w3.org/2006/time#) | `http://www.w3.org/2006/time#` |
| vCard Ontology | [`vcard:`](http://www.w3.org/2006/vcard/ns#) | `http://www.w3.org/2006/vcard/ns#` |
| XML Schema | [`xsd:`](http://www.w3.org/2001/XMLSchema#) | `http://www.w3.org/2001/XMLSchema#` |

## Controlled Vocabularies Used in the Model {#dcat-ap-es-vocabularies}
To ensure consistency and interoperability among data catalogs, DCAT-AP-ES recommends the use of controlled vocabularies for each property. The following table shows the recommended vocabularies, their relationship with the entities explicitly described in the profile, and the corresponding URIs, whose use may be mandatory in some cases according to the model specifications.

!!! info "Note on Vocabulary Mappings"

    The datos.gob.es conventions annexes include detailed mappings between the NTI-RISP primary sectors taxonomy, DCAT-AP Themes, and INSPIRE:

    - [Annex 1. Mapping table from primary sectors to DCAT-AP data themes](conventions.md#annex-1-mapping-nti-themes-dcatap-themes)
    - [Annex 2. Mapping table between INSPIRE themes and DCAT-AP themes](conventions.md#annex-2-mapping-inspire-themes-dcatap-themes)
  
| **Property** | **Class** | **Vocabulary** | **Vocabulary URI** |
| --- | --- | --- | --- |
| [**adms:status**](http://www.w3.org/ns/adms#status) | [`CatalogRecord`](#CatalogRecord) | [Concept status](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/authority/concept-status) | `http://publications.europa.eu/resource/authority/concept-status` |
| [**adms:status**](http://www.w3.org/ns/adms#status) | [`Distribution`](#Distribution) | [Distribution status](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/distribution-status) | `http://publications.europa.eu/resource/authority/distribution-status` |
| [**dcat:compressFormat**](http://www.w3.org/ns/dcat#compressFormat) | [`Distribution`](#Distribution) | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| [**dcat:mediaType**](http://www.w3.org/ns/dcat#mediaType) | [`Distribution`](#Distribution) | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| [**dcat:packageFormat**](http://www.w3.org/ns/dcat#packageFormat) | [`Distribution`](#Distribution) | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| [**dcat:theme**](http://www.w3.org/ns/dcat#theme) | [`Dataset`](#Dataset)<br>[`DataService`](#DataService) | <ul><li>[NTI-RISP Primary Sectors Taxonomy](http://datos.gob.es/kos/sector-publico/sector)</li><li> [Data Theme Vocabulary (DCAT-AP)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[INSPIRE Themes Register](http://inspire.ec.europa.eu/theme)</li></ul>  | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| [**dcat:themeTaxonomy**](http://www.w3.org/ns/dcat#themeTaxonomy) | [`Catalog`](#Catalog) | <ul><li>[NTI-RISP Primary Sectors Taxonomy](http://datos.gob.es/kos/sector-publico/sector)</li><li> [Data Theme Vocabulary (DCAT-AP)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[INSPIRE Themes Register](http://inspire.ec.europa.eu/theme)</li></ul> | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| [**dcatap:availability**](http://data.europa.eu/r5r/availability) | [`Distribution`](#Distribution) | [Planned availability](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/planned-availability) | `http://publications.europa.eu/resource/authority/planned-availability` |
| [**dcatap:hvdCategory**](http://data.europa.eu/r5r/hvdCategory) | [`Dataset`](#Dataset)<br>[`DataService`](#DataService) | [HVD Category](https://op.europa.eu/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/bna/asd487ae75) | `http://data.europa.eu/bna/asd487ae75` |
| [**dct:accessRights**](http://purl.org/dc/terms/accessRights) | [`Dataset`](#Dataset)<br>[`DataService`](#DataService) | [Access right](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/access-right) | `http://publications.europa.eu/resource/authority/access-right` |
| [**dct:accrualPeriodicity**](http://purl.org/dc/terms/accrualPeriodicity) | [`Dataset`](#Dataset) | [Frequency](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/frequency) | `http://publications.europa.eu/resource/authority/frequency` |
| [**dct:format**](http://purl.org/dc/terms/format) | [`Distribution`](#Distribution) | [File type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type) | `http://publications.europa.eu/resource/authority/file-type` |
| [**dct:language**](http://purl.org/dc/terms/language) | [`Catalog`](#Catalog)<br>[`Dataset`](#Dataset)<br>[`Distribution`](#Distribution) | [Language](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/language) | `http://publications.europa.eu/resource/authority/language` |
| [**dct:license**](http://purl.org/dc/terms/license) | [`Catalog`](#Catalog)<br>[`DataService`](#DataService)<br>[`Distribution`](#Distribution) | [Licence](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/licence) | `http://publications.europa.eu/resource/authority/licence` |
| [**dct:spatial**](http://purl.org/dc/terms/spatial) | [`Catalog`](#Catalog)<br>[`Dataset`](#Dataset) | <ul><li>[NTI-RISP Territory Taxonomy](https://datos.gob.es/es/recurso/sector-publico/territorio)</li><li> [Continent](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/continent)</li><li>[Countries and territories](http://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/country)</li><li>[Administrative territorial unit](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/atu)</li><li>[Place](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/place)</li><li>[Geonames](http://www.geonames.org/)</li></ul> | <ul><li>`http://datos.gob.es/es/recurso/sector-publico/territorio`</li><li>`http://publications.europa.eu/resource/authority/continent`</li><li>`http://publications.europa.eu/resource/authority/country`</li><li>`http://publications.europa.eu/resource/authority/atu`</li><li>`http://publications.europa.eu/resource/authority/place`</li><li>`http://sws.geonames.org/`</li></ul> |
| [**dct:type**](http://purl.org/dc/terms/type) | [`Agent`](#Agent) | [ADMS publisher type](http://purl.org/adms/publishertype/1.0) | `http://purl.org/adms/publishertype/1.0` |
| [**dct:type**](http://purl.org/dc/terms/type) | [`Dataset`](#Dataset) | [Dataset type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/dataset-type) | `http://publications.europa.eu/resource/authority/dataset-type` |
| [**dct:type**](http://purl.org/dc/terms/type) | [`LicenseDocument`](#LicenseDocument) | [ADMS licence type](http://purl.org/adms/licencetype/1.0) | `http://purl.org/adms/licencetype/1.0` |

# DCAT-AP-ES Model Metadata List {#dcat-ap-es-model-relations}

In the DCAT-AP-ES model metadata tables, the following information is specified:

- **Metadata**: Descriptive name of the metadata element
- **Description**: Brief explanation of the metadata's function and purpose
- **Property**: Formal identifier of the metadata in URI form (e.g., `dct:title`)
- **T** (Applicability): Type of metadata requirement, if different for high-value datasets (HVD) it is indicated. Types can be:
  - **Ob** (Mandatory): The publisher must provide this property's information, and the consumer must be able to process it.
  - **R** (Recommended): The publisher should provide this information if available, the consumer must be able to process it.
  - **Op** (Optional): The publisher may provide this information, the consumer must be able to process it.
- **C** (Cardinality): Indicates the minimum and maximum number of occurrences allowed, if different for high-value datasets (HVD) it is indicated. For example, `1..n` means at least one, potentially many.
- **Range**: Data type or class that the metadata value can take, including:
  - **Main type**: For example, `rdfs:Literal`, `foaf:Agent` or `dcat:Dataset`
  - **Additional description**: Information about the expected format or structure for the value.

This uniform structure facilitates the implementation and understanding of the DCAT-AP-ES application profile.

Likewise, the application requirement is indicated for each entity of the model - catalog, record, data service, dataset, etc.


## Catalog - Class: dcat:Catalog - Mandatory {#Catalog}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Name | Brief title or name given to the data catalog | [title](#Catalog.title) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Description | Descriptive summary of the data catalog | [description](#Catalog.description) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Publishing body | Organization that publishes the catalog | [publisher](#Catalog.publisher) | Ob | 1..1 | [**foaf:Agent**](#Agent) |
| Creation date | Initial publication date of the catalog | [issued](#Catalog.issued) | Ob | 1..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Update date | Date on which the catalog was last modified | [modified](#Catalog.modified) | Ob | 1..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Web page | Public web address for accessing the data catalog | [homepage](#Catalog.homepage) | Ob | 1..1 | [**foaf:Document**](http://xmlns.com/foaf/0.1/Document) |
| Theme(s) | Taxonomy of dataset categories included in the catalog | [themeTaxonomy](#Catalog.themeTaxonomy) | Ob | 1..3 | [**skos:ConceptScheme**](http://www.w3.org/2004/02/skos/core#ConceptScheme) |
| Language(s) | Language(s) in which metadata of the elements included in the catalog are found | [language](#Catalog.language) | Ob | 1..n | [**dct:LinguisticSystem**](http://purl.org/dc/terms/LinguisticSystem) |
| Terms of use | Reference to the general terms of use of the catalog | [license](#Catalog.license) | Ob | 1..1 | [**dct:LicenseDocument**](http://purl.org/dc/terms/LicenseDocument) |
| Dataset | Each of the datasets included in the catalog | [dataset](#Catalog.dataset) | R | 0..n | [**dcat:Dataset**](#Dataset) |
| Data service | Each of the data services included in the catalog | [service](#Catalog.service) | R | 0..n | [**dcat:DataService**](#DataService) |
| Geographic coverage | Geographic area covered by the catalog | [spatial](#Catalog.spatial) | R | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Catalog | Related catalog | [catalog](#Catalog.catalog) | Op | 0..n | [**dcat:Catalog**](#Catalog) |
| Record | Catalog Record | [record](#Catalog.record) | Op | 0..n | [**dcat:CatalogRecord**](#CatalogRecord) |
| Creator | Entity responsible for generating the Catalog | [creator](#Catalog.creator) | Op | 0..n | [**foaf:Agent**](#Agent) |
| Includes | Another Catalog that is included in the catalog | [hasPart](#Catalog.hasPart) | Op | 0..n | [**dcat:Catalog**](#Catalog) |
| Is included in | Part of another catalog | [isPartOf](#Catalog.isPartOf) | Op | 0..1 | [**dcat:Catalog**](#Catalog) |
| Rights statement | Statement of rights related to the catalog | [rights](#Catalog.rights) | Op | 0..1 | [**dct:RightsStatement**](http://purl.org/dc/terms/RightsStatement) |
| Temporal coverage | Defines the time period covered by the catalog | [temporal](#Catalog.temporal) | Op | 0..n | [**dct:PeriodOfTime**](#PeriodOfTime) |


## Catalog Record - Class: dcat:CatalogRecord - Optional {#CatalogRecord}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Main record content | Type of main content of the catalog record | [primaryTopic](#CatalogRecord.primaryTopic) | Ob | 1..1 | [**dcat:Dataset**](#Dataset), [**dcat:DataService**](#DataService) |
| Last update date | Last known date on which the catalog record was modified or updated | [modified](#CatalogRecord.modified) | Ob | 1..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Application profile | Regulatory framework relating to the catalog record | [conformsTo](#CatalogRecord.conformsTo) | R | 0..1 | [**dct:Standard**](http://purl.org/dc/terms/Standard) |
| Creation date | Initial date on which the record was created | [issued](#CatalogRecord.issued) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Status | Phase of the life cycle in which it is found | [status](#CatalogRecord.status) | R | 0..1 | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Name | Name or title of the Catalog Record | [title](#CatalogRecord.title) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Description | Summary description of the catalog record content | [description](#CatalogRecord.description) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |

## Data Service - Class: dcat:DataService - Optional {#DataService}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Name | Name of the data service | [title](#DataService.title) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Access URL | URL at which the service is published | [endpointURL](#DataService.endpointURL) | Ob | 1..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| HVD Category | High-value data category | [hvdCategory](#DataService.hvdCategory) | Op[^2]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Contact point | Contact information about the HVD data service | [contactPoint](#DataService.contactPoint) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**vcard:Kind**](http://www.w3.org/2006/vcard/ns#Kind) |
| Documentation | Relevant document about the HVD data service | [page](#DataService.page) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**foaf:Document**](http://xmlns.com/foaf/0.1/Document) |
| Theme(s) | Main theme or category of the data service | [theme](#DataService.theme) | Ob | 1..n | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Publisher | Organization that publishes the service | [publisher](#DataService.publisher) | Ob | 1..1 | [**foaf:Agent**](#Agent) |
| Endpoint description | Description of endpoint characteristics | [endpointDescription](#DataService.endpointDescription) | R | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Datasets | Datasets available through the service | [servesDataset](#DataService.servesDataset) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**dcat:Dataset**](#Dataset) |
| Applicable legislation | URI of legislation applicable to the resource | [applicableLegislation](#DataService.applicableLegislation) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**eli:LegalResource**](http://data.europa.eu/eli/ontology#LegalResource) |
| Description | Summary description of the data service | [description](#DataService.description) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Access rights | Statement about possible access restrictions | [accessRights](#DataService.accessRights) | Op | 0..1 | [**dct:RightsStatement**](http://purl.org/dc/terms/RightsStatement) |
| License | Data service license | [license](#DataService.license) | Op | 0..1 | [**dct:LicenseDocument**](http://purl.org/dc/terms/LicenseDocument) |
| Tag(s) | Textual tag(s) to freely categorize the data service | [keyword](#DataService.keyword) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |

## Dataset - Class: dcat:Dataset - Mandatory {#Dataset}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Name | Name or title of the dataset | [title](#Dataset.title) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Description | Detailed description of the dataset | [description](#Dataset.description) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Publisher | Organization that publishes the dataset | [publisher](#Dataset.publisher) | Ob | 1..1 | [**foaf:Agent**](#Agent) |
| Theme(s) | Main theme or category of the dataset | [theme](#Dataset.theme) | Ob | 1..n | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Distribution(s) | Dataset resources in their possible formats | [distribution](#Dataset.distribution) | R[^1]<br>Ob (HVD) | 1..n | [**dcat:Distribution**](#Distribution) |
| HVD Category | High-value data category | [hvdCategory](#Dataset.hvdCategory) | Op[^2]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Tag(s) | Textual tag(s) to freely categorize the dataset | [keyword](#Dataset.keyword) | R | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Contact point | Contact information about the dataset | [contactPoint](#Dataset.contactPoint) | R | 0..n | [**vcard:Kind**](http://www.w3.org/2006/vcard/ns#Kind) |
| Temporal coverage | Start and end date of the period covered by the dataset | [temporal](#Dataset.temporal) | R | 0..n | [**dct:PeriodOfTime**](#PeriodOfTime) |
| Geographic coverage | Geographic area covered by the dataset | [spatial](#Dataset.spatial) | R | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Applicable legislation | URI of legislation applicable to the resource | [applicableLegislation](#Dataset.applicableLegislation) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**eli:LegalResource**](http://data.europa.eu/eli/ontology#LegalResource) |
| Main identifier | Main URI that identifies the dataset | [identifier](#Dataset.identifier) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Other identifier | Secondary identifier of the dataset | [identifier](#Dataset.adms:identifier) | Op | 0..n | [**adms:Identifier**](#Identifier) |
| Creator | Organization responsible for generating the dataset | [creator](#Dataset.creator) | Op | 0..n | [**foaf:Agent**](#Agent) |
| Documentation | Reference to a document about the dataset | [page](#Dataset.page) | Op | 0..n | [**foaf:Document**](http://xmlns.com/foaf/0.1/Document) |
| Website | Page for accessing the dataset, its distributions and additional information | [landingPage](#Dataset.landingPage) | Op | 0..n | [**foaf:Document**](http://xmlns.com/foaf/0.1/Document) |
| Sample | Sample of the dataset | [sample](#Dataset.sample) | Op | 0..n | [**dcat:Distribution**](#Distribution) |
| Standard | Specifications that the dataset complies with | [conformsTo](#Dataset.conformsTo) | Op | 0..n | [**dct:Standard**](http://purl.org/dc/terms/Standard) |
| Creation date | Creation date of the dataset | [issued](#Dataset.issued) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Last update date | Last known date on which the dataset content was modified or updated | [modified](#Dataset.modified) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Type | Categorization of the dataset | [type](#Dataset.type) | Op | 0..1 | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Language(s) | Language(s) of the metadata and/or dataset values | [language](#Dataset.language) | Op | 0..n | [**dct:LinguisticSystem**](http://purl.org/dc/terms/LinguisticSystem) |
| Update frequency | Approximate time period between dataset updates | [accrualPeriodicity](#Dataset.accrualPeriodicity) | Op | 0..1 | [**dct:Frequency**](http://purl.org/dc/terms/Frequency) |
| Version | Version identification of the dataset | [version](#Dataset.version) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Version Notes | Description of differences between versions | [versionNotes](#Dataset.versionNotes) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Relationship | Relationship between resources | [qualifiedRelation](#Dataset.qualifiedRelation) | Op | 0..n | [**dcat:Relationship**](#Relationship) |
| Spatial resolution | Minimum distance between two distinct data points | [spatialResolutionInMeters](#Dataset.spatialResolutionInMeters) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Temporal resolution | Minimum time between two consecutive data records | [temporalResolution](#Dataset.temporalResolution) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Referenced by | Reference to the dataset | [isReferencedBy](#Dataset.isReferencedBy) | Op | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Provenance | Data provenance | [provenance](#Dataset.provenance) | Op | 0..n | [**dct:ProvenanceStatement**](http://purl.org/dc/terms/ProvenanceStatement) |
| Related resource | Relationship between resources | [relation](#Dataset.relation) | Op | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Attribution | Agents with some significant responsibility for the dataset | [qualifiedAttribution](#Dataset.qualifiedAttribution) | Op | 0..n | [**prov:Attribution**](http://www.w3.org/ns/prov#Attribution) |
| Generator | Reference to the activity that generated the dataset | [wasGeneratedBy](#Dataset.wasGeneratedBy) | Op | 0..n | [**prov:Activity**](http://www.w3.org/ns/prov#Activity) |
| Has version | Relates this dataset to a version, edition or adaptation | [hasVersion](#Dataset.hasVersion) | Op | 0..n | [**dcat:Dataset**](#Dataset) |
| Is version of | Relates this version to the versioned dataset | [isVersionOf](#Dataset.isVersionOf) | Op | 0..n | [**dcat:Dataset**](#Dataset) |
| Source | Reference to a source dataset | [source](#Dataset.source) | Op | 0..n | [**dcat:Dataset**](#Dataset) |
| Access rights | Statement about possible access restrictions | [accessRights](#Dataset.accessRights) | Op | 0..1 | [**dct:RightsStatement**](http://purl.org/dc/terms/RightsStatement) |



## Distribution - Class: dcat:Distribution - Recommended {#Distribution}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| URL de acceso | URL that allows access to the distribution | [accessURL](#Distribution.accessURL) | Ob | 1..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Applicable legislation | URI of legislation applicable to the resource | [applicableLegislation](#Distribution.applicableLegislation) | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | [**eli:LegalResource**](http://data.europa.eu/eli/ontology#LegalResource) |
| Description | Description of the distribution | [description](#Distribution.description) | R | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Availability | Planned availability of the distribution | [availability](#Distribution.availability) | R | 0..1 | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Format | Format in which the dataset is represented | [format](#Distribution.format) | R | 0..1 | [**dct:MediaTypeOrExtent**](http://purl.org/dc/terms/MediaTypeOrExtent) |
| License | License under which the distribution is published | [license](#Distribution.license) | R | 0..1 | [**dct:LicenseDocument**](http://purl.org/dc/terms/LicenseDocument) |
| MIME type format | MIME type of the distribution | [mediaType](#Distribution.mediaType) | Op | 0..1 | [**dct:MediaType**](http://purl.org/dc/terms/MediaType) |
| Access service | Data service that provides access to the distribution | [accessService](#Distribution.accessService) | Op | 0..n | [**dcat:DataService**](#DataService) |
| Name | Brief title or name given to the distribution | [title](#Distribution.title) | Op | 0..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Documentation | Reference to a document describing the distribution | [page](#Distribution.page) | Op | 0..n | [**foaf:Document**](http://xmlns.com/foaf/0.1/Document) |
| URL de descarga | URL for downloading the file in the defined format. | [downloadURL](#Distribution.downloadURL) | Op | 0..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |
| Schema | Linked data schema or model | [conformsTo](#Distribution.conformsTo) | Op | 0..n | [**dct:Standard**](http://purl.org/dc/terms/Standard) |
| Distribution creation date | Creation date | [issued](#Distribution.issued) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Distribution last update date | Last known date when the distribution was updated | [modified](#Distribution.modified) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Status | Status of the catalog record in the context of the editorial workflow for dataset and data service descriptions | [status](#Distribution.status) | Op | 0..1 | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |
| Language(s) | Language(s) used in the information contained in the distribution | [language](#Distribution.language) | Op | 0..n | [**dct:LinguisticSystem**](http://purl.org/dc/terms/LinguisticSystem) |
| Compressed format | Compression format in which the data is found | [compressFormat](#Distribution.compressFormat) | Op | 0..1 | [**dct:MediaType**](http://purl.org/dc/terms/MediaType) |
| Packaged format | Format in which files are grouped for download | [packageFormat](#Distribution.packageFormat) | Op | 0..1 | [**dct:MediaType**](http://purl.org/dc/terms/MediaType) |
| Size | Approximate size of the dataset | [byteSize](#Distribution.byteSize) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Spatial resolution | Minimum physical separation between data points | [spatialResolutionInMeters](#Distribution.spatialResolutionInMeters) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Temporal resolution | Minimum time between two data records | [temporalResolution](#Distribution.temporalResolution) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Checksum | Distribution integrity verification mechanism | [checksum](#Distribution.checksum) | Op | 0..1 | [**spdx:Checksum**](#Checksum) |
| ODLR norm | Expression of the rights associated with the use of the dataset distribution | [hasPolicy](#Distribution.hasPolicy) | Op | 0..1 | **odrl:Policy** |
| Rights statement | Statement specifying rights associated with the distribution | [rights](#Distribution.rights) | Op | 0..1 | **dct:RightsStatement** |


## Agent - Class: foaf:Agent - Mandatory {#Agent}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Name | Agent name | [name](#Agent.name) | Ob | 1..n | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Identifier | Agent identifier | [identifier](#Agent.identifier) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Type | Agent type | [type](#Agent.type) | R | 0..1 | [**skos:Concept**](http://www.w3.org/2004/02/skos/core#Concept) |

## Identifier - Class: adms:Identifier - Optional {#Identifier}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Notation | Alternative identifier based on UN/CEFACT identifier class | [notation](#Identifier.notation) | Ob | 1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |


## Location - Class: dct:Location - Optional {#Location}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Geographic scope (bounding box) | Geographic delimitation of a resource (rectangular area) | [bbox](#Location.bbox) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Geographic scope (centroid) | Geographic center of a resource (point) | [centroid](#Location.centroid) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Geometry | Geometry of a resource | [geometry](#Location.geometry) | Op | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |


## Period of Time - Class: dct:PeriodOfTime - Optional {#PeriodOfTime}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Start date | Start date of a time interval | [startDate](#PeriodOfTime.startDate) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| End date | End date of a time interval | [endDate](#PeriodOfTime.endDate) | R | 0..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) |
| Beginning | Start instant of an interval or period | [hasBeginning](#PeriodOfTime.hasBeginning) | Op | 0..1 | [**time:Instant**](http://www.w3.org/2006/time#Instant) |
| End | End instant of an interval or period | [hasEnd](#PeriodOfTime.hasEnd) | Op | 0..1 | [**time:Instant**](http://www.w3.org/2006/time#Instant) |

## Checksum - Class: spdx:Checksum - Optional {#Checksum}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Algorithm | Algorithm used to verify integrity | [algorithm](#Checksum.algorithm) | Ob | 1..1 | [**spdx:ChecksumAlgorithm_sha1**](http://spdx.org/rdf/terms#checksumAlgorithm_sha1) |
| Value | Result generated by the algorithm used for integrity verification | [checksumValue](#Checksum.checksumValue) | Ob | 1..1 | [**rdfs:Literal**](http://www.w3.org/2000/01/rdf-schema#Literal) written as [**xsd:hexBinary**](http://www.w3.org/2001/XMLSchema#hexBinary) |

## Relationship - Class: dcat:Relationship - Optional {#Relationship}

| Metadata | Description | Property | T | C | Range |
| --- | --- | --- | --- | --- | --- |
| Role | Role that an entity or agent exercises with respect to another entity or resource | [hadRole](#Relationship.hadRole) | Ob | 1..n | [**dcat:Role**](http://www.w3.org/ns/dcat#Role) |
| Relation | Resource about which the relationship is described | [relation](#Relationship.relation) | Ob | 1..n | [**rdfs:Resource**](http://www.w3.org/2000/01/rdf-schema#Resource) |

# Conformance

## DCAT-AP

### SEMIC Guidelines for Publishing DCAT-AP Profiles (*DCAT-AP reuse guidelines*) {#semic-reuse-guidelines}

The DCAT-AP-ES profile has been evaluated against the official SEMIC guidelines for creating DCAT-AP profiles (["*How to create your DCAT-AP profile*"](https://semiceu.github.io/DCAT-AP-reuse-guidelines/)). The analysis concludes **approximately 94% overall conformity**, with **3 non-critical actions** focused on governance and formal publication of LOD vocabularies. The profile is based on DCAT-AP 2.1.1 and aligns with the main restrictions effectively.

#### Detailed Results

!!! note "Summary (01/2026)"
    - **Profile evaluated:** DCAT-AP-ES
    - **Overall conformity:** **94%** (technically compliant)
    - **Non-critical improvement areas:** open governance, content negotiation, and SKOS publication
    - **Reference:** [SEMIC Guidelines](https://semiceu.github.io/DCAT-AP-reuse-guidelines/)

=== "Step 4 · Creation Methodology"

    | Aspect | Status | Key Evidence | Required Action |
    | --- | --- | --- | --- |
    | **4.1 Based on DCAT-AP** | ✅ Compliant | Based on [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) + [HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) | None |
    | **4.2 Use Case Resolution** | ✅ Compliant | Direct reuse and valid adjustments | None |
    | **4.3 Open Governance** | ⚠️ Partial | [Public repository](https://github.com/datosgobes/DCAT-AP-ES) and management of [Issues](https://github.com/datosgobes/DCAT-AP-ES/issues)/[Discussions](https://github.com/datosgobes/DCAT-AP-ES/discussions) | Formal public consultation and minutes |
    | **4.4 Profile Publication** | ✅ Compliant | [HTML](/), [SHACL](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/), URIs, [SEMIC registry](https://github.com/SEMICeu/DCAT-AP/issues/451) | None |

=== "Step 5 · Specific Situations"

    | Aspect | Status | Key Evidence | Required Action |
    | --- | --- | --- | --- |
    | **5.1 Linked Data and Dereference** | ⚠️ Substantial | Persistent URIs, lacking content negotiation | Document negotiation<br>Publish SKOS vocabularies |
    | **5.2 Semantic Fit** | ✅ Compliant | Semantic coherence preserved | None |
    | **5.3 Controlled Vocabularies** | ✅ Compliant | Maintains MUST and additional mappings | None | 
    | **5.4 Property Range** | ✅ Compliant | No incompatible changes | None |
    | **5.5 New Properties** | ✅ Not applicable | No new properties created | None |
    | **5.6 Cardinalities** | ✅ Compliant | Only allowed tightenings | None |
    | **5.7 Scope and Definitions** | ✅ Compliant | Context documented | None |
    | **5.8 External Vocabularies** | ✅ Compliant | Correct references (vCard, ELI) | None |

# Annex 1. Changes in the DCAT-AP-ES model compared to the NTI-RISP (2013) model {#annex-1-nti-risp-to-dcat-ap-es}

The following details the relationship of changes and updates in the metadata of the DCAT-AP-ES model with respect to the [NTI-RISP (2013) metadata model](https://datosgobes.github.io/NTI-RISP), as well as the relationship of metadata that have been deprecated.

## Metadata incorporated into the DCAT-AP-ES model
Indicated in parentheses is whether the metadata was defined in NTI-RISP or has been incorporated from the DCAT-AP-ES specification:

| Class | Class URI | Mandatory | Recommended | Optional |
| --- | --- | --- | --- | --- |
| Catalog | dcat:Catalog | dct:title (NTI-RISP)  dct:description (NTI-RISP)  dct:publisher (NTI-RISP)  foaf:homepage (NTI-RISP)  dcat:themeTaxonomy (NTI-RISP)  dct:issued (NTI-RISP)  dct:modified (NTI-RISP)  dct:language (DCAT-AP)/dc:language (NTI-RISP)  dct:license (NTI-RISP) | dct:spatial (NTI-RISP)  dcat:dataset (HVD) (NTI-RISP)  dcat:service (HVD) (DCAT-AP) | dcat:catalog (DCAT-AP)  dct:creator (DCAT-AP)  dct:hasPart (DCAT-AP)  dct:isPartOf (DCAT-AP)  dcat:record (HVD) (DCAT-AP)  dct:rights (DCAT-AP) |
| Catalog Record | dcat:CatalogRecord | dct:modified (DCAT-AP)  foaf:primaryTopic (HVD) (DCAT-AP) | dct:conformsTo (DCAT-AP)  dct:issued (DCAT-AP) | adms:status (DCAT-AP) dct:description (DCAT-AP)  dct:title (DCAT-AP) |
| Data Service | Dcat:DataService | dcat:endpointURL (HVD) (DCAT-AP)  dct:title (DCAT-AP)  dcatap:applicableLegislation (HVD) (DCAT-AP)  dcatap:hvdCategory (HVD) (DCAT-AP)  dcat:contactPoint (HVD) (DCAT-AP)  dcat:servesDataset (HVD) (DCAT-AP)  foaf:page (HVD) (DCAT-AP) dcat:theme (NTI-RISP) dct:publisher (DCAT-AP 3) | dcat:endpointDescription (HVD) (DCAT-AP)  dcat:servesDataset (DCAT-AP) dcatap:applicableLegislation (DCAT-AP) foaf:page (DCAT-AP) dcat:contactPoint (DCAT-AP) | dct:accessRights (HVD) (DCAT-AP)  dct:description (DCAT-AP)  dct:license (HVD) (DCAT-AP) dcat:keyword (DCAT-AP) |
| Dataset | dcat:Dataset | dct:description (NTI-RISP)  dct:title (NTI-RISP)  dct:publisher (NTI-RISP)  dcat:theme (NTI-RISP)  dcatap:applicableLegislation (HVD) (DCAT-AP)  dcatap:hvdCategory (HVD) (DCAT-AP)  dcat:distribution (HVD) (NTI-RISP) | dcat:contactPoint (HVD) (DCAT-AP)  dcat:distribution (NTI-RISP)  dcat:keyword (NTI-RISP)  dct:spatial (NTI-RISP)  dct:temporal (NTI-RISP)  dct:issued (NTI-RISP)  dct:modified (NTI-RISP) dcatap:applicableLegislation (DCAT-AP) | adms:identifier (DCAT-AP)  adms:sample (DCAT-AP)  adms:versionNotes (DCAT-AP)  dcat:landingPage (DCAT-AP)  dcat:spatialResolutionInMeters (DCAT-AP)  dcat:temporalResolution (DCAT-AP)  dcat:qualifiedRelation (DCAT-AP)  dct:accessRights (DCAT-AP)  dct:accrualPeriodicity (NTI-RISP)  dct:conformsTo (HVD) (DCAT-AP)  dct:creator (DCAT-AP)  dct:hasVersion (DCAT-AP)  dct:isReferencedBy (DCAT-AP)  dct:isVersionOf (DCAT-AP)  dct:identifier (NTI-RISP)  dct:language (DCAT-AP)/dc:language (NTI-RISP)  dct:provenance (DCAT-AP)  dct:relation (NTI-RISP)  dct:source (DCAT-AP)  dct:type (DCAT-AP)  foaf:page (DCAT-AP)  dcat:version (DCAT-AP)  prov:qualifiedAttribution (DCAT-AP)  prov:wasGeneratedBy (DCAT-AP) |
| Distribution | dcat:Distribution | dcat:accessURL (HVD) (NTI-RISP)  dcatap:applicableLegislation (HVD) (DCAT-AP) | dcatap:availability (DCAT-AP)  dct:description (DCAT-AP)  dct:format (DCAT-AP)  dct:license (HVD) (NTI-RISP) dcatap:applicableLegislation (DCAT-AP) | adms:status (DCAT-AP)  dcat:accessService (HVD) (DCAT-AP)  dcat:byteSize (NTI-RISP)  dcat:compressFormat (DCAT-AP)  dcat:downloadURL (DCAT-AP)  dcat:mediaType (NTI-RISP)  dcat:packageFormat (DCAT-AP)  dcat:spatialResolutionInMeters (DCAT-AP)  dcat:temporalResolution (DCAT-AP)  dct:conformsTo (HVD) (DCAT-AP)  dct:issued (DCAT-AP)  dct:language (DCAT-AP)/dc:language (NTI-RISP) (DCAT-AP)  dct:modified (DCAT-AP)  dct:rights (HVD) (DCAT-AP)  dct:title (NTI-RISP)  foaf:page (DCAT-AP)  odrl:hasPolicy (DCAT-AP)  spdx:checksum (DCAT-AP) |
| Agent | foaf:Agent | foaf:name (DCAT-AP) | dct:type (DCAT-AP) dct:identifier (DCAT-AP) |  |
| Contact | vcard:Kind |  | vcard:organization-name (HVD) (DCAT-AP)  vcard:hasUid (HVD) (DCAT-AP)  vcard:hasTelephone (HVD) (DCAT-AP)  vcard:hasEmail (HVD) (DCAT-AP)  vcard:hasURL (HVD) (DCAT-AP) |  |
| Checksum | spdx:Checksum | spdx:algorithm (DCAT-AP)  spdx:checksumValue (DCAT-AP) |  |  |
| Location | dct:Location |  | dcat:bbox (DCAT-AP)  dcat:centroid (DCAT-AP) | locn:geometry (DCAT-AP) |
| Time Period | dct:PeriodOfTime |  | dcat:startDate (DCAT-AP)  dcat:endDate (DCAT-AP) | time:hasBeginning (DCAT-AP)  time:hasEnd (DCAT-AP) |
| Relationship | dcat:Relationship | dct:relation (DCAT-AP)  dcat:hadRole (DCAT-AP) |  |  |
| Activity | prov:Activity |  | prov:startedAtTime (DCAT-AP)  prov:endedAtTime (DCAT-AP) |  |


## Obsolete elements from NTI-RISP (2013)

The following indicates the names of the metadata and properties described in the previous NTI-RISP (2013) model that are obsolete or have changed in DCAT-AP-ES:

* In the Catalog class (**dcat:Catalog**):
  * *Catalog size* (`dct:extent`)
  * *Identifier* (`dct:identifier`)

* In the Dataset class (**dcat:Dataset**):
  * *Conditions of use* ( `dct:license`) **[1]**
  * *Resource validity*: (`dct:valid`)
  * *Related resources* (`dct:references`)

* In the Distribution class (**dcat:Distribution**):
  * *Additional information about the format* (`dct:relation`) **[2]**
  * *Identifier* (`dct:identifier`)
  * *Format* (`dcat:mediaType`) **[3]**

**[1]** The `dct:license` property disappears from the Dataset class and is incorporated into the Distribution class.

**[2]** The `dct:relation` property disappears from the Distribution class and is incorporated into the Dataset class, although with a different function than described in NTI-RISP (2013). In this metadata model it is used to specify resources that are somehow related to the dataset.

**[3]** In DCAT-AP-ES the format property is divided into several, more specifically the property "Format" (`dct:format`) is added and distinguished from "MIME type format" (`dcat:mediaType`, which was "Format" in the previous model). The latter in [DCAT 2](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) has as range the more specific class `dct:MediaType`, instead of the more general `dct:MediaTypeOrExtent` (which is used in `dct:format`). This means that the "MIME type format" property (`dcat:mediaType`) is restricted to be used only with values that are instances of `dct:MediaType` ([IANA media types](http://www.iana.org/assignments/media-types/media-types.xhtml)), excluding other types of nodes that could have been allowed with `dct:MediaTypeOrExtent`.

# Annex 2. DCAT-AP-ES Quick Reference Guide {#annex-2-quickguide-dcat-ap-es}

The following list includes, alongside the HVD acronym, the properties that are mandatory, recommended or optional and are relevant for the publication of high-value data.

| Class | Class URI | Mandatory | Recommended | Optional |
| --- | --- | --- | --- | --- |
| Catalog | dcat:Catalog | dct:title  dct:description  dct:publisher  foaf:homepage  dcat:themeTaxonomy  dct:issued  dct:modified  dct:language  dct:license | dct:spatial  dcat:dataset (HVD)  dcat:service (HVD) | dcat:catalog  dct:creator  dct:hasPart  dct:isPartOf  dcat:record (HVD)  dct:rights |
| Catalog Record | dcat:CatalogRecord | dct:modified  foaf:primaryTopic (HVD) | dct:conformsTo  dct:issued | adms:status dct:description  dct:title |
| Data Service | dcat:DataService | dcat:endpointURL (HVD)  dct:title  dcatap:applicableLegislation (HVD)  dcatap:hvdCategory (HVD)  dcat:contactPoint (HVD)  dcat:servesDataset (HVD)  foaf:page (HVD) dcat:theme dct:publisher | dcat:endpointDescription (HVD) dcat:servesDataset dcatap:applicableLegislation foaf:page dcat:contactPoint | dct:accessRights (HVD)  dct:description  dct:license (HVD) dcat:keyword |
| Dataset | dcat:Dataset | dct:description  dct:title  dct:publisher  dcat:theme  dcatap:applicableLegislation (HVD)  dcatap:hvdCategory (HVD)  dcat:distribution (HVD) | dcat:contactPoint (HVD)  dcat:distribution  dcat:keyword  dct:spatial  dct:temporal  dct:issued  dct:modified dcatap:applicableLegislation | adms:identifier  adms:sample  adms:versionNotes  dcat:landingPage  dcat:spatialResolutionInMeters  dcat:temporalResolution  dcat:qualifiedRelation  dct:accessRights  dct:accrualPeriodicity  dct:conformsTo (HVD)  dct:creator  dct:hasVersion  dct:isReferencedBy  dct:isVersionOf  dct:identifier  dct:language  dct:provenance  dct:relation  dct:source  dct:type  foaf:page  dcat:version  prov:qualifiedAttribution  prov:wasGeneratedBy |
| Distribution | dcat:Distribution | dcat:accessURL (HVD)  dcatap:applicableLegislation (HVD) | dcatap:availability  dct:description  dct:format  dct:license (HVD) dcatap:applicableLegislation | adms:status  dcat:accessService (HVD)  dcat:byteSize  dcat:compressFormat  dcat:downloadURL  dcat:mediaType  dcat:packageFormat  dcat:spatialResolutionInMeters  dcat:temporalResolution  dct:conformsTo (HVD)  dct:issued  dct:language  dct:modified  dct:rights (HVD)  dct:title  foaf:page  odrl:hasPolicy  spdx:checksum |
| Agent | foaf:Agent | foaf:name | dct:type  dct:identifier |  |
| Contact | vcard:Kind |  | vcard:organization-name (HVD)  vcard:hasUid (HVD)  vcard:hasTelephone (HVD)  vcard:hasEmail (HVD)  vcard:hasURL (HVD) |  |
| Checksum | spdx:Checksum | spdx:algorithm  spdx:checksumValue |  |  |
| Location | dct:Location |  | dcat:bbox  dcat:centroid | locn:geometry |
| Time Period | dct:PeriodOfTime |  | dcat:startDate  dcat:endDate | time:hasBeginning  time:hasEnd |
| Relationship | dcat:Relationship | dct:relation  dcat:hadRole |  |  |


| Other auxiliary classes | Class URI | Property |
| --- | --- | --- |
| Category | skos:Concept | skos:prefLabel |
| Category Scheme | skos:ConceptScheme | dct:title |
| Document | foaf:Document |  |
| Frequency | dct:Frequency |  |
| Identifier | adms:Identifier | skos:notation |
| License Type | skos:Concept |  |
| Linguistic System | dct:LinguisticSystem |  |
| Literal | rdfs:Literal |  |
| Media Type | dct:MediaType |  |
| Publisher Type | skos:Concept |  |
| Resource | rdfs:Resource |  |
| Rights Statement | dct:RightsStatement |  |
| Role | dcat:Role |  |
| Standard | dct:Standard |  |
| Status | skos:Concept |  |

# Annex 3. Comparison between DCAT-AP-ES and DCAT-AP {#annex-3-dcat-ap-to-dcat-ap-es}

DCAT-AP-ES is based on [DCAT-AP 2.1.1](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) with the incorporation of elements from the [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) extension. Below are the additional specifications that the Spanish model includes with respect to the European versions.


The additional specifications are shown in the following comparative tables, where the header indicates:

- **Entity**: Class or element of the model (for example, `Catalog`, `Dataset`, `Distribution`, etc.).
- **Metadata**: Name of the metadata or property.
- **Property**: Formal name of the property (for example, `dct:title`).
- **T** (Applicability): Type of obligation in DCAT-AP-ES (`Mandatory`, `Recommended`, `Optional`).
- **DCAT-AP T**: Type of obligation in the DCAT-AP profile.
- **C** (Cardinality): Cardinality in DCAT-AP-ES.
- **DCAT-AP C**: Cardinality in the DCAT-AP profile.
- **Observations**: Comments on the change or main difference.

## DCAT-AP 2.1.1

### Summary

!!! info "Composition"

    <div style="font-size: 1em; text-align: center; padding: 0.5em;">
        <span style="font-weight: bold; color: #e6f3ff; background: #154481; padding: 5px 10px; border-radius: 5px; border: 1px solid #154481;">DCAT-AP-ES</span>
        <span style="font-weight: bold; font-size: 1.5em; color: #154481; vertical-align: middle; margin: 0 10px;">=</span>
        <span style="font-weight: bold; color: #154481; background: #e6f3ff; padding: 5px 10px; border-radius: 5px; border: 1px solid #154481;">DCAT-AP 2.1.1</span>
        <span style="font-weight: bold; font-size: 1.5em; color: #154481; vertical-align: middle; margin: 0 10px;">+</span>
        <span style="font-weight: bold; color: #154481; background: #e6f3ff; padding: 5px 10px; border-radius: 5px; border: 1px solid #154481;">DCAT-AP HVD 2.2.0</span>
        <span style="font-weight: bold; font-size: 1.5em; color: #154481; vertical-align: middle; margin: 0 10px;">+</span>
        <span style="font-weight: bold; color: #154481; background: #e6f3ff; padding: 5px 10px; border-radius: 5px; border: 1px solid #154481;">Additional specifications</span>
    </div>

    <span style="color:#154481"><b>:material-layers:</b></span>  DCAT-AP-ES is the result of combining the European profile DCAT-AP 2.1.1, the HVD 2.2.0 extension and additional requirements adapted to the Spanish context that are justified below.

    | Specificity | Property | Justification |
    |---|---|---|
    |**1. Mandatory declaration of the following optional properties**| (*Catalog*)<br>dcat:themeTaxonomy<br> dct:language<br> dct:issued<br> dct:modified<br> dct:license<br> foaf:homepage<br><br>(*Dataset*)<br>dcat:theme<br> dct:publisher<br> | Leverage best practices that were established by NTI-RISP (2013) that were already being applied in this way by public administrations |
    |**2. Maintenance of URI structure for geographical coverage**| (*Catalog*/*Dataset*)<br>dct:spatial | Leverage best practices that were established by NTI-RISP (2013) that were already being applied in this way by public administrations |
    |**3. Adjustment to 3 the maximum cardinality of theme taxonomies**| (*Catalog*)<br>dcat:themeTaxonomy | Facilitate interoperability by using commonly used taxonomies (NTI-RISP (2013), INSPIRE and EDP) |
    |**4. Mandatory use of at least the primary sectors taxonomy established by NTI-RISP (2013)**| (*Catalog*)<br>dcat:themeTaxonomy | Leverage best practices that were established by NTI-RISP (2013) and reinforce the use made for other purposes by public administrations |
    |**5. Obligation to incorporate at least the Spanish language in multilingual properties**| (*Catalog*/*Dataset*/*Distribution*)<br>dct:language | Guarantee interoperability |
    |**6. Use of DIR3 for publisher identification**|  (*Agent*)<br>dct:publisher<br> dct:identifier| Apply the standard form of unique identification of public bodies and reinforce the use made for other purposes by public administrations |
    |**7. Specification of the metadata vocabulary**| (*CatalogRecord*/*Distribution*)<br>adms:status | Future convergence with DCAT-AP 3.0.0 and ensure interoperability. adms:status defines the lifecycle of a distribution, with the options: OP_DATPRO, WITHDRAWN, COMPLETED, DEPRECATED, DEVELOP |
    |**8. Incorporation to *DataService***| (*DataService*)<br>dct:publisher<br> dcat:theme<br><br> | Future convergence with DCAT-AP 3.0.0 and ensure interoperability |
    |**9. Incorporation of the ATU vocabulary for**| (*Catalog*/*Dataset*)<br>dct:spatial | Allows greater precision for administrative divisions, guaranteeing interoperability. dct:spatial is Recommended |


### Full Detail

| Entity | Metadata | Property | T | DCAT-AP<br>T | C | DCAT-AP<br>C | Observations |
|---|---|---|---|---|---|---|---|
| Catalog | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| Catalog | Description | dct:description | Ob | Ob | 1..n | 1..n | - |
| Catalog | Publishing body | dct:publisher | Ob | Ob | 1..1 | 1..1 | - |
| Catalog | Theme(s) | dcat:themeTaxonomy | Ob | R | 1..3 | 0..n | DCAT-AP-ES mandatorily requires the [primary sectors taxonomy](http://datos.gob.es/kos/sector-publico/sector) and restricts cardinality |
| Catalog | Language(s) | dct:language | Ob | R | 1..n | 0..n | DCAT-AP-ES requires that at least one of the languages is Spanish |
| Catalog | Creation date | dct:issued | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Update date | dct:modified | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Web page | foaf:homepage | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Terms of use | dct:license | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| CatalogRecord | Editorial status | adms:status | R | R | 0..1 | 0..1 | In DCAT-AP 2.1.1 uses vocabulary [ADMS Status 1.0](http://www.w3.org/TR/vocab-adms/#status) |
| Dataset | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| Dataset | Description | dct:description | Ob | Ob | 1..n | 1..n | - |
| Dataset | Publisher | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory and adjusts cardinality (1..1) |
| Dataset | Theme(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES raises the property to Mandatory |
| Dataset | Distribution | dcat:distribution | R/Ob (HVD) | R | 0..n/1..n (HVD) | 0..n | DCAT-AP-ES makes this property mandatory for HVD datasets |
| Dataset | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Does not exist | 0..n/1..n (HVD) | - | Property incorporated in DCAT-AP-ES from DCAT-AP 3.0.0 |
| Dataset | Spatial resolution | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..n | DCAT-AP-ES limits to a single spatial resolution |
| Dataset | Temporal resolution | dcat:temporalResolution | Op | Op | 0..1 | 0..n | DCAT-AP-ES limits to a single temporal resolution |
| DataService | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| DataService | Access URL | dcat:endpointURL | Ob | Ob | 1..n | 1..n | - |
| DataService | Theme(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES raises the property to Mandatory |
| DataService | Publisher | dct:publisher | Ob | Does not exist  | 1..1 | - | DCAT-AP-ES includes the property and makes it Mandatory |
| DataService | Endpoint description | dcat:endpointDescription | R | R | 0..n | 0..n | - |
| DataService | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Does not exist | 0..n/1..n (HVD) | - | Property incorporated in DCAT-AP-ES from DCAT-AP 3.0.0 |
| Distribution | Access URL | dcat:accessURL | Ob | Ob | 1..n | 1..n | - |
| Distribution | Format | dct:format | R | R | 0..1 | 0..1 | - |
| Distribution | License | dct:license | R | R | 0..1 | 0..1 | - |
| Distribution | Applicable legislation | dcatap:applicableLegislation | R/Ob (HVD) | Does not exist | 0..n/1..n (HVD) | - | Property incorporated in DCAT-AP-ES from DCAT-AP 3.0.0 |
| Distribution | Availability | dcatap:availability | R | Does not exist | 0..1 | - | Property incorporated in DCAT-AP-ES from DCAT-AP 2.1.0 |
| Distribution | Status | adms:status | Op | R | 0..1 | 0..1 | DCAT-AP-ES lowers the property to Optional |
| Distribution | Spatial resolution | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | -|
| Distribution | Temporal resolution | dcat:temporalResolution | Op | Op | 0..1 | 0..n | DCAT-AP-ES limits to a single temporal resolution |
| Agent | Name | foaf:name | Ob | Ob | 1..n | 1..n | - |
| Agent | Type | dct:type | R | R | 0..1 | 0..1 | - |
| Agent | Identifier | dct:identifier | R | Op | 0..1 | 0..1 | DCAT-AP-ES raises to Recommended and establishes format for public bodies (DIR3) |

## DCAT-AP 3.0.0

| Entity | Metadata | Property | T | DCAT-AP<br>T | C | DCAT-AP<br>C | Observations |
|---|---|---|---|---|---|---|---|
| Catalog | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| Catalog | Description | dct:description | Ob | Ob | 1..n | 1..n | - |
| Catalog | Publishing body | dct:publisher | Ob | Ob | 1..1 | 1..1 | - |
| Catalog | Theme(s) | dcat:themeTaxonomy | Ob | R | 1..3 | 0..n | DCAT-AP-ES mandatorily requires the [primary sectors taxonomy](http://datos.gob.es/kos/sector-publico/sector) and restricts cardinality |
| Catalog | Language(s) | dct:language | Ob | R | 1..n | 0..n | DCAT-AP-ES requires that at least one of the languages is Spanish |
| Catalog | Creation date | dct:issued | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Update date | dct:modified | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Web page | foaf:homepage | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Terms of use | dct:license | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| Catalog | Applicable legislation | dcatap:applicableLegislation | Does not exist | R | - | 0..n | DCAT-AP 3 property not incorporated into DCAT-AP-ES |
| CatalogRecord | Editorial status | adms:status | R | R | 0..1 | 0..1 | In DCAT-AP 3 uses a different vocabulary than DCAT-AP 2.1.1, in DCAT-AP-ES it is adopted as a recommendation: [CatalogRecord.status](#CatalogRecord.status) |
| Dataset | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| Dataset | Description | dct:description | Ob | Ob | 1..n | 1..n | - |
| Dataset | Publisher | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory and adjusts cardinality (1..1) |
| Dataset | Theme(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES raises the property to Mandatory |
| Dataset | Distribution | dcat:distribution | R/Ob (HVD) | R | 0..n/1..n (HVD) | 0..n | DCAT-AP-ES makes this property mandatory for HVD datasets |
| Dataset | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | In DCAT-AP-ES it is Mandatory for HVD datasets |
| Dataset | Quality | dqv:hasQualityMeasurement | Does not exist | Op | - | 0..n | New property in DCAT-AP 3.0.0 not incorporated into DCAT-AP-ES |
| Dataset | Spatial resolution | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | DCAT-AP-ES maintains the same cardinality |
| Dataset | Temporal resolution | dcat:temporalResolution | Op | Op | 0..1 | 0..n | DCAT-AP-ES limits to a single temporal resolution |
| DataService | Name | dct:title | Ob | Ob | 1..n | 1..n | - |
| DataService | Access URL | dcat:endpointURL | Ob | Ob | 1..n | 1..n | - |
| DataService | Theme(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES raises the property to Mandatory |
| DataService | Publisher | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES raises the property to Mandatory |
| DataService | Endpoint description | dcat:endpointDescription | R | R | 0..n | 0..n | - |
| DataService | Endpoint description by type | dcat:endpointDescriptionByType | Does not exist | R | - | 0..n | New property in DCAT-AP 3.0.0 not incorporated into DCAT-AP-ES |
| DataService | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | In DCAT-AP-ES it is Mandatory for HVD services |
| Distribution | Access URL | dcat:accessURL | Ob | Ob | 1..n | 1..n | - |
| Distribution | Format | dct:format | R | R | 0..1 | 0..1 | - |
| Distribution | License | dct:license | R | R | 0..1 | 0..1 | - |
| Distribution | Applicable legislation | dcatap:applicableLegislation | R/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | DCAT-AP-ES raises to Recommended/Mandatory for HVD |
| Distribution | Availability | dcatap:availability | R | R | 0..1 | 0..1 | - |
| Distribution | Status | adms:status | Op | Op | 0..1 | 0..1 | -  |
| Distribution | Spatial resolution | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | -|
| Distribution | Temporal resolution | dcat:temporalResolution | Op | Op | 0..1 | 0..1 | - |
| Agent | Name | foaf:name | Ob | Ob | 1..n | 0..1 | - |
| Agent | Type | dct:type | R | Op | 0..1 | 0..1 | DCAT-AP-ES raises to Recommended |
| Agent | Identifier | dct:identifier | R | Does not exist | 0..1 | - | DCAT-AP-ES includes it, raises to Recommended, and sets format for public organizations (DIR3) |

## Extensions
The **Extensions** section describes how the DCAT-AP-ES model is adapted and extended to meet the specific needs of the Spanish context, incorporating additional requirements such as those relating to high-value datasets (HVD). 

### DCAT-AP HVD 2.2.0

| Entity | Metadata | Property | T | HVD<br>T | C | HVD<br>C | Observations |
|---|---|---|---|---|---|---|---|
| Dataset | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| Dataset | Applicable legislation | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| Dataset | Distribution | dcat:distribution | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| Dataset | Contact point | dcat:contactPoint | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| DataService | HVD Category | dcatap:hvdCategory | Op/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| DataService | Applicable legislation | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| DataService | Contact point | dcat:contactPoint | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| DataService | Served dataset | dcat:servesDataset | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| Distribution | Applicable legislation | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Full implementation of DCAT-AP HVD in DCAT-AP-ES |
| Distribution | License | dct:license | R/Ob (HVD) | Op/Ob (HVD) | 0..1/1..1 (HVD) | 0..1/1..1 (HVD) | Same obligation for licenses in HVD data is maintained |

## Distinctive Features of DCAT-AP-ES

This annex presents a consolidated view of the additional specificities between DCAT-AP-ES and the European DCAT-AP profiles (versions 2.1.1 and 3.0.0), facilitating understanding of the particularities of the Spanish profile and its specific implementation requirements.

### 1. Adaptation to the Spanish Context
- Mandatory use of national taxonomies: DCAT-AP-ES requires the use of the [primary sectors taxonomy](http://datos.gob.es/kos/sector-publico/sector) for thematic classification
- Linguistic requirement: At least one of the languages must be Spanish in multilingual properties
- Organizational identifier normalization: Defines standardized URIs with DIR3 format for public bodies (`http://datos.gob.es/recurso/sector-publico/org/Organismo/{ID}`)

### 2. Greater Obligation in Metadata
- DCAT-AP-ES raises numerous properties from Recommended to Mandatory, especially in `dcat:Catalog`, `dcat:Dataset` and `dcat:DataService`
- Defines obligation for key properties such as `dct:publisher`, `dcat:theme` and creation/update dates
- Adopts a stricter approach to ensure metadata completeness and interoperability

### 3. Comprehensive Support for High-Value Data (HVD)
- Integrates specific requirements for high-value data according to [Commission Implementing Regulation (EU) 2023/138](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0138)
- Defines additional mandatory properties for HVD datasets (`dcatap:hvdCategory`, `dcat:distribution`)
- Incorporates `dcatap:applicableLegislation` as mandatory for HVD distributions

### 4. Evolution from European Profiles
- Selectively incorporates DCAT-AP properties such as the mentioned `dcatap:applicableLegislation`, `dcatap:availability` and `dcatap:hvdCategory`
- Updates controlled vocabularies (e.g., for `adms:status` in `dcat:Distribution`)

### 5. Adapted Cardinalities
- Defines more restrictive cardinalities for greater precision (e.g., `dct:publisher` requires cardinality `1..1`)
- Limits spatial and temporal resolutions to a single instance (`0..1`)
- Restricts `dcat:themeTaxonomy` to maximum 3 taxonomies, mandatorily including the Spanish one

### 6. Aligned with the Legal Data Framework
- DCAT-AP-ES is an evolution of the [NTI-RISP metadata model](https://datosgobes.github.io/NTI-RISP/) and the [Application Guide](https://datosgobes.github.io/NTI-RISP/download/pdf/guia_nti_pdf_reutilizacion_recursos_informacion_2aed.pdf) that contains it. Therefore, it implements requirements according to Spanish open data regulations ([Law 37/2007, of November 16, on the reuse of public sector information](https://www.boe.es/eli/es/l/2007/11/16/37/con) and [Resolution of February 19, 2013, of the Secretary of State for Public Administrations, approving the Technical Interoperability Standard for Information Resources Reuse](https://www.boe.es/eli/es/res/2013/02/19/(4))). 
- Adapts to the ecosystem of related and interconnected specifications (DCAT-AP) in the context of data policies [Directive (EU) 2019/1024](http://data.europa.eu/eli/dir/2019/1024/oj), interoperability ([SEMIC](https://joinup.ec.europa.eu/)) and infrastructure ([EDP](https://data.europa.eu/)) of the European Commission.

# Change History

This section provides an overview of the changes incorporated in DCAT-AP-ES. A complete list of issues closed with this version is accessible at [GitHub](https://github.com/datosgobes/DCAT-AP-ES/issues).

## DCAT-AP-ES 1.0.0

### Main Changes

- Transformation of technical documentation into HTML representation ([RESPEC](https://respec.org/docs/) style using [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/))
- Integration of updated guidelines and texts related to DCAT-AP-ES
- Update and improvement of cross-references to facilitate navigation
- Correction of numerous typographical errors and conversion issues

### Adaptations to Different Sections
- Introduction: Review to reflect the current context and profile foundations
- Conformance: Update to reflect implementation requirements in the Spanish ecosystem
- Terminology: Updated prefix list with the most recent vocabularies
- Data model: Reorganized structure to improve readability
- Controlled vocabularies: Update of references to authorized vocabularies
- High-Value Datasets (HVD): Full integration of requirements from [Implementing Regulation (EU) 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj)
- Quick reference annex: Automatic generation from the data model to maintain synchronization

#### Changes Compared to NTI-RISP

- Complete update of classes and properties according to DCAT-AP
- Removal of obsolete properties and replacement with more appropriate alternatives
- Restructuring to adapt to new requirements of [Directive (EU) 2019/1024](http://data.europa.eu/eli/dir/2019/1024/oj)
- Implementation of specific metadata for High-Value Datasets (HVD)
- Expansion of capabilities to describe data services (APIs and endpoints)

#### Additional Specifications with DCAT-AP

- Higher level of obligation in key properties to ensure metadata quality
- Adaptation to the Spanish regulatory framework and its specific requirements
- More restrictive cardinalities to ensure uniformity and precision
- Specific linguistic requirements of the Spanish multilingual context
- Integration with Spanish public body identification systems (DIR3)

### Data Model Adaptations

The following list indicates the additional specifications compared to the previous version (NTI-RISP). It also includes the impact of alignment with the W3C recommendation: DCAT and the European DCAT-AP profile.

- Division of existing descriptive texts into definitions and usage notes following SEMIC best practices
- Alignment with DCAT-AP 2.1.1 and selective adoption of DCAT-AP 3.0.0 elements
- Organization of the profile into main entities, supporting entities, and data types
- Elevation of numerous properties to mandatory to ensure interoperability
- Incorporation of specific aspects for High-Value Data (HVD)
- Adaptation to linguistic requirements and territorial classification of Spain

### Specific Requirements for the Spanish Context

- National taxonomies: Mandatory implementation of the Spanish primary sectors taxonomy
- Linguistic requirement: Spanish mandatory as one of the languages in multilingual properties
- Standardized identifiers: Adoption of the DIR3 scheme for public body identification
- Includes the publisher (`dct:publisher`) in main entities to trace resource ownership.

### Alignment with HVD (High-Value Data)

- Full integration of the requirements of Implementing Regulation (EU) 2023/138
- Clear definition of additional mandatory properties for HVD datasets
- Incorporation of metadata for traceability and regulatory compliance (applicable legislation, HVD categories)

### SHACL and Validation

- Development of SHACL rules for automatic profile validation
- Inclusion of unique identifiers for each constraint
- Implementation of tests to verify conformance with the profile

### Error Corrections

- Alignment of properties with their definition in original vocabularies
- Correction of cardinalities to reflect specific requirements of the Spanish context
- Improvement of descriptions and usage notes to facilitate correct implementation
- Adjustments to controlled vocabulary references to ensure their availability and persistence

[^1]: Mandatory when dealing with high-value data, otherwise recommended.
[^2]: Mandatory when dealing with high-value data, otherwise optional.