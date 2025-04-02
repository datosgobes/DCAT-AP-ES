![](img/dge_shacl.en.drawio "Ilustración . Description of SHACL validation steps"){ align=center width="100%"}

To verify that the metadata exchange is technically compliant with [DCAT-AP-EN](/), the [SHACL shapes available in the repository](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0) graphs can be used. Shapes Constraint Language* (SHACL) is a [W3C recommendation](https://www.w3.org/TR/shacl/]) for expressing constraints in an RDF knowledge graph. 

SHACL shapes allow checking whether a catalog expressed in an RDF serialization is valid. Since it should be possible to transform the data exchange to RDF for DCAT-AP-ES compliance, these SHACL forms can be used in any data exchange context. However, the provided SHACL forms are only a starting point for implementers.

By using these templates, it is possible to identify and correct possible deviations from the specification, thereby improving the quality of the metadata produced. In addition, interactive tools such as the [SHACL playground](https://shacl-playground.zazuko.com/) [^1] or the [European Commission Interoperability Testbed](https://www.itb.ec.europa.eu/shacl/any/upload) [^2], which provides an online service where it is possible to upload and validate RDF files against DCAT-AP-ES SHACL forms, facilitate the validation of DCAT-AP files using SHACL.

!!! info "Information" 

    - More information about validation and SHACL forms in [SHACL, a language for validating RDF graphs](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf).

    - All versions of the DCAT-AP-ES shapefiles can be found in the code repository: [github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0)

# SHACL shapes of DCAT-AP-ES
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
  - [`shacl_common_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_catalog_shapes.ttl)
  - [`shacl_dataservice_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataservice_shapes.ttl)
  - [`shacl_dataset_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataset_shapes.ttl)
  - [`shacl_distribution_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_distribution_shapes.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

## **Case 2: Full DCAT-AP-ES (HVD)** {#case_2_dcat_ap_es_full_hvd}
Includes all of the above constraints, plus those to adequately describe high_value datasets ([HVD](/#high_value_datasets_high_value_datasets)).

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*.
  - [`shacl_common_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_catalog_shapes.ttl)
  - [`shacl_dataservice_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataservice_shapes.ttl)
  - [`shacl_dataset_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataset_shapes.ttl)
  - [`shacl_distribution_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_distribution_shapes.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *HVD: High value datasets specific constraints*
  - [`shacl_common_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_dataservice_hvd_shapes.ttl)
  - [`shacl_dataset_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_dataset_hvd_shapes.ttl)
  - [`shacl_distribution_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_distribution_hvd_shapes.ttl)


## **Case 3: Full DCAT-AP-ES (with background knowlegdge)**  {#case_3_dcat_ap_es_full_imports}
Extends [Case 1](validation/#case_1_dcat_ap_en_full) with background knowledge and adds conformance to external standards.

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*
  - [`shacl_common_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_catalog_shapes.ttl)
  - [`shacl_dataservice_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataservice_shapes.ttl)
  - [`shacl_dataset_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataset_shapes.ttl)
  - [`shacl_distribution_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_distribution_shapes.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *Imports*
  - [`shacl_imports.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr_imports.ttl)

## **Caso 4: Full DCAT-AP-ES (HVD with background knowlegdge)** {#case_4_dcat_ap_es_full_hvd_imports}
Extends [Case 1](validation/#case_1_dcat_ap_en_full) with background knowledge about conformance to external standards. It also includes the forms that allow to properly describe high value datasets ([HVD](#high_value_datasets_high_value_datasets)).

*SHACL Shapes*: 

- *Standard: Core entities and controlled vocabularies*
  - [`shacl_common_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_common_shapes.ttl)
  - [`shacl_catalog_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_catalog_shapes.ttl)
  - [`shacl_dataservice_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataservice_shapes.ttl)
  - [`shacl_dataset_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_dataset_shapes.ttl)
  - [`shacl_distribution_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_distribution_shapes.ttl)
  - [`shacl_mdr-vocabularies.shape.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl)

- *HVD: High value datasets specific constraints*
  - [`shacl_common_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_common_hvd_shapes.ttl)
  - [`shacl_dataservice_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_dataservice_hvd_shapes.ttl)
  - [`shacl_dataset_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_dataset_hvd_shapes.ttl)
  - [`shacl_distribution_hvd_shapes.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/hvd/shacl_distribution_hvd_shapes.ttl)

- *Imports*
  - [`shacl_imports.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_imports.ttl)
  - [`shacl_mdr_imports.ttl`](https://github.com/datosgobes/DCAT-AP-ES/tree/main/shacl/1.0.0/shacl_mdr_imports.ttl)

[^1]: Zazuko SHACL Playground: [github.com/zazuko/shacl-playground](https://github.com/zazuko/shacl-playground). Zazuko GmbH.
[^2]: SHACL validator: [github.com/ISAITB/shacl-validator](https://github.com/ISAITB/shacl-validator). Interoperability Test Bed, Interoperable Europe Unit, DIGIT, European Commission.