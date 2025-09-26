## Main Entities DCAT-AP 3.0.0

The main entities are those that form the core of the Application Profile. The properties and their associated constraints that apply in the context of this profile are listed in a tabular form. Each row corresponds to one property. In addition to the constraints also cross-references are provided to DCAT. To save space, the following abbreviations are used to indicate in short the difference with DCAT:

*   A: reused as-is defined and expressed in DCAT
*   E: reused with additional usage notes or additional restrictions compared to DCAT
*   P: DCAT-AP profile specific extension where DCAT had no requirements earlier on specified

This reuse qualification assessement is w.r.t. a specific version of DCAT. Therefore it may vary over time when new versions of DCAT-AP are created.

### [Agent](http://xmlns.com/foaf/0.1/Agent)

Definition

Any entity carrying out actions with respect to the entities Catalogue and the Catalogued Resources.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Organization_Person)

Usage Note

If the Agent is an organisation, the use of the [Organization Ontology](https://www.w3.org/TR/vocab-org/) is recommended.

Properties

For this entity the following properties are defined: [name](#Agent.name) , [type](#Agent.type) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [name](http://xmlns.com/foaf/0.1/name) | [Literal](#Literal) | 1..\* | A name of the agent. | This property can be repeated for different versions of the name (e.g. the name in different languages). |     | P   |
| [type](http://purl.org/dc/terms/type) | [Concept](#Concept) | 0..1 | The nature of the agent. |     |     | P   |

### [Catalogue](http://www.w3.org/ns/dcat#Catalog)

Definition

A catalogue or repository that hosts the Datasets or Data Services being described.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog)

Properties

For this entity the following properties are defined: [applicable legislation](#Catalogue.applicablelegislation) , [catalogue](#Catalogue.catalogue) , [creator](#Catalogue.creator) , [dataset](#Catalogue.dataset) , [description](#Catalogue.description) , [geographical coverage](#Catalogue.geographicalcoverage) , [has part](#Catalogue.haspart) , [homepage](#Catalogue.homepage) , [language](#Catalogue.language) , [licence](#Catalogue.licence) , [modification date](#Catalogue.modificationdate) , [publisher](#Catalogue.publisher) , [record](#Catalogue.record) , [release date](#Catalogue.releasedate) , [rights](#Catalogue.rights) , [service](#Catalogue.service) , [temporal coverage](#Catalogue.temporalcoverage) , [themes](#Catalogue.themes) , [title](#Catalogue.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | [Legal Resource](#LegalResource) | 0..\* | The legislation that mandates the creation or management of the Catalog. |     |     | P   |
| [catalogue](http://www.w3.org/ns/dcat#catalog) | [Catalogue](#Catalogue) | 0..\* | A catalogue whose contents are of interest in the context of this catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog) |
| [creator](http://purl.org/dc/terms/creator) | [Agent](#Agent) | 0..1 | An entity responsible for the creation of the catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) |
| [dataset](http://www.w3.org/ns/dcat#dataset) | [Dataset](#Dataset) | 0..\* | A Dataset that is part of the Catalogue. | As empty Catalogues are usually indications of problems, this property should be combined with the property [service](#Catalogue.service) to implement an empty Catalogue check. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset) |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 1..\* | A free-text account of the Catalogue. | This property can be repeated for parallel language versions of the description. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) |
| [geographical coverage](http://purl.org/dc/terms/spatial) | [Location](#Location) | 0..\* | A geographical area covered by the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) |
| [has part](http://purl.org/dc/terms/hasPart) | [Catalogue](#Catalogue) | 0..\* | A related Catalogue that is part of the described Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_has_part) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_has_part) |
| [homepage](http://xmlns.com/foaf/0.1/homepage) | [Document](#Document) | 0..1 | A web page that acts as the main page for the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_homepage) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_homepage) |
| [language](http://purl.org/dc/terms/language) | [Linguistic system](#Linguisticsystem) | 0..\* | A language used in the textual metadata describing titles, descriptions, etc. of the Datasets in the Catalogue. | This property can be repeated if the metadata is provided in multiple languages. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_language) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_language) |
| [licence](http://purl.org/dc/terms/license) | [Licence Document](#LicenceDocument) | 0..1 | A licence under which the Catalogue can be used or reused. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_license) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_license) |
| [modification date](http://purl.org/dc/terms/modified) | [Temporal Literal](#TemporalLiteral) | 0..1 | The most recent date on which the Catalogue was modified. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) |
| [publisher](http://purl.org/dc/terms/publisher) | [Agent](#Agent) | 1   | An entity (organisation) responsible for making the Catalogue available. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) |
| [record](http://www.w3.org/ns/dcat#record) | [Catalogue Record](#CatalogueRecord) | 0..\* | A Catalogue Record that is part of the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog_record) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_catalog_record) |
| [release date](http://purl.org/dc/terms/issued) | [Temporal Literal](#TemporalLiteral) | 0..1 | The date of formal issuance (e.g., publication) of the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) |
| [rights](http://purl.org/dc/terms/rights) | [Rights statement](#Rightsstatement) | 0..1 | A statement that specifies rights associated with the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_rights) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_rights) |
| [service](http://www.w3.org/ns/dcat#service) | [Data Service](#DataService) | 0..\* | A site or end-point (Data Service) that is listed in the Catalogue. | As empty Catalogues are usually indications of problems, this property should be combined with the property [dataset](#Catalogue.dataset) to implement an empty Catalogue check. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_service) |
| [temporal coverage](http://purl.org/dc/terms/temporal) | [Period of time](#Periodoftime) | 0..\* | A temporal period that the Catalogue covers. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal_resolution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal_resolution) |
| [themes](http://www.w3.org/ns/dcat#themeTaxonomy) | [Concept Scheme](#ConceptScheme) | 0..\* | A knowledge organization system used to classify the Resources that are in the Catalogue. | This property refers to a knowledge organization system used to classify the Catalogue's Datasets. It must have at least the value NAL:data-theme as this is the manatory controlled vocabulary for dcat:theme. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_themes) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_themes) |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 1..\* | A name given to the Catalogue. | This property can be repeated for parallel language versions of the name. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) |

### [Catalogue Record](http://www.w3.org/ns/dcat#CatalogRecord)

Definition

A description of a Catalogued Resource's entry in the Catalogue.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog_Record)

Properties

For this entity the following properties are defined: [application profile](#CatalogueRecord.applicationprofile) , [change type](#CatalogueRecord.changetype) , [description](#CatalogueRecord.description) , [language](#CatalogueRecord.language) , [listing date](#CatalogueRecord.listingdate) , [modification date](#CatalogueRecord.modificationdate) , [primary topic](#CatalogueRecord.primarytopic) , [source metadata](#CatalogueRecord.sourcemetadata) , [title](#CatalogueRecord.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [application profile](http://purl.org/dc/terms/conformsTo) | [Standard](#Standard) | 0..\* | An Application Profile that the Catalogued Resource's metadata conforms to. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_conforms_to) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_conforms_to) |
| [change type](http://www.w3.org/ns/adms#status) | [Concept](#Concept) | 0..1 | The status of the catalogue record in the context of editorial flow of the dataset and data service descriptions. |     |     | P   |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 0..\* | A free-text account of the record. This property can be repeated for parallel language versions of the description. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_description) |
| [language](http://purl.org/dc/terms/language) | [Linguistic system](#Linguisticsystem) | 0..\* | A language used in the textual metadata describing titles, descriptions, etc. of the Catalogued Resource. | This property can be repeated if the metadata is provided in multiple languages. |     | P   |
| [listing date](http://purl.org/dc/terms/issued) | [Temporal Literal](#TemporalLiteral) | 0..1 | The date on which the description of the Resource was included in the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_listing_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_listing_date) |
| [modification date](http://purl.org/dc/terms/modified) | [Temporal Literal](#TemporalLiteral) | 1   | The most recent date on which the Catalogue entry was changed or modified. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_update_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_update_date) |
| [primary topic](http://xmlns.com/foaf/0.1/primaryTopic) | [Catalogued Resource](#CataloguedResource) | 1   | A link to the Dataset, Data service or Catalog described in the record. | A catalogue record will refer to one entity in a catalogue. This can be either a Dataset or a Data Service. To ensure an unambigous reading of the cardinality the range is set to Catalogued Resource. However it is not the intend with this range to require the explicit use of the class Catalogued Record. As abstract class, an subclass should be used. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_primary_topic) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_primary_topic) |
| [source metadata](http://purl.org/dc/terms/source) | [Catalogue Record](#CatalogueRecord) | 0..1 | The original metadata that was used in creating metadata for the Dataset, Data Service or Dataset Series. |     |     | P   |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 0..\* | A name given to the Catalogue Record. | This property can be repeated for parallel language versions of the name. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_title) |

### [Catalogued Resource](http://www.w3.org/ns/dcat#Resource)

Definition

Resource published or curated by a single agent.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Resource)

Usage Note

This class Catalogued Record is an abstract class for DCAT-AP. Therefore only subclasses should be used in a data exchange.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Checksum](http://spdx.org/rdf/terms#Checksum)

Definition

A value that allows the contents of a file to be authenticated.

Reference in DCAT

[Link](https://w3c.github.io/dxwg/dcat/#Class:Checksum)

Usage Note

This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.

Properties

For this entity the following properties are defined: [algorithm](#Checksum.algorithm) , [checksum value](#Checksum.checksumvalue) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [algorithm](http://spdx.org/rdf/terms#algorithm) | [Checksum Algorithm](#ChecksumAlgorithm) | 1   | The algorithm used to produce the subject Checksum. |     | [Link](https://w3c.github.io/dxwg/dcat/#Property:checksum_algorithm) | [E](https://w3c.github.io/dxwg/dcat/#Property:checksum_algorithm) |
| [checksum value](http://spdx.org/rdf/terms#checksumValue) | [xsd:hexBinary](#xsd%3AhexBinary) | 1   | A lower case hexadecimal encoded digest value produced using a specific algorithm. |     | [Link](https://w3c.github.io/dxwg/dcat/#Property:checksum_checksum_value) | [E](https://w3c.github.io/dxwg/dcat/#Property:checksum_checksum_value) |

### [Data Service](http://www.w3.org/ns/dcat#DataService)

Definition

A collection of operations that provides access to one or more datasets or data processing functions.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Data_Service)

Subclass of

[Catalogued Resource](#CataloguedResource)

Properties

For this entity the following properties are defined: [access rights](#DataService.accessrights) , [applicable legislation](#DataService.applicablelegislation) , [conforms to](#DataService.conformsto) , [contact point](#DataService.contactpoint) , [description](#DataService.description) , [documentation](#DataService.documentation) , [endpoint description](#DataService.endpointdescription) , [endpoint URL](#DataService.endpointURL) , [format](#DataService.format) , [keyword](#DataService.keyword) , [landing page](#DataService.landingpage) , [licence](#DataService.licence) , [publisher](#DataService.publisher) , [serves dataset](#DataService.servesdataset) , [theme](#DataService.theme) , [title](#DataService.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [access rights](http://purl.org/dc/terms/accessRights) | [Rights statement](#Rightsstatement) | 0..1 | Information regarding access or restrictions based on privacy, security, or other policies. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_access_rights) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_access_rights) |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | [Legal Resource](#LegalResource) | 0..\* | The legislation that mandates the creation or management of the Data Service. |     |     | P   |
| [conforms to](http://purl.org/dc/terms/conformsTo) | [Standard](#Standard) | 0..\* | An established (technical) standard to which the Data Service conforms. | The standards referred here SHOULD describe the Data Service and not the data it serves. The latter is provided by the dataset with which this Data Service is connected. For instance the data service adheres to the OGC WFS API standard, while the associated dataset adheres to the [INSPIRE](https://knowledge-base.inspire.ec.europa.eu/index_en) Address data model. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:record_conforms_to) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:record_conforms_to) |
| [contact point](http://www.w3.org/ns/dcat#contactPoint) | [Kind](#Kind) | 0..\* | Contact information that can be used for sending comments about the Data Service. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 0..\* | A free-text account of the Data Service. | This property can be repeated for parallel language versions of the description. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) |
| [documentation](http://xmlns.com/foaf/0.1/page) | [Document](#Document) | 0..\* | A page or document about this Data Service |     |     | P   |
| [endpoint description](http://www.w3.org/ns/dcat#endpointDescription) | [Resource](#Resource) | 0..\* | A description of the services available via the end-points, including their operations, parameters etc. | The property gives specific details of the actual endpoint instances, while the property application profile (dct:conformsTo) is used to indicate the general standard or specification that the endpoints implement. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_description) |
| [endpoint URL](http://www.w3.org/ns/dcat#endpointURL) | [Resource](#Resource) | 1..\* | The root location or primary endpoint of the service (an IRI). |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_endpoint_url) |
| [format](http://purl.org/dc/terms/format) | [Media Type or Extent](#MediaTypeorExtent) | 0..\* | The structure that can be returned by querying the endpointURL. |     |     | P   |
| [keyword](http://www.w3.org/ns/dcat#keyword) | [Literal](#Literal) | 0..\* | A keyword or tag describing the Data Service. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword) |
| [landing page](http://www.w3.org/ns/dcat#landingPage) | [Document](#Document) | 0..\* | A web page that provides access to the Data Service and/or additional information. | It is intended to point to a landing page at the original data service provider, not to a page on a site of a third party, such as an aggregator. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page) |
| [licence](http://purl.org/dc/terms/license) | [Licence Document](#LicenceDocument) | 0..1 | A licence under which the Data service is made available. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_license) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_license) |
| [publisher](http://purl.org/dc/terms/publisher) | [Agent](#Agent) | 0..1 | An entity (organisation) responsible for making the Data Service available. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) |
| [serves dataset](http://www.w3.org/ns/dcat#servesDataset) | [Dataset](#Dataset) | 0..\* | This property refers to a collection of data that this data service can distribute. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:data_service_serves_dataset) |
| [theme](http://www.w3.org/ns/dcat#theme) | [Concept](#Concept) | 0..\* | A category of the Data Service. | A Data Service may be associated with multiple themes. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 1..\* | A name given to the Data Service. | This property can be repeated for parallel language versions of the name. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) |

### [Dataset](http://www.w3.org/ns/dcat#Dataset)

Definition

A conceptual entity that represents the information published.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset)

Usage Note

If a Dataset is used as part of a Dataset Series, the usage of the properties listed below must be coherent with the associated Dataset Series. For this usage, consult the guidelines in section \[\[\[#UsageGuidelines\]\]\].

Subclass of

[Catalogued Resource](#CataloguedResource)

Properties

For this entity the following properties are defined: [access rights](#Dataset.accessrights) , [applicable legislation](#Dataset.applicablelegislation) , [conforms to](#Dataset.conformsto) , [contact point](#Dataset.contactpoint) , [creator](#Dataset.creator) , [dataset distribution](#Dataset.datasetdistribution) , [description](#Dataset.description) , [documentation](#Dataset.documentation) , [frequency](#Dataset.frequency) , [geographical coverage](#Dataset.geographicalcoverage) , [has version](#Dataset.hasversion) , [identifier](#Dataset.identifier) , [in series](#Dataset.inseries) , [is referenced by](#Dataset.isreferencedby) , [keyword](#Dataset.keyword) , [landing page](#Dataset.landingpage) , [language](#Dataset.language) , [modification date](#Dataset.modificationdate) , [other identifier](#Dataset.otheridentifier) , [provenance](#Dataset.provenance) , [publisher](#Dataset.publisher) , [qualified attribution](#Dataset.qualifiedattribution) , [qualified relation](#Dataset.qualifiedrelation) , [related resource](#Dataset.relatedresource) , [release date](#Dataset.releasedate) , [sample](#Dataset.sample) , [source](#Dataset.source) , [spatial resolution](#Dataset.spatialresolution) , [temporal coverage](#Dataset.temporalcoverage) , [temporal resolution](#Dataset.temporalresolution) , [theme](#Dataset.theme) , [title](#Dataset.title) , [type](#Dataset.type) , [version](#Dataset.version) , [version notes](#Dataset.versionnotes) , [was generated by](#Dataset.wasgeneratedby) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [access rights](http://purl.org/dc/terms/accessRights) | [Rights statement](#Rightsstatement) | 0..1 | Information that indicates whether the Dataset is publicly accessible, has access restrictions or is not public. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_access_rights) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_access_rights) |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | [Legal Resource](#LegalResource) | 0..\* | The legislation that mandates the creation or management of the Dataset. |     |     | P   |
| [conforms to](http://purl.org/dc/terms/conformsTo) | [Standard](#Standard) | 0..\* | An implementing rule or other specification. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_conforms_to) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_conforms_to) |
| [contact point](http://www.w3.org/ns/dcat#contactPoint) | [Kind](#Kind) | 0..\* | Contact information that can be used for sending comments about the Dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) |
| [creator](http://purl.org/dc/terms/creator) | [Agent](#Agent) | 0..\* | An entity responsible for producing the dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator) |
| [dataset distribution](http://www.w3.org/ns/dcat#distribution) | [Distribution](#Distribution) | 0..\* | An available Distribution for the Dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution) |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 1..\* | A free-text account of the Dataset. | This property can be repeated for parallel language versions of the description. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) |
| [documentation](http://xmlns.com/foaf/0.1/page) | [Document](#Document) | 0..\* | A page or document about this Dataset. |     |     | P   |
| [frequency](http://purl.org/dc/terms/accrualPeriodicity) | [Frequency](#Frequency) | 0..1 | The frequency at which the Dataset is updated. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_frequency) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_frequency) |
| [geographical coverage](http://purl.org/dc/terms/spatial) | [Location](#Location) | 0..\* | A geographic region that is covered by the Dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) |
| [has version](http://www.w3.org/ns/dcat#hasVersion) | [Dataset](#Dataset) | 0..\* | A related Dataset that is a version, edition, or adaptation of the described Dataset. |     |     | P   |
| [identifier](http://purl.org/dc/terms/identifier) | [Literal](#Literal) | 0..\* | The main identifier for the Dataset, e.g. the URI or other unique identifier in the context of the Catalogue. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_identifier) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_identifier) |
| [in series](http://www.w3.org/ns/dcat#inSeries) | [Dataset Series](#DatasetSeries) | 0..\* | A dataset series of which the dataset is part. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_in_series) |
| [is referenced by](http://purl.org/dc/terms/isReferencedBy) | [Resource](#Resource) | 0..\* | A related resource, such as a publication, that references, cites, or otherwise points to the dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_is_referenced_by) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_is_referenced_by) |
| [keyword](http://www.w3.org/ns/dcat#keyword) | [Literal](#Literal) | 0..\* | A keyword or tag describing the Dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_keyword) |
| [landing page](http://www.w3.org/ns/dcat#landingPage) | [Document](#Document) | 0..\* | A web page that provides access to the Dataset, its Distributions and/or additional information. | It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_landing_page) |
| [language](http://purl.org/dc/terms/language) | [Linguistic system](#Linguisticsystem) | 0..\* | A language of the Dataset. | This property can be repeated if there are multiple languages in the Dataset. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_language) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_language) |
| [modification date](http://purl.org/dc/terms/modified) | [Temporal Literal](#TemporalLiteral) | 0..1 | The most recent date on which the Dataset was changed or modified. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) |
| [other identifier](http://www.w3.org/ns/adms#identifier) | [Identifier](#Identifier) | 0..\* | A secondary identifier of the Dataset | Examples are MAST/ADS \[\[MASTADS\]\], DOI \[\[DOI\]\], EZID \[\[EZID\]\] or W3ID \[\[W3ID\]\]. | [Link](https://www.w3.org/TR/vocab-dcat-3/#dereferenceable-identifiers) | [E](https://www.w3.org/TR/vocab-dcat-3/#dereferenceable-identifiers) |
| [provenance](http://purl.org/dc/terms/provenance) | [Provenance Statement](#ProvenanceStatement) | 0..\* | A statement about the lineage of a Dataset. |     |     | P   |
| [publisher](http://purl.org/dc/terms/publisher) | [Agent](#Agent) | 0..1 | An entity (organisation) responsible for making the Dataset available. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) |
| [qualified attribution](http://www.w3.org/ns/prov#qualifiedAttribution) | [Attribution](#Attribution) | 0..\* | An Agent having some form of responsibility for the resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_qualified_attribution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_qualified_attribution) |
| [qualified relation](http://www.w3.org/ns/dcat#qualifiedRelation) | [Relationship](#Relationship) | 0..\* | A description of a relationship with another resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_qualified_relation) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_qualified_relation) |
| [related resource](http://purl.org/dc/terms/relation) | [Resource](#Resource) | 0..\* | A related resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_relation) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_relation) |
| [release date](http://purl.org/dc/terms/issued) | [Temporal Literal](#TemporalLiteral) | 0..1 | The date of formal issuance (e.g., publication) of the Dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) |
| [sample](http://www.w3.org/ns/adms#sample) | [Distribution](#Distribution) | 0..\* | A sample distribution of the dataset. |     |     | P   |
| [source](http://purl.org/dc/terms/source) | [Dataset](#Dataset) | 0..\* | A related Dataset from which the described Dataset is derived. |     |     | P   |
| [spatial resolution](http://www.w3.org/ns/dcat#spatialResolutionInMeters) | [xsd:decimal](#xsd%3Adecimal) | 0..1 | The minimum spatial separation resolvable in a dataset, measured in meters. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial_resolution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial_resolution) |
| [temporal coverage](http://purl.org/dc/terms/temporal) | [Period of time](#Periodoftime) | 0..\* | A temporal period that the Dataset covers. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal) |
| [temporal resolution](http://www.w3.org/ns/dcat#temporalResolution) | [xsd:duration](#xsd%3Aduration) | 0..1 | The minimum time period resolvable in the dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal_resolution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal_resolution) |
| [theme](http://www.w3.org/ns/dcat#theme) | [Concept](#Concept) | 0..\* | A category of the Dataset. | A Dataset may be associated with multiple themes. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_theme) |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 1..\* | A name given to the Dataset. | This property can be repeated for parallel language versions of the name. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) |
| [type](http://purl.org/dc/terms/type) | [Concept](#Concept) | 0..\* | A type of the Dataset. | A recommended controlled vocabulary data-type is foreseen. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_type) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_type) |
| [version](http://www.w3.org/ns/dcat#version) | [Literal](#Literal) | 0..1 | The version indicator (name or identifier) of a resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_version) |
| [version notes](http://www.w3.org/ns/adms#versionNotes) | [Literal](#Literal) | 0..\* | A description of the differences between this version and a previous version of the Dataset. | This property can be repeated for parallel language versions of the version notes. |     | P   |
| [was generated by](http://www.w3.org/ns/prov#wasGeneratedBy) | [Activity](#Activity) | 0..\* | An activity that generated, or provides the business context for, the creation of the dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_was_generated_by) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_was_generated_by) |

### [Dataset Series](http://www.w3.org/ns/dcat#DatasetSeries)

Definition

A collection of datasets that are published separately, but share some characteristics that group them.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset_Series)

Usage Note

It is recommended to avoid Dataset Series without a dataset in the collection. Therefore at least one Dataset should refer to a Dataset Series using the property in series (dcat:inSeries).

Subclass of

[Catalogued Resource](#CataloguedResource)

Properties

For this entity the following properties are defined: [applicable legislation](#DatasetSeries.applicablelegislation) , [contact point](#DatasetSeries.contactpoint) , [description](#DatasetSeries.description) , [frequency](#DatasetSeries.frequency) , [geographical coverage](#DatasetSeries.geographicalcoverage) , [modification date](#DatasetSeries.modificationdate) , [publisher](#DatasetSeries.publisher) , [release date](#DatasetSeries.releasedate) , [temporal coverage](#DatasetSeries.temporalcoverage) , [title](#DatasetSeries.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | [Legal Resource](#LegalResource) | 0..\* | The legislation that mandates the creation or management of the Dataset Series. |     |     | P   |
| [contact point](http://www.w3.org/ns/dcat#contactPoint) | [Kind](#Kind) | 0..\* | Contact information that can be used for sending comments about the Dataset Series. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point) |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 1..\* | A free-text account of the Dataset Series. | This property can be repeated for parallel language versions. It is recommended to provide an indication about the dimensions the Dataset Series evolves. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_description) |
| [frequency](http://purl.org/dc/terms/accrualPeriodicity) | [Frequency](#Frequency) | 0..1 | The frequency at which the Dataset Series is updated. | The frequency of a dataset series is not equal to the frequency of the dataset in the collection. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_frequency) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_frequency) |
| [geographical coverage](http://purl.org/dc/terms/spatial) | [Location](#Location) | 0..\* | A geographic region that is covered by the Dataset Series. | When spatial coverage is a dimension in the dataset series then the spatial coverage of each dataset in the collection should be part of the spatial coverage. In that case, an open ended value is recommended, e.g. EU or a broad bounding box covering the expected values. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_spatial) |
| [modification date](http://purl.org/dc/terms/modified) | [Temporal Literal](#TemporalLiteral) | 0..1 | The most recent date on which the Dataset Series was changed or modified. | This is not equal to the most recent modified dataset in the collection of the dataset series. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_update_date) |
| [publisher](http://purl.org/dc/terms/publisher) | [Agent](#Agent) | 0..1 | An entity (organisation) responsible for ensuring the coherency of the Dataset Series | The publisher of the dataset series may not be the publisher of all datasets.  E.g. a digital archive could take over the publishing of older datasets in the series. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher) |
| [release date](http://purl.org/dc/terms/issued) | [Temporal Literal](#TemporalLiteral) | 0..1 | The date of formal issuance (e.g., publication) of the Dataset Series. | The moment when the dataset series was established as a managed resource. This is not equal to the release date of the oldest dataset in the collection of the dataset series. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_release_date) |
| [temporal coverage](http://purl.org/dc/terms/temporal) | [Period of time](#Periodoftime) | 0..\* | A temporal period that the Dataset Series covers. | When temporal coverage is a dimension in the dataset series then the temporal coverage of each dataset in the collection should be part of the temporal coverage. In that case, an open ended value is recommended, e.g. after 2012. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_temporal) |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 1..\* | A name given to the Dataset Series. | This property can be repeated for parallel language versions of the name. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_title) |

### [Distribution](http://www.w3.org/ns/dcat#Distribution)

Definition

A physical embodiment of the Dataset in a particular format.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution)

Properties

For this entity the following properties are defined: [access service](#Distribution.accessservice) , [access URL](#Distribution.accessURL) , [applicable legislation](#Distribution.applicablelegislation) , [availability](#Distribution.availability) , [byte size](#Distribution.bytesize) , [checksum](#Distribution.checksum) , [compression format](#Distribution.compressionformat) , [description](#Distribution.description) , [documentation](#Distribution.documentation) , [download URL](#Distribution.downloadURL) , [format](#Distribution.format) , [has policy](#Distribution.haspolicy) , [language](#Distribution.language) , [licence](#Distribution.licence) , [linked schemas](#Distribution.linkedschemas) , [media type](#Distribution.mediatype) , [modification date](#Distribution.modificationdate) , [packaging format](#Distribution.packagingformat) , [release date](#Distribution.releasedate) , [rights](#Distribution.rights) , [spatial resolution](#Distribution.spatialresolution) , [status](#Distribution.status) , [temporal resolution](#Distribution.temporalresolution) , [title](#Distribution.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [access service](http://www.w3.org/ns/dcat#accessService) | [Data Service](#DataService) | 0..\* | A data service that gives access to the distribution of the dataset. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_service) |
| [access URL](http://www.w3.org/ns/dcat#accessURL) | [Resource](#Resource) | 1..\* | A URL that gives access to a Distribution of the Dataset. | The resource at the access URL may contain information about how to get the Dataset. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_access_url) |
| [applicable legislation](http://data.europa.eu/r5r/applicableLegislation) | [Legal Resource](#LegalResource) | 0..\* | The legislation that mandates the creation or management of the Distribution. |     |     | P   |
| [availability](http://data.europa.eu/r5r/availability) | [Concept](#Concept) | 0..1 | An indication how long it is planned to keep the Distribution of the Dataset available. |     |     | P   |
| [byte size](http://www.w3.org/ns/dcat#byteSize) | [xsd:nonNegativeInteger](#xsd%3AnonNegativeInteger) | 0..1 | The size of a Distribution in bytes. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_size) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_size) |
| [checksum](http://spdx.org/rdf/terms#checksum) | [Checksum](#Checksum) | 0..1 | A mechanism that can be used to verify that the contents of a distribution have not changed. | The checksum is related to the downloadURL. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_checksum) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_checksum) |
| [compression format](http://www.w3.org/ns/dcat#compressFormat) | [Media Type](#MediaType) | 0..1 | The format of the file in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file. | It SHOULD be expressed using a media type as defined in the official register of media types managed by [IANA](https://www.iana.org/). | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_compression_format) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_compression_format) |
| [description](http://purl.org/dc/terms/description) | [Literal](#Literal) | 0..\* | A free-text account of the Distribution. | This property can be repeated for parallel language versions of the description. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_description) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_description) |
| [documentation](http://xmlns.com/foaf/0.1/page) | [Document](#Document) | 0..\* | A page or document about this Distribution. |     |     | P   |
| [download URL](http://www.w3.org/ns/dcat#downloadURL) | [Resource](#Resource) | 0..\* | A URL that is a direct link to a downloadable file in a given format. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_download_url) |
| [format](http://purl.org/dc/terms/format) | [Media Type or Extent](#MediaTypeorExtent) | 0..1 | The file format of the Distribution. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_format) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_format) |
| [has policy](http://www.w3.org/ns/odrl/2/hasPolicy) | [Policy](#Policy) | 0..1 | The policy expressing the rights associated with the distribution if using the \[\[ODRL\]\] vocabulary. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_has_policy) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_has_policy) |
| [language](http://purl.org/dc/terms/language) | [Linguistic system](#Linguisticsystem) | 0..\* | A language used in the Distribution. | This property can be repeated if the metadata is provided in multiple languages. |     | P   |
| [licence](http://purl.org/dc/terms/license) | [Licence Document](#LicenceDocument) | 0..1 | A licence under which the Distribution is made available. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_license) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_license) |
| [linked schemas](http://purl.org/dc/terms/conformsTo) | [Standard](#Standard) | 0..\* | An established schema to which the described Distribution conforms. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_conforms_to) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_conforms_to) |
| [media type](http://www.w3.org/ns/dcat#mediaType) | [Media Type](#MediaType) | 0..1 | The media type of the Distribution as defined in the official register of media types managed by IANA. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) |
| [modification date](http://purl.org/dc/terms/modified) | [Temporal Literal](#TemporalLiteral) | 0..1 | The most recent date on which the Distribution was changed or modified. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_update_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_update_date) |
| [packaging format](http://www.w3.org/ns/dcat#packageFormat) | [Media Type](#MediaType) | 0..1 | The format of the file in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together. | It SHOULD be expressed using a media type as defined in the official register of media types managed by [IANA](https://www.iana.org/). | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_packaging_format) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_packaging_format) |
| [release date](http://purl.org/dc/terms/issued) | [Temporal Literal](#TemporalLiteral) | 0..1 | The date of formal issuance (e.g., publication) of the Distribution. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_release_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_release_date) |
| [rights](http://purl.org/dc/terms/rights) | [Rights statement](#Rightsstatement) | 0..1 | A statement that specifies rights associated with the Distribution. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_rights) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_rights) |
| [spatial resolution](http://www.w3.org/ns/dcat#spatialResolutionInMeters) | [xsd:decimal](#xsd%3Adecimal) | 0..1 | The minimum spatial separation resolvable in a dataset distribution, measured in meters. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_spatial_resolution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_spatial_resolution) |
| [status](http://www.w3.org/ns/adms#status) | [Concept](#Concept) | 0..1 | The status of the distribution in the context of maturity lifecycle. | It MUST take one of the values Completed, Deprecated, Under Development, Withdrawn. |     | P   |
| [temporal resolution](http://www.w3.org/ns/dcat#temporalResolution) | [xsd:duration](#xsd%3Aduration) | 0..1 | The minimum time period resolvable in the dataset distribution. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_temporal_resolution) | [A](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_temporal_resolution) |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 0..\* | A name given to the Distribution. | This property can be repeated for parallel language versions of the description. | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_title) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_title) |

### [Kind](http://www.w3.org/2006/vcard/ns#Kind)

Definition

A description following the vCard specification, e.g. to provide telephone number and e-mail address for a contact point.

Usage Note

Note that the class Kind is the parent class for the four explicit types of [vCard](https://www.rfc-editor.org/rfc/rfc6350.html) (Individual, Organization, Location, Group).

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Licence Document](http://purl.org/dc/terms/LicenseDocument)

Definition

A legal document giving official permission to do something with a resource.

Properties

For this entity the following properties are defined: [type](#LicenceDocument.type) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [type](http://purl.org/dc/terms/type) | [Concept](#Concept) | 0..\* | A type of licence, e.g. indicating 'public domain' or 'royalties required'. |     |     | P   |

### [Location](http://purl.org/dc/terms/Location)

Definition

A spatial region or named place.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Location)

Usage Note

It can be represented using a controlled vocabulary or with geographic coordinates. In the latter case, the use of the [Core Location Vocabulary](https://semiceu.github.io/Core-Location-Vocabulary/) is recommended, following the approach described in the GeoDCAT-AP specification.

Properties

For this entity the following properties are defined: [bbox](#Location.bbox) , [centroid](#Location.centroid) , [geometry](#Location.geometry) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [bbox](http://www.w3.org/ns/dcat#bbox) | [Literal](#Literal) | 0..1 | The geographic bounding box of a resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:location_bbox) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:location_bbox) |
| [centroid](http://www.w3.org/ns/dcat#centroid) | [Literal](#Literal) | 0..1 | The geographic center (centroid) of a resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:location_centroid) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:location_centroid) |
| [geometry](http://www.w3.org/ns/locn#geometry) | [Geometry](#Geometry) | 0..1 | The corresponding geometry for a resource. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:location_geometry) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:location_geometry) |

### [Relationship](http://www.w3.org/ns/dcat#Relationship)

Definition

An association class for attaching additional information to a relationship between DCAT Resources.

Reference in DCAT

[Link](https://w3c.github.io/dxwg/dcat/#Class:Relationship)

Properties

For this entity the following properties are defined: [had role](#Relationship.hadrole) , [relation](#Relationship.relation) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [had role](http://www.w3.org/ns/dcat#hadRole) | [Role](#Role) | 1..n | A function of an entity or agent with respect to another entity or resource. |     | [Link](https://w3c.github.io/dxwg/dcat/#Property:relationship_hadRole) | [E](https://w3c.github.io/dxwg/dcat/#Property:relationship_hadRole) |
| [relation](http://purl.org/dc/terms/relation) | [Resource](#Resource) | 1..n | A resource related to the source resource. |     | [Link](https://w3c.github.io/dxwg/dcat/#Property:relationship_relation) | [E](https://w3c.github.io/dxwg/dcat/#Property:relationship_relation) |

## Supportive Entities

The supportive entities are supporting the main entities in the Application Profile. They are included in the Application Profile because they form the range of properties.

### [Activity](http://www.w3.org/ns/prov#Activity)

Definition

An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Attribution](http://www.w3.org/ns/prov#Attribution)

Definition

Attribution is the ascribing of an entity to an agent.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Checksum Algorithm](http://spdx.org/rdf/terms#ChecksumAlgorithm)

Definition

Algorithm for Checksums.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Concept](http://www.w3.org/2004/02/skos/core#Concept)

Definition

An idea or notion; a unit of thought.

Usage Note

In DCAT-AP, a Concept is used to denote codes within a codelist. In section \[\[\[#controlled-vocs\]\]\] the expectations are elaborated in more detail.

Properties

For this entity the following properties are defined: [preferred label](#Concept.preferredlabel) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [preferred label](http://www.w3.org/2004/02/skos/core#prefLabel) | [Literal](#Literal) | 1..n | A preferred label of the concept. | This property can be repeated for parallel language versions of the label. |     | P   |

### [Concept Scheme](http://www.w3.org/2004/02/skos/core#ConceptScheme)

Definition

An aggregation of one or more SKOS concepts.

Usage Note

In DCAT-AP, a Concept Scheme is used to denote a codelist. In section \[\[\[#controlled-vocs\]\]\] the expectations are elaborated in more detail.

Properties

For this entity the following properties are defined: [title](#ConceptScheme.title) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [title](http://purl.org/dc/terms/title) | [Literal](#Literal) | 1..n | A name of the concept scheme. | May be repeated for different versions of the name |     | P   |

### [Document](http://xmlns.com/foaf/0.1/Document)

Definition

A textual resource intended for human consumption that contains information, e.g. a web page about a Dataset.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Frequency](http://purl.org/dc/terms/Frequency)

Definition

A rate at which something recurs, e.g. the publication of a Dataset.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Geometry](http://www.w3.org/ns/locn#Geometry)

Definition

The locn:Geometry class provides the means to identify a location as a point, line, polygon, etc. expressed using coordinates in some coordinate reference system.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Identifier](http://www.w3.org/ns/adms#Identifier)

Definition

This is based on the UN/CEFACT Identifier class.

Usage Note

An identifier in a particular context, consisting of the

*   content string that is the identifier;
*   an optional identifier for the identifier scheme;
*   an optional identifier for the version of the identifier scheme;
*   an optional identifier for the agency that manages the identifier scheme.

Properties

For this entity the following properties are defined: [notation](#Identifier.notation) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [notation](http://www.w3.org/2004/02/skos/core#notation) | [Literal](#Literal) | 1   | A string that is an identifier in the context of the identifier scheme referenced by its datatype. |     |     | P   |

### [Legal Resource](http://data.europa.eu/eli/ontology#LegalResource)

Definition

This class represents the legislation,policy or policies that lie behind the Rules that govern the service.

Usage Note

The definition and properties of the Legal Resource class are aligned with the ontology included in "Council conclusions inviting the introduction of the European Legislation Identifier ([ELI](https://eur-lex.europa.eu/eli-register/about.html))". For describing the attributes of a Legal Resource (labels, preferred labels, alternative labels, definition, etc.) we refer to the ([ELI](https://op.europa.eu/en/web/eu-vocabularies/eli)) ontology. In this data specification the use is restricted to instances of this class that follow the ([ELI](https://op.europa.eu/en/web/eu-vocabularies/eli)) URI guidelines.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Linguistic system](http://purl.org/dc/terms/LinguisticSystem)

Definition

A system of signs, symbols, sounds, gestures, or rules used in communication, e.g. a language.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Literal](http://www.w3.org/2000/01/rdf-schema#Literal)

Definition

A literal value such as a string or integer; Literals may be typed, e.g. as a date according to xsd:date. Literals that contain human-readable text have an optional language tag as defined by BCP 47 \[\[rfc5646\]\].

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Media type](http://purl.org/dc/terms/MediaType)

Definition

A media type, e.g. the format of a computer file.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Media Type](http://purl.org/dc/terms/MediaType)

Definition

A file format or physical medium.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Media Type or Extent](http://purl.org/dc/terms/MediaTypeOrExtent)

Definition

A media type or extent.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Period of time](http://purl.org/dc/terms/PeriodOfTime)

Definition

An interval of time that is named or defined by its start and end dates.

Reference in DCAT

[Link](https://www.w3.org/TR/vocab-dcat-3/#Class:Period_of_Time)

Properties

For this entity the following properties are defined: [beginning](#Periodoftime.beginning) , [end](#Periodoftime.end) , [end date](#Periodoftime.enddate) , [start date](#Periodoftime.startdate) .

| Property | Range | Card | Definition | Usage | DCAT | Reuse |
| --- | --- | --- | --- | --- | --- | --- |
| [beginning](http://www.w3.org/2006/time#hasBeginning) | [Time instant](#Timeinstant) | 0..1 | The beginning of a period or interval. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:period_has_beginning) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:period_has_beginning) |
| [end](http://www.w3.org/2006/time#hasEnd) | [Time instant](#Timeinstant) | 0..1 | The end of a period or interval. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:period_has_end) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:period_has_end) |
| [end date](http://www.w3.org/ns/dcat#endDate) | [Temporal Literal](#TemporalLiteral) | 0..1 | The end of the period. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:period_end_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:period_end_date) |
| [start date](http://www.w3.org/ns/dcat#startDate) | [Temporal Literal](#TemporalLiteral) | 0..1 | The start of the period. |     | [Link](https://www.w3.org/TR/vocab-dcat-3/#Property:period_start_date) | [E](https://www.w3.org/TR/vocab-dcat-3/#Property:period_start_date) |

### [Policy](http://www.w3.org/ns/odrl/2/Policy)

Definition

A non-empty group of Permissions and/or Prohibitions.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Provenance Statement](http://purl.org/dc/terms/ProvenanceStatement)

Definition

A statement of any changes in ownership and custody of a resource since its creation that are significant for its authenticity, integrity, and interpretation.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Resource](http://www.w3.org/2000/01/rdf-schema#Resource)

Definition

Anything described by RDF.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Rights statement](http://purl.org/dc/terms/RightsStatement)

Definition

A statement about the intellectual property rights (IPR) held in or over a resource, a legal document giving official permission to do something with a resource, or a statement about access rights.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Role](http://www.w3.org/ns/dcat#Role)

Definition

A role is the function of a resource or agent with respect to another resource, in the context of resource attribution or resource relationships.

Reference in DCAT

[Link](https://w3c.github.io/dxwg/dcat/#Class:Role)

Usage Note

Note it is a subclass of skos:Concept.

Properties

This specification does not impose any additional requirements to properties for this entity.

### [Standard](http://purl.org/dc/terms/Standard)

Definition

A standard or other specification to which a resource conforms.

Properties

This specification does not impose any additional requirements to properties for this entity.

## Datatypes

The following datatypes are used within this specification.

|     | Class | Definition |
| --- | --- | --- |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20TemporalLiteral&body=Explain%20your%20issue) | [Temporal Literal](http://www.w3.org/2000/01/rdf-schema#Literal) | rdfs:Literal encoded using the relevant \[\[ISO8601\]\] Date and Time compliant string and typed using the appropriate XML Schema datatype (xsd:gYear, xsd:gYearMonth, xsd:date, or xsd:dateTime). |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20TimeInstant&body=Explain%20your%20issue) | [Time instant](http://www.w3.org/2006/time#Instant) | A temporal entity with zero extent or duration. |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20Xsd:datetime&body=Explain%20your%20issue) | [xsd:dateTime](http://www.w3.org/2001/XMLSchema#dateTime) | Object with integer-valued year, month, day, hour and minute properties, a decimal-valued second property, and a boolean timezoned property. |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20Xsd:decimal&body=Explain%20your%20issue) | [xsd:decimal](http://www.w3.org/2001/XMLSchema#decimal) | Decimal represents a subset of the real numbers, which can be represented by decimal numerals. The ·value space· of decimal is the set of numbers that can be obtained by multiplying an integer by a non-positive power of ten, i.e., expressible as i × 10^-n where i and n are integers and n >= 0. |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20Xsd:duration&body=Explain%20your%20issue) | [xsd:duration](http://www.w3.org/2001/XMLSchema#duration) | Duration represents a duration of time. The ·value space· of duration is a six-dimensional space where the coordinates designate the Gregorian year, month, day, hour, minute, and second components defined in § 5.5.3.2 of \[\[ISO8601\]\], respectively. |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20Xsd:hexbinary&body=Explain%20your%20issue) | [xsd:hexBinary](http://www.w3.org/2001/XMLSchema#hexBinary) | Hex-encoded binary data. The ·value space· of hexBinary is the set of finite-length sequences of binary octets. |
| [![(create issue)](html/callout.png)](https://github.com/SEMICeu/DCAT-AP/issues/new?title=Issue%20for%20Xsd:nonnegativeinteger&body=Explain%20your%20issue) | [xsd:nonNegativeInteger](http://www.w3.org/2001/XMLSchema#nonNegativeInteger) | Number derived from integer by setting the value of minInclusive to be 0. |
