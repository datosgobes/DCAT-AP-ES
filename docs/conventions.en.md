# Introduction
In Spain, the exchange of open data between the Open Data Initiative of the Government of Spain ([datos.gob.es](https://datos.gob.es)) and various data providers, such as regional catalogs, Local Entities, and other organizations, is framed to ensure interoperability and homogeneity of metadata. To achieve this, the European application profile [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) will be adapted together with the elements described in the extension [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) to incorporate the modeling of the [High Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) (*High Value Datasets*) to national needs, resulting in the standard **DCAT-AP-ES**, which will be established as a reference for the exchange of metadata on public information at national level.  

Since the implementation of the standard, [datos.gob.es](https://datos.gob.es) accepts metadata in **DCAT-AP-ES** format, as well as the application profile referred to in the Technical Standard. For those providers who federate directly to the portal, a transitional period will be established following the publication of new versions, during which they can adjust their systems to the updated standard from the previous profile of the Technical Standard for Interoperability of Public Sector Information Resources ([**NTI-RISP**](https://datos.gob.es/en/doc-tags/nti-risp)).

The conventions guide not only details the specific modifications introduced in the Spanish standard compared to the European version but also defines additional rules to address practical needs. These may include particularities of the Spanish open data context, where implementation might align with distinct technical requirements. Moreover, some of these rules are expected to evolve faster than the main specification, providing greater flexibility and adaptability to technological changes.

This document has as its **target audience** the ^^developers and maintainers of open data portals^^, as well as ^^data providers who collaborate with the national catalog^^. Its purpose is to provide clear guidelines and practical tools for implementing the standard efficiently. However, for use in specific contexts, the possibility of establishing additional conventions that complement general regulations is left open.

To ensure consistent interpretation, normative terms such as **MUST**, **SHOULD**, and **MAY** are used, as defined in **[RFC2119](https://www.rfc-editor.org/rfc/rfc2119)**, to differentiate mandatory guidelines from optional ones. Although the manual includes diagrams and illustrative examples, these are not normative unless explicitly stated.

This approach aims not only to standardize metadata exchange but also to foster greater harmonization and collaboration among different levels of government in Spain, ensuring robust and scalable interoperability.

## Prefixes Used
All namespace prefixes used throughout the document are referenced in [Annex 4. Namespaces used in the document](#annex-4-document-namespaces).

## Types of Conventions
### Technical Conventions
These conventions define technical aspects of implementation, including encoding, resource identification, and entity modeling. They are essential for ensuring technical interoperability and correct interpretation of metadata.

### Organizational Conventions
These conventions establish rules for the management and organization of catalogs, data federation, and the identification of organizations. They provide the necessary governance framework for effective metadata management.

### Semantic Conventions
These conventions ensure consistency in the description of resources, guaranteeing that metadata is semantically accurate and consistent.

## List of Conventions
- [**Convention 01**](#convention-01): The publisher's identifier **MUST** [be registered and available in the taxonomy of datos.gob.es](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es)
- [**Convention 02**](#convention-02): The literals `dct:title`, `dct:description`, `vcard:organization-name`, `vcard:fn`, `foaf:name`, `dcat:keyword` and `adms:versionNotes` **MUST** be defined with language tags, at least in Spanish `es`, and cannot be empty literals.
- [**Convention 03**](#convention-03): Identifiers and URI references **SHOULD** use the `http://` scheme instead of `https://` as a general rule.
- [**Convention 04**](#convention-04): Organizations **SHOULD** implement automatic federation through RDF as the sole method of publishing metadata in DCAT-AP-ES format, avoiding the coexistence of manual and automatic federation for the same organization.
- [**Convention 05**](#convention-05): URIs **MUST** be correctly encoded at their source, especially when they contain: 1. Reserved characters (`?`, `&`, `=`, `#`, etc.) 2. Spaces 3. Non-ASCII characters (accents, `ñ`, etc.) 4. Special characters (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)
- [**Convention 06**](#convention-06): Resources **MUST** have a unique and persistent identifier that meets the following requirements: 1. Include the `dct:identifier` property with a unique value for each resource. 2. Maintain identifier consistency even if the resource is updated. 3. Use the same identifier when the resource is published in different catalogs. 4. Generate, maintain, and manage the identifier by the resource publisher, being external to [datos.gob.es](https://datos.gob.es/)
- [**Convention 07**](#convention-07): References to legal documents **MUST** use ELI identifiers when available: 1. For European legislation: `http://data.europa.eu/eli/...` 2. For national legislation: `https://www.boe.es/eli/...` 3. For derived documents, use the ELI URI of the main document
- [**Convention 08**](#convention-08): Creation and modification dates of resources **MUST** meet the following requirements: 1. The modification date (`dct:modified`) **MUST** be later than the creation date (`dct:created`) 2. The modification date **MUST** reflect the last change in the data, not in the metadata
- [**Convention 09**](#convention-09): A single catalog per publishing organization **MUST** be used, avoiding the use of subcatalogs through `dct:hasPart`. Relationships between resources **MUST** be modeled using the following properties as appropriate.
- [**Convention 10**](#convention-10): The catalog **MUST** include at least the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector) in the `dcat:themeTaxonomy` property.
- [**Convention 11**](#convention-11): Additional taxonomies **MAY** be included to improve dataset classification: `http://publications.europa.eu/resource/authority/data-theme` or `http://inspire.ec.europa.eu/theme`
- [**Convention 12**](#convention-12): Datasets cataloged as HVD **MUST** include at least one data service (`dcat:DataService`) with the following mandatory properties: 1. Endpoint URL (`dcat:endpointURL`) 2. Endpoint Description (`dcat:endpointDescription`) 3. Contact Point (`dcat:contactPoint`) 4. Applicable Legislation (`dcatap:applicableLegislation`) 5. HVD Category (`dcatap:hvdCategory`) 6. Documentation (`foaf:page`) 7. Served Datasets (`dcat:servesDataset`)
- [**Convention 13**](#convention-13): OGC services **SHOULD** be modeled as `dcat:DataService` instead of `dcat:Distribution`.
- [**Convention 14**](#convention-14): Publisher information **SHOULD** contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`
- [**Convention 15**](#convention-15): Creator information **SHOULD** contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`
- [**Convention 16**](#convention-16): Geographic coverage **MUST** be declared using URIs from the [Annex V of NTI-RISP for geographic resources of Spanish territory](https://datos.gob.es/es/recurso/sector-publico/territorio), following these rules: 1. Use the most specific territorial level that corresponds to the dataset's actual scope. 2. Avoid using `Spain` by default when the scope is narrower. 3. Do not declare an Autonomous Community and its provinces simultaneously. 4. For single-province Autonomous Communities, preferably use the reference to the Autonomous Community.
- [**Convention 17**](#convention-17): When specifying geometric coverage, `WKT` **SHOULD** be used (according to [GeoSPARQL](http://www.opengeospatial.org/standards/geosparql)).
- [**Convention 18**](#convention-18): HVD data services **MUST** include at least one contact point (`dcat:contactPoint`) with one of the following properties: Email address (`vcard:hasEmail`) or Contact form URL (`vcard:hasURL`)
- [**Convention 19**](#convention-19): The contact point **SHOULD** include: 1. Name (`vcard:organization-name`) 2. Telephone number (`vcard:hasTelephone`) URI: `tel:` 3. Organization identifier (`vcard:hasUid`) 4. Email address (`vcard:hasEmail`) URI `mailto:` 5. Contact form URL (`vcard:hasURL`)
- [**Convention 20**](#convention-20): Contact points listed in the portal's taxonomy **MUST** be described as a `vcard:Kind` and not directly with the organization's URI.
- [**Convention 21**](#convention-21): In OGC service distributions, access URLs **MUST** be modeled as follows: In `dcat:accessURL`: Complete URL of the service capabilities request `GetCapabilities` (e.g.: `http://example.org/wms?request=GetCapabilities&service=WMS`) and in `dct:conformsTo`: URL of the corresponding OGC standard, e.g.: `http://www.opengeospatial.org/standards/wms`
- [**Convention 22**](#convention-22): Time periods **MUST** be described exclusively using the properties `dcat:startDate` and `dcat:endDate` within `dct:temporal`. The interval can also be open, that is, it can have only a start or only an end.
- [**Convention 23**](#convention-23): Datasets **MUST** include at least one distribution (`dcat:Distribution`).
- [**Convention 24**](#convention-24): When a DCAT-AP-ES resource derives from a source metadata of another standard (for example: INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.), a relationship **SHOULD** be included using the `adms:identifier` property pointing to the persistent identifier of the source metadata, using a node of type `adms:Identifier`.
- [**Convention 25**](#convention-25): To describe a dataset accessible via NSIP/ERPD, each `dcat:Dataset` **MUST** include: 1. `dct:title`: name given to the dataset. 2. `dct:description`: summary of the content in free text. 3. `dct:publisher`: entity (organization) responsible for making the dataset available. 4. `dct:accessRights`: access restrictions with one of the two only possible values [`RESTRICTED`](http://publications.europa.eu/resource/authority/access-right/RESTRICTED) or [`NON_PUBLIC`](http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC) 5. `dcat:distribution`: at least one distribution available to access the dataset.
- [**Convention 26**](#convention-26): To describe a distribution accessible via NSIP/ERPD, each `dcat:Distribution` **MUST** include: 1. `dcat:accessURL`: URL with information on how to request access. 2. `dcat:byteSize`: size in bytes (can be approximate). 3. `dct:format`: file type (vocabulary `file-type`) 4. `dct:rights`: reuse conditions applicable to this distribution.
- [**Convention 27**](#convention-27): A dataset accessible via NSIP/ERPD **SHOULD** be related through `dcatap:applicableLegislation` with specific legislation (at least the DGA Regulation: `http://data.europa.eu/eli/reg/2022/868/oj`) and, if it includes directly accessible endpoints or APIs, use the class [`dcat:DataService`](index.md#DataService) to describe the service in addition to `dcat:Distribution`.
- [**Convention 28**](#convention-28): For APIs with **universal access** APIKey (automatic registration without manual approval), a `dcat:DataService` **SHOULD** use `dct:accessRights` with value `PUBLIC` and include `dcat:endpointDescription` with OpenAPI document that specifies `securitySchemes` or document in `foaf:page` the documentation to obtain the key.
- [**Convention 29**](#convention-29): For APIs with **restricted access** APIKey (requires approval, contract or payment), a `dcat:DataService` **SHOULD** use `dct:accessRights` with value `RESTRICTED` and indicate in `dct:rights` the terms of use and `dcat:endpointDescription` with OpenAPI document.
- [**Convention 30**](#convention-30): The `dcat:themeTaxonomy` property in catalogs and the `dcat:theme` property in datasets and data services **MUST** support flexible cardinality `1..*` to allow classification in as many thematic schemes or taxonomies as necessary, as long as at least one corresponds to the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector).
- [**Convention 31**](#convention-31): Temporal duration values (`dcat:temporalResolution`) *MUST* preferably be expressed in ISO 8601 format (`xsd:duration`) as `PT24M`, but numerical representations in seconds (such as `1440.0`) are allowed due to technical limitations.

# General conventions {#general}

## Organization must have an identifier registered in datos.gob.es taxonomy. {#general-dir3}

To ensure the traceability of publishing organizations, they must be [registered and available in datos.gob.es taxonomy)](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es), either as a DIR3 for a public organization or a private organization whose identifier is the letter P followed by their NIF as a fictitious code ([see Annex 3. Mapping of Organizational Identifiers](#anexo-3-mapeo-de-identificadores-organizativos)).

!!! must organisational "Convention 01"

    The publisher's identifier **MUST** [be registered and available in the taxonomy of datos.gob.es](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es)

## Indicating Spanish language in declarations {#general-idioma}

Literal fields with multilingual `xml:lang` tags must be at least in Spanish (`es`).

!!! must technical "Convention 02" 

    The literals `dct:title`, `dct:description`, `vcard:organization-name `, `vcard:fn`, `foaf:name`, `dcat:keyword` and `adms:versionNotes` **MUST** be defined with language tags, at least in the spanish language `es`, and cannot be empty literals.

## Using HTTP URIs {#general-http-uris}

To maintain compatibility and avoid interoperability issues with systems that do not support TLS/SSL, it is recommended to use HTTP URIs instead of HTTPS in identifiers and references. HTTP URIs are equally dereferencable as HTTPS through redirection.

!!! should technical "Convention 03"

    Identifiers and URI references **SHOULD** use the `http://` scheme instead of `https://` as a general rule. This applies to:

    1.  Resource identifiers (`dcat:Dataset`, `dcat:Distribution`, etc.)
    2.  References to controlled vocabularies
    3.  URIs of taxonomies and concept schemes

!!! info "Example of correct URI usage"

    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-http-uris.ttl"
    ```

!!! info "Note on exceptions"
    There are exceptions to this recommendation, where the use of `https://` is justified:

    *   **[BOE ELI URIs](https://www.elidata.es/documentacion_tecnica/especificacion_tecnica.php):** The ELI identifiers of the Official State Gazette (BOE) use the `https://` scheme (`https://www.boe.es/eli/...`). Due to the nature of these identifiers and their widespread adoption, it is allowed and recommended to maintain the `https://` scheme for BOE ELI URIs.

## Automatic Data Federation {#general-federation}

To ensure consistency and quality of metadata, as well as to simplify the federation process, the exclusive use of automatic federation through RDF (DCAT-AP-ES) is established as the sole method for data ingestion into the portal.

!!! should organisational "Convention 04"
    
    Organizations SHOULD implement automatic federation through RDF as the sole method of publishing metadata in DCAT-AP-ES format, avoiding the coexistence of manual and automatic federation for the same organization.

!!! warning "Important"
    The coexistence of manual and automatic federation for the same organization can cause:
    
    - Inconsistencies in metadata
    - Duplicate datasets
    - Synchronization issues
    - Validation difficulties

!!! info "Note on Transition"
    Organizations currently using manual federation must plan the migration of their datasets to the new automatic federation system through RDF for DCAT-AP-ES.

## URI Encoding {#general-uri-encoding}

To ensure RDF validity and avoid processing issues, all URIs must be correctly encoded according to [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986#section-2.4).

!!! must technical "Convention 05"
    
    **URIs MUST** be correctly encoded at their source, especially when they contain:
    
    1. Reserved characters (`?`, `&`, `=`, `#`, etc.)
    2. Spaces
    3. Non-ASCII characters (accents, ñ, etc.)
    4. Special characters (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)

!!! info "Example of Correct URI Encoding"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-uri-encoding.ttl"
    ```

!!! warning "Important"
    The responsibility for encoding lies with the origin that generates the URIs:
    
    1. URIs must be encoded before serializing RDF to prevent it from being invalid.
    2. Encoding should not be delegated to subsequent systems

!!! info "Note on Implementation"
    To encode URIs, standard functions can be used:
    
    - JavaScript: `encodeURIComponent()`
    - Python: `urllib.parse.quote()`
    - Java: `URLEncoder.encode()`

## Unique and Persistent Identifiers {#general-resource-identifier}

To ensure correct identification and traceability of resources over time, as well as to avoid duplicities during federation from multiple sources, it is necessary to establish a system of unique and persistent identifiers since the identifier (`dct:identifier`) is the property that allows unique and unambiguous identification of the dataset.

!!! must technical "Convention 06"
    Resources **MUST** have a unique and persistent identifier that meets the following requirements:

    1. Include the `dct:identifier` property with a unique value for each resource.
    2. Maintain identifier consistency even if the resource is updated.
    3. Use the same identifier when the resource is published in different catalogs.
    4. Generate, maintain, and manage the identifier by the resource publisher, being external to [datos.gob.es](https://datos.gob.es/)

!!! info "Example of consistent identifiers"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-resource-identifier.ttl"
    ```

!!! warning "Important"
    - Identifiers must not change even if the resource's URI changes.
    - The same dataset published in different catalogs must maintain the same `dct:identifier`.
    - In case of conflict during federation, the last federated dataset will prevail according to the established order.
    - It is the sole responsibility of the publisher to maintain, persist, and ensure uniqueness of the identifier. Identifiers **CANNOT** be those assigned by datos.gob.es, as these are external and may change for internal reasons.

!!! info "Recommended identifier schemes"
    
    The following identifier schemes are recommended:

    | Scheme | Example | Recommended use |
    |---------|---------|-----------------|
    | **UUID v4** | `550e8400-e29b-41d4-a716-446655440000` | **Recommended by default** for new datasets without a previous identifier |
    | **URI + UUID** | `http://{base}/catalogo/{UUID}` | Web-resolvable identifiers |

!!! info "Note on Implementation"
    To avoid duplicates during federation:

    1. Coordinate with other publishers the assignment of identifiers.
    2. Document the identifier scheme used.
    3. Maintain a record of equivalences between identifiers from different sources.
    4. Consult the established federation order in case of multiple publications.

## ELI Identifiers for Legal Documents {#general-eli}

To ensure a unique and persistent reference to legal documents, the [European Legislation Identifier (ELI)](https://eur-lex.europa.eu/eli-register/about.html) must be used as the standard URI.

!!! must technical "Convention 07"
    References to legal documents **MUST** use ELI identifiers when available:

    1. For European legislation: `http://data.europa.eu/eli/...`
    2. For national legislation: `https://www.boe.es/eli/...`
    3. For derived documents, use the ELI URI of the main document

!!! info "Example of Using ELI Identifiers"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-eli.ttl"
    ```

!!! warning "Important"
    - Always use the consolidated version when available
    - For documents without ELI, use an alternative persistent URI
    - Maintain a record of equivalences between different identifiers

!!! info "Note on Implementation"
    - Consult the [ELI registry](https://eur-lex.europa.eu/eli-register/about.html) to obtain identifiers
    - Use ELI validation tools to verify the correctness of identifiers
    - Document the equivalences between different versions of legal documents

## Managing Creation and Modification Dates {#general-dates}

To ensure the temporal traceability of resources and their correct tracking, it is important to properly manage creation and modification dates.

!!! must technical "Convention 08"
    Creation and modification dates of resources **MUST** meet the following requirements:

    1. The modification date (`dct:modified`) **MUST** be later than the creation date (`dct:created`)
    2. The modification date **MUST** reflect the last change in the data, not in the metadata

!!! info "Example of Proper Date Management"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-dates.ttl"
    ```

!!! warning "Important"
    - The modification date must reflect changes in the data, not in the metadata
    - Dates must be consistent across different catalogs
    - Do not use future dates

!!! warning "Important"
    - Dates must be consistent across different catalogs
    - Do not use future dates

!!! info "Note on Implementation"
    To validate dates:
    
    1. Verify that the modification date is later than the creation date
    2. Check that the dates are in the formats defined by the model. Dates can be recorded using the standard format: `YYYY-MM-DD` (`xsd:date`), or the [ISO-8601 datetime](https://www.w3.org/TR/1998/NOTE-datetime-19980827) `YYYY-MM-DDThh:mm:ss` (`xsd:dateTime`). To improve interoperability it is **recommended** to include a time zone (TZD), for example `Z` or `+01:00` (the validator will emit a warning if missing). The year: `YYYY` (`xsd:gYear`) or the year and month: `YYYY-MM` (`xsd:gYearMonth`) are also allowed.

## Specification of Temporal Periods {#general-temporal}

The `dct:temporal` property in DCAT-AP-ES is used to describe the time period to which a dataset refers. Currently, there are multiple ways to describe this information, including the use of `dcat:startDate`, `dcat:endDate`, `time:hasBeginning`, `time:hasEnd` and `schema:startDate`, `schema:endDate`. However, this flexibility can generate inconsistencies in the representation of temporal periods.

Since both `dcat:startDate` and `dcat:endDate` can be recorded with [sufficiently flexible ranges](#PeriodOfTime.startDate), this approach is adopted for organizational reasons.


!!! must organisational "Convention 22"
    Time periods **MUST** be described exclusively using the properties `dcat:startDate` and `dcat:endDate` within `dct:temporal`. The interval can also be open, that is, it can have only a start or only an end.

!!! info "Example of correct use of a temporal period"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-temporal.ttl"
    ```

!!! info "Note on Implementation"
    It is recommended to review metadata, if inherited from the initial version of NTI-RISP, to update `schema:startDate`, `schema:endDate` (properties prior to [DCAT 2](https://www.w3.org/TR/vocab-dcat-2/#changes)) in new records according to the DCAT vocabulary.

## Restricted data but accessible through NSIP/ERPD {#general-nsip-erpd-publication}

This convention defines how to represent datasets that are not open but are accessible under the implementation of the [DGA (*Data Governance Act*) through NSIP/ERPD](https://digital-strategy.ec.europa.eu/en/policies/data-governance-act-explained). For more information on publishing restricted data in the context of NSIP/ERPD, you can find it in the [Guidelines for collecting data from the European Protected Data Registry (ERPD) in the possession of the public sector](https://dataeuropa.gitlab.io/data-provider-manual/how-to-publish/guidelines/#required-metadata).

!!! must semantic "Convention 25"
    To describe a dataset accessible via NSIP/ERPD, each `dcat:Dataset` **MUST** include:

    1. `dct:title`: name given to the dataset.
    2. `dct:description`: summary of the content in free text.
    3. `dct:publisher`: entity (organization) responsible for making the dataset available.
    4. `dct:accessRights`: access restrictions with one of the two only possible values [`RESTRICTED`](http://publications.europa.eu/resource/authority/access-right/RESTRICTED) or [`NON_PUBLIC`](http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC)
    5. `dcat:distribution`: at least one distribution available to access the dataset.

!!! must semantic "Convention 26"
    To describe a distribution accessible via NSIP/ERPD, each `dcat:Distribution` **MUST** include:

    1. `dcat:accessURL`: URL with information on how to request access.
    2. `dcat:byteSize`: size in bytes (can be approximate).
    3. `dct:format`: file type (vocabulary [`file-type`](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type))
    4. `dct:rights`: reuse conditions applicable to this distribution.

!!! should semantic "Convention 27"
    A dataset accessible via NSIP/ERPD **SHOULD** be related through `dcatap:applicableLegislation` with specific legislation (at least the DGA Regulation: `http://data.europa.eu/eli/reg/2022/868/oj`) and, if it includes directly accessible endpoints or APIs, use the [`dcat:DataService`](index.md#DataService) class to describe the service in addition to `dcat:Distribution`.

!!! success "Example of correct usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-nsip-erpd-publication.ttl"
    ```

!!! warning "Important"
    - The data.europa.eu harvester will automatically filter datasets with `dct:accessRights` containing: `http://publications.europa.eu/resource/authority/access-right/RESTRICTED` or `http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC` for the ERPD catalog
    - The absence of `dcat:byteSize` or `dct:format` in the distribution may cause it to be rejected in the ingestion process.
    - If both `dct:accessURL` and `dcat:downloadURL` are provided, the harvester will prioritize `accessURL` for NSIP.

## Expansion of Topic Taxonomies {#general-themes}
In the DCAT-AP-ES profile, the cardinality of the `dcat:themeTaxonomy` properties (in catalog) and `dcat:theme` (in datasets and services) [is currently limited to a maximum of 3 values (`1..3`)](index.md#Catalog.themeTaxonomy). However, there are scenarios where it is necessary to associate more than three thematic taxonomies or topics, especially for interoperability with sectoral profiles (INSPIRE, Eurovoc), integration with international catalogs, or for multithematic datasets.

!!! must organisational "Convention 30"
    The `dcat:themeTaxonomy` property in catalogs and the `dcat:theme` property in datasets and data services **MUST** support flexible cardinality `1..*` to allow classification in as many thematic schemes or taxonomies as necessary, as long as at least one corresponds to the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector). 

!!! info "Example of expanded topics serialization"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-themes.ttl"
    ```

## Representation of temporal durations {#general-temporal-resolution}

The `dcat:temporalResolution` property is used to specify the minimum temporal granularity of the data in a dataset or distribution. According to the DCAT specification, these values must be expressed as `xsd:duration` following the [ISO 8601 duration format](https://tc39.es/proposal-temporal/docs/duration.html) (for example, `PT24M` for 24 minutes, `P7D` for 7 days).

However, a [technical limitation in Virtuoso](https://github.com/openlink/virtuoso-opensource/issues/936) has been identified that can automatically convert valid ISO 8601 durations to numeric representations in seconds when retrieving data from the triple store. This affects the federation and SHACL validation process when the original values submitted by publishers in correct ISO 8601 format are inadvertently transformed.

When numeric values in seconds appear in the [datos.gob.es](https://datos.gob.es) federator, an informative warning will be generated that **does not require corrective action** from the publisher if:

1. The original value was correctly submitted in ISO 8601 format
2. The conversion occurred during storage in the triple store
3. The numeric value in seconds is mathematically equivalent to the original ISO 8601 value

!!! should organisational "Convention 31"
    Temporal duration values (`dcat:temporalResolution`) **SHOULD** preferably be expressed in ISO 8601 format (`xsd:duration`) such as `PT24M`, but numeric representations in seconds (such as `1440.0`) are accepted due to technical limitations.

!!! info "Example of temporal durations"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general_temporal-resolution.ttl"
    ```

!!! warning "Note on validation"
    * Publishers must always submit values in standard ISO 8601 format
    * SHACL validation will accept both formats to avoid rejections due to inadvertent conversions
    * Warnings about numeric format in the federator indicate the technical issue but do not require correction if the source was correct
    * It is recommended to verify the original values in the source catalogue before making any modifications

# Conventions for `dcat:Catalog` {#catalog}

## Subcatalogs and relationships between resources (`dct:hasPart`) {#catalog-dct-haspart}

To maintain simplicity and avoid ambiguity problems in catalog federation, it is recommended to use a single catalog per organization and express relationships between resources through the specific subproperties of [`dcterms:relation`](https://www.w3.org/TR/vocab-dcat-2/#Property:resource_relation).

!!! must organisational "Convention 09"
    A single catalog per publishing organization **MUST** be used, avoiding the use of subcatalogs through `dct:hasPart`. Relationships between resources **MUST** be modeled using the following properties as appropriate:

    1. For dataset distributions: `dcat:distribution`
    2. For data services: `dcat:service`
    3. For versions: `dct:hasVersion`
    4. For related resources with known semantics: other subproperties of `dct:relation`
    5. For non-specific relationships: `dct:relation`

!!! info "Example of modeling relationships without subcatalogs"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_catalog-dct-haspart.ttl"
    ```

!!! info "Note on the use of relationships"
    1. Always use the most specific property available to express the relationship
    2. `dct:relation` should be used only when the nature of the relationship is unknown
    3. Hierarchical relationships can be expressed through `dct:isPartOf`/`dct:hasPart`

## Thematic taxonomies (`dcat:themeTaxonomy`) {#catalog-dcat-themetaxonomy}

Catalogs must include at least the primary sector taxonomy to classify their *datasets*. One of the two additional taxonomies can be included to enrich the classification, information on mappings between [NTI-RISP Sectors and DCAT-AP Themes (Annex 1)](#annex-1-mapping-nti-themes-dcatap-themes), as well as between [DCAT-AP Themes and INSPIRE Themes (Annex 2)](#annex-2-mapping-inspire-themes-dcatap-themes) is included.

!!! must organisational "Convention 10"
    
    The catalog **MUST** include at least the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector) in the `dcat:themeTaxonomy` property. 
    

!!! may semantic "Convention 11"
    
    Additional taxonomies **MAY** be included to improve dataset classification: `http://publications.europa.eu/resource/authority/data-theme` or `http://inspire.ec.europa.eu/theme`

!!! info "Example of taxonomy usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_catalog-dcat-themetaxonomy.ttl"
    ```

# Conventions for `dcat:DataService` {#dataservice}

## HVD data services (`dcat:DataService`) {#dataservice-hvd-dataservice}

[High value datasets (HVD) must provide programmatic access to their data through APIs](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138). The specification of data services is done through the `dcat:DataService` class associated with the dataset distributions through `dcat:accessService`.

!!! must semantic "Convention 12"
    Datasets cataloged as HVD **MUST** include at least one data service (`dcat:DataService`) with the following mandatory properties:
    
    1. Endpoint URL (`dcat:endpointURL`)  
    2. Endpoint Description (`dcat:endpointDescription`)
    3. Contact Point (`dcat:contactPoint`)
    4. Applicable Legislation (`dcatap:applicableLegislation`)
    5. HVD Category (`dcatap:hvdCategory`)
    6. Documentation (`foaf:page`)
    7. Served Datasets (`dcat:servesDataset`)


!!! info "Example of service access property in a distribution"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-hvd-dataservice.ttl"
    ```

!!! info "Note on Implementation"
    - If the data service serves at least one HVD *dataset*, implementation requirements according to the HVD regulation apply.
    - The endpoint description should follow standard specifications such as OpenAPI.
    - Services must be documented at least in Spanish.
    - For non-HVD *datasets*, the inclusion of data services is optional but recommended.

## Modeling of OGC Services {#dataservice-ogc-services}

To improve interoperability and description of OGC services (`WMS`, `WFS`, `WMTS`, `CSW`, etc.), these should be modeled using `dcat:DataService` instead of `dcat:Distribution`.

!!! should technical "Convention 13"
    OGC services **SHOULD** be modeled as `dcat:DataService` instead of `dcat:Distribution`. This applies to:
    
    1. WMS (Web Map Service) services
    2. WFS (Web Feature Service) services
    3. CSW (Catalog Service for the Web) services
    4. Other standard OGC services

!!! info "Example of cartographic service modeling"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-ogc-services.ttl"
    ```

!!! warning "Important"
    The use of `dcat:Distribution` for OGC services:

    - Does not allow adequate description of service capabilities
    - Makes automatic federation and discovery difficult
    - Does not facilitate linking with other served *datasets*

!!! info "Note on Implementation"
    When modeling OGC services as `dcat:DataService`:

    - Include the URL of `GetCapabilities` in `dcat:endpointDescription`
    - Link with served *datasets* using `dcat:servesDataset`
    - In `dcat:endpointURL` indicate the base URL of the service without parameters.

## APIs with APIKey Authentication {#dataservice-apikey}

APIs that require [*API Key*](https://swagger.io/docs/specification/v3_0/authentication/api-keys/) are classified according to the [access-right vocabulary](https://op.europa.eu/en/web/eu-vocabularies/concept-scheme/-/resource?uri=http://publications.europa.eu/resource/authority/access-right) into two main categories:

!!! should semantic "Convention 28"
    For APIs with **universal access** APIKey (automatic registration without manual approval), a `dcat:DataService` **SHOULD** use `dct:accessRights` with value `PUBLIC` and include `dcat:endpointDescription` with OpenAPI document that specifies `securitySchemes` or document in `foaf:page` the documentation to obtain the key.

!!! should semantic "Convention 29"
    For APIs with **restricted access** APIKey (requires approval, contract or payment), a `dcat:DataService` **SHOULD** use `dct:accessRights` with value `RESTRICTED` and indicate in `dct:rights` the terms of use and `dcat:endpointDescription` with OpenAPI document.

!!! info "Example of public description"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-apikey-public.ttl"
    ```

!!! info "Example of restricted description"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-apikey-restricted.ttl"
    ```

!!! warning "Important"
    The `dcat:Dataset` and `dcat:Distribution` accessible via API Key should be consistent with the `dct:accessRights` of the `dcat:DataService` that serves them.

!!! info "Note on Implementation"
    Universal access is considered when:
    
    - Registration is automatic and without manual approval
    - Does not require contracts, [*SLAs*](https://en.wikipedia.org/wiki/Service-level_agreement) or special agreements
    - Can include technical limits (*rate limiting*, *geofencing*)

    Restricted access is considered when:
    
    - Requires manual approval or review
    - Requires signing contracts, [*SLAs*](https://en.wikipedia.org/wiki/Service-level_agreement) or confidentiality agreements
    - Has an economic cost
    - Is limited to specific types of users/organizations

# Conventions for `dcat:Dataset` {#dataset}

## Publisher (`dct:publisher`) {#dataset-dct-publisher}
The traceability of the publisher should be determined by the public sector organization identifier available in the [Common Directory of organizational units and offices (DIR3)](https://datos.gob.es/es/catalogo/e05188501-directorio-comun-de-unidades-organicas-y-oficinas-dir3) whenever available.

!!! should organisational "Convention 14" 

    Publisher information **SHOULD** contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`


## Creator (`dct:creator`) {#dataset-dct-creator}
The traceability of the creator should be determined by the public sector organization identifier available in the [Common Directory of organizational units and offices (DIR3)](https://datos.gob.es/es/catalogo/e05188501-directorio-comun-de-unidades-organicas-y-oficinas-dir3) whenever available.

!!! should organisational "Convention 15" 

    Creator information **SHOULD** contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`


## Geographic coverage (`dct:spatial`) {#dataset-dct-spatial}

The geographic coverage of a dataset must be described as precisely as possible using the identifiers corresponding to the geographic resources of Spanish territory described in Annex V of [NTI-RISP](https://www.boe.es/eli/es/res/2013/02/19/(4)).

!!! must semantic "Convention 16"
    Geographic coverage **MUST** be declared using URIs from the [Annex V of NTI-RISP for geographic resources of Spanish territory](https://datos.gob.es/es/recurso/sector-publico/territorio), following these rules:
    
    1. Use the most specific territorial level that corresponds to the dataset's actual scope
    2. Avoid using `Spain` by default when the scope is narrower.
    3. Do not declare an Autonomous Community and its provinces simultaneously.
    4. For single-province Autonomous Communities, preferably use the reference to the Autonomous Community.


!!! success "Examples of correct usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial_correct.ttl"
    ```

!!! failure "Examples of incorrect usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial_incorrect.ttl"
    ```

## Geometric spatial references (`dct:spatial` with geometries) {#dataset-dct-spatial-geometry}

To describe the geometric coverage of *datasets* in an interoperable way, different properties and standard formats can be used, in particular it is recommended to use `WKT` ([*Well-Known Text*](https://www.ogc.org/es/publications/standard/sfa/)) to describe the geometric coverage.

!!! should semantic "Convention 17"
    When specifying geometric coverage, `WKT` **SHOULD** be used (according to [GeoSPARQL](http://www.opengeospatial.org/standards/geosparql))

!!! info "Example of geometry usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial-geometry.ttl"
    ```

!!! info "Note on Implementation"
    - `dcat:bbox`: Recommended to specify the bounding box (`0..1`).
    - `dcat:centroid`: Recommended to specify the geographic center of a spatial area or other characteristic point (`0..1`).
    - `locn:geometry`: For more complex, extensive or precise geometries, allows expressing a set of coordinates denoting the vertices of the geographic area.


## Distribution (`dcat:distribution`) {#dataset-dcat-distribution}

Temporary obligatoriness of distributions in datasets

!!! must semantic "Convention 23"

    Any resource of type `dcat:Dataset` **MUST** contain at least one instance of `dcat:Distribution`. This convention aims to ensure the persistence of the obligatoriness of the metadata model of NTI-RISP 2013 until its deprecation according to the new DCAT-AP-ES in the datos.gob.es federator

!!! info "Minimum example of dataset with distribution"

    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-distribution.ttl"
    ```

## Explicit relationship with source metadata through `adms:identifier` {#dataset-metadata-relation}
The federation and migration of metadata from different profiles and standards (INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.) to DCAT-AP-ES generates the need to link the source metadata with the generated DCAT-AP-ES resources. Establishing a clear convention facilitates traceability, semantic interoperability and efficient version management in migration and federation processes between different metadata models.

!!! should technical "Convention 24"
    When a DCAT-AP-ES resource derives from a source metadata of another standard (for example: INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.), a relationship **SHOULD** be included using the `adms:identifier` property pointing to the persistent identifier of the source metadata, using a node of type `adms:Identifier`.

!!! info "Example of a dataset related to a geographic service"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-metadata-relation.ttl"
    ```

!!! warning "Important"
    - The URI referenced in the `adms:identifier` property must be persistent and resolvable, preferably the complete identifier of the source metadata.
    - The [`adms:Identifier`](https://www.w3.org/TR/vocab-adms/#identifier) class requires providing `skos:notation`, with a data type that specifies the identification scheme (including the version number if appropriate).
    - This convention does not prevent the use of other relationship properties (`dct:relation`, `rdfs:seeAlso`, `dcat:qualifiedRelation`) if greater granularity or complementarity is required.
    - The use of `adms:Identifier` as an informative node allows enriching the link to make it more usable in catalog metadata views or for external reusers.

!!! info "Note on Implementation"
    - Using `adms:identifier` allows including additional contextual properties about the secondary identifier (conformity standard, format, display page, etc.).
    - Reference: [Best practices for linking DCAT-AP datasets to alternative metadata descriptions (SEMICeu/DCAT-AP#450)](https://github.com/SEMICeu/DCAT-AP/issues/450)

# Conventions for `dcat:Distribution` {#distribution}

## Modeling of access URLs in OGC services {#distribution-ogc-urls}

To ensure correct access to OGC services and comply with INSPIRE requirements, it is important to properly model the access URLs to services, both if they are modeled as `dcat:Distribution` (discouraged) or [if they are modeled as `dcat:DataService` (recommended)](#dataservice-ogc-services).

!!! must technical "Convention 21"
    In OGC service distributions, access URLs **MUST** be modeled as follows: In `dcat:accessURL`: Complete URL of the service capabilities request `GetCapabilities` (e.g.: `http://example.org/wms?request=GetCapabilities&service=WMS`) and in `dct:conformsTo`: URL of the corresponding OGC standard, e.g.: `http://www.opengeospatial.org/standards/wms`

!!! info "Example of description of access to cartographic services"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_distribution-ogc-urls.ttl"
    ```

!!! warning "Important"
    - It is recommended to model OGC services as DataService instead of Distribution ([see Convention](#dataservice-ogc-services))
    - Do not use base URLs without `GetCapabilities` in the `accessURL` of distributions.

# Conventions for dcat:contactPoint {#dcat-contactpoint}

To facilitate communication with those responsible for *datasets* or *data services*, structured contact information must be provided using the [vCard ontology](https://www.w3.org/TR/vcard-rdf/) for the description of people and organizations and not refer directly to IRIs of the taxonomy such as: (`dcat:contactPoint <http://datos.gob.es/recurso/sector-publico/org/Organismo/A00000000>`)

!!! must semantic "Convention 18"
    
    *HVD data services* **MUST** include at least one contact point (`dcat:contactPoint`) with one of the following properties:
    
    1. Email address (`vcard:hasEmail`) or Contact form URL (`vcard:hasURL`)

!!! should semantic "Convention 19"
    
    The contact point **SHOULD** include:
    
    1. Name (`vcard:organization-name`)
    2. Telephone number (`vcard:hasTelephone`) URI `tel:`
    3. Organization identifier (`vcard:hasUid`)
    4. Email address (`vcard:hasEmail`) URI `mailto:`
    5. Contact form URL (`vcard:hasURL`)

!!! must organisational "Convention 20"
    
    Contact points listed in the portal's taxonomy **MUST** be described as a `vcard:Kind` and not directly with the organization's URI.

!!! success "Example of correct usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-contactpoint_correct.ttl"
    ```

!!! failure "Example of incorrect usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-contactpoint_incorrect.ttl"
    ```

!!! warning "Important"
    
    All values provided are recommended to be of a public and persistent nature, ^^avoiding references to personal data^^ or temporarily unstable, and preferably as close as possible to the origin of the datasets.

    The properties `vcard:hasEmail` and `vcard:hasTelephone` use URIs, not literals:
    
    - `vcard:hasEmail`: use the `mailto:` scheme 
      (e.g., `<mailto:contacto@example.org>`)
    - `vcard:hasTelephone`: use the `tel:` scheme 
      (e.g.: `<tel:+34912345678>`)

# Annex 1. Mapping table of primary sectors to DCAT-AP Data Themes {#annex-1-mapping-nti-themes-dcatap-themes}

| Primary sector (NTI) | NTI URI | DCAT-AP Theme | DCAT-AP URI |
|----------------------|---------|------------------|-------------|
| Science and technology | http://datos.gob.es/kos/sector-publico/sector/ciencia-tecnologia | Science and Technology | http://publications.europa.eu/resource/authority/data-theme/TECH |
| Commerce | http://datos.gob.es/kos/sector-publico/sector/comercio | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Culture and leisure | http://datos.gob.es/kos/sector-publico/sector/cultura-ocio | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Demography | http://datos.gob.es/kos/sector-publico/sector/demografia | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Sports | http://datos.gob.es/kos/sector-publico/sector/deporte | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Economy | http://datos.gob.es/kos/sector-publico/sector/economia | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Education | http://datos.gob.es/kos/sector-publico/sector/educacion | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Employment | http://datos.gob.es/kos/sector-publico/sector/empleo | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Energy | http://datos.gob.es/kos/sector-publico/sector/energia | Energy | http://publications.europa.eu/resource/authority/data-theme/ENER |
| Finance | http://datos.gob.es/kos/sector-publico/sector/hacienda | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Industry | http://datos.gob.es/kos/sector-publico/sector/industria | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Legislation and justice | http://datos.gob.es/kos/sector-publico/sector/legislacion-justicia | Justice | http://publications.europa.eu/resource/authority/data-theme/JUST |
| Environment | http://datos.gob.es/kos/sector-publico/sector/medio-ambiente | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Rural environment | http://datos.gob.es/kos/sector-publico/sector/medio-rural-pesca | Agriculture | http://publications.europa.eu/resource/authority/data-theme/AGRI |
| Health | http://datos.gob.es/kos/sector-publico/sector/salud | Health | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| Public sector | http://datos.gob.es/kos/sector-publico/sector/sector-publico | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Security | http://datos.gob.es/kos/sector-publico/sector/seguridad | Justice | http://publications.europa.eu/resource/authority/data-theme/JUST |
| Society and welfare | http://datos.gob.es/kos/sector-publico/sector/sociedad-bienestar | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Transport | http://datos.gob.es/kos/sector-publico/sector/transporte | Transport | http://publications.europa.eu/resource/authority/data-theme/TRAN |
| Tourism | http://datos.gob.es/kos/sector-publico/sector/turismo | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Urbanism and infrastructures | http://datos.gob.es/kos/sector-publico/sector/urbanismo-infraestructuras | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Housing | http://datos.gob.es/kos/sector-publico/sector/vivienda | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |


# Annex 2. Mapping table between INSPIRE Themes and DCAT-AP Themes {#annex-2-mapping-inspire-themes-dcatap-themes}

| INSPIRE Theme | INSPIRE URI | DCAT-AP Theme | DCAT-AP URI |
|-------------|-------------|------------------|-------------|
| Addresses (AD) | http://inspire.ec.europa.eu/theme/ad | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Administrative units (AU) | http://inspire.ec.europa.eu/theme/au | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Reference systems (RS) | http://inspire.ec.europa.eu/theme/rs | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Geographic grids (GG) | http://inspire.ec.europa.eu/theme/gg | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Cadastral parcels (CP) | http://inspire.ec.europa.eu/theme/cp | Regions, Economy | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/ECON |
| Geographic names (GN) | http://inspire.ec.europa.eu/theme/gn | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Hydrography (HY) | http://inspire.ec.europa.eu/theme/hy | Environment, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Protected sites (PS) | http://inspire.ec.europa.eu/theme/ps | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Transport networks (TN) | http://inspire.ec.europa.eu/theme/tn | Transport | http://publications.europa.eu/resource/authority/data-theme/TRAN |
| Elevation (EL) | http://inspire.ec.europa.eu/theme/el | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Geology (GE) | http://inspire.ec.europa.eu/theme/ge | Regions, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Land cover (LC) | http://inspire.ec.europa.eu/theme/lc | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Orthoimagery (OI) | http://inspire.ec.europa.eu/theme/oi | Regions, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Agricultural facilities (AF) | http://inspire.ec.europa.eu/theme/af | Agriculture | http://publications.europa.eu/resource/authority/data-theme/AGRI |
| Environmental monitoring (AM) | http://inspire.ec.europa.eu/theme/am | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Atmospheric conditions (AC) | http://inspire.ec.europa.eu/theme/ac | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Biogeographical regions (BR) | http://inspire.ec.europa.eu/theme/br | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Buildings (BU) | http://inspire.ec.europa.eu/theme/bu | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Energy resources (ER) | http://inspire.ec.europa.eu/theme/er | Energy | http://publications.europa.eu/resource/authority/data-theme/ENER |
| Environmental monitoring facilities (EF) | http://inspire.ec.europa.eu/theme/ef | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Habitats and biotopes (HB) | http://inspire.ec.europa.eu/theme/hb | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Human health and safety (HH) | http://inspire.ec.europa.eu/theme/hh | Health | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| Land use (LU) | http://inspire.ec.europa.eu/theme/lu | Economy, Environment | http://publications.europa.eu/resource/authority/data-theme/ECON, http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Mineral resources (MR) | http://inspire.ec.europa.eu/theme/mr | Economy, Environment, Energy | http://publications.europa.eu/resource/authority/data-theme/ECON, http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/ENER |
| Natural risk zones (NZ) | http://inspire.ec.europa.eu/theme/nz | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Oceanographic (OF) | http://inspire.ec.europa.eu/theme/of | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Population distribution (PD) | http://inspire.ec.europa.eu/theme/pd | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Production facilities (PF) | http://inspire.ec.europa.eu/theme/pf | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Species distribution (SR) | http://inspire.ec.europa.eu/theme/sr | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Soil (SO) | http://inspire.ec.europa.eu/theme/so | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Species distribution (SD) | http://inspire.ec.europa.eu/theme/sd | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Utility and government services (SU) | http://inspire.ec.europa.eu/theme/su | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Government services (US) | http://inspire.ec.europa.eu/theme/us | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Meteorological facilities (MF) | http://inspire.ec.europa.eu/theme/mf | Environment, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/TECH |


# Annex 3. Mapping of organizational identifiers {#annex-3-mapping-org-identifiers}

This annex provides guidelines for mapping between different organization identification systems, [see convention](#general-dir3). In the Spanish open data ecosystem, different organization identification systems coexist:

1. DIR3 codes (official)
2. NIF (tax identification)
3. Internal codes of ministries and organizations
4. Inherited historical identifiers

This can generate inconsistencies when:

* Relating *datasets* between different catalogs
* Linking publishing and creating organizations
* Maintaining historical traceability of data

**Equivalence table**

| ID Type | Format | Example | Use | Notes |
|---------|---------|---------|-----|-------|
| DIR3 | `EAXXXXXXX` | `EA0000000` | Active public organizations | Recommended primary identifier |
| NIF | `PAXXXXXXX` | `P28000000` | Private organizations | Use as prefix P + NIF |
| Internal code | Variable | `INE-INT-001` | Historical use | Discouraged for new *datasets* |


# Annex 4. Namespaces used in the document {#annex-4-document-namespaces}

This annex provides a complete reference of the namespaces ([*namespaces*](https://www.w3.org/TR/xml-names11/)) used in the DCAT-AP-ES profile and in the examples of this document. Namespaces are fundamental for:

1. Unambiguously identifying the elements and properties used
2. Avoiding conflicts between different vocabularies
3. Facilitating RDF validation and processing

**Example of namespace declaration**
=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/Conventions_annex-4.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_annex-4.ttl"
    ```

The listed prefixes are the most commonly used, although technically other prefixes could be used as long as they are correctly declared.

| Prefix | URI | Name | Description |
|---------|-----|---------|-------------|
| `adms` | `http://www.w3.org/ns/adms#` | Asset Description | Description of semantic assets |
| `cnt`  | `http://www.w3.org/2011/content#` | Representing Content in RDF | Representation of content in RDF |
| `dcat` | `http://www.w3.org/ns/dcat#` | Data Catalog Vocabulary | Vocabulary for describing data catalogs |
| `dcatap` | `http://data.europa.eu/r5r/` | DCAT-AP | Specific extensions of the DCAT-AP profile |
| `dct` | `http://purl.org/dc/terms/` | Dublin Core Terms | Basic metadata for describing resources |
| `eli` | `http://data.europa.eu/eli/ontology#` | European Legislation Identifier | Identification of European legislation |
| `foaf` | `http://xmlns.com/foaf/0.1/` | Friend of a Friend | Vocabulary for describing people and organizations |
| `geo` | `http://www.opengis.net/ont/geosparql#` | GeoSPARQL Ontology | Geographic query language for RDF data |
| `locn` | `http://www.w3.org/ns/locn#` | Location Core | Vocabulary for locations and addresses |
| `odrl` | `http://www.w3.org/ns/odrl/2/` | Open Digital Rights Language | Expression of digital rights |
| `prov` | `http://www.w3.org/ns/prov#` | Provenance Ontology | Data traceability and provenance |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | RDF Schema | Basic vocabulary for defining RDF resources |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` | RDF Schema | Extension of RDF for defining classes and properties |
| `schema` | `http://schema.org/` | Schema.org | Vocabulary for structuring data on the web |
| `skos` | `http://www.w3.org/2004/02/skos/core#` | SKOS | Knowledge organization system |
| `spdx` | `http://spdx.org/rdf/terms#` | Software Package Data Exchange | Licenses and software packages |
| `time` | `http://www.w3.org/2006/time#` | Time Ontology | Temporal concepts and durations |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` | vCard Ontology | Ontology for contact information |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` | XML Schema | XML Schema data types |
