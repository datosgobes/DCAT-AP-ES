# Frequently Asked Questions

This section compiles the most frequently asked questions about DCAT-AP-ES, its implementation, and use. The aim is to provide clear and concise answers to facilitate understanding and adoption of this application profile.

Sections:

* [About DCAT-AP-ES](#dcat-ap-es): Addresses common questions about the application profile.
* [Data Model](#model): Explains doubts and fundamental concepts of the data model.
* [Federation](#federation): Answers questions about technical implementation and federation with the [national catalog](https://datos.gob.es/).
* [Repository](#repository): Introduces the [`datosgobes/DCAT-AP-ES`](https://github.com/datosgobes/DCAT-AP-ES) repository and its purpose.
* [Related Application Profiles](#application-profile): Contextualizes specifications related to DCAT-AP-ES.


!!! warning "Relationship with datos.gob.es Frequently Asked Questions"

    This document focuses on specific issues regarding the DCAT-AP-ES specification and its technical implementation. For general inquiries about the national catalog, we recommend visiting the [datos.gob.es frequently asked questions](https://datos.gob.es/faq-page).

---

## **About DCAT-AP-ES** { .faq-h #dcat-ap-es}

<div class="grid cards" markdown>
-   :boostrap-spain:{ .lg .middle .grid-emoji } **DCAT-AP-ES**{ .grid-title #vocab-dcat-ap-es } 

    ---  

    Adaptation of DCAT-AP that incorporates specifications specific to the Spanish context and the HVD extension.

    [:octicons-arrow-right-24: Learn more](index.en.md)

-   :fontawesome-solid-plus:{ .lg .middle .grid-emoji } **Main new features of DCAT-AP-ES?**{ .grid-title #novedades }

    ---

    It aligns with the European DCAT-AP profile, incorporates data services (`dcat:DataService`), high-value dataset modeling (HVD), and improvements in metadata quality description.
    
    [:octicons-arrow-right-24: Classes](index.en.md#dcat-ap-es-entities)


-   :material-connection:{ .lg .middle .grid-emoji } **Relationship with other standards?**{ .grid-title #relacion }

    ---

    DCAT-AP-ES implements DCAT-AP and its HVD extension, ensuring compatibility with the European open data ecosystem.
    
    [:octicons-arrow-right-24: UML](index.en.md#dcat-ap-es-model)

-   :material-calendar:{ .lg .middle .grid-emoji } **When does it come into effect?**{ .grid-title #vigencia }

    ---

    DCAT-AP-ES is expected to come into effect in 2025, following the approval of the new NTI-RISP, the day after its publication in the Official State Gazette (BOE).
    
    [:octicons-arrow-right-24: NTI-RISP](https://www.boe.es/eli/es/res/2013/02/19/(4))

-   :material-clock-fast:{ .lg .middle .grid-emoji } **What is the deadline for migration?**{ .grid-title #migracion }

    ---

    Publishers have an adaptation period of six months from the entry into force of the NTI-RISP.
    
    [:octicons-arrow-right-24: Changes](index.en.md#annex-1-nti-risp-to-dcat-ap-es)

</div>

## **Data Model** { .faq-h #model}

<div class="grid cards grid-2col" markdown>

-   :fontawesome-solid-diagram-project:{ .lg .middle .grid-emoji } **How do the DCAT-AP-ES elements relate to each other?**{ .grid-title #relaciones-modelo }

    ---

    The DCAT-AP-ES model functions as a network where elements connect to each other:

    - A **catalog** (`dcat:Catalog`) serves as the main container hosting datasets and services

    - **Data services** (`dcat:DataService`) provide access to the datasets

    - Each **dataset** (`dcat:Dataset`) can have multiple distributions (formats)

    - **Distributions** (`dcat:Distribution`) can be accessed through specific services

    ```mermaid
    graph LR
        %% Node definitions
        Catalog((dcat:Catalog)):::main
        Dataset[dcat:Dataset]:::entity
        DataService[dcat:DataService]:::entity
        Distribution[dcat:Distribution]:::entity
        
        %% Relationships with labels
        Catalog -->|dcat:dataset| Dataset
        Catalog -->|dcat:service| DataService
        DataService -->|dcat:servesDataset| Dataset
        Dataset -->|dcat:distribution| Distribution
        Distribution -->|dcat:accessService| DataService
        
        %% Styles with rounded borders
        classDef main fill:#B8C2CC,stroke:none,font-size:24px,color:#00a99d,font-weight:bold;
        classDef entity fill:#e6f3ff,stroke:none,font-size:20px,color:#154481 !important,rx:10,ry:10,font-weight:bold;
        
        %% Line styles
        linkStyle default stroke:#154481,stroke-width:1px,stroke-dasharray:3;
    ```
    
    [:octicons-arrow-right-24: Relationships](index.en.md#dcat-ap-es-model-relations)

</div>


---

## **Federation** { .faq-h #federation}

<div class="grid cards" markdown>

-   :fontawesome-solid-laptop-code:{ .lg .middle .grid-emoji } **Where can I find DCAT-AP-ES examples?**{ .grid-title #implementacion-ejemplos }

    ---

    Available in the online guide and in the `examples/` directory of the repository, organized by entities and specific use cases.

    [:octicons-arrow-right-24: Examples](examples.en.md)

-   :fontawesome-solid-file-code:{ .lg .middle .grid-emoji } **What format should the catalog have?**{ .grid-title #implementacion-formatos }

    ---

    The catalog file that will be federated must be described according to the XML syntax for RDF called `RDF/XML`

    [:octicons-arrow-right-24: Syntax](https://www.w3.org/TR/rdf-syntax-grammar/)

</div>

---

## **Repository** { .faq-h #repository}

<div class="grid cards" markdown>

-   :material-source-repository:{ .lg .middle .grid-emoji } **What is the DCAT-AP-ES repository?**{ .grid-title #repository-repositorio }  

    ---

    Code repository and tracking for the implementation of the NTI according to the DCAT-AP-ES application profile.

    [:octicons-arrow-right-24: Repository](https://github.com/datosgobes/DCAT-AP-ES "All DCAT-AP-ES material source code repository" )

-   :fontawesome-brands-readme:{ .lg .middle .grid-emoji } **What to find in the DCAT-AP-ES repository?**{ .grid-title #repository-readme }

    ---

    The evolution of the DCAT-AP-ES specification with technical documentation, guides, examples and user feedback.

    [:octicons-arrow-right-24: README](https://github.com/datosgobes/DCAT-AP-ES#guía-para-dcat-ap-es "README of the DCAT-AP-ES repository including how to contribute." )

-   :fontawesome-solid-folder-open:{ .lg .middle .grid-emoji } **Are there support materials?**{ .grid-title #materiales }

    ---

    There are application guides and technical implementation documents, conventions, data models, vocabularies, examples, SHACL validation files, etc.
    
    [:octicons-arrow-right-24: Guide](index.en.md)

-   :fontawesome-solid-code-pull-request:{ .lg .middle .grid-emoji } **Designed to contribute**{ .grid-title #repository-contribuir }

    ---

    Designed to allow the community to suggest improvements and be involved in developing the DCAT-AP-ES specification.

    [:octicons-arrow-right-24: Contribute](https://github.com/datosgobes/DCAT-AP-ES?tab=readme-ov-file#contribución "Reports DCAT-AP-ES profile issues or enhancements.")

-   :fontawesome-brands-creative-commons:{ .lg .middle .grid-emoji } **Open source, CC-BY 4.0**{ .grid-title #repository-license }  

    ---

    All of the material is licensed under the open source license Creative Commons Attribution 4.0 International. 

    [:octicons-arrow-right-24: License](https://github.com/datosgobes/DCAT-AP-ES#CC-BY-4.0-1-ov-file "Free use license that allows sharing, copying, distributing and modifying a work, even for commercial purposes, on the sole condition that the original authorship is acknowledged.")

</div>

---

## **Application Profiles** { .faq-h #application-profile}

<div class="grid cards" markdown>

-   :simple-semanticweb:{ .lg .middle .grid-emoji } **DCAT**{ .grid-title{ .grid-title #vocab-dcat }   

    ---  

    The fundamental vocabulary for describing catalogs and data resources on the web developed by the W3C.

    [:octicons-arrow-right-24: Learn more](https://www.w3.org/TR/vocab-dcat/)

-   :simple-europeanunion:{ .lg .middle .grid-emoji } **DCAT-AP**{ .grid-title #vocab-dcat-ap }  
 
    ---  

    The European profile based on DCAT that defines common standards for open data catalogs, facilitating interoperability.

    [:octicons-arrow-right-24: Learn more](https://op.europa.eu/es/web/eu-vocabularies/dcat-ap)

-   :fontawesome-solid-star:{ .lg .middle .grid-emoji } **DCAT-AP HVD**{ .grid-title #vocab-dcat-ap-hvd} 

    ---  

    Extension of DCAT-AP for describing and cataloging high-value datasets in compliance with the HVD Implementing Regulation.

    [:octicons-arrow-right-24: Learn more](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-ap-hvd)

</div>

---
