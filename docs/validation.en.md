To verify that the metadata exchange is technically compliant with [DCAT-AP-EN](/), the [SHACL shapes available in the repository](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/) graphs can be used. Shapes Constraint Language* (SHACL) is a [W3C recommendation](https://www.w3.org/TR/shacl/]) for expressing constraints in an RDF knowledge graph. 

The following illustration schematically shows the main stages of the SHACL validation process applied to metadata, from data preparation to obtaining the conformance results.

![](img/dge_shacl.en.drawio "Ilustración . Description of SHACL validation steps"){ align=center width="100%"}

SHACL shapes allow checking whether a catalog expressed in an RDF serialization is valid. Since it should be possible to transform the data exchange to RDF for DCAT-AP-ES compliance, these SHACL forms can be used in any data exchange context. However, the provided SHACL forms are only a starting point for implementers.

By using these templates, it is possible to identify and correct possible deviations from the specification, thereby improving the quality of the metadata produced. In addition, interactive tools such as the [European Commission Interoperability Testbed](https://www.itb.ec.europa.eu/shacl/any/upload) [^1] or [SHACL playground](https://shacl-playground.zazuko.com/) [^2], which provides an online service where it is possible to upload and validate RDF files against DCAT-AP-ES SHACL forms, facilitate the validation of DCAT-AP files using SHACL.

!!! info "More info" 

    - **✅ How to use SHACL validators in different technology stacks**: [github.com/datosgobes/DCAT-AP-ES/.../shacl/README.md](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/README.md)

    - More information about validation and SHACL forms in [SHACL, a language for validating RDF graphs](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf).

# DCAT-AP-ES SHACL constraint definitions
DCAT-AP-ES SHACL shapes for all versions can be found in the source code repository [`shacl/{version}/`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/): 

- `shacl_common_shapes.ttl`: Common constraints for all entities.
- `shacl_catalog_shape.ttl`: Constraints for catalogs
- `shacl_dataservice_shape.ttl`: Constraints for data services
- `shacl_dataset_shape.ttl`: Constraints for datasets
- `shacl_distribution_shape.ttl`: Constraints for distributions
- `shacl_dataservice_shape.ttl`: Constraints for data services
- `shacl_mdr-vocabularies.shape.ttl`: Controlled vocabularies and their constraints
- `shacl_imports.ttl`: Import definitions for external ontologies
- `shacl_mdr_imports.ttl`: Import definitions for MDR vocabularies

**`hvd/`**: Subdirectory with additional constraints for High Value Datasets (HVD): - `shacl_common_hvd_shapes.ttl`: Common constraints for all entities.

- `shacl_catalog_shape.ttl`: Constraints for HVD catalogues.
- `shacl_dataservice_hvd_shape.ttl`: Constraints for HVD Data Services.
- `shacl_dataset_hvd_shape.ttl`: Constraints for HVD datasets.
- `shacl_distribution_hvd_shape.ttl`: Constraints for HVD distributions.

# Use Cases
*Non-normative section*

The different validation cases in the DCAT-AP-ES Validator are based on the level of completeness of the checks and the incorporation of background knowledge (vocabularies). Each case is designed for a specific data exchange scenario.

!!! tip "Tip. Use case."

    For most use cases, the [`Case 1: DCAT-AP-ES full`](/validation/#case_1_dcat_ap_es_full) is recommended. It provides a complete validation of basic consistency and conformance to standard vocabularies.
    If your catalog contains High Value Datasets (HVD), consider using [`Case 2: Full DCAT-AP-ES (HVD)`](/validation/#case_1_dcat_ap_es_full_hvd) for a validation that includes the requirements of the [European Commission Implementing Regulation (EU) 2023/138](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138).

    Choosing the appropriate validation case depends on your specific needs and data exchange context.

Below, each case is described and recommendations are provided on which one to use for a catalog:

## **Case 1: Full DCAT-AP-ES**  {#case_1_dcat_ap_es_full}
It contains all the necessary constraints for the technical consistency of the different entities of the model, including the constraints of membership to rank classes and all the vocabularies used in DCAT-AP-ES.

*SHACL Shapes*:

- *Standard: Core entities and controlled vocabularies*.
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

## **Case 2: Full DCAT-AP-ES (HVD)** {#case_2_dcat_ap_es_full_hvd}
Includes all of the above constraints, plus those to adequately describe high_value datasets ([HVD](/#high_value_datasets_high_value_datasets)).

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*.
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *HVD: High value datasets specific constraints*
  - [`shacl_common_hvd_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_dataservice_hvd_shape.ttl)
  - [`shacl_dataset_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_dataset_hvd_shape.ttl)
  - [`shacl_distribution_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_distribution_hvd_shape.ttl)


## **Case 3: Full DCAT-AP-ES (with background knowlegdge)**  {#case_3_dcat_ap_es_full_imports}
Extends [Case 1](validation/#case_1_dcat_ap_en_full) with background knowledge and adds conformance to external standards.

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *Imports*
  - [`shacl_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr_imports.ttl)

!!! info "What is background knowledge?"
    Background knowledge consists of importing external ontologies and vocabularies that complement the validation. These import files (`shacl_imports.ttl` and `shacl_mdr_imports.ttl`) contain definitions of classes, properties, and hierarchical relationships from the standards used in DCAT-AP-ES.
    
    Using this background knowledge allows:
    
    1. *Semantically richer validations*: By knowing the complete structure of the ontologies.
    2. *Type inference*: Enables detection of inconsistencies in the class hierarchy.
    3. *Derived property validation*: Checks relationships that might not be explicit in the data.
    
    However, including this background knowledge can make validation slower and more resource-intensive.

## **Caso 4: Full DCAT-AP-ES (HVD with background knowlegdge)** {#case_4_dcat_ap_es_full_hvd_imports}
Extends [Case 1](validation/#case_1_dcat_ap_en_full) with background knowledge about conformance to external standards. It also includes the forms that allow to properly describe high value datasets ([HVD](#high_value_datasets_high_value_datasets)).

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*
  - [`shacl_common_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_catalog_shape.ttl)
  - [`shacl_dataservice_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataservice_shape.ttl)
  - [`shacl_dataset_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_dataset_shape.ttl)
  - [`shacl_distribution_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_distribution_shape.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *HVD: High value datasets specific constraints*
  - [`shacl_common_hvd_shapes.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_dataservice_hvd_shape.ttl)
  - [`shacl_dataset_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_dataset_hvd_shape.ttl)
  - [`shacl_distribution_hvd_shape.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/hvd/shacl_distribution_hvd_shape.ttl)

- *Imports*
  - [`shacl_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://datosgobes.github.io/DCAT-AP-ES/releases/1.0.0/shacl/1.0.0/shacl_mdr_imports.ttl)

[^1]: SHACL validator: [github.com/ISAITB/shacl-validator](https://github.com/ISAITB/shacl-validator). Interoperability Test Bed, Interoperable Europe Unit, DIGIT, European Commission.
[^2]: Zazuko SHACL Playground: [github.com/zazuko/shacl-playground](https://github.com/zazuko/shacl-playground). Zazuko GmbH.