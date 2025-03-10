# Introduction
In Spain, open data exchange between the portal of the Spanish Government’s Open Data Initiative ([datos.gob.es](https://datos.gob.es)) and the various data providers—such as regional catalogs, local entities, and other organizations—is envisioned within a framework that ensures metadata interoperability and homogeneity. To this end, the European application profile [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) is adapted, along with the elements described in the extension [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/), to incorporate the modeling of [High-Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) into the national context. This results in the **DCAT-AP-ES** standard, set as a reference for the exchange of metadata on public information at the national level.

From the date the standard enters into force, [datos.gob.es](https://datos.gob.es) will accept metadata in **DCAT-AP-ES** format. For those providers who deliver data directly to the portal, a transitional period will be established after the publication of new versions, during which they can adapt their systems to the updated standard from the previous profile defined by the Technical Interoperability Standard for Public Sector Information Resources ([**NTI-RISP**](https://datos.gob.es/es/doc-tags/nti-risp)).

The conventions manual not only details the specific modifications introduced in the Spanish standard compared to the European version, but it also defines additional rules to address practical requirements. These may include particularities of the Spanish open data context, where implementation could be adjusted to different technical needs. Furthermore, some of these rules are expected to evolve more rapidly than the main specification, allowing greater flexibility and adaptation to technological changes.

This document is targeted at ^^those responsible for the development and maintenance of open data portals^^, as well as ^^data providers collaborating with the national catalog^^. Its purpose is to provide clear guidelines and practical tools for efficiently implementing the standard. However, for use in specific contexts, the possibility remains open to establish additional conventions that supplement the general regulations.

To ensure a uniform interpretation, the normative terms **MUST**, **SHOULD**, and **MAY** are used, in accordance with **[RFC2119](https://www.rfc-editor.org/rfc/rfc2119)**, in order to distinguish mandatory guidelines from optional ones. Although the manual includes diagrams and illustrative examples, these are not normative unless explicitly stated.

This approach aims not only to standardize the exchange of metadata but also to foster greater harmonization and collaboration among different levels of government in Spain, guaranteeing solid and scalable interoperability.

## Prefixes Used
All namespace prefixes used throughout this document are referenced in [Annex 4. Document Namespaces](#annex-4-document-namespaces).

## Types of Conventions
### Technical Conventions
These conventions define technical implementation aspects, including coding, resource identification, and entity modeling. They are essential to ensure technical interoperability and the correct interpretation of metadata.

### Organizational Conventions
These conventions establish rules for managing and organizing catalogs, federating data, and identifying organizations. They provide the governance framework necessary for effective metadata management.

### Semantic Conventions
These conventions ensure consistency in resource descriptions, guaranteeing that metadata is semantically accurate and consistent.

## List of Conventions
- [**Convention 01**](#convencion-01): The publisher identifier *MUST* be [registered and available in the datos.gob.es taxonomy](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es)
- [**Convention 02**](#convencion-02): If language tags are defined for `dct:title`, `dct:description`, `vcard:organization_name`, `vcard:fn`, `foaf:name`, `dcat:keyword`, and `adms:versionNotes`, they *MUST* at least be in Spanish (`es`) and may not be empty literals.
- [**Convention 03**](#convencion-03): Identifiers and URI references *SHOULD* use the `http://` scheme instead of `https://` as a general rule.
- [**Convention 04**](#convencion-04): Organizations *SHOULD* implement automated federation via RDF as the sole method for publishing metadata in DCAT-AP-ES format, avoiding the coexistence of manual and automated federation for the same organization.
- [**Convention 05**](#convencion-05): URIs *MUST* be correctly encoded at their source, especially when they contain:  
  1. Reserved characters (`?`, `&`, `=`, `#`, etc.)  
  2. Spaces  
  3. Non-ASCII characters (accented letters, `ñ`, etc.)  
  4. Special characters (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)
- [**Convention 06**](#convencion-06): Resources *MUST* have a unique and persistent identifier meeting the following requirements:  
  1. Include the property `dct:identifier` with a unique value for each resource.  
  2. Maintain identifier consistency even if the resource is updated.  
  3. Use the same identifier when the resource is published in different catalogs.
- [**Convention 07**](#convencion-07): References to legal documents *MUST* use ELI identifiers when available:  
  1. For European legislation: `http://data.europa.eu/eli/...`  
  2. For national legislation: `https://www.boe.es/eli/...`  
  3. For derived documents, use the main document’s ELI URI.
- [**Convention 08**](#convencion-08): The creation and modification dates of resources *MUST* meet the following requirements:  
  1. The modification date (`dct:modified`) *MUST* follow the creation date (`dct:created`).  
  2. The modification date *MUST* reflect the last change in the data, not in the metadata.
- [**Convention 09**](#convencion-09): A single catalog per publishing organization *MUST* be used, avoiding subcatalogs via `dct:hasPart`. Relationships between resources *MUST* be modeled using the following properties as appropriate.
- [**Convention 10**](#convencion-10): The catalog *MUST* include at least the [primary sector taxonomy](https://datos.gob.es/kos/sector-publico/sector) in the `dcat:themeTaxonomy` property.
- [**Convention 11**](#convencion-11): Additional taxonomies *MAY* be included to enhance dataset classification:  
  `http://publications.europa.eu/resource/authority/data-theme` or `http://inspire.ec.europa.eu/theme`
- [**Convention 12**](#convencion-12): Datasets classified as HVD *MUST* include at least one data service (`dcat:DataService`) with the following mandatory properties:  
  1. Endpoint URL (`dcat:endpointURL`)  
  2. Endpoint description (`dcat:endpointDescription`)  
  3. Contact point (`dcat:contactPoint`)  
  4. Applicable legislation (`dcatap:applicableLegislation`)  
  5. HVD category (`dcatap:hvdCategory`)  
  6. Documentation (`foaf:page`)  
  7. Served datasets (`dcat:servesDataset`)
- [**Convention 13**](#convencion-13): OGC services *SHOULD* be modeled as `dcat:DataService` instead of `dcat:Distribution`.
- [**Convention 14**](#convencion-14): Publisher information *SHOULD* include a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`
- [**Convention 15**](#convencion-15): Creator information *SHOULD* include a [DIR3 identifier code](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) in the identifier property (`dct:identifier`), for example: `EA0000000`
- [**Convention 16**](#convencion-16): Geographic coverage *MUST* be declared using the URIs from [Annex V of the NTI-RISP for Spain’s territorial resources](https://datos.gob.es/es/recurso/sector-publico/territorio), following these rules:  
  1. Use the most specific territorial level corresponding to the dataset’s actual scope.  
  2. Avoid using `España` by default when the scope is more limited.  
  3. Do not declare both an Autonomous Community and its provinces at the same time.  
  4. For single-province Autonomous Communities, preferably use the reference to the Community.
- [**Convention 17**](#convencion-17): When specifying geometric coverage, `WKT` (per [GeoSPARQL](http://www.opengeospatial.org/standards/geosparql)) *SHOULD* be used.
- [**Convention 18**](#convencion-18): Datasets *MUST* include at least one contact point (`dcat:contactPoint`) with the following mandatory properties: email address (`vcard:hasEmail`) or contact form URL (`vcard:hasURL`).
- [**Convention 19**](#convencion-19): The contact point *SHOULD* also include:  
  1. Name of the area or person (`vcard:fn`)  
  2. Phone number (`vcard:hasTelephone`)  
  3. Organization identifier (`vcard:hasUid`)
- [**Convention 20**](#convencion-20): Contact points stored in the portal taxonomy *MUST* be described as `vcard:Kind` and not directly with the organization’s URI.
- [**Convention 21**](#convencion-21): For distributions of OGC services, access URLs *MUST* be modeled as follows:  
  In `dcat:accessURL`: the full GetCapabilities request URL of the service (e.g., `http://example.org/wms?request=GetCapabilities&service=WMS`), and in `dct:conformsTo`: the corresponding OGC standard URL, e.g., `http://www.opengeospatial.org/standards/wms`
- [**Convention 22**](#convencion-22): Time periods *MUST* be described exclusively using the properties `dcat:startDate` and `dcat:endDate` inside `dct:temporal`.