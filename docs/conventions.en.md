# Introduction
In Spain, the exchange of open data between the Open Data Initiative of the Government of Spain ([datos.gob.es](https://datos.gob.es)) and various data providers, such as regional catalogs, Local Entities, and other organizations, is framed to ensure interoperability and homogeneity of metadata. To achieve this, the European application profile [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) will be adapted together with the elements described in the extension [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) to incorporate the modeling of the [High Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) (*High Value Datasets*) to national needs, resulting in the standard **DCAT-AP-ES**, which will be established as a reference for the exchange of metadata on public information at national level.  

Since the implementation of the standard, the central portal will only accept metadata in **DCAT-AP-ES** format. For those providers delivering data directly to the portal, a transitional period will be established following the publication of new versions, allowing systems to adapt to the updated standard using the previous profile of the Technical Standard for Interoperability of Public Sector Information Resources ([**NTI-RISP**](https://datos.gob.es/en/doc-tags/nti-risp)).

The conventions guide not only details the specific modifications introduced in the Spanish standard compared to the European version but also defines additional rules to address practical needs. These may include particularities of the Spanish open data context, where implementation might align with distinct technical requirements. Moreover, some of these rules are expected to evolve faster than the main specification, providing greater flexibility and adaptability to technological changes.

This document targets developers and maintainers of open data portals and data providers collaborating with the national catalog. Its purpose is to provide clear guidelines and practical tools for implementing the standard efficiently. However, for specific contexts, the possibility of establishing additional conventions complementing general regulations is left open.

To ensure consistent interpretation, normative terms such as **MUST**, **SHOULD**, and **MAY** are used, as defined in **[RFC2119](https://www.rfc-editor.org/rfc/rfc2119)**, to differentiate mandatory guidelines from optional ones. Although the manual includes diagrams and illustrative examples, these are not normative unless explicitly stated.

This approach aims not only to standardize metadata exchange but also to foster greater harmonization and collaboration among different levels of government in Spain, ensuring robust and scalable interoperability.

## Types of Conventions
### Technical Conventions
These conventions define technical aspects of implementation, including encoding, resource identification, and entity modeling. They are essential for ensuring technical interoperability and correct interpretation of metadata.

### Organizational Conventions
These conventions establish rules for the management and organization of catalogs, data federation, and the identification of organizations. They provide the necessary governance framework for effective metadata management.

### Semantic Conventions
These conventions ensure consistency in the description of resources, guaranteeing that metadata is semantically accurate and consistent.

## List of Conventions
- [**Convention 01**](#convention-01): The publisher's identifier *MUST* be registered in the [Identification of Public Organizations (DIR3)](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) taxonomy.
- [**Convention 02**](#convention-02): The literals `dct:title`, `dct:description`, `vcard:organization-name `, `vcard:fn`, `foaf:name`, `dcat:keyword` and `adms:versionNotes` *MUST* be defined with language tags, at least in the spanish language `es`, and cannot be empty literals.
- [**Convention 03**](#convention-03): Identifiers and URI references *SHOULD* use the `http://` scheme instead of `https://`.
- [**Convention 04**](#convention-04): Organizations *SHOULD* implement automatic federation through RDF as the sole method of publishing metadata in DCAT-AP-ES format, avoiding the coexistence of manual and automatic federation for the same organization.
- [**Convention 05**](#convention-05): URIs *MUST* be correctly encoded at their source, especially when they contain:
    1. Reserved characters (`?`, `&`, `=`, `#`, etc.)
    2. Spaces
    3. Non-ASCII characters (accents, `ñ`, etc.)
    4. Special characters (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)
- [**Convention 06**](#convention-06): Resources *MUST* have a unique and persistent identifier that meets the following requirements:
    1. Include the `dct:identifier` property with a unique value for each resource.
    2. Maintain identifier consistency even if the resource is updated.
    3. Use the same identifier when the resource is published in different catalogs.
- [**Convention 07**](#convention-07): References to legal documents *MUST* use ELI identifiers when available:
    1. For European legislation: `http://data.europa.eu/eli/...`
    2. For national legislation: `https://www.boe.es/eli/...`
    3. For derived documents, use the ELI URI of the main document
- [**Convention 08**](#convention-08): Creation and modification dates of resources *MUST* meet the following requirements:
    1. The modification date (`dct:modified`) *MUST* be later than the creation date (`dct:created`)
    2. The modification date *MUST* reflect the last change in the data, not in the metadata
- [**Convention 09**](#convention-09): A single catalog per publishing organization *MUST* be used, avoiding the use of subcatalogs through `dct:hasPart`. Relationships between resources *MUST* be modeled using the appropriate properties as necessary.
- [**Convention 10**](#convention-10): The catalog *MUST* include at least the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector) in the `dcat:themeTaxonomy` property.
- [**Convention 11**](#convention-11): Additional taxonomies may be included to improve dataset classification: `http://publications.europa.eu/resource/authority/data-theme` or `http://inspire.ec.europa.eu/theme`
- [**Convention 12**](#convention-12): Datasets categorized as HVD *MUST* include at least one data service (`dcat:DataService`) with the following mandatory properties:
    1. Endpoint URL (`dcat:endpointURL`)
    2. Endpoint Description (`dcat:endpointDescription`)
    3. Contact Point (`dcat:contactPoint`)
    4. Applicable Legislation (`dcatap:applicableLegislation`)
    5. HVD Category (`dcatap:hvdCategory`)
    6. Documentation (`foaf:page`)
    7. Served Datasets (`dcat:servesDataset`)
- [**Convention 13**](#convention-13): OGC services *SHOULD* be modeled as `dcat:DataService` instead of `dcat:Distribution`.
- [**Convention 14**](#convention-14): Publisher information *SHOULD* contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `http://datos.gob.es/recurso/sector-publico/org/Organismo/EA0000000`
- [**Convention 15**](#convention-15): Creator information *SHOULD* contain a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organism) in the identifier property (`dct:identifier`), for example: `http://datos.gob.es/recurso/sector-publico/org/Organismo/EA0000000`
- [**Convention 16**](#convention-16): Geographic coverage *MUST* be declared using URIs from the NTI-RISP vocabulary for Territories, following these rules:
    1. Use the most specific territorial level that corresponds to the dataset's actual scope.
    2. Avoid using `Spain` by default when the scope is narrower.
    3. Do not declare a Autonomous Community and its provinces simultaneously.
    4. For single-province Autonomous Communities, preferably use the reference to the Autonomous Community.
- [**Convention 17**](#convention-17): When specifying geometric coverage, one of the following formats *MUST* be used:
    1. Using `locn:geometry`.
    2. Using `dcat:bbox` for the geographic bounding box.
    3. Using `dcat:centroid` for the geographic center (centroid).
- [**Convention 18**](#convention-18): *Dataservices HVD*  *MUST* include at least one contact point (`dcat:contactPoint`) with one of the following mandatory properties:
    1. Email address (`vcard:hasEmail`) OR Contact URL (`vcard:hasURL`)
- [**Convention 19**](#convention-19): The contact point *SHOULD* also include:
    1. Name of the area or person (`vcard:organization-name`)
    2. Telephone number (`vcard:hasTelephone`)
    3. Organization identifier (`vcard:hasUid`)
    4. Email (`vcard:hasEmail`)
    5. Contact form URL (`vcard:hasURL`)

- [**Convention 20**](#convention-20): Contact points listed in the portal's taxonomy *MUST* be described as a `vcard:Kind` and not directly with the organization's URI.
- [**Convention 21**](#convention-21): In OGC service distributions, access URLs *MUST* be modeled as follows: In `dcat:accessURL`: Complete URL of the service `GetCapabilities` request (e.g., `http://example.org/wms?request=GetCapabilities&service=WMS`) and in `dct:conformsTo`: URL of the corresponding OGC standard, e.g., `http://www.opengeospatial.org/standards/wms`.
- [**Convention 22**](#convention-22): Time periods *MUST* be described exclusively using the properties `dcat:startDate` and `dcat:endDate` within `dct:temporal`. The interval can also be open - i.e., it can have just a start or just an end.
- [**Convención 23**](#convention-23): *Datasets* *MUST* include at least a distribution (`dcat:Distribution`).

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

To maintain compatibility and avoid interoperability issues, it is recommended to use HTTP URIs instead of HTTPS in identifiers and references. HTTP URIs are equally dereferencable as HTTPS through redirection.

!!! should technical "Convention 03"
    
    **Identifiers and URI references SHOULD** use the `http://` scheme instead of `https://`. This applies to:
    
    1. Resource identifiers (`dcat:Dataset`, `dcat:Distribution`, etc.)
    2. References to controlled vocabularies
    3. URIs of taxonomies and concept schemes

!!! info "Example of Correct URI Usage"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-http-uris.ttl"
    ```

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

To ensure the correct identification and traceability of resources over time, as well as to avoid duplicates during federation from multiple sources, it is necessary to establish a system of unique and persistent identifiers since the identifier (`dct:identifier`) is the property that allows the unique and unequivocal identification of the dataset.

!!! must technical "Convention 06"
    Resources **MUST** have a unique and persistent identifier that meets the following requirements:

    1. Include the `dct:identifier` property with a unique value for each resource.
    2. Maintain identifier consistency even if the resource is updated.
    3. Use the same identifier when the resource is published in different catalogs.

!!! info "Example of Consistent Identifiers"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-resource-identifier.ttl"
    ```

!!! warning "Important"
    - Identifiers must not change even if the resource's URI changes.
    - The same dataset published in different catalogs must maintain the same `dct:identifier`.
    - In case of conflict during federation, the last federated dataset according to the established order will prevail.

!!! info "Note on Implementation"
    To avoid duplicates during federation:
    
    1. Coordinate with other publishers on identifier assignment.
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

!!! info "Note on Implementation"
    To validate dates:
    
    1. Verify that the modification date is later than the creation date
    2. Check that the dates are in the formats defined by the model; dates can be recorded using the standard format: `YYYY-MM-DD` (`xsd:date`), or ISO-8601 datetime with time zone: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), as well as the year: `YYYY` (`xsd:gYear`) or the year and month: `YYYY-MM` (`xsd:gYearMonth`).
