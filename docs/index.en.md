# Introduction

This document presents a detailed specification of the metadata required to describe catalogs and reusable data resources.

These metadata are described based on the Semantic Web paradigm, which implements resource descriptions using the standard model for data exchange on the Web, RDF (Resource Description Framework). This approach enables different data cataloging systems to interact and exchange information effectively and consistently, achieving semantic interoperability to facilitate the search and discovery of data resources, significantly increasing their value for reuse.

The application profile, hereafter model, DCAT-AP-ES, underpinning the **Norma Técnica de Interoperabilidad de Recursos de Información del Sector Público (NTI-RISP)**, adopts the guidelines of the European DCAT-AP metadata exchange schema, with certain additional restrictions and adjustments. In turn, DCAT-AP is based on the **DCAT specification**, which has been developed by the [Dataset Exchange Working Group](https://www.w3.org/2017/dxwg/) since its initial publication as a W3C Recommendation in 2014. **DCAT** is an RDF vocabulary created to improve interoperability among online data catalogs. The version of DCAT-AP used as a reference for building this model is [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) together with the elements described in the [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) extension, which deals with modeling [High-Value Datasets](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir).

An open data catalog can consist solely of datasets or of data services, though it is more common to have both. It is represented by instances of the classes and properties specified in this model.

This document describes the main classes of the application profile: Catalog, Dataset, Distribution, and Data Service, as well as other relevant classes that provide a complete descriptive framework for the reusable elements cataloged according to the DCAT-AP-ES model. In addition, it specifies the set of controlled vocabularies that must be used for the properties describing the cataloged elements.

# High-Value Datasets

Reflecting the growing importance of data in society and the economy, the European Commission adopted [**Commission Implementing Regulation (EU) 2023/138**](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138) (High-Value Datasets Implementing Regulation, HVD IR) on December 21, 2022. This regulation establishes clear guidelines for public bodies regarding the availability of high-value datasets and aims to improve the quality, accessibility, and use of specific key datasets within the public sector. To achieve this goal, the HVD regulation sets specific requirements for the metadata associated with published datasets.

!!! note "Relationship between the specification and data-specific regulations"

    The **DCAT-AP-ES application profile is the minimal core set of metadata** that applies to all entities within the model. However, **compliance with this specification does not exempt organizations from meeting specific applicable regulations** in each sector, such as the HVD regulation. In particular, datasets meeting the HVD criteria may include additional metadata or restrictions not covered by DCAT-AP-ES but required by relevant legislation.

# DCAT-AP-ES Metadata Model {#dcat-ap-es-model}

Below are the fundamental elements of the model, beginning with a UML diagram, the class relationships, the namespaces used in the specification, and the related controlled vocabularies.

## Model Diagram {#uml}

The DCAT-AP-ES model is shown below as a UML diagram that illustrates the specification described in this document. For clarity, certain details included in each metadata description are omitted here. Essentially, it displays the key classes and some relevant supporting classes.

![](img/uml/dcat-ap-es.drawio "Illustration. UML Diagram of the DCAT-AP-ES metadata model"){ align=center width="100%" }