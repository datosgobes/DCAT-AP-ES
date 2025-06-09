# Introducción

En este documento se presenta una especificación detallada de los metadatos que permiten describir catálogos y recursos de datos reutilizables.

Los metadatos se describen sobre la base del paradigma de la Web Semántica, que implementa la descripción de recursos utilizando el modelo estándar para el intercambio de datos sobre la Web, RDF (Resource Description Framework). Este enfoque permite que diferentes sistemas de catalogación de datos puedan interactuar e intercambiar información de manera efectiva y coherente, logrando interoperabilidad semántica para facilitar la búsqueda y encontrabilidad de recursos de datos, mejorando considerablemente su valor para la reutilización.

El perfil de aplicación, en adelante, DCAT-AP-ES, es el modelo de metadatos que se recoge en la nueva versión de la Norma Técnica de Interoperabilidad de Recursos de Información del Sector Público ([NTI-RISP](https://datos.gob.es/es/doc-tags/nti-risp)), que está en proceso de tramitación administrativa. El modelo adopta las directrices del esquema europeo de intercambio de metadatos DCAT-AP con algunas restricciones y ajustes adicionales, perfil de aplicación que a su vez, se basa en la especificación DCAT, un vocabulario RDF creado con el objetivo de mejorar la interoperabilidad entre catálogos de datos en línea que viene siendo desarrollada por el [Grupo de trabajo de intercambio de conjuntos de datos](https://www.w3.org/2017/dxwg/) desde que fue publicada como recomendación por W3C en 2014. La versión del perfil europeo que se toma como referencia para la elaboración de DCAT-AP-ES es [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) junto a los elementos descritos en la extensión [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) para incorporar el modelado de los [Conjuntos de datos de alto valor](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) (*High Value Datasets*).

Como es sabido, un catálogo de datos abiertos puede estar constituido únicamente por conjuntos de datos o por servicios de datos, aunque lo habitual será que cuente tanto conjuntos de datos como servicios y se representa mediante instancias de las clases y propiedades que se especifican en este modelo.

En este documento, se detallan las clases principales del perfil de aplicación: Catálogo, Dataset, Distribución y Servicio de datos, así como otras clases relevantes para una completa información descriptiva de los elementos reutilizables catalogados de acuerdo con el modelo DCAT-AP-ES. Se especifica, además, el conjunto de vocabularios controlados que deben ser utilizados para ajustar las propiedades que describen los elementos catalogados.

!!! warning "Guía de convenciones "
    Como material adicional a esta guía técnica se incluyen las [**Convenciones datos.gob.es**](./conventions) que establecen **convenciones específicas** donde se definen **reglas adicionales** para abordar necesidades prácticas, semánticas o técnicas de la aplicación de DCAT-AP-ES que complementan esta especificación formal.

En respuesta a la creciente importancia de los datos en la sociedad y la economía, la Comisión Europea adoptó el [**Reglamento de ejecución (UE) 2023/138 de la Comisión Europea**](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138) (*High Value Datasets Implementing Regulation, HVD IR*) el 21 de diciembre de 2022. Este reglamento establece pautas claras para los organismos públicos en la disponibilidad de conjuntos de datos de alto valor y tiene como objetivo mejorar la calidad, accesibilidad y uso de un conjunto especifico de datos clave dentro del sector público. Para lograrlo, el reglamento HVD establece requisitos específicos para los metadatos asociados a los conjuntos de datos publicados.


!!! note "Relación entre la especificación y normativa específica sobre datos"

    El perfil de aplicación **DCAT-AP-ES es el núcleo mínimo de metadatos** que se aplica a todas las entidades del modelo. Sin embargo, **la conformidad con la especificación no exime del cumplimiento de las regulaciones específicas aplicables** en cada sector, como es el caso del reglamento HVD. En particular, los conjuntos de datos que cumplen con los criterios de HVD pueden incluir metadatos o restricciones adicionales que no están cubiertos por DCAT-AP-ES pero sí por la legislación.

# Modelo de metadatos DCAT-AP-ES {#dcat-ap-es-model}

A continuación, se detallan los elementos fundamentales del modelo, comenzando con el diagrama UML, la relación de clases, el espacio de nombres utilizado en la especificación y la relación de vocabularios controlados.

## Diagrama del modelo {#uml}

El modelo DCAT-AP-ES se representa a continuación como un diagrama UML que ilustra la especificación descrita en este documento. Para facilitar su interpretación, se omiten detalles que están incluidos en la descripción de cada metadato en este documento. Fundamentalmente, se incluyen las clases clave y algunas relevantes de soporte a las primeras.

![](img/uml/dcat-ap-es.drawio "Ilustración . Esquema UML del modelo de metadatos DCAT-AP-ES"){ align=center width="100%"}

## Clases del perfil de aplicación DCAT-AP-ES {#dcat-ap-es-entities}

Se enumeran a continuación las clases más relevantes utilizadas en el modelo:

* [**Catálogo**](#catalogo_-_clase_dcatcatalog_-_obligatorio). La clase **`dcat:Catalog`** representa un catálogo, que es un conjunto de datos en el que cada elemento individual es un registro de metadatos que describe algún recurso. El contenido de un catálogo son colecciones de metadatos sobre conjuntos de datos, servicios de datos u otros tipos de recursos, incluso otros catálogos. Funciona como un punto de acceso unificado que facilita la búsqueda y reutilización de recursos de datos.
* [**Registro del Catálogo**](#registro_del_catalogo_-_clase_dcatcatalogrecord_-_opcional). La clase Registro de Catálogo (**`dcat:CatalogRecord`**) describe entradas individuales dentro de un catálogo de datos, siendo cada una un registro específico de metadatos. Un registro de catálogo referencia una entidad en el catálogo pudiendo ser un conjunto de datos o un servicio de datos. Se utiliza principalmente para recopilar explícitamente información de procedencia sobre las entradas en un catálogo.
* [**Servicio de Datos**](#servicio_de_datos_-_clase_dcatdataservice_-_opcional). La clase Servicio de Datos (**`dcat:DataService`**) representa una colección de operaciones accesibles a través de una interfaz (API) que proporciona acceso a uno o más conjuntos de datos o funciones de procesamiento de datos. Mediante su uso es posible la catalogación de diversos tipos de servicios de datos facilitando la implementación de funcionalidades para el manejo y/o explotación programática de los datos.
* **[Conjunto de datos](#conjunto_de_datos_-_clase_dcatdataset_-_obligatorio)**. La clase Conjunto de Datos (**`dcat:Dataset`**) representa una conceptualización de una colección de información publicada por un único agente identificable. La noción de conjunto de datos es amplia con la intención de dar cabida a los tipos de recursos que surgen de un contexto de publicación pudiendo representarse de muchas formas, incluidos números, texto, imágenes, sonido y otros medios o tipos, cualquiera de los cuales podría recopilarse en un conjunto de datos.
* [**Distribución**](#distribucion_-_clase_dcatdistribution_-_recomendado). La clase Distribución de un conjunto de datos (**`dcat:Distribution`**) representa una forma accesible y reutilizable de un conjunto de datos, como un archivo descargable.
* [**Agente**](#agente_-_clase_foafagent_-_obligatorio). La clase Agent (**`foaf:Agent`**) se utiliza para representar cualquier organización o persona que posee competencias para realizar actuaciones sobre un catálogo y los recursos catalogados. Su función principal es proporcionar referencias concretas sobre los diferentes actores que pueden intervenir con diferentes roles en la gestión de un catálogo de datos.
* [**Identificador**](#nota-dcat_dataset-dct_identifier). La clase Identificador de un conjunto de datos (**`dct:Identifier`**) se utiliza para expresar la referencia exclusiva asignada a un conjunto de datos en el contexto de un esquema de identificadores determinado.
* [**Localización**](#localizacion_-_clase_dctlocation_-_opcional). La clase Localización (**`dct:Location`**), se emplea para identificar una región geográfica o un lugar. Se puede representar utilizando un vocabulario controlado o mediante la expresión de coordenadas geográficas que delimitan un área específica.
* [**Vigencia**](#vigencia_-_clase_dctperiodoftime_-_opcional). La clase Vigencia o Período Temporal (**`dct:PeriodOfTime`**) se utiliza para definir un intervalo de tiempo que se delimita por una fecha de inicio y otra de finalización.
* [**Control y verificación de integridad**](#control_y_verificacion_-_clase_spdxchecksum_-_opcional). La clase Control y Verificación de recursos (**`spdx:Checksum`**) se utiliza para especificar el método que se implementa y el resultado obtenido para garantizar la integridad de las distribuciones de conjuntos de datos, es decir, que su contenido no ha sido alterado.
* [**Relación**](#relacion_entre_recursos_-_clase_dcatrelationship_-_opcional). La clase Relación entre recursos (**`dcat:Relationship`**), se utiliza para especificar información adicional relativa a una relación entre recursos o agentes aportando contextualización sobre cómo dichos recursos están interrelacionados.

## Espacio de nombres utilizados en el modelo {#dcat-ap-es-namespaces}

Cada propiedad de una clase que describe algún atributo de los elementos del catálogo, registro de catálogo, servicio de datos, dataset, distribución, etc., reutiliza términos de otros vocabularios existentes. Se especifican mediante una URI determinada por la composición del prefijo del vocabulario correspondiente referenciado en el espacio de nombres del modelo DCAT-AP-ES y el nombre de la clase o propiedad. Por ejemplo, la propiedad `dct:issued` de la clase Catálogo, se expresa de forma equivalente en su forma abreviada y extendida de la siguiente forma:

!!! info "Nota sobre espacios de nombres"

    `dct:issued` es equivalente a `http://purl.org/dc/terms/issued`

Se enumerarán a continuación vocabularios genéricos que configuran el espacio de nombres reutilizados en la implementación del modelo DCAT-AP-ES:

| **Vocabulario** | **Prefijo** | **URI** |
| --- | --- | --- |
| Asset Description Metadata Schema | `adms:` | `http://www.w3.org/ns/adms#` |
| Data Catalog Vocabulary | `dcat:` | `http://www.w3.org/ns/dcat#` |
| DCAT Application profile for data portals | `dcatap:` | `http://data.europa.eu/r5r/` |
| Dublin Core Terms | `dct:` | `http://purl.org/dc/terms/` |
| Friend Of A Friend | `foaf:` | `http://xmlns.com/foaf/0.1/` |
| Location Core Vocabulary | `locn:` | `http://www.w3.org/ns/locn#` |
| Web Ontology Document | `owl:` | `http://www.w3.org/2002/07/owl#` |
| Open Digital Rights Language | `odrl:` | `http://www.w3.org/ns/odrl/2/` |
| Prov Family of Documents | `prov:` | `http://www.w3.org/ns/prov#` |
| Resource Description Framework | `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| Resource Description Framework Schema | `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| Simple Knowledge Organization System | `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| Software Package Data Exchange | `spdx:` | `http://spdx.org/rdf/terms#` |
| W3C Time Ontology | `time:` | `http://www.w3.org/2006/time#` |
| vCard Ontology | `vcard:` | `http://www.w3.org/2006/vcard/ns#` |
| XML Schema | `xsd:` | `http://www.w3.org/2001/XMLSchema#` |

## Vocabularios controlados utilizados en el modelo {#dcat-ap-es-vocabularies}
Para garantizar la coherencia e interoperabilidad entre catálogos de datos, DCAT-AP-ES recomienda el uso de vocabularios controlados para cada propiedad. La siguiente tabla muestra los vocabularios recomendados y sus correspondientes URIs, cuyo uso puede ser obligatorio en algunos casos según las especificaciones del modelo.

| **Propiedad** | **Clase** | **Vocabulario** | **URI del vocabulario** |
| --- | --- | --- | --- |
| **adms:status** | CatalogRecord | [Concept status](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/authority/concept-status) | `http://publications.europa.eu/resource/authority/concept-status` |
| **adms:status** | Distribution | [Distribution status](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/distribution-status) | `http://publications.europa.eu/resource/authority/distribution-status` |
| **dcat:compressFormat** | Distribution | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| **dcat:mediaType** | Distribution | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| **dcat:packageFormat** | Distribution | [IANA Media Types](http://www.iana.org/assignments/media-types/) | `http://www.iana.org/assignments/media-types/` |
| **dcat:theme** | Dataset<br>DataService | <ul><li>[Taxonomía de sectores primarios NTI-RISP](http://datos.gob.es/kos/sector-publico/sector)</li><li> [Vocabulario de Temas de datos (DCAT-AP)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[Registro de temas INSPIRE](http://inspire.ec.europa.eu/theme)</li></ul>  | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| **dcat:themeTaxonomy** | Catalog | <ul><li>[Taxonomía de sectores primarios NTI-RISP](http://datos.gob.es/kos/sector-publico/sector)</li><li> [Vocabulario de Temas de datos (DCAT-AP)](http://publications.europa.eu/resource/authority/data-theme)</li><li>[Registro de temas INSPIRE](http://inspire.ec.europa.eu/theme)</li></ul> | <ul><li>`http://datos.gob.es/kos/sector-publico/sector`</li><li>`http://publications.europa.eu/resource/authority/data-theme`</li><li>`http://inspire.ec.europa.eu/theme`</li></ul> |
| **dcatap:availability** | Distribution | [Planned availability](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/planned-availability) | `http://publications.europa.eu/resource/authority/planned-availability` |
| **dcatap:hvdCategory** | Dataset<br>DataService | [HVD Category](https://op.europa.eu/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/bna/asd487ae75) | `http://data.europa.eu/bna/asd487ae75` |
| **dct:accessRights** | Dataset<br>DataService | [Access right](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/access-right) | `http://publications.europa.eu/resource/authority/access-right` |
| **dct:accrualPeriodicity** | Dataset | [Frequency](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/frequency) | `http://publications.europa.eu/resource/authority/frequency` |
| **dct:format** | Distribution | [File type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/file-type) | `http://publications.europa.eu/resource/authority/file-type` |
| **dct:language** | Catalog<br>Dataset<br>Distribution | [Language](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/language) | `http://publications.europa.eu/resource/authority/language` |
| **dct:license** | Catalog<br>DataService<br>Distribution | [Licence](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/licence) | `http://publications.europa.eu/resource/authority/licence` |
| **dct:spatial** | Catalog<br>Dataset | <ul><li>[Taxonomía de territorio NTI-RISP](https://datos.gob.es/es/recurso/sector-publico/territorio)</li><li> [Continent](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/continent)</li><li>[Countries and territories](http://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/country)</li><li>[Administrative territorial unit](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/atu)</li><li>[Place](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/place)</li><li>[Geonames](http://www.geonames.org/)</li></ul> | <ul><li>`http://datos.gob.es/es/recurso/sector-publico/territorio`</li><li>`http://publications.europa.eu/resource/authority/continent`</li><li>`http://publications.europa.eu/resource/authority/country`</li><li>`http://publications.europa.eu/resource/authority/atu`</li><li>`http://publications.europa.eu/resource/authority/place`</li><li>`http://sws.geonames.org/`</li></ul> |
| **dct:type** | Agent | [ADMS publisher type](http://purl.org/adms/publishertype/1.0) | `http://purl.org/adms/publishertype/1.0` |
| **dct:type** | Dataset | [Dataset type](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/dataset-type) | `http://publications.europa.eu/resource/authority/dataset-type` |
| **dct:type** | LicenseDocument | [ADMS licence type](http://purl.org/adms/licencetype/1.0) | `http://purl.org/adms/licencetype/1.0` |

# Relación de metadatos del modelo DCAT-AP-ES {#dcat-ap-es-model-relations}

En las tablas de metadatos del modelo DCAT-AP-ES se especifica la siguiente información:

- **Metadato**: Nombre descriptivo del elemento de metadatos
- **Descripción**: Breve explicación de la función y propósito del metadato
- **Propiedad**: Identificador formal del metadato en forma de URI (por ejemplo, `dct:title`)
- **T** (Aplicabilidad): Tipo de requisito del metadato, sí es distinto para conjuntos de alto valor (HVD) se indica. Los tipos pueden ser:
  - **Ob** (Obligatorio): El publicador debe aportar la información de esta propiedad, y el consumidor debe ser capaz de procesarla.
  - **R** (Recomendado): El publicador debe proporcionar esta información si dispone de ella, el consumidor ha de ser capaz de procesarla.
  - **Op** (Opcional): El publicador puede proporcionar esta información, el consumidor ha de ser capaz de procesarla.
- **C** (Cardinalidad): Indica el número mínimo y máximo de ocurrencias permitidas, sí es distinto para conjuntos de alto valor (HVD) se indica. Por ejemplo, `1..n` significa al menos una, potencialmente muchas.
- **Rango**: Tipo de datos o clase que puede tomar el valor del metadato, incluyendo:
  - **Tipo principal**: Por ejemplo, `rdfs:Literal`, `foaf:Agent` o `dcat:Dataset`
  - **Descripción adicional**: Información sobre el formato o estructura esperada para el valor.

Esta estructura uniforme facilita la implementación y comprensión del perfil de aplicación DCAT-AP-ES.

Igualmente, se indica para cada entidad del modelo -catálogo, registro, servicio de datos, dataset, etc.- el requisito de aplicación.


## Catálogo - Clase: dcat:Catalog - Obligatorio

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Nombre | Breve título o nombre dado al catálogo de datos | dct:title | Ob | 1..n | **rdfs:Literal** |
| Descripción | Resumen descriptivo del catálogo de datos | dct:description | Ob | 1..n | **rdfs:Literal** |
| Órgano publicador | Organización que publica el catálogo. | dct:publisher | Ob | 1..1 | **foaf:Agent** |
| Fecha de creación | Fecha de publicación inicial del catálogo. | dct:issued | Ob | 1..1 | **rdfs:Literal** |
| Fecha de actualización | Fecha en la que se modificó por última vez el catálogo | dct:modified | Ob | 1..1 | **rdfs:Literal** |
| Página web | Dirección web pública de acceso al catálogo de datos | foaf:homepage | Ob | 1..1 | **foaf:Document** |
| Temáticas | Taxonomía de categorías de datasets incluidas en el catálogo. | dcat:themeTaxonomy | Ob | 1..3 | **skos:ConceptScheme** |
| Idioma(s) | Idioma(s) en el(los) que se encuentran metadatos de los elementos incluidos en el catálogo | dct:language | Ob | 1..n | **dct:****LinguisticSystem** |
| Términos de uso | Referencia a los términos de uso generales del catálogo | dct:license | Ob | 1..1 | **dct:LicenseDocument** |
| Dataset | Cada uno de los datasets incluidos en el catálogo | dcat:dataset | R | 0..n | **dcat:Dataset** |
| Servicio de datos | Cada uno de los servicios de datos incluidos en el catálogo | dcat:service | R | 0..n | **dcat:DataService** |
| Cobertura geográfica | Ámbito geográfico cubierto por el catálogo | dct:spatial | R | 0..n | **rdfs:Resource** |
| Catálogo | Catálogo relacionado | dcat:catalog | Op | 0..n | **dcat:Catalog** |
| Registro | Registro del Catálogo | dcat:record | Op | 0..n | **dcat:CatalogRecord** |
| Autor | Entidad responsable de generar el Catálogo | dct:creator | Op | 0..n | **foaf:Agent** |
| Incluye a | Otro Catálogo que está incluido en el catálogo | dct:hasPart | Op | 0..n | **dcat:Catalog** |
| Está incluido en | Forma parte de otro catálogo | dct:isPartOf | Op | 0..1 | **dcat:Catalog** |
| Declaración de derechos | Declaración de los derechos relacionados con el catálogo. | dct:rights | Op | 0..1 | **dct:RightsStatement** |
| Cobertura temporal | Define el período de tiempo que abarca el catálogo. | dct:temporal | Op | 0..n | **dct:PeriodOfTime** |


## Registro del catálogo - Clase: dcat:CatalogRecord - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Contenido principal del registro | Tipo de contenido principal del registro del catálogo | foaf:primaryTopic | Ob | 1..1 | **dcat:Dataset, dcat:DataService** |
| Fecha de última actualización | Última fecha conocida en la que se modificó o actualizó el registro del catálogo. | dct:modified | Ob | 1..1 | **rdfs:Literal** |
| Perfil de aplicación | Marco normativo relativo al registro del catálogo. | dct:conformsTo | R | 0..1 | **dct:Standard** |
| Fecha de creación | Fecha inicial en la que se creó el registro. | dct:issued | R | 0..1 | **rdfs:Literal** |
| Estado | Fase del ciclo de vida en que se encuentra | adms:status | R | 0..1 | **skos:Concept** |
| Nombre | Nombre o título del Registro del Catálogo | dct:title | Op | 0..n | **rdfs:Literal** |
| Descripción | Descripción resumida del contenido del registro del catálogo | dct:description | Op | 0..n | **rdfs:Literal** |

## Servicio de datos - Clase: dcat:DataService - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Nombre | Nombre del servicio de datos | dct:title | Ob | 1..n | **rdfs:Literal** |
| URL de acceso | URL en la que se publica el servicio. | dcat:endpointURL | Ob | 1..n | **rdfs:Resource** |
| Categoría de HVD | Categoría de dato de alto valor | dcatap:hvdCategory | Op[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **skos:Concept** |
| Punto de contacto | Información de contacto sobre el servicio de datos HVD | dcat:contactPoint | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **vcard:Kind** |
| Documentación | Documento relevante sobre el servicio de datos HVD | foaf:page | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **foaf:Document** |
| Temática(s) | Temática o categoría principal del servicio de datos. | dcat:theme | Ob | 1..n | **skos:Concept** |
| Publicador | Organización que publica el servicio. | dct:publisher | Ob | 1..1 | **foaf:Agent** |
| Descripción del punto de acceso | Descripción de las características del punto de acceso | dcat:endpointDescription | R | 0..n | **rdfs:Resource** |
| Conjuntos de datos | Conjuntos de datos disponibles a través del servicio. | dcat:servesDataset | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **dcat:Dataset** |
| Legislación aplicable | URI de la legislación que es aplicable al recurso | dcatap:applicableLegislation | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **eli:LegalResource** |
| Descripción | Descripción resumida del servicio de datos | dct:description | Op | 0..n | **rdfs:Literal** |
| Derechos de acceso | Declaración acerca de las posibles restricciones de acceso | dct:accessRights | Op | 0..1 | **dct:RightsStatement** |
| Licencia | Licencia del Servicio de datos | dct:license | Op | 0..1 | **dct:LicenseDocument** |
| Etiqueta(s) | Etiqueta(s) textual(es) para categorizar libremente el servicio de datos. | dcat:keyword | Op | 0..n | **rdfs:Literal** |

## Conjunto de datos - clase: dcat:Dataset - Obligatorio

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Nombre | Nombre o título del conjunto de datos. | dct:title | Ob | 1..n | **rdfs:Literal** |
| Descripción | Descripción detallada del conjunto de datos. | dct:description | Ob | 1..n | **rdfs:Literal** |
| Publicador | Organización que publica el conjunto de datos. | dct:publisher | Ob | 1..1 | **foaf:Agent** |
| Temática(s) | Temática o categoría principal del conjunto de datos. | dcat:theme | Ob | 1..n | **skos:Concept** |
| Distribución(es) | Recursos del conjunto de datos en sus posibles formatos. | dcat:distribution | R[^1]<br>Ob (HVD) | 1..n | **dcat:Distribution** |
| Categoría de HVD | Categoría de dato de alto valor | dcatap:hvdCategory | Op[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **skos:Concept** |
| Etiqueta(s) | Etiqueta(s) textual(es) para categorizar libremente el conjunto de datos. | dcat:keyword | R | 0..n | **rdfs:Literal** |
| Punto de contacto | Información de contacto sobre el conjunto de datos | dcat:contactPoint | R | 0..n | **vcard:Kind** |
| Cobertura temporal | Fecha inicial y final del período cubierto por el conjunto de datos. | dct:temporal | R | 0..n | **dct:PeriodOfTime** |
| Cobertura geográfica | Ámbito geográfico cubierto por el conjunto de datos. | dct:spatial | R | 0..n | **rdfs:Resource** |
| Legislación aplicable | URI de la legislación que es aplicable al recurso | dcatap:applicableLegislation | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **eli:LegalResource** |
| Identificador principal | URI principal que identifica al conjunto de datos | dct:identifier | Op | 0..n | **rdfs:Literal** |
| Otro identificador | Identificador secundario del conjunto de datos | adms:identifier | Op | 0..n | **adms:Identifier** |
| Autor | Organización responsable de generar el conjunto de datos. | dct:creator | Op | 0..n | **foaf:Agent** |
| Documentación | Referencia a un documento sobre el conjunto de datos | foaf:page | Op | 0..n | **foaf:Document** |
| Sitio web | Página de acceso al conjunto de datos, sus distribuciones e información adicional | dcat:landingPage | Op | 0..n | **foaf:Document** |
| Muestra | Muestra del conjunto de datos. | adms:sample | Op | 0..n | **dcat:Distribution** |
| Estándar | Especificaciones que cumple el dataset. | dct:conformsTo | Op | 0..n | **dct:Standard** |
| Fecha de creación | Fecha de creación del conjunto de datos. | dct:issued | Op | 0..1 | **rdfs:Literal** |
| Fecha de última actualización | Última fecha conocida en la que se modificó o actualizó el contenido del conjunto de datos. | dct:modified | Op | 0..1 | **rdfs:Literal** |
| Tipo | Categorización del conjunto de datos. | dct:type | Op | 0..1 | **skos:Concept** |
| Idioma(s) | Idioma(s) de los metadatos y/o de los valores del conjunto de datos | dct:language | Op | 0..n | **dct:LinguisticSystem** |
| Frecuencia de actualización | Período de tiempo aproximado entre actualizaciones del conjunto de datos | dct:accrualPeriodicity | Op | 0..1 | **dct:Frequency** |
| Versión | Identificación de la versión del conjunto de datos | dcat:version | Op | 0..1 | **rdfs:Literal** |
| Notas de Versión | Descripción de las diferencias entre versiones | adms:versionNotes | Op | 0..n | **rdfs:Literal** |
| Relación | Relación entre recursos | dcat:qualifiedRelation | Op | 0..n | **dcat:Relationship** |
| Resolución espacial | Mínima distancia entre dos datos distintos | dcat:spatialResolutionInMeters | Op | 0..1 | **rdfs:Literal** |
| Resolución temporal | Tiempo mínimo entre dos registros de datos consecutivos | dcat:temporalResolution | Op | 0..1 | **rdfs:Literal** |
| Referenciado por | Referencia al conjunto de datos | dct:isReferencedBy | Op | 0..n | **rdfs:Resource** |
| Procedencia | Procedencia de los datos | dct:provenance | Op | 0..n | **dct:ProvenanceStatement** |
| Recurso relacionado | Relación entre recursos | dct:relation | Op | 0..n | **rdfs:Resource** |
| Atribución | Agentes con alguna responsabilidad significativa sobre el conjunto de datos | prov:qualifiedAttribution | Op | 0..n | **prov:Attribution** |
| Generador | Referencia a la actividad que generó el conjunto de datos. | prov:wasGeneratedBy | Op | 0..n | **prov:Activity** |
| Tiene versión | Relaciona este conjunto de datos con una versión, edición o adaptación. | dcat:hasVersion | Op | 0..n | **dcat:Dataset** |
| Es versión de | Relaciona esta versión con el conjunto de datos versionado. | dcat:isVersionOf | Op | 0..n | **dcat:Dataset** |
| Origen | Referencia a un dataset de origen | dct:source | Op | 0..n | **dcat:Dataset** |
| Derechos de acceso | Declaración acerca de posibles restricciones de acceso | dct:accessRights | Op | 0..1 | **dct:RightsStatement** |



## Distribución - Clase: dcat:Distribution - Recomendado

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| URL de acceso | URL que permite el acceso a la distribución | dcat:accessURL | Ob | 1..n | **rdfs:Resource** |
| Legislación aplicable | URI de la legislación que es aplicable al recurso  | dcatap:applicableLegislation | R[^1]<br>Ob (HVD) | 0..n<br>1..n (HVD) | **eli:LegalResource** |
| Descripción | Descripción de la distribución | dct:description | R | 0..n | **rdfs:Literal** |
| Disponibilidad | Disponibilidad planificada de la distribución | dcatpa:availability | R | 0..1 | **skos:Concept** |
| Formato | Formato en que se encuentra representado el conjunto de datos | dct:format | R | 0..1 | **dct:MediaTypeOrExtent** |
| Licencia | Licencia bajo la que se publica la distribución | dct:license | R | 0..1 | **dct:LicenseDocument** |
| Formato tipo MIME | Tipo MIME de la distribución | dcat:mediaType | Op | 0..1 | **dct:MediaType** |
| Servicio de acceso | Servicio de datos que proporciona acceso a la distribución | dcat:accessService | Op | 0..n | **dcat:DataService** |
| Nombre | Breve título o nombre dado a la distribución. | dct:title | Op | 0..n | **rdfs:Literal** |
| Documentación | Referencia a un documento que describe la distribución | foaf:page | Op | 0..n | **foaf:Document** |
| URL de descarga | URL para la descarga del archivo en el formato definido. | dcat:downloadURL | Op | 0..n | **rdfs:Resource** |
| Esquema | Esquema o modelo de datos vinculado | dct:conformsTo | Op | 0..n | **dct:Standard** |
| Fecha de creación de la distribución | Fecha de creación | dct:issued | Op | 0..1 | **rdfs:Literal** |
| Fecha de última actualización de la distribución | Última fecha conocida en la que se actualizó la distribución | dct:modified | Op | 0..1 | **rdfs:Literal** |
| Estado | Estado del registro de catálogo en el contexto del flujo editorial de las descripciones de conjuntos de datos y servicios de datos. | adms:status | Op | 0..1 | **skos:Concept** |
| Idioma(s) | Idioma(s) empleado en la información contenida en la distribución | dct:language | Op | 0..n | **dct:LinguisticSystem** |
| Formato comprimido | Formato de compresión en el que se encuentran los datos | dcat:compressFormat | Op | 0..1 | **dct:MediaType** |
| Formato empaquetado | Formato en el que agrupan archivos para su descarga | dcat:packageFormat | Op | 0..1 | **dct:MediaType** |
| Tamaño | Tamaño aproximado del conjunto de datos. | dcat:byteSize | Op | 0..1 | **rdfs:Literal** |
| Resolución espacial | Mínima separación física entre datos | dcat:spatialResolutionInMeters | Op | 0..1 | **rdfs:Literal** |
| Resolución temporal | Tiempo mínimo entre dos registros de datos | dcat:temporalResolution | Op | 0..1 | **rdfs:Literal** |
| Control de verificación | Mecanismo de verificación de integridad de la distribución | spdx:checksum | Op | 0..1 | **spdx:Checksum** |
| Norma ODLR | Expresión de los derechos asociados con el uso de la distribución del conjunto de datos | odrl:hasPolicy | Op | 0..1 | **odrl:Policy** |
| Declaración de derechos | Declaración que especifica los derechos vinculados con la distribución | dct:rights | Op | 0..1 | **dct:RightsStatement** |


## Agente - Clase: foaf:Agent - Obligatorio

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Nombre | Nombre del agente | foaf:name | Ob | 1..n | **rdfs:Literal** |
| Identificador | Identificador del agente | dct:identifier | R | 0..1 | **rdfs:Literal** |
| Tipo | Tipo de agente | dct:type | R | 0..1 | **skos:Concept** |


## Localización - Clase: dct:Location - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Ámbito geográfico (delimitación) | Delimitación geográfica de un recurso (área rectangular) | dcat:bbox | R | 0..1 | **rdfs:Literal** |
| Ámbito geográfico (centroide) | Centro geográfico de un recurso (punto) | dcat:centroid | R | 0..1 | **rdfs:Literal** |
| Geometría | Geometría de un recurso | locn:geometry | Op | 0..1 | **rdfs:Literal** |


## Vigencia - Clase: dct:PeriodOfTime - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Fecha de inicio | Fecha de inicio de un intervalo temporal | dcat:startDate | R | 0..1 | **rdfs:Literal** |
| Fecha de finalización | Fecha de finalización de un intervalo temporal | dcat:endDate | R | 0..1 | **rdfs:Literal** |
| Comienzo | Instante de inicio de un intervalo o período | time:hasBeginning | Op | 0..1 | **time:Instant** |
| Final | Instante de finalización de un intervalo o período | time:hasEnd | Op | 0..1 | **time:Instant** |

## Control y verificación - Clase: spdx:Checksum - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Algoritmo | Algoritmo utilizado para verificar la integridad | spdx:algorithm | Ob | 1..1 | **spdx:ChecksumAlgorithm\_sha1** |
| Valor | Resultado generado por el algoritmo utilizado para la verificación de integridad | spdx:checksumValue | Ob | 1..1 | **rdfs:Literal** escrito como  **xsd:hexBinary** |

## Relación entre recursos - Clase: dcat:Relationship - Opcional

| Metadato | Descripción | Propiedad | T | C | Rango |
| --- | --- | --- | --- | --- | --- |
| Función | Función que una entidad o agente ejerce respecto a otra entidad o recurso | dcat:hadRole | Ob | 1..n | **dcat:Role** |
| Relación | Recurso sobre el que se describe la relación | dct:relation | Ob | 1..n | **rdfs:Resource** |


# Especificación detallada de metadatos del modelo DCAT-AP-ES {#dcat-ap-es-detailed-model}

A continuación, se detalla para cada clase del modelo DCAT-AP-ES la relación de propiedades o metadatos con sus características de ajuste y las notas de uso para su implementación.

## Metadatos de la clase Catálogo {#dcat-catalog}

Un catálogo es un repositorio para organizar conjuntos de datos y/o servicios de datos principalmente, aunque también puede ser un catálogo de catálogos de datos. Funciona como un punto de acceso unificado que facilita la búsqueda y reutilización de recursos de datos. En DCAT-AP-ES se representa mediante instancias de la clase Catálogo (`dcat:Catalog`).

Se describe mediante las siguientes propiedades:

| dcat:Catalog | dct:title |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Breve título o nombre dado al catálogo de datos. |
| **Propiedad** | **dct:title** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal.** Cadena alfanumérica. |

!!! note "Nota de uso"

    Se debe especificar un literal conciso. Se recomienda no incluir en el nombre ninguna referencia temporal o geográfica dado que este tipo de información debe expresarse mediante las propiedades específicas cobertura espacial (`dct:spatial`) y temporal (`dct:temporal`). Esta propiedad puede ser repetida para expresar el nombre en diferentes idiomas.


| dcat:Catalog | dct:description |
| --- | --- |
| **Metadato** | **Descripción** |
| **Descripción** | Descripción que ofrece un resumen claro del contenido y contexto del catálogo de datos proporcionando una visión general rápida y eficaz de los recursos de datos. |
| **Propiedad** | **dct:description** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal.** Cadena alfanumérica. |

!!! note "Nota de uso"

    Se debe especificar un literal. Esta propiedad puede ser repetida para expresar la descripción en diferentes idiomas.


| dcat:Catalog | dct:publisher |
| --- | --- |
| **Metadato** | **Publicador** |
| **Descripción** | Agente, en este caso una Organización, responsable de publicar y mantener el catálogo. Proporciona información clave sobre la autoría y la fuente oficial de los recursos de datos. |
| **Propiedad** | **dct:publisher** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **foaf:Agent** |

!!! note "Nota de uso"

    Cada organización se especificará mediante el siguiente patrón de URI:  `http://datos.gob.es/recurso/sector-publico/org/Organismo/{ID-DIR}`  Donde `{ID-DIR}` es el identificador alfanumérico único que diferencia a todas las entidades. En el caso de organismos del sector público éste se encuentra disponible en el Directorio Común de unidades orgánicas y oficinas (DIR3). En el caso de entidades del sector privado, el identificador a utilizar es el `NIF`.


| dcat:Catalog | foaf:homepage |
| --- | --- |
| **Metadato** | **Página web** |
| **Descripción** | Se refiere a la URL o dirección de internet que proporciona acceso directo a la página de inicio del catálogo de datos. |
| **Propiedad** | **foaf:homepage** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **dcat:Document** |

!!! note "Nota de uso"

    Se debe referir una URL directa y estable para asegurar que los usuarios puedan acceder al recurso de manera confiable y consistente, y que esté actualizada para reflejar el contenido más reciente del catálogo o del recurso de datos específico.


| dcat:Catalog | dcat:themeTaxonomy |
| --- | --- |
| **Metadato** | **Temáticas** |
| **Descripción** | Clasificación taxonómica de las categorías o temas que determinan el contexto de los recursos de datos incluidos en el catálogo que se describe Este metadato facilita a los usuarios la búsqueda y el acceso a información relevante por áreas de interés. |
| **Propiedad** | **dcat:themeTaxonomy** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..3** |
| **Rango** | **skos:ConceptScheme** |

!!! note "Nota de uso"

    Se debe expresar al menos una clasificación taxonómica. Para ello se utilizará obligatoriamente la taxonomía de sectores primaros definida en el vocabulario `http://datos.gob.es/kos/sector-publico/sector` y de manera opcional, el vocabulario de Temas de datos (DCAT-AP): `http://publications.europa.eu/resource/authority/data-theme` o el registro de temas INSPIRE `http://inspire.ec.europa.eu/theme/`


| dcat:Catalog | dct:issued |
| --- | --- |
| **Metadato** | **Fecha de creación** |
| **Descripción** | Fecha en la que se generó o publicó por primera vez el catálogo de datos, proporcionando contexto temporal. |
| **Propiedad** | **dct:issued** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Catalog | dct:modified |
| --- | --- |
| **Metadato** | **Fecha de actualización** |
| **Descripción** | Fecha en la que se realizó el último cambio en el catálogo, como la adición, eliminación o modificación de un recurso de datos, asegurando que los usuarios acceden a la versión más actualizada. |
| **Propiedad** | **dct:modified** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Catalog | dct:language |
| --- | --- |
| **Metadato** | **Idioma** |
| **Descripción** | Especifica el idioma en el que se encuentra la información contenida en el catálogo de datos. |
| **Propiedad** | **dct:language** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **dct:LinguisticSystem** |

!!! note "Nota de uso"

    Esta propiedad expresa el, o los idiomas, utilizados en los literales que describen títulos, descripciones, palabras clave, etc. de los recursos de datos incluidos en el Catálogo.
    
    * Se puede repetir si los metadatos se proporcionan en varios idiomas, ^pero al menos uno de los idiomas debe ser español^.  
    * Se debe usar el vocabulario normalizado de idiomas:  `http://publications.europa.eu/resource/authority/language`  
    
    Complementariamente, es recomendable el uso del atributo `xml:lang` ajustado con el valor correspondiente para expresar literales en cada idioma especificado en la propiedad. Para ello, se recomienda usar los códigos de idioma normalizados definidos en el [RFC-5646](https://www.rfc-editor.org/rfc/rfc5646.html) (por ejemplo, `es` para español, `en` para inglés, `ca` para catalán, `eu` para vasco, `gl` para gallego, etc.).


| dcat:Catalog | dct:license |
| --- | --- |
| **Metadato** | **Términos de uso** |
| **Descripción** | Especifica las condiciones de reutilización del catálogo de datos. Informa a los usuarios sobre los derechos y obligaciones asociados al uso de los recursos de datos. |
| **Propiedad** | **dct:license** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **dct:LicenseDocument** |

!!! note "Nota de uso"

    Se debe incluir una URI que enlace directamente al documento o recurso online que detalla los términos y condiciones de uso del catálogo. Se recomienda el uso de licencias tipo mediante el vocabulario `http://publications.europa.eu/resource/authority/licence` que permite describir dichas condiciones, asegurando así una interpretación y aplicación coherente de las normas de uso y reutilización de los datos. En el caso de datos de alto valor (HVD) la propiedad debe ajustarse especificando el tipo de [licencia CC-BY 4.0](http://publications.europa.eu/resource/authority/licence/CC_BY_4_0) u otra más permisiva. Alternativamente, se podrá referenciar un documento de licencia mediante una URL del texto legal que el publicador determine.


| dcat:Catalog | dcat:dataset |
| --- | --- |
| **Metadato** | **Dataset** |
| **Descripción** | Referencia a un conjunto de datos incluido en el catálogo que se describe. |
| **Propiedad** | **dcat:dataset** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Dataset** |

!!! note "Nota de uso"

    Se deben incluir referencias a datasets. Se sugiere incluir referencias claras y precisas a cada conjunto de datos, idealmente utilizando identificadores únicos o URIs.


| dcat:Catalog | dcat:service |
| --- | --- |
| **Metadato** | **Servicio** |
| **Descripción** | Referencia a un servicio de datos incluido en el catálogo que se describe. |
| **Propiedad** | **dcat:service** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:DataService** |

!!! note "Nota de uso"

    Se deben incluir referencias a servicios de datos Se recomienda proporcionar referencias claras y precisas para cada servicio de datos.


| dcat:Catalog | dct:spatial |
| --- | --- |
| **Metadato** | **Cobertura geográfica** |
| **Descripción** | Específica el área geográfica a la que se circunscriben o son relevantes los datos del catálogo. |
| **Propiedad** | **dct:spatial** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se recomienda especificar la región o área geográfica utilizando alguno de los siguientes métodos:
    
    1. preferentemente un vocabulario o nomenclátor geográfico, para garantizar una descripción normalizada del ámbito territorial. Para ello, la cobertura geográfica se puede expresar mediante cualquiera de los siguientes: 

       1. `http://datos.gob.es/es/recurso/sector-publico/territorio`
       2. `http://publications.europa.eu/resource/authority/continent`
       3. `http://publications.europa.eu/resource/authority/country`
       4. `http://publications.europa.eu/resource/authority/atu`
       5. `http://publications.europa.eu/resource/authority/place/`
       6. `http://sws.geonames.org/`

    2.  Como alternativa, es posible delimitar el área geográfica utilizando las propiedades de la clase [Location](#loca) (explicada más adelante en este documento).


| dcat:Catalog | dcat:catalog |
| --- | --- |
| **Metadato** | **Catálogo** |
| **Descripción** | Especifica un catálogo de datos que es relevante o de interés en relación con el catálogo actual. |
| **Propiedad** | **dcat:catalog** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Catalog** |

!!! note "Nota de uso"

    Como subpropiedad de `dct:haspart` se usa para especificar una jerarquía de catálogos.


| dcat:Catalog | dcat:record |
| --- | --- |
| **Metadato** | **Registro** |
| **Descripción** | Especifica un registro que es una entrada específica incluida en el catálogo. Dicha entrada describe un conjunto de datos o servicio de datos. |
| **Propiedad** | **dcat:record** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:CatalogRecord** |

!!! note "Nota de uso"

    Se especificará la referencia a un registro del catálogo.


| dcat:Catalog | dct:creator |
| --- | --- |
| **Metadato** | **Autor** |
| **Descripción** | Especifica la organización responsable de la creación del catálogo que se describe. Identifica la autoría y reconoce la fuente original del catálogo, proporcionando transparencia y contexto sobre su origen. |
| **Propiedad** | **dct:creator** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **foaf:Agent** |

!!! note "Nota de uso"

    Para su especificación se deben usar las propiedades de la clase [`foaf:Agent`](#agente---clase-foafagent---obligatorio).


| dcat:Catalog | dct:hasPart |
| --- | --- |
| **Metadato** | **Incluye a** |
| **Descripción** | Referencia uno o varios catálogos cuyo contenido es relevante en el contexto del catálogo que se describe y por tanto está vinculado con él estableciendo así una relación de pertenencia. |
| **Propiedad** | **dct:hasPart** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Catalog** |

!!! note "Nota de uso"

    Se especificará uno o varios catálogos que son parte del catálogo que se describe. Esta propiedad es inversa a la propiedad `dct:isPartOf`


| dcat:Catalog | dct:isPartOf |
| --- | --- |
| **Metadato** | **Está incluido en** |
| **Descripción** | Referencia un catálogo para el cual, el catálogo que se describe es relevante y por tanto está vinculado a él estableciendo así una relación de inclusión. |
| **Propiedad** | **dct:isPartOf** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dcat:Catalog** |

!!! note "Nota de uso"

    Se especificará un catálogo del que forma parte el catálogo que se describe. Esta propiedad es inversa a la propiedad `dct:hasPart`


| dcat:Catalog | dct:rights |
| --- | --- |
| **Metadato** | **Declaración de derechos** |
| **Descripción** | Declaración que especifica los derechos vinculados con el catálogo que se describe. |
| **Propiedad** | **dct:rights** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:RightsStatement** |

!!! note "Nota de uso"

    Mediante esta declaración se especifican los derechos que no están cubiertos por los términos de uso (`dct:licence`) o los derechos de acceso (`dct:accessRights`), por ejemplo, derechos de propiedad intelectual. Para ajustar esta propiedad se pueden utilizar propiedades del vocabulario `http://schema.theodi.org/odrs/`

| dcat:DataseCatalogt | dct:temporal |
| --- | --- |
| **Metadato** | **Cobertura temporal** |
| **Descripción** | Define el período de tiempo que abarca el catálogo. |
| **Propiedad** | **dct:temporal** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:PeriodOfTime** |

!!! note "Nota de uso"

    Se ajusta utilizando las propiedades de la clase Período temporal (`dct:PeriodOfTime`). Se recomienda incluir un intervalo de tiempo, definido por inicio y fin como fecha o instante temporal. Si se usa fecha para el inicio, debería usarse fecha como fin (ídem para instante temporal) y siempre emparejados, evitando los intervalos abiertos.

## Metadatos de la clase Registro del Catálogo {#dcat-catalogrecord}

La clase Registro de Catálogo (`dcat:CatalogRecord`) describe entradas individuales dentro de un catálogo de datos. Un registro de catálogo referencia una entidad en el catálogo pudiendo ser un conjunto de datos o un servicio de datos.

El uso de esta clase es opcional. Se utiliza principalmente para recopilar explícitamente información de procedencia sobre las entradas en un catálogo. Es útil cuando se desea hacer una distinción entre los metadatos propios de un conjunto de datos o servicio y los metadatos descriptores de la entrada del conjunto de datos o servicio en el catálogo. Por ejemplo, la propiedad fecha de publicación de un conjunto de datos (`dct:issued` de la clase `dcat:Dataset`) refleja la fecha en que el publicador puso a disposición la información, mientras que la fecha de publicación del registro del catálogo (`dct:issued` de la clase `dcat:CatalogRecord`) es la fecha en que se agregó el conjunto de datos al catálogo. En los casos en que ambas fechas difieran, o cuando sólo se conozca esta última, la fecha de publicación debe especificarse únicamente para el registro del catálogo.

Si esta función no es necesaria, la clase `dcat:CatalogRecord` se puede ignorar sin problema.

| dcat:CatalogRecord | foaf:primaryTopic |
| --- | --- |
| **Metadato** | **Contenido principal del registro** |
| **Descripción** | Indica el tipo de contenido de un registro específico del catálogo: conjunto de datos o servicio de datos. |
| **Propiedad** | **foaf:primaryTopic** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **dcat:Dataset, dcat:DataService** |

!!! note "Nota de uso"

    Se debe especificar el recurso principal que se registra en el catálogo. Puede ser un conjunto de datos específico o un servicio de datos


| dcat:CatalogRecord | dct:modified |
| --- | --- |
| **Metadato** | **Fecha de actualización del registro** |
| **Descripción** | Indica la última fecha en la que se actualizó el contenido del registro de un conjunto de datos o servicio de datos en el catálogo. |
| **Propiedad** | **dct:modified** |
| **Aplicabilidad** | **Obligatoria** |
| **Cardinalidad** | **1..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:CatalogRecord | dct:conformsTo |
| --- | --- |
| **Metadato** | **Perfil de aplicación** |
| **Descripción** | Marco normativo asociado con el registro del catálogo, señalando el contexto en el que se encuentra. Generalmente incluye un enlace a un documento específico, proporcionando una referencia directa a las leyes o regulaciones aplicables. |
| **Propiedad** | **dct:conformsTo** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:Standard** |

!!! note "Nota de uso"

    Se debe incluir enlaces directos y actualizados a los documentos legales o marcos normativos específicos que se aplican al conjunto de datos, asegurando que los usuarios puedan acceder fácilmente a la información legal relevante.  Se aconseja verificar que los enlaces conducen a las versiones vigentes de las normativas para mantener la precisión y relevancia del metadato.


| dcat:CatalogRecord | dct:issued |
| --- | --- |
| **Metadato** | **Fecha de creación del registro** |
| **Descripción** | Fecha en que se creó el registro en el catálogo. Especifica el momento en que se insertó por primera vez el registro de un conjunto de datos o servicio de datos en el catálogo. |
| **Propiedad** | **dct:issued** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).

| dcat:CatalogRecord | adms:status |
| --- | --- |
| **Metadato** | **Estado editorial del registro** |
| **Descripción** | Estado del registro de catálogo en el contexto del flujo editorial de las descripciones de conjuntos de datos y servicios de datos. |
| **Propiedad** | **adms:status** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    El estado del registro del catálogo puede ser alguno de los valores definidos en el vocabulario:  `http://publications.europa.eu/resource/authority/concept-status` ([Recomendación DCAT 3](https://www.w3.org/TR/vocab-dcat-3/#life-cycle))

| dcat:CatalogRecord | dct:title |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Breve nombre o título del Registro del Catálogo |
| **Propiedad** | **dct:title** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica** |

!!! note "Nota de uso"

    Se debe especificar un literal conciso. Esta propiedad puede ser repetida para expresar el nombre en diferentes idiomas.


| dcat:CatalogRecord | dct:description |
| --- | --- |
| **Metadato** | **Descripción** |
| **Descripción** | Descripción resumida del contenido del registro del catálogo. |
| **Propiedad** | **dct:description** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica** |

!!! note "Nota de uso"

    Se debe especificar un literal. Esta propiedad puede ser repetida para expresar la descripción en diferentes idiomas


## Metadatos de la clase Servicio de Datos {#dcat-dataservice}

La clase Servicio de Datos (`dcat:DataService`) permite describir operaciones que proporcionan acceso a uno o más conjuntos de datos o funciones de procesamiento de datos. Mediante su uso es posible la catalogación de diversos tipos de servicios de datos facilitando la implementación de funcionalidades para el manejo y/o explotación programática de los datos. Esta clase es importante para facilitar el acceso programable de los datos, permitiendo así su integración y uso efectivo en diferentes aplicaciones y servicios.

Utilizando esta clase, un dataset se puede distribuir en diferentes representaciones servidas por diferentes servicios de datos. Cada URL de acceso indicada en cada distribución se corresponde con el punto de acceso o endpoint del servicio que la sirve. Cada servicio se caracteriza por un tipo concreto (por ejemplo, un tipo de servicio de datos espaciales de [INSPIRE](https://datos.gob.es/es/noticia/inspire-infraestructura-europea-de-datos-espaciales)), el punto de acceso que será conforme a una especificación concreta y sus especificidades se detallarán mediante una descripción que explica el uso de parámetros y opciones.

!!! warning "Importante"
    Para la descripción de **datos de alto valor (HVD) se deberán añadir**, a las ya obligatorias, las propiedades **legislación aplicable** (`dcatap:applicableLegislation`), **categoría HVD** (`dcatap:hvdCategory`), **punto de contacto** (`dcat:contactPoint`), **conjuntos de datos servidos** (`dcat:servesDataset`) y **documentación** `foaf:page`.


| dcat:DataService | dct:title |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Breve título o nombre dado al servicio de datos. |
| **Propiedad** | **dct:title** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica** |

!!! note "Nota de uso"

    Se debe especificar un literal conciso. Se recomienda no incluir en el nombre ninguna referencia temporal o geográfica dado que este tipo de información debe expresarse mediante las propiedades específicas cobertura espacial (`dct:spatial`) y temporal (`dct:temporal`). Esta propiedad puede ser repetida para expresar el nombre en diferentes idiomas.


| dcat:DataService | dcatap:applicableLegislation |
| --- | --- |
| **Metadato** | **Legislación aplicable** |
| **Descripción** | Referencia a la legislación aplicable, sí contiene datos de alto valor, entonces debe indicarse al menos el [Reglamento de Implementación 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj) |
| **Propiedad** | **dcatap:applicableLegislation** |
| **Aplicabilidad** | **Recomendado - Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - Sí es HVD: 1..n |
| **Rango** | **eli:LegalResource** |

!!! note "Nota de uso"

    Se debe proporcionar como mínimo el ELI del reglamento: `http://data.europa.eu/eli/reg_impl/2023/138/oj`. Dado que la disponibilidad del HVD puede estar regulada por múltiples normativas específicas del dato, la cardinalidad máxima no está limitada.


| dcat:DataService | dcatap:hvdCategory |
| --- | --- |
| **Metadato** | **Categoría de HVD** |
| **Descripción** | Referencia la categoría de dato de alto valor con la que se vincula el servicio de datos que se describe según el [reglamento de implementación 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj). |
| **Propiedad** | **dcatap:hvdCategory** |
| **Aplicabilidad** | **Opcional** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se debe proporcionar, al menos, un valor de la taxonomía: <https://op.europa.eu/web/eu-vocabularies/concept-scheme/-/resource?uri=http://data.europa.eu/bna/asd487ae75>


| dcat:DataService | dcat:contactPoint |
| --- | --- |
| **Metadato** | **Punto de contacto** |
| **Descripción** | Proporciona la información de contacto que se puede utilizar para enviar comentarios sobre el Servicio de Datos. |
| **Propiedad** | **dcat:contactPoint** |
| **Aplicabilidad** | **Recomendado** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **vcard:Kind** |

!!! note "Nota de uso"

    La información de contacto para para el servicio de datos se puede expresar utilizando las propiedades de la [ontología vCard](https://www.w3.org/TR/vcard-rdf/). Se recomienda especialmente el siguiente subconjunto de propiedades:

    | Propiedad     |                   Descripción       |
    | :-------------------- | :----------------------------------------------------- |
    | `vcard:fn`            | Nombre                                                 |
    | `vcard:hasUid`        | Identificador del organismo                            |
    | `vcard:fn`            | Denominación de área o persona                         |
    | `vcard:hasEmail`      | Dirección de correo electrónico                         |
    | `vcard:hasTelephone`  | Número de teléfono                                      |
    | `vcard:hasURL`        | Enlace al formulario de contacto (recomendado) o al sitio web |

| dcat:DataService | foaf:page |
| --- | --- |
| **Metadato** | **Documentación** |
| **Descripción** | Proporciona la referencia a un documento que contiene información relevante sobre el servicio de datos. Entre otras cuestiones relevantes susceptibles de ser documentadas, se encuentra la calidad. La calidad de un servicio de datos cubre un amplio espectro de aspectos. El reglamento HVD no incluye ningún aspecto obligatorio. Por lo tanto, la información sobre la calidad del servicio se considera parte de la documentación genérica de un Servicio de Datos. |
| **Propiedad** | **foaf:page** |
| **Aplicabilidad** | **Recomendado** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **foaf:Document** |

!!! note "Nota de uso"

    Se recomienda incluir enlaces a recursos documentales que proporcionen a los usuarios un contexto más amplio y una mejor comprensión del servicio de datos.


| dcat:DataService | dcat:theme |
| --- | --- |
| **Metadato** | **Temática** |
| **Descripción** | Este metadato identifica la temática o materia principal del Servicio de datos. Sirve para categorizar los datos según su contenido conforme a una clasificación cerrada, facilitando su búsqueda y localización. |
| **Propiedad** | **dcat:theme** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se ajustará utilizando uno o varios de los temas de las clasificaciones taxonómicas que se indican en la clase Catálogo mediante el metadato temáticas (`dcat:themeTaxonomy`). Cada uno de los temas se designará referenciando la URI asociada a la categoría correspondiente de la taxonomía.  Se deben utilizar obligatoriamente temas de la taxonomía de sectores primaros definida en el vocabulario `http://datos.gob.es/kos/sector-publico/sector` y de manera opcional se podrán indicar temas del vocabulario de Temas de datos (DCAT-AP): `http://publications.europa.eu/resource/authority/data-theme` o los temas del registro de temas INSPIRE `http://inspire.ec.europa.eu/theme/`


| dcat:DataService | dct:publisher |
| --- | --- |
| **Metadato** | **Publicador** |
| **Descripción** | Agente, en este caso una organización, responsable de hacer que el Servicio de datos esté disponible. |
| **Propiedad** | **dct:publisher** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **foaf:Agent** |

!!! note "Nota de uso"

    Cada organización se especificará mediante el siguiente patrón de URI:  `http://datos.gob.es/recurso/sector-publico/org/Organismo/{ID-DIR}`  Donde `{ID-DIR}` es el identificador alfanumérico único que diferencia a todas las entidades. En el caso de organismos del sector público éste se encuentra disponible en el Directorio Común de unidades orgánicas y oficinas (DIR3). En el caso de entidades del sector privado, el identificador que a utilizar es el NIF.


| dcat:DataService | dcat:endpointURL |
| --- | --- |
| **Metadato** | **URL de Acceso** |
| **Descripción** | Este metadato proporciona la localización principal del punto de acceso al servicio de datos. |
| **Propiedad** | **dcat:endpointURL** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se indicará la localización raíz o punto de acceso primario (un IRI resoluble web) del servicio de datos.


| dcat:DataService | dcat:endpointDescription |
| --- | --- |
| **Metadato** | **Descripción del punto de acceso** |
| **Descripción** | Proporciona detalles sobre las características y capacidades disponibles en el punto de acceso del servicio de datos. Esto incluye información sobre las operaciones, parámetros y otras características técnicas del servicio. |
| **Propiedad** | **dcat:endpointDescription** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Es posible expresar la descripción de dos formas, siendo preferente la primera:

    1. en formato legible por máquina, ajustando la URI que referencia alguna de las siguientes alternativas:

      * descripción [OpenAPI](https://www.openapis.org/) (Swagger)
      * respuesta OGC GetCapabilities ([WFS](http://www.opengeospatial.org/standards/wfs)) o ([WMS](http://www.opengeospatial.org/standards/wms)).
      * descripción del servicio [SPARQL](https://www.w3.org/TR/sparql11-service-description/)
    
    2. documento [OpenSearch](https://github.com/dewitt/opensearch/blob/master/opensearch-1-1-draft-6.md), [WSDL 2.0](https://www.w3.org/TR/wsdl20/) o descripción de la API [Hydra](https://www.hydra-cg.com/spec/latest/core/) u otras alternativas autodescriptivas legibles por máquina.
    
    3. un recurso web que referencie un documento en formato texto o algún otro modo informal.


| dcat:DataService | dcat:servesDataset |
| --- | --- |
| **Metadato** | **Conjunto de datos** |
| **Descripción** | Este metadato indica el vínculo existente entre un servicio de datos y uno o varios conjuntos de datos, es decir, la colección de datos que el servicio puede distribuir. |
| **Propiedad** | **dcat:servesDataset** |
| **Aplicabilidad** | **Recomendado** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **dcat:Dataset** |

!!! note "Nota de uso"

    Se debe referenciar cada dataset que el servicio de datos distribuye.  Conviene tener en cuenta que diferentes servicios de datos pueden servir un mismo dataset.


| dcat:DataService | dct:description |
| --- | --- |
| **Metadato** | **Descripción** |
| **Descripción** | Descripción que ofrece un resumen claro del propósito y alcance del servicio de datos. |
| **Propiedad** | **dct:description** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    Se debe especificar un literal. La descripción debe ser clara y concisa, pero a la vez suficientemente detallada para que los usuarios entiendan el propósito del servicio de datos.  Esta propiedad puede ser repetida para expresar la descripción en diferentes idiomas.


| dcat:DataService | dct:accessRights |
| --- | --- |
| **Metadato** | **Derechos de acceso** |
| **Descripción** | Contiene una declaración acerca de las posibles restricciones de acceso, políticas de seguridad, privacidad u otras condiciones relevantes que afectan la forma en que se interactúa con el servicio de datos. |
| **Propiedad** | **dct:accessRights** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:RightsStatement** |

!!! note "Nota de uso"

    Se debe ajustar uno de los valores del vocabulario:  `http://publications.europa.eu/resource/authority/access-right`


| dcat:DataService | dct:license |
| --- | --- |
| **Metadato** | **Términos de uso** |
| **Descripción** | Especifica la licencia o condiciones de reutilización del servicio de datos. Informa a los usuarios sobre los derechos y obligaciones asociados a su uso. |
| **Propiedad** | **dct:license** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:LicenseDocument** |

!!! note "Nota de uso"

    Se debe incluir una URI que enlace directamente al documento o recurso online que detalla los términos y condiciones de uso del catálogo. Se recomienda el uso de licencias tipo mediante el vocabulario `http://publications.europa.eu/resource/authority/licence` que permite describir dichas condiciones, asegurando así una interpretación y aplicación coherente de las normas de uso y reutilización de los datos. En el caso de datos de alto valor (HVD) la propiedad debe ajustarse especificando el tipo de `http://publications.europa.eu/resource/authority/licence/CC_BY_4_0` (licencia CC-BY 4.0), u otra más permisiva. Alternativamente, se podrá referenciar un documento de licencia mediante una URL del texto legal que el publicador determine.

| dcat:DataService | dcat:keyword |
| --- | --- |
| **Metadato** | **Etiqueta** |
| **Descripción** | Permite asignar una o más palabras clave o etiquetas a un conjunto de datos, para categorizarlo libremente. Las etiquetas son términos simples y breves o frases cortas que describen el contenido y el contexto del conjunto de datos. Facilitan la búsqueda y categorización del conjunto de datos, mejorando su descubrimiento y accesibilidad. |
| **Propiedad** | **dcat:keyword** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica compacta.** |

!!! note "Nota de uso"

    Se recomienda elegir cuidadosamente las etiquetas para reflejar de manera precisa el contenido, ámbito y propósito del conjunto de datos para ayudar a los usuarios a identificar y localizar conjuntos de datos de interés y establecer relaciones con otros elementos similares.  Es conveniente etiquetar de forma homogénea, aplicando reglas y criterios normalizados y válidos ortográficamente.  Se permite que los términos sean texto libre, aunque se recomienda utilizar únicamente los incluidos en un conjunto de términos cerrado (vocabulario, taxonomía, tesauro, etc.) como puede ser [Eurovoc](https://eur-lex.europa.eu/browse/eurovoc.html).


## Metadatos de la clase Conjunto de datos {#dcat-dataset}

La clase Conjunto de datos (`dcat:Dataset`) representa una conceptualización que expresa una colección de información estructurada. Estos conjuntos son publicados por una entidad y están destinados a ser consumidos o utilizados por actores o aplicaciones.

Esta clase es una de las clases fundamentales en repositorios y catálogos, ya que proporcionan identificación, acceso y reutilización de información.

!!! warning "Importante"
    Para la descripción de **datos de alto valor (HVD) se deberán añadir**, a las ya obligatorias, la **legislación aplicable** (`dcatap:applicableLegislation`), **categoría HVD** (`dcatap:hvdCategory`) y deberán añadirse **distribuciones** (`dcat:distribution`).

| dcat:Dataset | dct:title |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Breve título o nombre dado al conjunto de datos. |
| **Propiedad** | **dct:title** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal.** Cadena alfanumérica. |

!!! note "Nota de uso"

    Se debe especificar un literal conciso. Se recomienda no incluir en el nombre ninguna referencia temporal o geográfica dado que este tipo de información debe expresarse mediante las propiedades específicas cobertura espacial (`dct:spatial`) y temporal (`dct:temporal`). Esta propiedad puede ser repetida para expresar el nombre en diferentes idiomas.


| dcat:Dataset | dct:description |
| --- | --- |
| **Metadato** | **Descripción** |
| **Descripción** | Descripción que ofrece un resumen claro del contenido del conjunto de datos proporcionando una visión general rápida y eficaz del recurso de información. |
| **Propiedad** | **dct:description** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal.** Cadena alfanumérica. |

!!! note "Nota de uso"

    Se debe especificar un literal. Esta propiedad puede ser repetida para expresar la descripción en diferentes idiomas.


| dcat:Dataset | dct:publisher |
| --- | --- |
| **Metadato** | **Publicador** |
| **Descripción** | Agente, en este caso una organización, responsable de hacer que el conjunto de datos esté disponible. |
| **Propiedad** | **dct:publisher** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **foaf:Agent** |

!!! note "Nota de uso"

    Cada organización se especificará mediante el siguiente patrón de URI:  `http://datos.gob.es/recurso/sector-publico/org/Organismo/{ID-DIR}`  Donde `{ID-DIR}` es el identificador alfanumérico único que diferencia a todas las entidades. En el caso de organismos del sector público éste se encuentra disponible en el Directorio Común de unidades orgánicas y oficinas (DIR3). En el caso de entidades del sector privado, el identificador que a utilizar es el NIF.


| dcat:Dataset | dcat:theme |
| --- | --- |
| **Metadato** | **Temática** |
| **Descripción** | Este metadato identifica la temática o materia principal del conjunto de datos. Sirve para categorizar los datos según su contenido conforme a una clasificación cerrada, facilitando su búsqueda y localización. |
| **Propiedad** | **dcat:theme** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se ajustará utilizando uno o varios de los temas de las clasificaciones taxonómicas que se indican en la clase Catálogo mediante el metadato temáticas (`dcat:themeTaxonomy`). Cada uno de los temas se designará referenciando la URI asociada a la categoría correspondiente de la taxonomía.  Se deben utilizar obligatoriamente temas de la taxonomía de sectores primaros definida en el vocabulario `http://datos.gob.es/kos/sector-publico/sector` y de manera opcional se podrán indicar temas del vocabulario de Temas de datos (DCAT-AP): `http://publications.europa.eu/resource/authority/data-theme` o los temas del registro de temas INSPIRE `http://inspire.ec.europa.eu/theme/`


| dcat:Dataset | dcatap:applicableLegislation |
| --- | --- |
| **Metadato** | **Legislación aplicable** |
| **Descripción** | Referencia a la legislación aplicable, sí contiene datos de alto valor, entonces debe indicarse al menos el [Reglamento de Implementación 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj) |
| **Propiedad** | **dcatap:applicableLegislation** |
| **Aplicabilidad** | **Recomendado** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **eli:LegalResource** |

!!! note "Nota de uso"

    Se debe proporcionar como mínimo el ELI del reglamento: `http://data.europa.eu/eli/reg_impl/2023/138/oj`. Dado que la disponibilidad del HVD puede estar regulada por múltiples normativas específicas del dato, la cardinalidad máxima no está limitada.


| dcat:Dataset | dcatap:hvdCategory |
| --- | --- |
| **Metadato** | **Categoría de HVD** |
| **Descripción** | Referencia la categoría de dato de alto valor con la que se vincula el conjunto de datos que se describe según el [reglamento de implementación 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj). |
| **Propiedad** | **dcatap:hvdCategory** |
| **Aplicabilidad** | **Opcional** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se debe proporcionar, al menos, un valor de la taxonomía: <http://publications.europa.eu/resource/dataset/high-value-dataset-category>


| dcat:Dataset | dcat:distribution |
| --- | --- |
| **Metadato** | **Distribución** |
| **Descripción** | Vincula el dataset a las distribuciones disponibles |
| **Propiedad** | **dcat:distribution** |
| **Aplicabilidad** | **Recomendado** - **Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - **Sí es HVD: 1..n** |
| **Rango** | **dcat:Distribution** |

!!! note "Nota de uso"

    Normalmente, un dataset puede tener diferentes representaciones de los datos, en diferentes formatos, disponibles para su descarga como distribuciones de este. Hay ocasiones en las que el dataset simplemente es la referencia a la colección de datos que es servida por un servicio de datos. Para indicar representaciones descargables de datos, se deben proporcionar referencias precisas de cada distribución utilizando identificadores únicos o URI.


| dcat:Dataset | dcat:keyword |
| --- | --- |
| **Metadato** | **Etiqueta** |
| **Descripción** | Permite asignar una o más palabras clave o etiquetas a un conjunto de datos, para categorizarlo libremente. Las etiquetas son términos simples y breves o frases cortas que describen el contenido y el contexto del conjunto de datos. Facilitan la búsqueda y categorización del conjunto de datos, mejorando su descubrimiento y accesibilidad. |
| **Propiedad** | **dcat:keyword** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica compacta.** |

!!! note "Nota de uso"

    Se recomienda elegir cuidadosamente las etiquetas para reflejar de manera precisa el contenido, ámbito y propósito del conjunto de datos para ayudar a los usuarios a identificar y localizar conjuntos de datos de interés y establecer relaciones con otros elementos similares.  Es conveniente etiquetar de forma homogénea, aplicando reglas y criterios normalizados y válidos ortográficamente.  Se permite que los términos sean texto libre, aunque se recomienda utilizar únicamente los incluidos en un conjunto de términos cerrado (vocabulario, taxonomía, tesauro, etc.) como puede ser [Eurovoc](https://eur-lex.europa.eu/browse/eurovoc.html).


| dcat:Dataset | dcat:contactPoint |
| --- | --- |
| **Metadato** | **Punto de contacto** |
| **Descripción** | Proporciona la información de contacto que se puede utilizar para enviar comentarios sobre el conjunto de datos. |
| **Propiedad** | **dcat:contactPoint** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **vcard:Kind** |

!!! note "Nota de uso"

    La información de contacto para para el conjunto de datos se puede expresar utilizando las propiedades de la [ontología vCard](https://www.w3.org/TR/vcard-rdf/). Se recomienda especialmente el siguiente subconjunto de propiedades:

    | Propiedad     |                   Descripción       |
    | :-------------------- | :----------------------------------------------------- |
    | `vcard:fn`            | Nombre                                                 |
    | `vcard:hasUid`        | Identificador del organismo                            |
    | `vcard:fn`            | Denominación de área o persona                         |
    | `vcard:hasEmail`      | Dirección de correo electrónico                         |
    | `vcard:hasTelephone`  | Número de teléfono                                      |
    | `vcard:hasURL`        | Enlace al formulario de contacto (recomendado) o al sitio web |


| dcat:Dataset | dct:temporal |
| --- | --- |
| **Metadato** | **Cobertura temporal** |
| **Descripción** | Define el período de tiempo que cubre el conjunto de datos. |
| **Propiedad** | **dct:temporal** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:PeriodOfTime** |

!!! note "Nota de uso"

    Se ajusta utilizando las propiedades de la clase Período temporal (`dct:PeriodOfTime`). Se recomienda incluir un intervalo de tiempo, definido por inicio y fin como fecha o instante temporal. Si se usa fecha para el inicio, debería usarse fecha como fin (ídem para instante temporal) y siempre emparejados, evitando los intervalos abiertos.


| dcat:Dataset | dct:spatial |
| --- | --- |
| **Metadato** | **Cobertura geográfica** |
| **Descripción** | Específica el área geográfica a la que se circunscriben o son relevantes los datos del conjunto de datos. |
| **Propiedad** | **dct:spatial** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se recomienda especificar la región o área geográfica utilizando alguno de los siguientes métodos:
    
    1. preferentemente un vocabulario o nomenclátor geográfico, para garantizar una descripción normalizada del ámbito territorial. Para ello, la cobertura geográfica se puede expresar mediante cualquiera de los siguientes: 

       1. `http://datos.gob.es/es/recurso/sector-publico/territorio`
       2. `http://publications.europa.eu/resource/authority/continent`
       3. `http://publications.europa.eu/resource/authority/country`
       4. `http://publications.europa.eu/resource/authority/atu`
       5. `http://publications.europa.eu/resource/authority/place/`
       6. `http://sws.geonames.org/`

    2.  Como alternativa, es posible delimitar el área geográfica utilizando las propiedades de la clase [`dct:Location`](#localización---clase-dctlocation---opcional).


| dcat:Dataset | dct:identifier |
| --- | --- |
| **Metadato** | **Identificador** |
| **Descripción** | El identificador es la propiedad que permite la identificación única e inequívoca del conjunto de datos. |
| **Propiedad** | **dct:identifier** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal.** |

!!! note "Nota de uso"

    El uso de esta propiedad es apropiado para indicar el identificador principal del dataset. Es posible ajustar otros identificadores utilizando la propiedad *"Otro Identificador"* (`adms:identifier`). El identificador podría ser parte de la URI del conjunto de datos, pero por sí mismo debería ser significativo y proporcionar una referencia única y no ambigua dentro de un contexto determinado. Este identificador debería ser persistente en el tiempo ante futuros cambios del conjunto de datos.


| dcat:Dataset | adms:identifier |
| --- | --- |
| **Metadato** | **Otro Identificador** |
| **Descripción** | Metadato que expresa un identificador secundario del conjunto de datos cuyo propósito es referenciarlo de manera única e inequívoca. |
| **Propiedad** | **adms:identifier** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **adms:Identifier** |

!!! note "Nota de uso"

    Se recomienda expresar mediante un literal de tipo URI de uno de los patrones posibles del [esquema de identificadores de recursos Datacite](http://purl.org/spar/datacite/ResourceIdentifierScheme). Entre otros, [DOI](http://purl.org/spar/datacite/doi), [URI](http://purl.org/spar/datacite/uri), [URN](http://purl.org/spar/datacite/urn) o [ISBN](http://purl.org/spar/datacite/isbn).


| dcat:Dataset | dct:creator |
| --- | --- |
| **Metadato** | **Autor** |
| **Descripción** | Especifica la organización responsable de la creación del conjunto de datos. |
| **Propiedad** | **dct:creator** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **foaf:Agent** |

!!! note "Nota de uso"

    Para su especificación se deben usar las propiedades de la clase Agent (explicada más adelante en este documento).  Es recomendable indicar el autor del conjunto de datos para proporcionar claridad sobre la fuente y responsabilidad del contenido, así como una correcta atribución y reconocimiento.


| dcat:Dataset | foaf:page |
| --- | --- |
| **Metadato** | **Documentación** |
| **Descripción** | Proporciona la referencia a un documento que contiene información relevante sobre el conjunto de datos. |
| **Propiedad** | **foaf:page** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **foaf:Document** |

!!! note "Nota de uso"

    Se recomienda incluir enlaces a recursos documentales que proporcionen a los usuarios un contexto más amplio y una mejor comprensión del conjunto de datos. Estos recursos pueden incluir detalles sobre la metodología utilizada, limitaciones de los datos, guías y condiciones de uso, etc.


| dcat:Dataset | dcat:landingPage |
| --- | --- |
| **Metadato** | **Sitio Web** |
| **Descripción** | Referencia a una página web que proporciona acceso al conjunto de datos, sus distribuciones e información adicional. |
| **Propiedad** | **dcat:landingPage** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **foaf:Document** |

!!! note "Nota de uso"

    Este metadato se debe utilizar para incluir la URL que referencia a la página del proveedor original del conjunto de datos y no un tercero como, por ejemplo, un agregador.


| dcat:Dataset | adms:sample |
| --- | --- |
| **Metadato** | **Muestra** |
| **Descripción** | Parte representativa o ejemplo del conjunto de datos. |
| **Propiedad** | **adms:sample** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Distribution** |

!!! note "Nota de uso"

    Este metadato es útil para proporcionar una vista previa de los datos contenidos en el conjunto de datos completo. No es posible modelarlo como una distribución ya que ésta debe ser completa para el conjunto de datos.


| dcat:Dataset | dct:conformsTo |
| --- | --- |
| **Metadato** | **Estándar** |
| **Descripción** | Determina las especificaciones, normas o estándares a los que se ajusta el conjunto de datos. |
| **Propiedad** | **dct:conformsTo** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:Standard** |

!!! note "Nota de uso"

    Se recomienda utilizar este metadato para indicar las especificaciones técnicas que cumple el dataset. Esto puede incluir referencias a estándares de datos, esquemas de metadatos, protocolos de comunicación, formatos de archivo, etc.  La representación de esta propiedad debe hacerse mediante una URI que enlace al estándar o especificación correspondiente.  En el caso de que sea normativa recogida en la legislación europea, debería utilizarse el identificador ELI correspondiente.


| dcat:Dataset | dct:issued |
| --- | --- |
| **Metadato** | **Fecha de creación** |
| **Descripción** | Fecha en la que se generó o publicó por primera vez el conjunto de datos. |
| **Propiedad** | **dct:issued** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Dataset | dct:modified |
| --- | --- |
| **Metadato** | **Fecha de actualización** |
| **Descripción** | Fecha en la que se realizó el último cambio en el conjunto de datos, con el fin de asegurar que los usuarios acceden a la versión más actualizada. |
| **Propiedad** | **dct:modified** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Dataset | dct:type |
| --- | --- |
| **Metadato** | **Tipo** |
| **Descripción** | Categorización del conjunto de datos. |
| **Propiedad** | **dct:type** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se recomienda utilizar un vocabulario que permita expresar mediante URI el tipo de conjunto de datos que se describe. Preferentemente se utilizará el vocabulario: `http://publications.europa.eu/resource/authority/dataset-type` que permite categorizar diferentes tipos de conjuntos de datos. Los conjuntos de datos espaciales también pueden categorizarse mediante la URI `http://inspire.ec.europa.eu/metadata-codelist/ResourceType/dataset`.


| dcat:Dataset | dct:language |
| --- | --- |
| **Metadato** | **idioma** |
| **Descripción** | Especifica el idioma utilizado para los metadatos textuales (es decir, títulos, descripciones, palabras clave, etc.) que describen el dataset y/o el idioma que se utiliza en los valores textuales de la o las distribuciones del conjunto de datos. |
| **Propiedad** | **dct:language** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:LinguisticSystem** |

!!! note "Nota de uso"

    Esta propiedad se puede repetir si los metadatos se proporcionan en varios idiomas, pero _uno de los idiomas utilizado para los metadatos textuales debe ser español_.  Se ha actualizado respecto de la propiedad `dc:language` [que se usaba en NTI-RISP](https://datosgobes.github.io/NTI-RISP/#catalogo_-_clase_dcatcatalog_-_obligatorio).  Se debe usar el vocabulario normalizado de idiomas:  `http://publications.europa.eu/resource/authority/language`  Complementariamente, es recomendable el uso del atributo xml:lang ajustado con el valor correspondiente para expresar literales en cada idioma especificado en la propiedad. Para ello, se recomienda usar los códigos de idioma normalizados definidos en el [RFC-5646](https://www.rfc-editor.org/rfc/rfc5646.html) (por ejemplo, `es` para español, `en` para inglés, `ca` para catalán, `eu` para vasco, `gl` para gallego, etc.).  Los valores ajustados en esta propiedad de dataset anulan los valores proporcionados para el catálogo si entran en conflicto.
    
    Por otro lado, se prevé un segundo uso de esta propiedad: si las distribuciones de un conjunto de datos están disponibles para cada idioma por separado, se debe definir una instancia de `dcat:Distribution` para cada idioma y describir el idioma específico de cada distribución usando `dct:language`. Es decir, el conjunto de datos tendrá múltiples valores de `dct:language` y cada distribución tendrá solo un valor de la propiedad `dct:language`. En el caso de distribuciones multilingües, éstas tendrán múltiples valores `dct:language`.


| dcat:Dataset | dct:accrualPeriodicity |
| --- | --- |
| **Metadato** | **Frecuencia de actualización** |
| **Descripción** | Describe la periodicidad con la que se actualiza el conjunto de datos. |
| **Propiedad** | **dct:accrualPeriodicity** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:Frequency** |

!!! note "Nota de uso"

    Se recomienda usar conceptos del vocabulario estandarizado:  [`http://publications.europa.eu/resource/authority/frequency`](http://publications.europa.eu/resource/authority/frequency)


| dcat:Dataset | dcat:version |
| --- | --- |
| **Metadato** | **Versión** |
| **Descripción** | Especifica la versión del conjunto de datos. |
| **Propiedad** | **dcat:version** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    Se utiliza para proporcionar información sobre la versión del conjunto de datos cuando éste se actualiza o modifica con el tiempo. El detalle de la información puede incluir un número de versión o cualquier otra política de denominación de versiones. Se recomienda que sea independientemente de un idioma concreto.


| dcat:Dataset | adms:versionNotes |
| --- | --- |
| **Metadato** | **Notas de versión** |
| **Descripción** | Proporciona detalles adicionales sobre la diferencia entre esta versión del conjunto de datos y versiones anteriores del mismo. |
| **Propiedad** | **adms:versionNotes** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal** |
****
!!! note "Nota de uso"

    Se recomienda que se detallen las diferencias con la versión inmediatamente anterior. Puede incluirse esta descripción en varios idiomas.


| dcat:Dataset | dcat:hasVersion |
| --- | --- |
| **Metadato** | **Tiene versión** |
| **Descripción** | Referencia a otro conjunto de datos que es una versión, edición o adaptación del conjunto de datos que se describe. |
| **Propiedad** | **dcat:hasVersion** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Dataset** |

!!! note "Nota de uso"

    Se recomienda incluir la referencia clara y precisa al dataset versionado, idealmente utilizando identificadores únicos o URIs. Su propiedad inversa es dcat:isVersionOf


| dcat:Dataset | dcat:isVersionOf |
| --- | --- |
| **Metadato** | **Es versión de** |
| **Descripción** | Referencia a otro conjunto de datos del cual, el que se describe, es una versión, edición o adaptación. |
| **Propiedad** | **dcat:isVersionOf** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Dataset** |

!!! note "Nota de uso"

    Se recomienda incluir la referencia clara y precisa al dataset versionado, idealmente utilizando identificadores únicos o URIs. Su propiedad inversa es dcat:hasVersion.


| dcat:Dataset | dcat:qualifiedRelation |
| --- | --- |
| **Metadato** | **Relación** |
| **Descripción** | Especifica un vínculo a una descripción de una relación específica entre el conjunto de datos que se describe y otros recursos de datos. |
| **Propiedad** | **dcat:qualifiedRelation** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Relationship** |

!!! note "Nota de uso"

    Se utiliza para especificar vínculos entre recursos donde se conoce la naturaleza de la relación pero no coincide con una de las propiedades estándar contempladas en el vocabulario [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) (como [dct:hasPart](http://purl.org/dc/terms/hasPart), [dct:isPartOf](http://purl.org/dc/terms/isPartOf), [dct:conformsTo](http://purl.org/dc/terms/conformsTo),[dct:isVersionOf](http://purl.org/dc/terms/isVersionOf), [dct:hasVersion](http://purl.org/dc/terms/hasVersion), [dct:replaces](http://purl.org/dc/terms/replaces), [dct:isReplacedBy](http://purl.org/dc/terms/isReplacedBy), [dct:references](http://purl.org/dc/terms/references), [dct:isReferencedBy](http://purl.org/dc/terms/isReferencedBy), [dct:requires](http://purl.org/dc/terms/requires), [dct:isRequiredBy](http://purl.org/dc/terms/isRequiredBy), entre otras) o las propiedades del vocabulario para especificar procedencia [PROV-O](https://www.w3.org/TR/vocab-dcat/#bib-prov-o) (como [prov:wasDerivedFrom](https://www.w3.org/TR/prov-o/#wasDerivedFrom), [prov:wasInfluencedBy](https://www.w3.org/TR/prov-o/#wasInfluencedBy), [prov:wasQuotedFrom](https://www.w3.org/TR/prov-o/#wasQuotedFrom), [prov:wasRevisionOf](https://www.w3.org/TR/prov-o/#wasRevisionOf), [prov:hadPrimarySource](https://www.w3.org/TR/prov-o/#hadPrimarySource), [prov:alternateOf](https://www.w3.org/TR/prov-o/#alternateOf), [prov:specializationOf](https://www.w3.org/TR/prov-o/#specializationOf)).  Una forma de especificar relaciones alternativas entre recursos es utilizando la especificación: <https://www.iana.org/assignments/link-relations/>


| dcat:Dataset | dcat:spatialResolutionInMeters |
| --- | --- |
| **Metadato** | **Resolución Espacial** |
| **Descripción** | Refiere a la mínima distancia entre dos datos distintos que el conjunto de datos puede distinguir, medida en metros. |
| **Propiedad** | **dcat:spatialResolutionInMeters** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal de tipo xsd:decimal o xsd:double** |

!!! note "Nota de uso"

    Se aplica principalmente para conjunto de datos geoespaciales y refleja la granularidad y el nivel de detalle. El valor se asume que será siempre positivo. En el caso de mallas (grid) o imágenes, corresponde con la distancia entre dos puntos, y en otros datasets geoespaciales es la distancia mínima entre elementos.


| dcat:Dataset | dcat:temporalResolution |
| --- | --- |
| **Metadato** | **Resolución Temporal** |
| **Descripción** | Refiere el intervalo de tiempo mínimo entre dos registros de datos consecutivos dentro del conjunto de datos. |
| **Propiedad** | **dcat:temporalResolution** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal de tipo xsd:duration** |

!!! note "Nota de uso"

    Se recomienda proporcionar este metadato en conjuntos de datos que se actualizan o capturan a intervalos regulares, como datos meteorológicos, datos de tráfico en tiempo real o cualquier otro tipo de datos que se registren a lo largo del tiempo.  Esta duración debe seguir el formato ISO-8601 (P si contiene detalle de fecha sin hora o PT si contiene detalle de tiempo horario).  Por ejemplo, se pueden utilizar valores como “PT1S” (segundos), “PT1M” (minutos), “PT1H” (horas), "P1D" (diario), "P1W" (semanal), "P1M" (mensual), "P1Y" (anual).


| dcat:Dataset | dct:isReferencedBy |
| --- | --- |
| **Metadato** | **Referenciado por** |
| **Descripción** | Este metadato identifica otros recursos web que hacen referencia o citan al conjunto de datos que se describe. |
| **Propiedad** | **dct:isReferencedBy** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    En el caso de otras relaciones que no sean una cita o vinculo al conjunto de datos, se recomienda utilizar la propiedad genérica dcat:qualifiedRelation.


| dcat:Dataset | dct:provenance |
| --- | --- |
| **Metadato** | **Procedencia** |
| **Descripción** | Contiene una declaración sobre el linaje del dataset. El objetivo es aportar información relevante para que los usuarios comprendan de dónde provienen los datos y cómo pueden haberse modificado a lo largo del tiempo. |
| **Propiedad** | **dct:provenance** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:ProvenanceStatement** |

!!! note "Nota de uso"

    Se recomienda especificar cualquier cambio en la propiedad o custodia que sea significativo para verificar la autenticidad, integridad e interpretación del dataset. Es aconsejable utilizar la [ontología PROV-O](https://www.w3.org/TR/prov-o/), si bien una descripción en texto libre también es aceptada.


| dcat:Dataset | dct:relation |
| --- | --- |
| **Metadato** | **Recurso relacionado** |
| **Descripción** | Especifica recursos que están de alguna manera relacionados con el conjunto de datos. |
| **Propiedad** | **dct:relation** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se debe utilizar esta propiedad cuando la naturaleza de la relación entre un elemento catalogado y los recursos relacionados no es conocida; en caso de que sí sea conocida, debería utilizarse otras propiedades más específicas como dct:hasPart, dct:hasVesion, entre otras.


| dcat:Dataset | prov:qualifiedAttribution |
| --- | --- |
| **Metadato** | **Atribución** |
| **Descripción** | Agentes (personas, organizaciones o entidades) que tienen algún tipo de responsabilidad o una contribución significativa sobre el conjunto de datos. |
| **Propiedad** | **prov:qualifiedAttribution** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **prov:Attribution** |

!!! note "Nota de uso"

    Se debe utilizar cuando la naturaleza de la relación entre Agente y conjunto de datos es conocida, pero no encaja con ninguno de los roles específicos (`dct:creator`, `dct:publisher`). Se recomienda utilizar además la propiedad `dcat:hadRole` para especificar la responsabilidad del Agente respecto al recurso.


| dcat:Dataset | prov:wasGeneratedBy |
| --- | --- |
| **Metadato** | **Generador** |
| **Descripción** | Referencia a la actividad, proceso o contexto de negocio que propició la creación del conjunto de datos. |
| **Propiedad** | **prov:wasGeneratedBy** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **prov:Activity** |

!!! note "Nota de uso"

    La actividad asociada a la creación de un dataset, habitualmente parte de alguna iniciativa, proyecto, encuesta, etc. Que da lugar a la generación del conjunto de datos. Pueden incluirse múltiples elementos con diferente nivel de detalle.


| dcat:Dataset | dct:source |
| --- | --- |
| **Metadato** | **Origen** |
| **Descripción** | Identifica el dataset original o fuente primaria del que deriva el conjunto de datos que se describe. |
| **Propiedad** | **dct:source** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:Dataset** |

!!! note "Nota de uso"

    Esta propiedad suele estar relacionada con dct:provenance. No implica que la fuente primaria sea necesariamente un conjunto de datos preexistente.


| dcat:Dataset | dct:accessRights |
| --- | --- |
| **Metadato** | **Derechos de acceso** |
| **Descripción** | Especifica una declaración acerca de las posibles restricciones de acceso, políticas de seguridad, privacidad u otras condiciones relevantes que afectan a la forma en que se interactúa con el conjunto de datos. |
| **Propiedad** | **dct:accessRights** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:RightsStatement** |

!!! note "Nota de uso"

    En general, se utiliza para informar acerca de la condición del dataset, si son datos abiertos, tiene restricciones de acceso o no es público. Se debe ajustar usando valores del vocabulario:  `http://publications.europa.eu/resource/authority/access-right`


## Metadatos de la clase Distribución {#dcat-distribution}

La clase Distribución de un conjunto de datos (`dcat:Distribution`), modela diferentes formas o representaciones específicas de un conjunto de datos. Esta clase permite especificar y describir las diversas maneras en las que un conjunto de datos puede estar disponible, por ejemplo, en diferentes formatos o a través de distintos canales.

Esta entidad se considera clave para entender cómo se puede obtener y utilizar un conjunto de datos específico.

!!! warning "Importante"
    Para la descripción de **datos de alto valor (HVD) se deberá añadir**, a las ya obligatorias, la **legislación aplicable** (`dcatap:applicableLegislation`).

| dcat:Distribution | dcat:accessURL |
| --- | --- |
| **Metadato** | **URL de Acceso** |
| **Descripción** | URL que permite acceder a la distribución. |
| **Propiedad** | **dcat:accessURL** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se utiliza para designar la URL del sitio web que facilita el acceso a la distribución (por ejemplo, mediante formulario web o consulta a una API). La URL puede contener información sobre cómo obtener el dataset.  El valor de esta propiedad debería duplicarse en la propiedad dcat:landingPage de su conjunto de datos asociado.  Esta propiedad debe utilizarse si la distribución no tiene URL directa a la descarga del dataset. Alternativamente, si la URL da acceso directo a la distribución descargable deberá, además, duplicarse en la propiedad dcat:downloadURL.


| dcat:Distribution | dcatap:applicableLegislation |
| --- | --- |
| **Metadato** | **Legislación aplicable** |
| **Descripción** | Referencia a la legislación aplicable, sí distribuye datos de alto valor, entonces debe indicarse al menos el [Reglamento de Implementación 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj) |
| **Propiedad** | **dcatap:applicableLegislation** |
| **Aplicabilidad** | **Recomendado - Sí es HVD: Obligatorio** |
| **Cardinalidad** | **0..n** - Sí es HVD: 1..n |
| **Rango** | **eli:LegalResource** |

!!! note "Nota de uso"

    Se debe proporcionar como mínimo el ELI del reglamento: `http://data.europa.eu/eli/reg_impl/2023/138/oj`. Dado que la disponibilidad del HVD puede estar regulada por múltiples normativas específicas del dato, la cardinalidad máxima no está limitada.


| dcat:Distribution | dct:description |
| --- | --- |
| **Metadato** | **Descripción** |
| **Descripción** | Proporciona un resumen claro del contenido de la distribución aportando una visión general rápida y eficaz del recurso de información. |
| **Propiedad** | **dct:description** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal.** Cadena alfanumérica |

!!! note "Nota de uso"

    Se debe especificar un literal. Esta propiedad puede ser repetida para expresar la descripción en diferentes idiomas.


| dcat:Distribution | dcatap:availability |
| --- | --- |
| **Metadato** | **Disponibilidad** |
| **Descripción** | Estado de la disponibilidad prevista de la distribución del conjunto de datos. |
| **Propiedad** | **dcatap:availability** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se debe usar un concepto del vocabulario controlado `http://publications.europa.eu/resource/authority/planned-availability`


| dcat:Distribution | dct:format |
| --- | --- |
| **Metadato** | **Formato** |
| **Descripción** | Especifica el formato del fichero de la distribución del conjunto de datos. |
| **Propiedad** | **dct:format** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:MediaTypeOrExtent** |

!!! note "Nota de uso"

    Se recomienda utilizar los conceptos definidos en el vocabulario: `http://publications.europa.eu/resource/authority/file-type` Además, si el valor es uno de los definidos por IANA para los *media types,* debe ajustarse la [propiedad formato tipo MIME (`dcat:mediaType`)](#nota-dcat_distribution-dcat_mediatype).


| dcat:Distribution | dct:license |
| --- | --- |
| **Metadato** | **Licencia** |
| **Descripción** | Especifica la licencia o condiciones de reutilización de la distribución del conjunto de datos. Informa a los usuarios sobre los derechos y obligaciones asociados a su uso. |
| **Propiedad** | **dct:license** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:LicenseDocument** |

!!! note "Nota de uso"

    Se debe incluir una URI que enlace directamente al documento o recurso online que detalla los términos y condiciones de uso del catálogo. Se recomienda el uso de licencias tipo mediante el vocabulario `http://publications.europa.eu/resource/authority/licence` que permite describir dichas condiciones, asegurando así una interpretación y aplicación coherente de las normas de uso y reutilización de los datos. En el caso de datos de alto valor (HVD) la propiedad debe ajustarse especificando el tipo de [licencia CC-BY 4.0](http://publications.europa.eu/resource/authority/licence/CC_BY_4_0) u otra más permisiva. Alternativamente, se podrá referenciar un documento de licencia mediante una URL del texto legal que el publicador determine.


| dcat:Distribution | dcat:accessService |
| --- | --- |
| **Metadato** | **Servicio de acceso** |
| **Descripción** | Este metadato indica el servicio de datos que proporciona acceso a la distribución del conjunto de datos. |
| **Propiedad** | **dcat:accessService** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dcat:DataService** |

!!! note "Nota de uso"

    Se debe incluir la referencia al servicio de datos que proporciona acceso a la distribución que se describe


| dcat:Distribution | dct:title |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Breve título o nombre dado a la distribución del conjunto de datos |
| **Propiedad** | **dct:title** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Literal. Cadena alfanumérica** |

!!! note "Nota de uso"

    Se debe especificar un literal conciso. Se recomienda no incluir en el nombre ninguna referencia temporal o geográfica dado que este tipo de información debe expresarse mediante las propiedades específicas cobertura espacial (dct:spatial) y temporal (dct:temporal). Esta propiedad puede ser repetida para expresar el nombre en diferentes idiomas.


| dcat:Distribution | foaf:page |
| --- | --- |
| **Metadato** | **Documentación** |
| **Descripción** | Proporciona la referencia a un documento que contiene información relevante sobre la distribución del conjunto de datos. |
| **Propiedad** | **foaf:page** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **foaf:Document** |

!!! note "Nota de uso"

    Se recomienda incluir enlaces a recursos documentales que proporcionen a los usuarios un contexto más amplio y una mejor comprensión de la distribución de datos. Estos recursos pueden incluir detalles sobre la metodología utilizada, la estructura, las limitaciones, el propósito de la distribución de los datos., etc.


| dcat:Distribution | dcat:mediaType |
| --- | --- |
| **Metadato** | **Formato tipo MIME** |
| **Descripción** | Permite especificar el tipo de medio (MIME) de la distribución del conjunto de datos. |
| **Propiedad** | **dcat:mediaType** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:MediaType** |

!!! note "Nota de uso"

    Se debe expresar tal como se define en el registro oficial de tipos de medios administrado por IANA, si está entre los incluidos en <http://www.iana.org/assignments/media-types/media-types.xhtml>.


| dcat:Distribution | dcat:downloadURL |
| --- | --- |
| **Metadato** | **URL de descarga** |
| **Descripción** | URL que permite la descarga directa de la distribución. |
| **Propiedad** | **dcat:downloadURL** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Las URLs deben ser estables y conducir directamente al archivo de datos en el formato definido, sin requerir pasos adicionales, típicamente mediante una petición HTTP Get. Se recomienda duplicar el valor de esta propiedad como dcat:accessURL.


| dcat:Distribution | dct:conformsTo |
| --- | --- |
| **Metadato** | **Esquema** |
| **Descripción** | Determina la especificación, norma, estándar o modelo de datos al que se ajusta la distribución. |
| **Propiedad** | **dct**:**conformsTo** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:Standard** |

!!! note "Nota de uso"

    Se recomienda utilizar este metadato para indicar las especificaciones técnicas que cumple la distribución. Esto puede incluir referencias a modelos, esquemas, ontologías o perfiles de aplicación con los cuales esta distribución es conforme. El uso preferente es especificar el modelo o estructura de datos subyacente a la distribución.


| dcat:Distribution | dct:issued |
| --- | --- |
| **Metadato** | **Fecha de creación de la distribución** |
| **Descripción** | Fecha en la que se creó o publicó la distribución del conjunto de datos. |
| **Propiedad** | **dct:issued** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Distribution | dct:modified |
| --- | --- |
| **Metadato** | **Fecha de última actualización de la distribución** |
| **Descripción** | Indica la última fecha en que se actualizó o modificó la distribución del conjunto de datos asegurando que los usuarios acceden a la versión más actualizada. |
| **Propiedad** | **dct:modified** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dcat:Distribution | adms:status |
| --- | --- |
| **Metadato** | **Estado** |
| **Descripción** | Permite definir la fase actual del ciclo de vida en la que se encuentra la distribución del conjunto de datos en el momento de su descripción. |
| **Propiedad** | **adms:status** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    El estado de la distribución de un conjunto de datos puede ser alguno de los siguientes: `completa`, `obsoleta`, `en desarrollo` o `retirada`. Estos valores están definidos en el vocabulario:  `http://publications.europa.eu/resource/authority/distribution-status`


| dcat:Distribution | dct:language |
| --- | --- |
| **Metadato** | **Idioma** |
| **Descripción** | Especifica el idioma en el que se encuentra la información contenida en la distribución del conjunto de datos. |
| **Propiedad** | **dct:language** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..n** |
| **Rango** | **dct:LinguisticSystem** |

!!! note "Nota de uso"

    Se ajusta utilizando valores del vocabulario normalizado de idiomas: `http://publications.europa.eu/resource/authority/language`. En el caso de distribuciones multilingües, esta propiedad puede ser ajustada con múltiples valores y no se requiere ningun valor específico ya que hace referencia al idioma de los datos.


| dcat:Distribution | dcat:compressFormat |
| --- | --- |
| **Metadato** | **Formato comprimido** |
| **Descripción** | Define el formato de compresión utilizado para agrupar y comprimir los datos en la distribución, habitualmente para reducir su tamaño. |
| **Propiedad** | **dcat:compressFormat** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:MediaType** |

!!! note "Nota de uso"

    Se debe expresar tal como se define en el registro oficial de tipos de medios administrado por IANA, si está entre los incluidos en <http://www.iana.org/assignments/media-types/media-types.xhtml>.


| dcat:Distribution | dcat:packageFormat |
| --- | --- |
| **Metadato** | **Formato empaquetado** |
| **Descripción** | Este metadato especifica el formato utilizado para agrupar varios archivos de datos en un único fichero para que se descarguen todos juntos. |
| **Propiedad** | **dcat:packageFormat** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:MediaType** |

!!! note "Nota de uso"

    Se debe expresar tal como se define en el registro oficial de tipos de medios administrado por IANA, si está entre los incluidos en <http://www.iana.org/assignments/media-types/media-types.xhtml>.


| dcat:Distribution | dcat:byteSize |
| --- | --- |
| **Metadato** | **Tamaño** |
| **Descripción** | Indica el tamaño total de la distribución del conjunto de datos expresado en bytes. |
| **Propiedad** | **dcat:byteSize** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** habitualmente de tipo **xsd:nonNegativeInteger** |

!!! note "Nota de uso"

    Este metadato ayuda a los usuarios a estimar la capacidad necesaria para las necesidades de almacenamiento y tiempo de descarga.  Es posible incluir un valor aproximado (siempre como número no negativo), por ejemplo: `843636`


| dcat:Distribution | dcat:spatialResolutionInMeters |
| --- | --- |
| **Metadato** | **Resolución espacial** |
| **Descripción** | Refiere a la mínima separación espacial entre dos datos distintos que la distribución puede distinguir, medida en metros. |
| **Propiedad** | **dcat:spatialResolutionInMeters** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal de tipo xsd:decimal o xsd:double** |

!!! note "Nota de uso"

    Se aplica principalmente para distribuciones de conjuntos de datos geoespaciales y refleja la granularidad y el nivel de detalle. El valor se asume que será siempre positivo. En el caso de mallas (grid) o imágenes, corresponde con la distancia entre dos puntos, y en otros datasets geoespaciales es la distancia mínima entre elementos.


| dcat:Distribution | dcat:temporalResolution |
| --- | --- |
| **Metadato** | **Resolución temporal** |
| **Descripción** | Refiere el intervalo de tiempo mínimo entre dos registros de datos consecutivos dentro del conjunto de datos. |
| **Propiedad** | **dcat:temporalResolution** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal de tipo xsd:duration** |

!!! note "Nota de uso"

    Se recomienda proporcionar este metadato en conjuntos de datos que se actualizan o capturan a intervalos regulares, como datos meteorológicos, datos de tráfico en tiempo real o cualquier otro tipo de datos que se registren a lo largo del tiempo.  Esta duración debe seguir el formato ISO-8601 (P si contiene detalle de fecha sin hora o PT si contiene detalle de tiempo horario).  Por ejemplo, se pueden utilizar valores como “PT1S” (segundos), “PT1M” (minutos), “PT1H” (horas), "P1D" (diario), "P1W" (semanal), "P1M" (mensual), "P1Y" (anual).


| dcat:Distribution | spdx:checksum |
| --- | --- |
| **Metadato** | **Control de verificación** |
| **Descripción** | Proporciona un mecanismo de verificación de la integridad del conjunto de datos. Ayuda a asegurar que el contenido de una distribución no haya sido alterado o corrompido durante el proceso de transferencia o almacenamiento. |
| **Propiedad** | **spdx:checksum** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **spdx:Checksum** |

!!! note "Nota de uso"

    En el caso de incluirse, el checksum debe contener la información del algoritmo utilizado y del valor obtenido como resultado en binario hexadecimal (xsd:hexBinary).


| dcat:Distribution | odrl:hasPolicy |
| --- | --- |
| **Metadato** | **Norma ODLR** |
| **Descripción** | Este metadato expresa los derechos y condiciones asociados con el uso de la distribución del conjunto de datos, utilizando el vocabulario de la Open Digital Rights Language (ODRL). |
| **Propiedad** | **odrl:hasPolicy** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **odrl:Policy** |

!!! note "Nota de uso"

    Siempre que se utilice este metadato, su valor se debe ajustar mediante el uso del vocabulario Open Digital Rights Language (ODRL) definido en: <https://www.w3.org/TR/odrl-vocab/>. ODLR es un lenguaje de expresión de políticas para representar declaraciones sobre el uso (es decir, permisos, prohibiciones y obligaciones) de contenidos y servicios.


| dcat:Distribution | dct:rights |
| --- | --- |
| **Metadato** | **Declaración de derechos** |
| **Descripción** | Permite especificar los derechos vinculados con la distribución que se describe. |
| **Propiedad** | **dct:rights** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **dct:RightsStatement** |

!!! note "Nota de uso"

    Mediante esta declaración se especifican los derechos que no están cubiertos por los términos de uso (dct:licence), por ejemplo, derechos de propiedad intelectual. Para ajustar esta propiedad se pueden utilizar propiedades del vocabulario <http://schema.theodi.org/odrs/>.  Es recomendable establecer la licencia y derechos de uso para las distribuciones. En todo caso, nunca debería haber discrepancias entre los derechos de uso de un conjunto de datos y de una de sus distribuciones para que no genere un conflicto legal.


## Metadatos de la clase Agente {#foaf-agent}

La clase Agent (`foaf:Agent`) se utiliza para representar cualquier organización o persona que posee competencias para realizar actuaciones sobre un catálogo y los recursos de datos catalogados.

Su función principal es proporcionar referencias concretas sobre los diferentes actores que pueden intervenir con diferentes roles en la gestión de un catálogo de datos. Los roles posibles son:

* Creador o productor (**dct:creator**): entidad responsable de producir o generar el recurso.
* Publicador (**dct:publisher**): entidad responsable de poner a disposición el recurso en un catálogo de datos.

El agente o entidad podrá ser una organización o una persona. Si el agente es una organización es recomendable el uso de la clase [foaf:Organization](http://xmlns.com/foaf/0.1/Organization) y si se trata de personas, es recomendable el uso de la clase [foaf:Person](http://xmlns.com/foaf/0.1/Person).

Como se indica a continuación, todo agente o entidad debe tener un nombre y es recomendable que se indique de qué tipo de agente se trata.

| foaf:Agent | foaf:name |
| --- | --- |
| **Metadato** | **Nombre** |
| **Descripción** | Identifica el nombre del agente (persona u organización) que ejerce alguno de los roles posibles en el catálogo o los recursos de datos que se describen, |
| **Propiedad** | **foaf:name** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    Es importante proporcionar el nombre completo y preciso del agente para una mejor identificación y atribución. Esta propiedad se puede repetir para diferentes versiones del nombre en diferentes idiomas.


| foaf:Agent | dct:identifier |
| --- | --- |
| **Metadato** | **Identificador** |
| **Descripción** | El identificador es la propiedad que permite la identificación única e inequívoca de un agente. |
| **Propiedad** | **dct:identifier** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal.** |

!!! note "Nota de uso"

    El uso de esta propiedad es apropiado para indicar el identificador principal de un agente. El identificador podrá ser una URI que proporciona una referencia única y no ambigua respecto al agente. Este identificador debería ser persistente en el tiempo.


| foaf:Agent | dct:type |
| --- | --- |
| **Metadato** | **Tipo** |
| **Descripción** | Permite identificar la categoría de entidad en la que se enmarca el agente. |
| **Propiedad** | **dct:type** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se deben utilizar vocabularios controlados o esquemas de clasificación estandarizados para describir el tipo de agente o rol que desempeña de manera coherente y precisa. Se recomienda el uso del vocabulario `http://purl.org/adms/publishertype/1.0`


## Metadatos de la clase Control y verificación de la integridad {#spdx-checksum}

La clase Control y Verificación de recursos de datos (`spdx:Checksum`) se utiliza para especificar el método y el resultado obtenido que se implementa para garantizar la integridad de las distribuciones de conjuntos de datos, es decir, que su contenido no ha sido alterado.. Permite representar el resultado de una variedad de algoritmos de verificación.

| spdx:Checksum | spdx:algorithm |
| --- | --- |
| **Metadato** | **Algoritmo** |
| **Descripción** | Identificador del algoritmo utilizado para verificar la integridad de la distribución del conjunto de datos. |
| **Propiedad** | **spdx:algorithm** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **spdx:checksumAlgorithm\_sha1** |

!!! note "Nota de uso"

    Se recomienda describir el algoritmo utilizado mediante el uso de alguna de los definidos en la [ontología SPDX](http://spdx.org/rdf/spdx-terms-v2.2/#d4e1968).


| spdx:Checksum | spdx:checksumValue |
| --- | --- |
| **Metadato** | **Valor** |
| **Descripción** | Especifica el resultado único generado por el algoritmo utilizado para la verificación de integridad. |
| **Propiedad** | **spdx:checksumValue** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..1** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    El valor del resultado de verificación debe ser único, exacto y se debe expresar codificado en formato hexadecimal.


## Metadatos de la clase Localización {#dct-location}

La clase Localización (`dct:Location`), se emplea para identificar una región geográfica o un lugar . Se puede representar utilizando un vocabulario controlado o mediante la expresión de coordenadas geográficas. Esta clase es importante para determinar el ámbito geográfico de los datos que se describen, como una localidad, una región, un país o un área geográfica específica.

Para su implementación, se pueden utilizar las siguientes propiedades recomendadas u opcionales:

* Para referir un delimitar geográfico rectangular, debe usarse la propiedad `dcat:bbox`.
* Para referir el centro geográfico de un área espacial u otro punto característico, debe usarse la propiedad `dcat:centroid`.
* Para referir una geometría extensa, se recomienda utilizar la propiedad `locn:geometry` para expresar un conjunto de coordenadas que denotan los vértices del área geográfica.

| dct:Location | dcat:bbox |
| --- | --- |
| **Metadato** | **Delimitador rectangular** |
| **Descripción** | Esta propiedad permite especificar el área geográfica determinada por las coordenadas de un delimitador rectangular. |
| **Propiedad** | **dcat:bbox** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    El rango de esta propiedad es genérico (`rdfs:Literal`) para poder expresar la geometría utilizando diferentes codificaciones. Por ejemplo, se puede expresar indicando las coordenadas geográficas (Longitud y Latitud) de las cuatro esquinas que delimitan el rectángulo geográfico.


| dct:Location | dcat:centroid |
| --- | --- |
| **Metadato** | **Centroide** |
| **Descripción** | Esta propiedad permite especificar el punto central de un área geográfica específica |
| **Propiedad** | **dcat:centroid** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    El rango de esta propiedad es genérico (`rdfs:Literal`) para poder expresar la geometría utilizando diferentes codificaciones. Por ejemplo, se puede expresar indicando las coordenadas geográficas (Longitud y Latitud) del punto geográfico.


| dct:Location | locn:geometry |
| --- | --- |
| **Metadato** | **Geometría** |
| **Descripción** | Esta propiedad permite especificar la forma geométrica específica que representa un área geográfica. Puede referir polígonos o o cualquier área irregular que delimite la región geográfica. |
| **Propiedad** | **locn:geometry** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** |

!!! note "Nota de uso"

    El rango de esta propiedad es genérico (`rdfs:Literal`) para poder expresar la geometría utilizando diferentes codificaciones. Por ejemplo, se puede expresar indicando la secuencia de coordenadas geográficas (Longitud y Latitud) que delimitan la región geográfica que se describe.


## Metadatos de la clase Período temporal {#dct-periodoftime}

La clase Período temporal (`dct:PeriodOfTime`) se utiliza para definir un intervalo temporal que se define por sus fechas de inicio y finalización. Se utiliza para ajustar la propiedad cobertura temporal (`dct:temporal`) que abarca el contenido de un conjunto de datos.

Respecto al uso de las propiedades fecha de inicio (`dcat:startDate`) y fecha de finalización (`dcat:endDate`), aunque es recomendado el uso de ambas propiedades, al menos una de las dos debe ser especificada cuando se utiliza una instancia de la clase `dct:PeriodOfTime`.

| dct:PeriodOfTime | dcat:startDate |
| --- | --- |
| **Metadato** | **Fecha de inicio** |
| **Descripción** | Este metadato define la fecha de inicio del intervalo temporal que abarca el contenido de un conjunto de datos. |
| **Propiedad** | **dcat:startDate** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dct:PeriodOfTime | dcat:endDate |
| --- | --- |
| **Metadato** | **Fecha de finalización** |
| **Descripción** | Este metadato especifica la fecha de finalización del período temporal que abarca el contenido de un conjunto de datos. |
| **Propiedad** | **dcat:endDate** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **rdfs:Literal** de tipo **xsd:date** (Fecha), **xsd:dateTime** (Fecha/Hora), **xsd:gYear** (Año) o **xsd:gYearMonth** (Año-Mes) |

!!! note "Nota de uso"

    Se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).


| dct:PeriodOfTime | time:hasBeginning |
| --- | --- |
| **Metadato** | **Comienzo** |
| **Descripción** | Este metadato indica el instante concreto que marca el inicio de un período de tiempo relevante para el conjunto de datos. |
| **Propiedad** | **time:hasBeginning** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **time:Instant** |

!!! note "Nota de uso"

    Se recomienda proporcionar el momento específico de comienzo del período temporal expresando un valor tipificado con alguna de las propiedades que proporciona la [ontología Time](https://www.w3.org/TR/owl-time/#time:Instant) para definir un instante concreto de una línea temporal: 
    
    * [time:inXSDDate](https://www.w3.org/TR/owl-time/#time:inXSDDate)
    * [time::inXSDDateTimeStamp](https://www.w3.org/TR/owl-time/#time:inXSDDateTimeStamp)
    * [time::inXSDgYear](https://www.w3.org/TR/owl-time/#time:inXSDgYear)
    * [time::inXSDgYearMonth](https://www.w3.org/TR/owl-time/#time:inXSDgYearMonth)
    * [time::inTimePosition](https://www.w3.org/TR/owl-time/#time:inTimePosition)
    * [time::inDateTime](https://www.w3.org/TR/owl-time/#time:inDateTime)


| dct:PeriodOfTime | time:hasEnd |
| --- | --- |
| **Metadato** | **Final** |
| **Descripción** | Este metadato indica el instante concreto que marca el final del período de tiempo relacionado con el conjunto de datos. |
| **Propiedad** | **time:hasEnd** |
| **Aplicabilidad** | **Opcional** |
| **Cardinalidad** | **0..1** |
| **Rango** | **time:Instant** |

!!! note "Nota de uso"

    Se recomienda proporcionar el momento específico de finalización del período temporal expresando un valor tipificado con alguna de las propiedades que proporciona la [ontología Time](https://www.w3.org/TR/owl-time/#time:Instant) para definir un instante concreto de una línea temporal: 
    
    * [time:inXSDDate](https://www.w3.org/TR/owl-time/#time:inXSDDate)
    * [time::inXSDDateTimeStamp](https://www.w3.org/TR/owl-time/#time:inXSDDateTimeStamp)
    * [time::inXSDgYear](https://www.w3.org/TR/owl-time/#time:inXSDgYear)
    * [time::inXSDgYearMonth](https://www.w3.org/TR/owl-time/#time:inXSDgYearMonth)
    * [time::inTimePosition](https://www.w3.org/TR/owl-time/#time:inTimePosition)
    * [time::inDateTime](https://www.w3.org/TR/owl-time/#time:inDateTime)


## Metadatos de la clase Relación entre Recursos {#dcat-relationship}

La clase Relación entre Recursos (`dcat:Relationship`), se utiliza para especificar información adicional a una relación entre Recursos DCAT-AP (recursos o agentes) permitiendo así una mayor contextualización sobre cómo estos recursos están interrelacionados.

Este enfoque enriquece la capacidad de describir las relaciones, ofreciendo una flexibilidad ampliada para detallar las características y roles de las conexiones entre recursos de datos y/o agentes dentro del ecosistema de datos.

Se utilizan dos propiedades (`dct:relation` y `dcat:hadRole`) que se declaran obligatoriamente si se implementa una instancia de esta clase.

| dcat:Relationship | dcat:hadRole |
| --- | --- |
| **Metadato** | **Función** |
| **Descripción** | Especifica la función que una entidad o agente ejerce respecto a otra entidad o recurso. |
| **Propiedad** | **dcat:hadRole** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **dcat:Role** |

!!! note "Nota de uso"

    Esta propiedad se puede utilizar para especificar funciones alternativas a las definidas en la clase [`foaf:Agent`](#agente---clase-foafagent---obligatorio) (creador o publicador)). Para ello se puede utilizar uno de los valores del vocabulario controlado de roles de agentes de `http://inspire.ec.europa.eu/metadata-codelist/ResponsiblePartyRole` o [RoleCode-ISO19115](https://standards.iso.org/iso/19115/resources/Codelists/gml/CI_RoleCode.xml).


| dcat:Relationship | dct:relation |
| --- | --- |
| **Metadato** | **Relación** |
| **Descripción** | Especifica el recurso sobre el que se describe la relación. |
| **Propiedad** | **dct:relation** |
| **Aplicabilidad** | **Obligatorio** |
| **Cardinalidad** | **1..n** |
| **Rango** | **rdfs:Resource** |

!!! note "Nota de uso"

    Se debe especificar la referencia a un recurso de datos ([`dcat:Dataset`](#conjunto-de-datos---clase-dcatdataset---obligatorio) o [`dcat:DataService`](#servicio-de-datos---clase-dcatdataservice---opcional)).

Aquí tienes una actualización para la sección de **Documento de licencia** (`dct:LicenseDocument`) siguiendo la referencia de DCAT-AP 3 (sección 7.11):

## Metadatos de la clase Documento de licencia {#dct-licencedocument}

La clase **Documento de licencia** (`dct:LicenseDocument`) representa un documento legal que otorga permiso oficial para hacer algo con un recurso, como reutilizar, compartir o modificar datos.

Se utiliza para describir las condiciones legales bajo las cuales se puede utilizar un recurso, proporcionando claridad sobre los derechos y obligaciones asociados.

| dct:LicenseDocument | dct:type |
| --- | --- |
| **Metadato** | **Tipo** |
| **Descripción** | Permite identificar el tipo de licencia en el que se enmarca el documento. |
| **Propiedad** | **dct:type** |
| **Aplicabilidad** | **Recomendado** |
| **Cardinalidad** | **0..1** |
| **Rango** | **skos:Concept** |

!!! note "Nota de uso"

    Se deben utilizar vocabularios controlados o esquemas de clasificación estandarizados para describir el tipo de documento de licencia. Se recomienda el uso del vocabulario `http://purl.org/adms/licencetype/1.0`

# Conformidad

## DCAT-AP

DCAT-AP-ES se basa en DCAT-AP 2.1.1, y se alinea con las principales restricciones.

## DCAT-AP-ES

### Requisitos del publicador de datos

Un publicador de datos es conforme con DCAT-AP-ES cuando:

1. **Implementación de clases obligatorias**: Implementa todas las clases y propiedades propiedades obligatorias definidas por el modelo.

2. **Coherencia semántica**: Mantiene la coherencia en las descripciones y relaciones entre entidades, asegurando que los metadatos proporcionan una representación precisa y consistente de los recursos. Esto incluye:
   - Uso apropiado de las propiedades según su definición semántica
   - Consistencia entre los valores de las propiedades relacionadas
   - Evitar contradicciones o redundancias en los metadatos
   - Asegurar que las referencias entre recursos son válidas y significativas

3. **Vocabularios controlados**: Utiliza los vocabularios controlados especificados en la sección Vocabularios controlados utilizados en el modelo para todas las propiedades que lo requieran, especialmente aquellas marcadas como obligatorias.

4. **Datos de Alto Valor (HVD)**: Para conjuntos de datos clasificados como HVD, implementa las propiedades adicionales obligatorias para HVD marcadas en el documento.

### Requisitos del catálogo de datos

Un catálogo de datos es conforme con DCAT-AP-ES cuando:

1. **Estructura del catálogo**: Se estructura como una instancia de `dcat:Catalog` que contiene o referencia todas las instancias de `dcat:Dataset` y/o `dcat:DataService`.

2. **Propiedades obligatorias del catálogo**: Implementa todas las propiedades obligatorias de la clase [`dcat:Catalog`](/#catalogo_-_clase_dcatcatalog_-_obligatorio).

3. **Vocabularios controlados**: Utiliza los [vocabularios controlados recomendados por el modelo](/#dcat-ap-es-vocabularies), y particularmente aquellos que son obligatorios para las propiedades descritas.

4. **Federación**: Es capaz de compartir sus metadatos con el [catálogo nacional](https://datos.gob.es/) a través de alguno de los mecanismos de federación soportados.

5. **Consistencia y validación**: Todos los recursos del catálogo cumplen con los requisitos estructurales y semánticos del [modelo DCAT-AP-ES](/#dcat-ap-es-model), y pueden ser [validados utilizando las formas SHACL previstas](/validación).

6. **Metadatos de alto valor (HVD)**: Para los conjuntos de datos de alto valor (HVD), el catálogo proporciona todos los [metadatos adicionales obligatorios según la normativa HVD](##dcat-ap-es-hvd), incluyendo la legislación aplicable y la categoría HVD correspondiente.

7. **Recursos accesibles**: Todas las distribuciones referenciadas en el catálogo son accesibles a través de las URLs proporcionadas, o se indica claramente cuando no lo son mediante las propiedades de disponibilidad y estado apropiadas.

# Anexo 1. Cambios del modelo DCAT-AP-ES respecto del modelo NTI-RISP (v.2013) {#annex-1-nti-risp-to-dcat-ap-es}

A continuación, se detalla la relación de cambios y actualizaciones en los metadatos del modelo DCAT-AP-ES respecto al [modelo de metadatos NTI-RISP (v. 2013)](https://datosgobes.github.io/NTI-RISP), así como la relación de metadatos que han sido deprecados.

## Metadatos incorporados al modelo DCAT-AP-ES
Entre paréntesis se indica si el metadato estaba definido en la NTI-RISP o se ha incorporado de la especificación DCAT-AP-ES:

| Clase | URI de la clase | Obligatorias | Recomendadas | Opcionales |
| --- | --- | --- | --- | --- |
| Catalogo | dcat:Catalog | dct:title (NTI-RISP)  dct:description (NTI-RISP)  dct:publisher (NTI-RISP)  foaf:homepage (NTI-RISP)  dcat:themeTaxonomy (NTI-RISP)  dct:issued (NTI-RISP)  dct:modified (NTI-RISP)  dct:language (DCAT-AP)/dc:language (NTI-RISP)  dct:license (NTI-RISP) | dct:spatial (NTI-RISP)  dcat:dataset (HVD) (NTI-RISP)  dcat:service (HVD) (DCAT-AP) | dcat:catalog (DCAT-AP)  dct:creator (DCAT-AP)  dct:hasPart (DCAT-AP)  dct:isPartOf (DCAT-AP)  dcat:record (HVD) (DCAT-AP)  dct:rights (DCAT-AP) |
| Registro de catálogo | dcat:CatalogRecord | dct:modified (DCAT-AP)  foaf:primaryTopic (HVD) (DCAT-AP) | dct:conformsTo (DCAT-AP)  dct:issued (DCAT-AP) | dct:description (DCAT-AP)  dct:title (DCAT-AP) |
| Servicio de datos | Dcat:DataService | dcat:endpointURL (HVD) (DCAT-AP)  dct:title (DCAT-AP)  dcatap:applicableLegislation (HVD) (DCAT-AP)  dcatap:hvdCategory (HVD) (DCAT-AP)  dcat:contactPoint (HVD) (DCAT-AP)  dcat:servesDataset (HVD) (DCAT-AP)  foaf:page (HVD) (DCAT-AP) dcat:theme (NTI-RISP) dct:publisher (DCAT-AP 3) | dcat:endpointDescription (HVD) (DCAT-AP)  dcat:servesDataset (DCAT-AP) dcatap:applicableLegislation (DCAT-AP) foaf:page (DCAT-AP) dcat:contactPoint (DCAT-AP) | dct:accessRights (HVD) (DCAT-AP)  dct:description (DCAT-AP)  dct:license (HVD) (DCAT-AP) dcat:keyword (DCAT-AP) |
| Conjunto de datos | dcat:Dataset | dct:description (NTI-RISP)  dct:title (NTI-RISP)  dct:publisher (NTI-RISP)  dcat:theme (NTI-RISP)  dcatap:applicableLegislation (HVD) (DCAT-AP)  dcatap:hvdCategory (HVD) (DCAT-AP)  dcat:distribution (HVD) (NTI-RISP) | dcat:contactPoint (HVD) (DCAT-AP)  dcat:distribution (NTI-RISP)  dcat:keyword (NTI-RISP)  dct:spatial (NTI-RISP)  dct:temporal (NTI-RISP)  dct:issued (NTI-RISP)  dct:modified (NTI-RISP) dcatap:applicableLegislation (DCAT-AP) | adms:identifier (DCAT-AP)  adms:sample (DCAT-AP)  adms:versionNotes (DCAT-AP)  dcat:landingPage (DCAT-AP)  dcat:spatialResolutionInMeters (DCAT-AP)  dcat:temporalResolution (DCAT-AP)  dcat:qualifiedRelation (DCAT-AP)  dct:accessRights (DCAT-AP)  dct:accrualPeriodicity (NTI-RISP)  dct:conformsTo (HVD) (NTI-RISP)  dct:creator (DCAT-AP)  dct:hasVersion (DCAT-AP)  dct:isReferencedBy (DCAT-AP)  dct:isVersionOf (DCAT-AP)  dct:identifier (NTI-RISP)  dct:language (DCAT-AP)/dc:language (NTI-RISP)  dct:provenance (DCAT-AP)  dct:relation (NTI-RISP)  dct:source (DCAT-AP)  dct:type (DCAT-AP)  foaf:page (DCAT-AP)  dcat:version (DCAT-AP)  prov:qualifiedAttribution (DCAT-AP)  prov:wasGeneratedBy (DCAT-AP) |
| Distribución | dcat:Distribution | dcat:accessURL (HVD) (NTI-RISP)  dcatap:applicableLegislation (HVD) (DCAT-AP) | dcatap:availability (DCAT-AP)  dct:description (DCAT-AP)  dct:format (DCAT-AP)  dct:license (HVD) (NTI-RISP) dcatap:applicableLegislation (DCAT-AP) | adms:status (DCAT-AP)  dcat:accessService (HVD) (DCAT-AP)  dcat:byteSize (NTI-RISP)  dcat:compressFormat (DCAT-AP)  dcat:downloadURL (DCAT-AP)  dcat:mediaType (NTI-RISP)  dcat:packageFormat (DCAT-AP)  dcat:spatialResolutionInMeters (DCAT-AP)  dcat:temporalResolution (DCAT-AP)  dct:conformsTo (HVD) (DCAT-AP)  dct:issued (DCAT-AP)  dct:language (DCAT-AP)/dc:language (NTI-RISP) (DCAT-AP)  dct:modified (DCAT-AP)  dct:rights (HVD) (DCAT-AP)  dct:title (NTI-RISP)  foaf:page (DCAT-AP)  odrl:hasPolicy (DCAT-AP)  spdx:checksum (DCAT-AP) |
| Agente | foaf:Agent | foaf:name (DCAT-AP) | dct:type (DCAT-AP) dct:identifier (DCAT-AP) |  |
| Contacto | vcard:Kind |  | vcard:hasEmail (HVD) (DCAT-AP)  vcard:hasURL (HVD) (DCAT-AP) |  |
| Checksum | spdx:Checksum | spdx:algorithm (DCAT-AP)  spdx:checksumValue (DCAT-AP) |  |  |
| Localización | dct:Location |  | dcat:bbox (DCAT-AP)  dcat:centroid (DCAT-AP) | locn:geometry (DCAT-AP) |
| Período temporal | dct:PeriodOfTime |  | dcat:startDate (DCAT-AP)  dcat:endDate (DCAT-AP) | time:hasBeginning (DCAT-AP)  time:hasEnd (DCAT-AP) |
| Relación | dcat:Relationship | dct:relation (DCAT-AP)  dcat:hadRole (DCAT-AP) |  |  |


## Elementos de la NTI-RISP (V.2013) obsoletos

A continuación se indican los nombres de los metadatos y las propiedades descritas en el modelo previo NTI-RISP (V. 2013) que están obsoletas o han cambiado en DCAT-AP-ES:

* En la clase Catálogo (**dcat:Catalog**):
  * *Tamaño del catálogo* (`dct:extent`)
  * *Identificador* (`dct:identifier`)

* En la clase Dataset (**dcat:Dataset**):
  * *Condiciones de uso* ( `dct:license`) **[1]**
  * *Vigencia del recurso*: (`dct:valid`)
  * *Recursos relacionados* (`dct:references`)

* En la clase Distribución (**dcat:Distribution**):
  * *Información adicional sobre el formato* (`dct:relation`) **[2]**
  * *Identificador* (`dct:identifier`)
  * *Formato* (`dcat:mediaType`) **[3]**

**[1]** La propiedad `dct:license` desaparece de la clase Dataset y se incorpora a la clase Distribution.

**[2]** La propiedad `dct:relation` desaparece de la clase Distribution y se incorpora a la clase Dataset, aunque con una función diferente a la descrita en la NTI-RISP (V. 2013). En este modelo de metadatos se utiliza para especificar recursos que están de alguna manera relacionados con el conjunto de datos.

**[3]** En DCAT-AP-ES la propiedad de formato se divide en varias, más especificamente se añade la propiedad "Formato" (`dct:format`) y se distingue del "Formato tipo MIME" (`dcat:mediaType`, qué era "Formato" en el anterior modelo). Está última en [DCAT 2](https://www.w3.org/TR/vocab-dcat-3/#Property:distribution_media_type) tiene como rango la clase más específica `dct:MediaType`, en lugar de la más general `dct:MediaTypeOrExtent` (qué se usa en `dct:format`). Esto significa que la propiedad "Formato tipo MIME" (`dcat:mediaType`) se restringe para usarse únicamente con valores que sean instancias de `dct:MediaType` ([tipos de media de IANA](http://www.iana.org/assignments/media-types/media-types.xhtml)), excluyendo otros tipos de nodos que podrían haberse permitido con `dct:MediaTypeOrExtent`.

# Anexo 2. Guía de referencia rápida de DCAT-AP-ES {#annex-1-quickguide-dcat-ap-es}

En la siguiente relación, se incluye junto al acrónimo HVD, las propiedades que con carácter obligatorio, recomendado u opcional son relevantes para la publicación de datos de alto valor.

| Clase | URI de la clase | Obligatorias | Recomendadas | Opcionales |
| --- | --- | --- | --- | --- |
| Catálogo | dcat:Catalog | dct:title  dct:description  dct:publisher  foaf:homepage  dcat:themeTaxonomy  dct:issued  dct:modified  dct:language  dct:license | dct:spatial  dcat:dataset (HVD)  dcat:service (HVD) | dcat:catalog  dct:creator  dct:hasPart  dct:isPartOf  dcat:record (HVD)  dct:rights |
| Registro de catálogo | dcat:CatalogRecord | dct:modified  foaf:primaryTopic (HVD) | dct:conformsTo  dct:issued | dct:description  dct:title |
| Servicio de datos | dcat:DataService | dcat:endpointURL (HVD)  dct:title  dcatap:applicableLegislation (HVD)  dcatap:hvdCategory (HVD)  dcat:contactPoint (HVD)  dcat:servesDataset (HVD)  foaf:page (HVD) dcat:theme dct:publisher | dcat:endpointDescription (HVD) dcat:servesDataset dcatap:applicableLegislation foaf:page dcat:contactPoint | dct:accessRights (HVD)  dct:description  dct:license (HVD) dcat:keyword |
| Conjunto de datos | dcat:Dataset | dct:description  dct:title  dct:publisher  dcat:theme  dcatap:applicableLegislation (HVD)  dcatap:hvdCategory (HVD)  dcat:distribution (HVD) | dcat:contactPoint (HVD)  dcat:distribution  dcat:keyword  dct:spatial  dct:temporal  dct:issued  dct:modified dcatap:applicableLegislation | adms:identifier  adms:sample  adms:versionNotes  dcat:landingPage  dcat:spatialResolutionInMeters  dcat:temporalResolution  dcat:qualifiedRelation  dct:accessRights  dct:accrualPeriodicity  dct:conformsTo (HVD)  dct:creator  dct:hasVersion  dct:isReferencedBy  dct:isVersionOf  dct:identifier  dct:language  dct:provenance  dct:relation  dct:source  dct:type  foaf:page  dcat:version  prov:qualifiedAttribution  prov:wasGeneratedBy |
| Distribución | dcat:Distribution | dcat:accessURL (HVD)  dcatap:applicableLegislation (HVD) | dcatap:availability  dct:description  dct:format  dct:license (HVD) dcatap:applicableLegislation | adms:status  dcat:accessService (HVD)  dcat:byteSize  dcat:compressFormat  dcat:downloadURL  dcat:mediaType  dcat:packageFormat  dcat:spatialResolutionInMeters  dcat:temporalResolution  dct:conformsTo (HVD)  dct:issued  dct:language  dct:modified  dct:rights (HVD)  dct:title  foaf:page  odrl:hasPolicy  spdx:checksum |
| Agente | foaf:Agent | foaf:name | dct:type  dct:identifier |  |
| Contacto | vcard:Kind |  | vcard:hasEmail (HVD)  vcard:hasURL (HVD) |  |
| Checksum | spdx:Checksum | spdx:algorithm  spdx:checksumValue |  |  |
| Localización | dct:Location |  | dcat:bbox  dcat:centroid | locn:geometry |
| Período temporal | dct:PeriodOfTime |  | dcat:startDate  dcat:endDate | time:hasBeginning  time:hasEnd |
| Relación | dcat:Relationship | dct:relation  dcat:hadRole |  |  |


| Otras clases auxiliaries: | URI de la clase | Propiedad |
| --- | --- | --- |
| Categoría | skos:Concept | skos:prefLabel |
| Esquema de categorías | skos:ConceptScheme | dct:title |
| Documento | foaf:Document |  |
| Frequencia | dct:Frequency |  |
| Identificador | adms:Identifier | skos:notation |
| Tipo de licencia | skos:Concept |  |
| Sistema de idiomas | dct:LinguisticSystem |  |
| Literal | rdfs:Literal |  |
| Tipo de medio | dct:MediaType |  |
| Tipo de publicador | skos:Concept |  |
| Recurso | rdfs:Resource |  |
| Declaración de derechos | dct:RightsStatement |  |
| Role | dcat:Role |  |
| Standard | dct:Standard |  |
| Status | skos:Concept |  |

# Anexo 3. Diferencias entre DCAT-AP-ES y DCAT-AP {#annex-3-dcat-ap-to-dcat-ap-es}

DCAT-AP-ES se basa en [DCAT-AP 2.1.1](https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) con la incorporación de elementos de la extensión [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/). A continuación, se presentan las principales diferencias entre el modelo español y las versiones europeas.


Las diferencias se muestran en las siguientes tablas comparativas, donde la cabecera indica:

- **Entidad**: Clase o elemento del modelo (por ejemplo, `Catalog`, `Dataset`, `Distribution`, etc.).
- **Metadato**: Nombre del metadato o propiedad.
- **Propiedad**: Nombre formal de la propiedad (por ejemplo, `dct:title`).
- **T** (Aplicabilidad): Tipo de obligatoriedad en DCAT-AP-ES (`Obligatorio`, `Recomendado`, `Opcional`).
- **DCAT-AP T**: Tipo de obligatoriedad en el perfil DCAT-AP.
- **C** (Cardinalidad): Cardinalidad en DCAT-AP-ES.
- **DCAT-AP C**: Cardinalidad en el perfil DCAT-AP.
- **Observaciones**: Comentarios sobre el cambio o diferencia principal.

## DCAT-AP 2.1.1

### Resumen de cambios

!!! note "DCAT-AP-ES&nbsp;= DCAT-AP&nbsp;2.1.1 +&nbsp;DCAT-AP-HVD&nbsp;2.2.0 + diferencias"

Las diferencias se enumeran en la siguiente tabla junto con una justificación.

| Diferencias | Justificación |
|---|---|
|**1. Declaración obligatoria de las siguientes propiedades opcionales**<br>*Catalog*<ul><li>`dcat:themeTaxonomy`</li><li>`dct:language`</li><li>`dct:issued`</li><li>`dct:modified`</li><li>`dct:license`</li><li>`foaf:homepage`</li></ul>*Dataset*<ul><li>`dcat:theme`</li><li>`dct:publisher`</li></ul>**2. Mantenimiento de estructura de URIs para la cobertura geográfica**| Aprovechar buenas prácticas que venían fijadas por la NTI-RISP v2013  que ya venían siendo aplicadas de esta forma por las AAPP |
|**3. Ajuste a 3 la cardinalidad máxima de taxonomías de sectores primarios (`dcat:themeTaxonomy`)**| Facilitar la interoperabilidad al utilizar taxonomías de uso común (NTI-RISP v2013, INSPIRE y EDP) |
|**4. Uso obligatorio de, al menos, la taxonomía de sectores primarios fijada por la NTI-RISP v2013**|Aprovechar buenas prácticas que venían fijadas por la NTI-RISP v2013 y  reforzar el uso que se realiza para otros fines de las AAPP |
|**5. Obligación de incorporación de, al menos, el idioma castellano en propiedades multilingües.**|Garantizar la interoperabilidad|
|**6. Uso del DIR3 para la identificación de publicadores (`dct:publisher` y `dct:identifier` de *Agent*)**|Aplicar la forma estándar de identificación única de organismos públicos y reforzar el uso que se realiza para otros fines de las AAPP |
|**7. Concreción del vocabulario del metadato `adms:status`**<br>**8. Incorporación de `dct:publisher` y `dcat:theme` a *DataService***| Convergencia futura con DCAT-AP 3.0.0 y asegurar interoperabilidad.<br>`adms:status` define el ciclo de vida de una distribución, con las opciones: `OP_DATPRO`, `WITHDRAWN`, `COMPLETED`, `DEPRECATED`, `DEVELOP`|
|**9. Incorporación del vocabulario ATU para `dct:spatial`**|Permite mayor precisión para divisiones administrativas, garantizando la interoperabilidad. `dct:spatial` es Recomendado |

### Detalle completo de cambios

| Entidad | Metadato | Propiedad | T | DCAT-AP<br>T | C | DCAT-AP<br>C | Observaciones |
|---|---|---|---|---|---|---|---|
| Catalog | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| Catalog | Descripción | dct:description | Ob | Ob | 1..n | 1..n | Sin cambios |
| Catalog | Órgano publicador | dct:publisher | Ob | Ob | 1..1 | 1..1 | Sin cambios |
| Catalog | Temática(s) | dcat:themeTaxonomy | Ob | R | 1..3 | 0..n | DCAT-AP-ES requiere obligatoriamente la [taxonomía de sectores primarios](http://datos.gob.es/kos/sector-publico/sector) y restringe cardinalidad |
| Catalog | Idioma(s) | dct:language | Ob | R | 1..n | 0..n | DCAT-AP-ES exige que al menos uno de los idiomas sea español |
| Catalog | Fecha de creación | dct:issued | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Fecha de actualización | dct:modified | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Página web | foaf:homepage | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Términos de uso | dct:license | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| CatalogRecord | Estado editorial | adms:status | R | R | 0..1 | 0..1 | En DCAT-AP 2.1.1 usa vocabulario [ADMS Status 1.0](http://www.w3.org/TR/vocab-adms/#status) |
| Dataset | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| Dataset | Descripción | dct:description | Ob | Ob | 1..n | 1..n | Sin cambios |
| Dataset | Publicador | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria y ajusta cardinalidad (1..1) |
| Dataset | Temática(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Dataset | Distribución | dcat:distribution | R/Ob (HVD) | R | 0..n/1..n (HVD) | 0..n | DCAT-AP-ES hace obligatoria esta propiedad para conjuntos de datos HVD |
| Dataset | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | No existe | 0..n/1..n (HVD) | - | Propiedad incorporada en DCAT-AP-ES desde DCAT-AP 3.0.0 |
| Dataset | Resolución espacial | dcat:spatialResolutionInMeters | Op | R | 0..1 | 0..n | DCAT-AP-ES limita a una única resolución espacial |
| Dataset | Resolución temporal | dcat:temporalResolution | Op | R | 0..1 | 0..n | DCAT-AP-ES limita a una única resolución temporal |
| DataService | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| DataService | URL de acceso | dcat:endpointURL | Ob | Ob | 1..n | 1..n | Sin cambios |
| DataService | Temática(s) | dcat:theme | Ob | R | 1..n | 0..n | DCAT-AP-ES eleva la propiedad a Obligatoria |
| DataService | Publicador | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| DataService | Descripción del punto de acceso | dcat:endpointDescription | R | R | 0..n | 0..n | Sin cambios |
| DataService | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | No existe | 0..n/1..n (HVD) | - | Propiedad incorporada en DCAT-AP-ES desde DCAT-AP 3.0.0 |
| Distribution | URL de acceso | dcat:accessURL | Ob | Ob | 1..n | 1..n | Sin cambios |
| Distribution | Formato | dct:format | R | R | 0..1 | 0..1 | Sin cambios |
| Distribution | Licencia | dct:license | R | R | 0..1 | 0..1 | Sin cambios |
| Distribution | Legislación aplicable | dcatap:applicableLegislation | R/Ob (HVD) | No existe | 0..n/1..n (HVD) | - | Propiedad incorporada en DCAT-AP-ES desde DCAT-AP 3.0.0 |
| Distribution | Disponibilidad | dcatap:availability | R | No existe | 0..1 | - | Propiedad incorporada en DCAT-AP-ES desde DCAT-AP 3.0.0 |
| Distribution | Estado | adms:status | Op | R | 0..1 | 0..1 | DCAT-AP-ES rebaja la propiedad a Opcional |
| Distribution | Resolución espacial | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | Sin cambios|
| Distribution | Resolución temporal | dcat:temporalResolution | Op | R | 0..1 | 0..n | DCAT-AP-ES limita a una única resolución temporal |
| Agent | Nombre | foaf:name | Ob | Ob | 1..n | 1..n | Sin cambios |
| Agent | Tipo | dct:type | R | R | 0..1 | 0..1 | Sin cambios |
| Agent | Identificador | dct:identifier | R | Op | 0..1 | 0..1 | DCAT-AP-ES eleva a Recomendado y establece formato para organismos públicos (DIR3) |

## DCAT-AP 3.0.0

| Entidad | Metadato | Propiedad | T | DCAT-AP<br>T | C | DCAT-AP<br>C | Observaciones |
|---|---|---|---|---|---|---|---|
| Catalog | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| Catalog | Descripción | dct:description | Ob | Ob | 1..n | 1..n | Sin cambios |
| Catalog | Órgano publicador | dct:publisher | Ob | Ob | 1..1 | 1..1 | Sin cambios |
| Catalog | Temática(s) | dcat:themeTaxonomy | Ob | R | 1..3 | 0..n | DCAT-AP-ES requiere obligatoriamente la [taxonomía de sectores primarios](http://datos.gob.es/kos/sector-publico/sector) y restringe cardinalidad |
| Catalog | Idioma(s) | dct:language | Ob | R | 1..n | 0..n | DCAT-AP-ES exige que al menos uno de los idiomas sea español |
| Catalog | Fecha de creación | dct:issued | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Fecha de actualización | dct:modified | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Página web | foaf:homepage | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Términos de uso | dct:license | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Catalog | Legislación aplicable | dcatap:applicableLegislation | No existe | R | - | 0..* | Propiedad de DCAT-AP 3 no incorporada a DCAT-AP-ES |
| CatalogRecord | Estado editorial | adms:status | R | R | 0..1 | 0..1 | En DCAT-AP 3 usa vocabulario diferente al de DCAT-AP 2.1.1, en `DCAT-AP-ES` se adopta como una recomendación: `http://publications.europa.eu/resource/authority/concept-status`|
| Dataset | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| Dataset | Descripción | dct:description | Ob | Ob | 1..n | 1..n | Sin cambios |
| Dataset | Publicador | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria y ajusta cardinalidad (`1..1`) |
| Dataset | Temática(s) | dcat:theme | Ob | R | 1..n | 0..* | DCAT-AP-ES eleva la propiedad a Obligatoria |
| Dataset | Distribución | dcat:distribution | R/Ob (HVD) | R | 0..n/1..n (HVD) | 0..* | DCAT-AP-ES hace obligatoria esta propiedad para conjuntos de datos HVD |
| Dataset | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | En DCAT-AP-ES es Obligatorio para conjuntos de datos HVD |
| Dataset | Calidad | dqv:hasQualityMeasurement | No existe | Op | - | 0..n | Propiedad nueva en DCAT-AP 3.0.0 no incorporada a DCAT-AP-ES |
| Dataset | Resolución espacial | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | DCAT-AP-ES mantiene la misma cardinalidad |
| Dataset | Resolución temporal | dcat:temporalResolution | Op | Op | 0..1 | 0..n | DCAT-AP-ES limita a una única resolución temporal |
| DataService | Nombre | dct:title | Ob | Ob | 1..n | 1..n | Sin cambios |
| DataService | URL de acceso | dcat:endpointURL | Ob | Ob | 1..n | 1..n | Sin cambios |
| DataService | Temática(s) | dcat:theme | Ob | R | 1..n | 0..* | DCAT-AP-ES eleva la propiedad a Obligatoria |
| DataService | Publicador | dct:publisher | Ob | R | 1..1 | 0..1 | DCAT-AP-ES eleva la propiedad a Obligatoria |
| DataService | Descripción del punto de acceso | dcat:endpointDescription | R | R | 0..n | 0..* | Sin cambios |
| DataService | Descripción del punto por tipo | dcat:endpointDescriptionByType | No existe | R | - | 0..n | Propiedad nueva en DCAT-AP 3.0.0 no incorporada a DCAT-AP-ES |
| DataService | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | En DCAT-AP-ES es Obligatorio para servicios HVD |
| Distribution | URL de acceso | dcat:accessURL | Ob | Ob | 1..n | 1..n | Sin cambios |
| Distribution | Formato | dct:format | R | R | 0..1 | 0..1 | Sin cambios |
| Distribution | Licencia | dct:license | R | R | 0..1 | 0..1 | Sin cambios |
| Distribution | Legislación aplicable | dcatap:applicableLegislation | R/Ob (HVD) | Op | 0..n/1..n (HVD) | 0..n | DCAT-AP-ES eleva a Recomendado/Obligatorio para HVD |
| Distribution | Disponibilidad | dcatap:availability | R | R | 0..1 | 0..1 | Sin cambios |
| Distribution | Estado | adms:status | Op | Op | 0..1 | 0..1 | Sin cambios  |
| Distribution | Resolución espacial | dcat:spatialResolutionInMeters | Op | Op | 0..1 | 0..1 | Sin cambios|
| Distribution | Resolución temporal | dcat:temporalResolution | Op | Op | 0..1 | 0..1 | Sin cambios |
| Agent | Nombre | foaf:name | Ob | Ob | 1..n | 0..1 | Sin cambios |
| Agent | Tipo | dct:type | R | Op | 0..1 | 0..1 | DCAT-AP-ES eleva a Recomendado |
| Agent | Identificador | dct:identifier | R | Op | 0..1 | 0..1 | DCAT-AP-ES eleva a Recomendado y establece formato para organismos públicos (DIR3) |


## Extensiones
La sección de **Extensiones** describe cómo DCAT-AP-ES amplía y adapta el modelo base de DCAT-AP para cubrir necesidades específicas del contexto español y para incorporar requisitos adicionales, como los relativos a los conjuntos de datos de alto valor (HVD). 

### DCAT-AP HVD 2.2.0

| Entidad | Metadato | Propiedad | T | HVD<br>T | C | HVD<br>C | Observaciones |
|---|---|---|---|---|---|---|---|
| Dataset | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| Dataset | Legislación aplicable | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| Dataset | Distribución | dcat:distribution | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| Dataset | Punto de contacto | dcat:contactPoint | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| DataService | Categoría HVD | dcatap:hvdCategory | Op/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| DataService | Legislación aplicable | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| DataService | Punto de contacto | dcat:contactPoint | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| DataService | Conjunto de datos servido | dcat:servesDataset | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| Distribution | Legislación aplicable | dcatap:applicableLegislation | R/Ob (HVD) | Op/Ob (HVD) | 0..n/1..n (HVD) | 0..n/1..n (HVD) | Implementación completa de DCAT-AP HVD en DCAT-AP-ES |
| Distribution | Licencia | dct:license | R/Ob (HVD) | Op/Ob (HVD) | 0..1/1..1 (HVD) | 0..1/1..1 (HVD) | Se mantiene la misma obligatoriedad para licencias en datos HVD |

## Características distintivas de DCAT-AP-ES

Este anexo presenta una visión consolidada de las diferencias principales entre DCAT-AP-ES y los perfiles europeos DCAT-AP (versiones 2.1.1 y 3.0.0), facilitando la comprensión de las particularidades del perfil español y sus requisitos específicos de implementación.

### 1. Adaptación al contexto español
- Uso obligatorio de taxonomías nacionales: DCAT-AP-ES exige el uso de la [taxonomía de sectores primarios](http://datos.gob.es/kos/sector-publico/sector) para clasificación temática
- Requisito lingüístico: Al menos uno de los idiomas debe ser español en propiedades multilingües
- Normalización de identificadores organizativos: Define URI normalizadas con formato DIR3 para organismos públicos (`http://datos.gob.es/recurso/sector-publico/org/Organismo/{ID}`)

### 2. Mayor obligatoriedad en metadatos
- DCAT-AP-ES eleva numerosas propiedades de Recomendadas a Obligatorias, especialmente en `dcat:Catalog`, `dcat:Dataset` y `dcat:DataService`
- Define obligatoriedad para propiedades clave como `dct:publisher`, `dcat:theme` y fechas de creación/actualización
- Adopta un enfoque más estricto para garantizar completitud e interoperabilidad de metadatos

### 3. Soporte integral para datos de alto valor (HVD)
- Integra requisitos específicos para datos de alto valor según el [Reglamento de ejecución (UE) 2023/138 de la Comisión Europea](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138)
- Define propiedades obligatorias adicionales para conjuntos de datos HVD (`dcatap:hvdCategory`, `dcat:distribution`)
- Incorpora `dcatap:applicableLegislation` como obligatoria para distribuciones HVD

### 4. Evolución desde los perfiles europeos
- Incorpora selectivamente propiedades de DCAT-AP 3.0.0 como la mencionada `dcatap:applicableLegislation`, `dcatap:availability` y `dcatap:hvdCategory`
- Actualiza vocabularios controlados (ej., para `adms:status` en `dcat:Distribution`)

### 5. Cardinalidades adaptadas
- Define cardinalidades más restrictivas para mayor precisión (ej., `dct:publisher` exige cardinalidad `1..1`)
- Limita resoluciones espaciales y temporales a una única instancia (`0..1`)
- Restringe `dcat:themeTaxonomy` a máximo 3 taxonomías, incluyendo obligatoriamente la española

### 6. Alineado con el marco legal de datos
- DCAT-AP-ES es una evolución del [modelo de metadatos NTI-RISP](https://datosgobes.github.io/NTI-RISP/) y la [Guía de aplicación](https://datosgobes.github.io/NTI-RISP/download/pdf/guia_nti_pdf_reutilizacion_recursos_informacion_2aed.pdf) que lo contiene. Por lo que implementa los requisitos de acuerdo con la normativa española de datos abiertos ([Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público](https://www.boe.es/eli/es/l/2007/11/16/37/con) y [Resolución de 19 de febrero de 2013, de la Secretaría de Estado de Administraciones Públicas, por la que se aprueba la Norma Técnica de Interoperabilidad de Reutilización de recursos de la información](https://www.boe.es/eli/es/res/2013/02/19/(4))). 
- Se adapta al ecosistema de especificaciones relacionadas e interconectadas (DCAT-AP) en el contexto de las políticas de datos [Directiva (UE) 2019/1024](http://data.europa.eu/eli/dir/2019/1024/oj), interoperabilidad ([SEMIC](https://joinup.ec.europa.eu/)) e infraestructura ([EDP](https://data.europa.eu/)) de la Comisión Europea.

# Histórico de cambios

Este apartado proporciona una visión general de los cambios incorporados en DCAT-AP-ES. Una lista completa de las incidencias cerradas con esta versión está accesible en [GitHub](https://github.com/datosgobes/DCAT-AP-ES/issues).

## DCAT-AP-ES 1.0.0

### Cambios principales

- Transformación de la documentación técnica en representación HTML (estilo [RESPEC](https://respec.org/docs/) usando [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/))
- Integración de directrices y textos actualizados relacionados con DCAT-AP-ES
- Actualización y mejora de referencias cruzadas para facilitar la navegación
- Corrección de numerosas erratas y problemas de conversión

### Adaptaciones a las diferentes secciones
- Introducción: Revisión para reflejar el contexto actual y los fundamentos del perfil
- Conformidad: Actualización para reflejar los requisitos de implementación en el ecosistema español
- Terminología: Lista de prefijos actualizada con los vocabularios más recientes
- Modelo de datos: Estructura reorganizada para mejorar la legibilidad
- Vocabularios controlados: Actualización de referencias a vocabularios autorizados
- Conjuntos de datos de alto valor (HVD): Integración completa de los requisitos del [Reglamento de Ejecución (UE) 2023/138](http://data.europa.eu/eli/reg_impl/2023/138/oj)
- Anexo de referencia rápida: Generación automática desde el modelo de datos para mantener sincronización

#### Cambios respecto a NTI-RISP

- Actualización completa de las clases y propiedades conforme a DCAT-AP
- Eliminación de propiedades obsoletas y reemplazo por alternativas más adecuadas
- Reestructuración para adaptarse a los nuevos requisitos de la [Directiva (UE) 2019/1024](http://data.europa.eu/eli/dir/2019/1024/oj)
- Implementación de metadatos específicos para conjuntos de datos de alto valor (HVD)
- Ampliación de capacidades para describir servicios de datos (APIs y endpoints)

#### Diferencias con DCAT-AP

- Mayor nivel de obligatoriedad en propiedades clave para garantizar calidad de metadatos
- Adaptación al marco normativo español y sus requisitos específicos
- Cardinalidades más restrictivas para garantizar uniformidad y precisión
- Requisitos lingüísticos específicos del contexto multilingüe español
- Integración con sistemas de identificación de organismos públicos españoles (DIR3)

### Adaptaciones del modelo de datos

La lista siguiente indica los cambios y diferencias respecto a la versión anterior (NTI-RISP). También se incluye el impacto de la alineación con la recomendación del W3C: DCAT y el perfil DCAT-AP europeo.

- División de los textos descriptivos existentes en definiciones y notas de uso siguiendo las mejores prácticas de SEMIC
- Alineación con DCAT-AP 2.1.1 y adopción selectiva de elementos de DCAT-AP 3.0.0
- Organización del perfil en entidades principales, entidades de soporte y tipos de datos
- Elevación de numerosas propiedades a obligatorias para garantizar interoperabilidad
- Incorporación de aspectos específicos para datos de alto valor (HVD)
- Adaptación a requisitos lingüísticos y de clasificación territorial de España

### Requisitos específicos para el contexto español

- Taxonomías nacionales: Implementación obligatoria de la taxonomía de sectores primarios española
- Requisito lingüístico: Obligatoriedad del español como uno de los idiomas en propiedades multilingües
- Identificadores normalizados: Adopción del esquema DIR3 para la identificación de organismos públicos

### Alineación con HVD (Datos de Alto Valor)

- Integración completa de los requisitos del Reglamento de Ejecución (UE) 2023/138
- Definición clara de propiedades obligatorias adicionales para conjuntos de datos HVD
- Incorporación de metadatos para la trazabilidad y cumplimiento normativo (legislación aplicable, categorías HVD)

### SHACL y validación

- Desarrollo de reglas SHACL para validación automática del perfil
- Inclusión de identificadores únicos para cada restricción
- Implementación de pruebas para verificar conformidad con el perfil

### Correcciones de errores

- Alineación de propiedades con su definición en los vocabularios originales
- Corrección de cardinalidades para reflejar requisitos específicos del contexto español
- Mejora de las descripciones y notas de uso para facilitar la implementación correcta
- Ajustes en referencias a vocabularios controlados para asegurar su disponibilidad y persistencia

[^1]: Obligatorio cuando se trata de datos de alto valor, en otro caso, recomendado.
