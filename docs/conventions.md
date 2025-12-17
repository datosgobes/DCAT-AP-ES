# Introducción
En España, el intercambio de datos abiertos entre el portal de la Iniciativa de datos abiertos del Gobierno de España ([datos.gob.es](https://datos.gob.es)) y los distintos proveedores de datos, como catálogos de la Administración General del Estado, autonómicos, de Entidades Locales y otros organismos, se plantea bajo un marco que asegure la interoperabilidad y homogeneidad de los metadatos. Para ello, se adapta el perfil de aplicación europeo  [DCAT-AP 2.1.1](https://joinup.ec.europa.eu/collection/semic-support-centre/solution/dcat-application-profile-data-portals-europe/release/211) junto a los elementos descritos en la extensión [DCAT-AP HVD 2.2.0](https://semiceu.github.io/DCAT-AP/releases/2.2.0-hvd/) para incorporar el modelado de los [Conjuntos de datos de alto valor](https://datos.gob.es/es/noticia/europa-define-los-conjuntos-de-datos-de-alto-valor-que-el-sector-publico-tendra-que-abrir) (*High Value Datasets*) a las necesidades nacionales, dando lugar al estándar **DCAT-AP-ES**, que se establece como referencia para el intercambio de metadatos sobre información pública a nivel nacional.  

Desde la entrada en vigor del estándar, [datos.gob.es](https://datos.gob.es) acepta metadatos en formato **DCAT-AP-ES**, así como el perfil de aplicación referido en la Norma Técnica. Para aquellos proveedores que federen directamente al portal se establecerá un período transitorio tras la publicación de nuevas versiones, durante el cual podrán ajustar sus sistemas al estándar actualizado desde el perfil anterior de la Norma Técnica de Interoperabilidad de Recursos de Información del Sector Público ([**NTI-RISP**](https://datos.gob.es/es/doc-tags/nti-risp))

La guía de convenciones no solo detalla las modificaciones específicas introducidas en el estándar español respecto a la versión europea, sino que también define reglas adicionales para abordar necesidades prácticas. Estas pueden incluir particularidades del contexto español de datos abiertos, donde la implementación podría ajustarse a requerimientos técnicos distintos. Además, se prevé que algunas de estas reglas puedan evolucionar más rápidamente que la especificación principal, permitiendo mayor flexibilidad y adaptación a los cambios tecnológicos.  

Este documento tiene como **público objetivo** a los ^^responsables de desarrollo y mantenimiento de los portales de datos abiertos^^, así como a los ^^proveedores de datos que colaboren con el catálogo nacional^^. Su propósito es proporcionar directrices claras y herramientas prácticas para implementar el estándar de manera eficiente. Sin embargo, para usos en contextos específicos, se deja abierta la posibilidad de establecer convenciones adicionales que complementen las normativas generales.  

Para asegurar una interpretación uniforme, se utilizan términos normativos como **DEBE** (*MUST*), **DEBERÍA** (*SHOULD*) y **PUEDE** (*MAY*), conforme a lo establecido en el estándar **[RFC2119](https://www.rfc-editor.org/rfc/rfc2119)**, con el fin de diferenciar las directrices obligatorias de las opcionales. Aunque el manual incluye diagramas y ejemplos ilustrativos, estos no tienen carácter normativo, a menos que se indique explícitamente.

Este enfoque busca no solo estandarizar el intercambio de metadatos, sino también fomentar una mayor armonización y colaboración entre los diferentes niveles de gobierno en España, garantizando una interoperabilidad sólida y escalable.  

## Prefijos usados 
Todos los prefijos de espacios de nombres (*namespaces*) utilizados a lo largo del documento se encuentran referenciados en el [Anexo 4. Espacios de nombres utilizados en el documento](#annex-4-document-namespaces).

## Tipos de convenciones
### Convenciones técnicas
Estas convenciones definen aspectos técnicos de implementación, incluyendo codificación, identificación de recursos y modelado de entidades. Son esenciales para garantizar la interoperabilidad técnica y la correcta interpretación de los metadatos.

### Convenciones organizativas
Estas convenciones establecen reglas para la gestión y organización de catálogos, la federación de datos y la identificación de organismos. Proporcionan el marco de gobernanza necesario para una gestión efectiva de los metadatos.

### Convenciones semánticas
Estas convenciones aseguran la coherencia en la descripción de los recursos, garantizan que los metadatos sean semánticamente precisos y consistentes.

## Lista de convenciones
- [**Convención 01**](#convencion-01): El identificador del publicador *DEBE* estar [dado de alta y disponible en la taxonomía de datos.gob.es](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es)
- [**Convención 02**](#convencion-02): Los literales `dct:title`, `dct:description`, `vcard:organization-name `, `vcard:fn`, `foaf:name`, `dcat:keyword` y `adms:versionNotes` *DEBEN* estar definidos con las etiquetas de idioma, al menos estar en idioma español `es` y no pueden ser literales vacíos.
- [**Convención 03**](#convencion-03): Los identificadores y referencias URI *DEBERÍAN* utilizar el esquema `http://` en lugar de `https://` como norma general.
- [**Convención 04**](#convencion-04): Los organismos *DEBERÍAN* implementar la federación automática mediante RDF como único método de publicación de metadatos en formato DCAT-AP-ES, evitando la coexistencia de federación manual y automática para un mismo organismo.
- [**Convención 05**](#convencion-05): Las URIs *DEBEN* estar correctamente codificadas en su origen, especialmente cuando contengan: 1. Caracteres reservados (`?`, `&`, `=`, `#`, etc.) 2. Espacios 3. Caracteres no ASCII (acentos, `ñ`, etc.) 4. Caracteres especiales (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)
- [**Convención 06**](#convencion-06): Los recursos *DEBEN* tener un identificador único y persistente que cumpla los siguientes requisitos: 1. Incluir la propiedad `dct:identifier` con un valor único para cada recurso. 2. Mantener la coherencia del identificador aunque el recurso se actualice. 3. Usar el mismo identificador cuando el recurso se publique en diferentes catálogos.
- [**Convención 07**](#convencion-07): Las referencias a documentos legales *DEBEN* utilizar identificadores ELI cuando estén disponibles: 1. Para legislación europea: `http://data.europa.eu/eli/...` 2. Para legislación nacional: `https://www.boe.es/eli/...` 3. Para documentos derivados usar la URI ELI del documento principal
- [**Convención 08**](#convencion-08): Las fechas de creación y modificación de recursos *DEBEN* cumplir los siguientes requisitos: 1. La fecha de modificación (`dct:modified`) *DEBE* ser posterior a la fecha de creación (`dct:created`) 2. La fecha de modificación *DEBE* reflejar el último cambio en los datos, no en los metadatos
- [**Convención 09**](#convencion-09): Se *DEBE* utilizar un único catálogo por organismo publicador, evitando el uso de subcatálogos mediante `dct:hasPart`. Las relaciones entre recursos *DEBEN* modelarse usando las siguientes propiedades según corresponda.
- [**Convención 10**](#convencion-10): El catálogo *DEBE* incluir como mínimo la [taxonomía de sectores primarios](https://datos.gob.es/kos/sector-publico/sector) en la propiedad `dcat:themeTaxonomy`.
- [**Convención 11**](#convencion-11): Se *PUEDEN* incluir taxonomías adicionales para mejorar la clasificación de los *datasets*: `http://publications.europa.eu/resource/authority/data-theme` o `http://inspire.ec.europa.eu/theme`
- [**Convención 12**](#convencion-12): Los *datasets* catalogados como HVD *DEBEN* incluir al menos un servicio de datos (`dcat:DataService`) con las siguientes propiedades obligatorias: 1. URL del endpoint (`dcat:endpointURL`)   2. Descripción del endpoint (`dcat:endpointDescription`) 3. Punto de contacto (`dcat:contactPoint`) 4. Legislación aplicable (`dcatap:applicableLegislation`) 5. Categoría HVD (`dcatap:hvdCategory`) 6. Documentación (`foaf:page`) 7. *Datasets* servidos (`dcat:servesDataset`)
- [**Convención 13**](#convencion-13): Los servicios OGC *DEBERÍAN* modelarse como `dcat:DataService` en lugar de `dcat:Distribution`. 
- [**Convención 14**](#convencion-14): La información de publicador *DEBERÍA* contener un [código identificador DIR3](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) en la propiedad identificador (`dct:identifier`), por ejemplo: `EA0000000`
- [**Convención 15**](#convencion-15): La información de creador *DEBERÍA* contener un [código identificador DIR3](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) en la propiedad identificador (`dct:identifier`), por ejemplo: `EA0000000`
- [**Convención 16**](#convencion-16): La cobertura geográfica *DEBE* declararse utilizando las URIs del [Anexo V de la NTI-RISP para recursos geográficos del territorio español](https://datos.gob.es/es/recurso/sector-publico/territorio), siguiendo estas reglas: 1. Utilizar el nivel territorial más específico que corresponda al ámbito real del dataset. 2. Evitar el uso de `España` por defecto cuando el ámbito sea más reducido. 3. No declarar simultáneamente una Comunidad Autónoma y sus provincias. 4. Para Comunidades Autónomas uniprovinciales, utilizar preferentemente la referencia a la Comunidad Autónoma.
- [**Convención 17**](#convencion-17): Cuando se especifique la cobertura geométrica, se *DEBERÍA* usar `WKT` (según [GeoSPARQL](http://www.opengeospatial.org/standards/geosparql)).
- [**Convención 18**](#convencion-18): Los *servicios de datos HVD* *DEBEN* incluir al menos un punto de contacto (`dcat:contactPoint`) con alguna de las siguientes propiedades: Correo electrónico (`vcard:hasEmail`) o URL del formulario de contacto (`vcard:hasURL`)
- [**Convención 19**](#convencion-19): El punto de contacto *DEBERÍA* incluir también: 1. Nombre (`vcard:organization-name`) 2. Número de teléfono (`vcard:hasTelephone`) 3. Identificador del organismo (`vcard:hasUid`) 4. Correo electrónico (`vcard:hasEmail`) 5. URL del formulario de contacto (`vcard:hasURL`)
- [**Convención 20**](#convencion-20): Los puntos de contacto recogidos en la taxonomía del portal *DEBEN* describirse como un `vcard:Kind` y no directamente con la URI del organismo.
- [**Convención 21**](#convencion-21): En las distribuciones de servicios OGC, las URLs de acceso *DEBEN* modelarse de la siguiente manera: En `dcat:accessURL`: URL completa de la petición de capacidades del servicio `GetCapabilities` (ej: `http://example.org/wms?request=GetCapabilities&service=WMS`) y en `dct:conformsTo`: URL del estándar OGC correspondiente, ej: `http://www.opengeospatial.org/standards/wms`
- [**Convención 22**](#convencion-22): Los periodos temporales *DEBEN* ser descritos exclusivamente mediante las propiedades `dcat:startDate` y `dcat:endDate` dentro de `dct:temporal`. El intervalo también puede ser abierto, es decir, puede tener solo un comienzo o solo un final.
- [**Convención 23**](#convencion-23): Los *datasets* *DEBEN* incluir al menos una distribución (`dcat:Distribution`).
- [**Convención 24**](#convencion-24): Cuando un recurso DCAT-AP-ES derive de un metadato fuente de otro estándar (por ejemplo: INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.), *DEBERÍA* incluirse una relación mediante la propiedad `adms:identifier` que apunte al identificador persistente del metadato fuente, utilizando un nodo de tipo `adms:Identifier`.
- [**Convención 25**](#convencion-25): Para describir un conjunto de datos accesible vía NSIP/ERPD en cada `dcat:Dataset` se *DEBE* indicar `dct:accessRights` con uno de los valores: `http://publications.europa.eu/resource/authority/access-right/RESTRICTED` o `NON_PUBLIC`
- [**Convención 26**](#convencion-26): Un conjunto de datos accesible vía NSIP/ERPD se *DEBERÍA* relacionar mediante `dcatap:applicableLegislation` con la legislación específica (al menos el Reglamento DGA: `http://data.europa.eu/eli/reg/2022/868/oj`).
- [**Convención 27**](#convencion-27): Para describir una distribución accesible vía NSIP/ERPD en cada `dcat:Distribution` se *DEBE* indicar: 1. `dcat:accessURL`: URL con información sobre cómo solicitar el acceso 2. `dcat:byteSize`: tamaño en bytes (puede ser aproximado) 3. `dct:format`: tipo de archivo (vocabulario `file-type`) 4. `dct:rights`: condiciones de reutilización aplicables a esta distribución

# Convenciones generales {#general}

## El organismo debe disponer de identificador dado de alta en la taxonomía de datos.gob.es {#general-dir3}
Para garantizar la trazabilidad de los organismos publicadores, éstos deben estar [dados de alta y disponibles en la taxonomía de datos.gob.es](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es), ya sea como [DIR3 de organismo público](https://administracionelectronica.gob.es/ctt/dir3) u organismo privado cuyo identificador es la letra P seguida de su NIF cómo código ficticio ([ver Anexo 3. Mapeo de identificadores organizativos](#annex-3-mapping-org-identifiers)).

!!! must organisational "Convención 01"

    El identificador del publicador **DEBE** estar [dado de alta y disponible en la taxonomía de datos.gob.es](mailto:soporte@datos.gob.es?subject=Solicitud%20de%20alta%20de%20Organismo%20y%20usuario%20en%20datos.gob.es)

## Indicación de idioma español en declaraciones {#general-idioma}
Los campos de literales de etiquetas multilingüe `xml:lang` deben estar al menos en idioma español (`es`).

!!! must technical "Convención 02" 

    Los literales `dct:title`, `dct:description`, `vcard:organization-name `, `vcard:fn`, `foaf:name`, `dcat:keyword` y `adms:versionNotes` **DEBEN** estar definidos con las etiquetas de idioma, al menos estar en idioma español `es` y no pueden ser literales vacíos.

## Uso de URIs HTTP {#general-http-uris}

Para mantener la compatibilidad y evitar problemas de interoperabilidad con sistemas que no soporten TLS/SSL, se recomienda usar URIs HTTP en lugar de HTTPS en los identificadores y referencias. Las URIs HTTP son igualmente derreferenciables que HTTPS mediante redirección.

!!! should technical "Convención 03"

    Los identificadores y referencias URI **DEBERÍAN** utilizar el esquema `http://` en lugar de `https://` como norma general. Esto aplica a:

    1.  Identificadores de recursos (`dcat:Dataset`, `dcat:Distribution`, etc.)
    2.  Referencias a vocabularios controlados
    3.  URIs de taxonomías y esquemas de conceptos

!!! info "Ejemplo de uso correcto de URIs"

    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-http-uris.ttl"
    ```

!!! info "Nota sobre excepciones"
    Existen excepciones a esta recomendación, donde el uso de `https://` está justificado:

    *   **[URIs ELI del BOE](https://www.elidata.es/documentacion_tecnica/especificacion_tecnica.php):** Los identificadores ELI del Boletín Oficial del Estado (BOE) utilizan el esquema `https://` (`https://www.boe.es/eli/...`). Debido a la naturaleza de estos identificadores y su adopción generalizada, se permite y recomienda mantener el esquema `https://` para las URIs ELI del BOE.


## Federación automática de datos {#general-federation}

Para garantizar la consistencia y calidad de los metadatos, así como simplificar el proceso de federación, se establece el uso exclusivo de federación automática mediante RDF (DCAT-AP-ES) como único método de ingesta de datos en el portal.

!!! should organisational "Convención 04"
    
    Los organismos **DEBERÍAN** implementar la federación automática mediante RDF como único método de publicación de metadatos en formato DCAT-AP-ES, evitando la coexistencia de federación manual y automática para un mismo organismo.

!!! warning "Importante"
    La coexistencia de federación manual y automática para un mismo organismo puede causar:
    
    - Inconsistencias en los metadatos
    - Duplicidad de *datasets*
    - Problemas de sincronización
    - Dificultades en la validación

!!! info "Nota sobre la transición"
    Los organismos que actualmente utilizan federación manual deberán planificar la migración de sus *datasets* al nuevo sistema de federación automática mediante RDF para DCAT-AP-ES.

## Codificación de URIs {#general-uri-encoding}

Para garantizar la validez del RDF y evitar problemas de procesamiento, todas las URIs deben estar correctamente codificadas según la [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986#section-2.4).

!!! must technical "Convención 05"
    
    Las URIs **DEBEN** estar correctamente codificadas en su origen, especialmente cuando contengan:
    
    1. Caracteres reservados (`?`, `&`, `=`, `#`, etc.)
    2. Espacios
    3. Caracteres no ASCII (acentos, ñ, etc.)
    4. Caracteres especiales (`<`, `>`, `"`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` ``)

!!! info "Ejemplo de codificación correcta de URIs"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-uri-encoding.ttl"
    ```

!!! warning "Importante"
    La responsabilidad de la codificación recae en el origen que genera las URIs:
    
    1. Las URIs deben codificarse antes de serializar el RDF para evitar que sea inválido.
    2. No se debe delegar la codificación a sistemas posteriores

!!! info "Nota sobre implementación"
    Para codificar URIs se pueden utilizar funciones estándar como:
    
    - JavaScript: `encodeURIComponent()`
    - Python: `urllib.parse.quote()`
    - Java: `URLEncoder.encode()`


## Identificadores únicos y persistentes {#general-resource-identifier}

Para garantizar la correcta identificación y trazabilidad de los recursos a lo largo del tiempo, así como evitar duplicidades durante la federación desde múltiples fuentes, es necesario establecer un sistema de identificadores únicos y persistentes dado que el identificador (`dct:identifier`) es la propiedad que permite la identificación única e inequívoca del conjunto de datos. 

!!! must technical "Convención 06"
    Los recursos **DEBEN** tener un identificador único y persistente que cumpla los siguientes requisitos:

    1. Incluir la propiedad `dct:identifier` con un valor único para cada recurso.
    2. Mantener la coherencia del identificador aunque el recurso se actualice.
    3. Usar el mismo identificador cuando el recurso se publique en diferentes catálogos.

!!! info "Ejemplo de identificadores coherentes"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-resource-identifier.ttl"
    ```

!!! warning "Importante"
    - Los identificadores no deben cambiar aunque cambie la URI del recurso.
    - El mismo dataset publicado en diferentes catálogos debe mantener el mismo `dct:identifier`.
    - En caso de conflicto durante la federación, prevalecerá el último dataset federado según el orden establecido.

!!! info "Nota sobre implementación"
    Para evitar duplicados durante la federación:
    
    1. Coordinar con otros publicadores la asignación de identificadores.
    2. Documentar el esquema de identificadores utilizado.
    3. Mantener un registro de equivalencias entre identificadores de diferentes fuentes.
    4. Consultar el orden de federación establecido en caso de publicación múltiple.

## Identificadores ELI para documentos legales {#general-eli}

Para garantizar una referencia unívoca y persistente a documentos legales, se debe utilizar el [Identificador Europeo de Legislación (ELI)](https://eur-lex.europa.eu/eli-register/about.html) como URI estándar.

!!! must technical "Convención 07"
    Las referencias a documentos legales **DEBEN** utilizar identificadores ELI cuando estén disponibles:

    1. Para legislación europea: `http://data.europa.eu/eli/...`
    2. Para legislación nacional: `https://www.boe.es/eli/...`
    3. Para documentos derivados usar la URI ELI del documento principal

!!! info "Ejemplo de uso de identificadores legales"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-eli.ttl"
    ```

!!! warning "Importante"
    - Usar siempre la versión consolidada cuando esté disponible
    - Para documentos sin ELI, usar una URI persistente alternativa
    - Mantener registro de equivalencias entre diferentes identificadores

!!! info "Nota sobre implementación"
    - Consultar la [documentación ELI](https://eur-lex.europa.eu/eli-register/about.html) para obtener más información sobre los identificadores
    - Usar herramientas de validación ELI para verificar la corrección de los identificadores
    - Documentar las equivalencias entre diferentes versiones de documentos legales

## Gestión de fechas de creación y modificación {#general-dates}

Para garantizar la trazabilidad temporal de los recursos y su correcto seguimiento, es importante gestionar adecuadamente las fechas de creación y modificación.

!!! must technical "Convención 08"
    Las fechas de creación y modificación de recursos **DEBEN** cumplir los siguientes requisitos:

    1. La fecha de modificación (`dct:modified`) **DEBE** ser posterior a la fecha de creación (`dct:created`)
    2. La fecha de modificación **DEBE** reflejar el último cambio en los datos, no en los metadatos

!!! info "Ejemplo de gestión correcta de fechas"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-dates.ttl"
    ```

!!! warning "Importante"
    - Las fechas deben ser coherentes entre diferentes catálogos
    - No usar fechas futuras

!!! info "Nota sobre implementación"
    Para validar las fechas:
    
    1. Verificar que la fecha de modificación sea posterior a la de creación
    2. Comprobar que las fechas estén en los formatos definidos por el modelo, se puede registrar la fecha utilizando el formato estándar: `YYYY-MM-DD` (`xsd:date`), o el [datetime ISO-8601](https://www.w3.org/TR/1998/NOTE-datetime-19980827) con zona horaria: `YYYY-MM-DDThh:mm:ssTZD` (`xsd:dateTime`), así como el año: `YYYY` (`xsd:gYear`) o el año y el mes: `YYYY-MM` (`xsd:gYearMonth`).

## Especificación de períodos temporales {#general-temporal}

La propiedad `dct:temporal` en DCAT-AP-ES se usa para describir el periodo de tiempo al que se refiere un conjunto de datos. En la actualidad, existen múltiples formas de describir esta información, incluyendo el uso de `dcat:startDate`, `dcat:endDate`, `time:hasBeginning`, `time:hasEnd` y `schema:startDate`, `schema:endDate`. Sin embargo, esta flexibilidad puede generar inconsistencias en la representación de los periodos temporales.

Dado que tanto `dcat:startDate` como `dcat:endDate` pueden registrarse con [rangos suficientemente flexibles](#PeriodOfTime.startDate), se opta por adoptar este enfoque por motivos organizativos.


!!! must organisational "Convención 22"
    Los periodos temporales **DEBEN** ser descritos exclusivamente mediante las propiedades `dcat:startDate` y `dcat:endDate` dentro de `dct:temporal`. El intervalo también puede ser abierto, es decir, puede tener solo un comienzo o solo un final.

!!! info "Ejemplo de uso correcto de un período temporal"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-temporal.ttl"
    ```

!!! info "Nota sobre implementación"
    Se recomienda revisar los metadatos, sí son heredados de la versión inicial de NTI-RISP, para actualizar `schema:startDate`, `schema:endDate` (propiedades anteriores a [DCAT 2](https://www.w3.org/TR/vocab-dcat-2/#changes)) en los nuevos registros conforme al vocabulario DCAT.

## Datos restringidos pero accesibles a través de NSIP/ERPD {#general-nsip-erpd-publication}

Esta convención define cómo representar conjuntos de datos que no son abiertos pero que están accesibles bajo la implementación de la [DGA (*Data Governance Act*) a través de NSIP/ERPD](https://digital-strategy.ec.europa.eu/en/policies/data-governance-act-explained).

!!! must semantic "Convención 25"
    Para describir un conjunto de datos accesible vía NSIP/ERPD en cada `dcat:Dataset` se **DEBE** indicar `dct:accessRights` con uno de los valores: `http://publications.europa.eu/resource/authority/access-right/RESTRICTED` o `NON_PUBLIC` y se **DEBERÍA** relacionar mediante `dcatap:applicableLegislation` con la legislación específica (por ejemplo el Reglamento DGA: `http://data.europa.eu/eli/reg/2022/868/oj`)

!!! should semantic "Convención 26"
    Un conjunto de datos accesible vía NSIP/ERPD se **DEBERÍA** relacionar mediante `dcatap:applicableLegislation` con la legislación específica (al menos el Reglamento DGA: `http://data.europa.eu/eli/reg/2022/868/oj`).

!!! must semantic "Convención 27"
    Para describir una distribución accesible vía NSIP/ERPD en cada `dcat:Distribution` se **DEBE** indicar:

    1. `dcat:accessURL`: URL con información sobre cómo solicitar el acceso
    2. `dcat:byteSize`: tamaño en bytes (puede ser aproximado)
    3. `dct:format`: tipo de archivo (vocabulario `file-type`)
    4. `dct:rights`: condiciones de reutilización aplicables a esta distribución

!!! success "Ejemplo de uso correcto"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_general-nsip-erpd-publication.ttl"
    ```

!!! warning "Importante"
    - El harvester de data.europa.eu filtrará automáticamente los datasets con `dct:accessRights` = `RESTRICTED` o `NON_PUBLIC` para el catálogo ERPD
    - La ausencia de `dcat:byteSize` o `dct:format` en Distribution causará rechazo del registro
    - Si se proporciona tanto `dct:accessURL` como `dcat:downloadURL`, el harvester priorizará `accessURL` para NSIP

# Convenciones para `dcat:Catalog` {#catalog}

## Subcatálogos y relaciones entre recursos (`dct:hasPart`) {#catalog-dct-haspart}

Para mantener la simplicidad y evitar problemas de ambigüedad en la federación de catálogos, se recomienda utilizar un único catálogo por organismo y expresar las relaciones entre recursos mediante las subpropiedades específicas de [`dcterms:relation`](https://www.w3.org/TR/vocab-dcat-2/#Property:resource_relation).

!!! must organisational "Convención 09"
    Se **DEBE** utilizar un único catálogo por organismo publicador, evitando el uso de subcatálogos mediante `dct:hasPart`. Las relaciones entre recursos **DEBEN** modelarse usando las siguientes propiedades según corresponda:

    1. Para distribuciones de *datasets*: `dcat:distribution`
    2. Para servicios de datos: `dcat:service`
    3. Para versiones: `dct:hasVersion`
    4. Para recursos relacionados con semántica conocida: otras subpropiedades de `dct:relation`
    5. Para relaciones no específicas: `dct:relation`

!!! info "Ejemplo de modelado de relaciones sin subcatálogos"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_catalog-dct-haspart.ttl"
    ```

!!! info "Nota sobre el uso de relaciones"
    1. Use siempre la propiedad más específica disponible para expresar la relación
    2. `dct:relation` debe usarse solo cuando la naturaleza de la relación es desconocida
    3. Las relaciones jerárquicas pueden expresarse mediante `dct:isPartOf`/`dct:hasPart`

## Taxonomías temáticas (`dcat:themeTaxonomy`) {#catalog-dcat-themetaxonomy}

Los catálogos deben incluir al menos la taxonomía de sectores primarios para clasificar sus *datasets*. Se pueden incluir alguna de las dos taxonomías adicionales para enriquecer la clasificación, se incluye información sobre mapeos entre [Sectores NTI-RISP y Temáticas DCAT-AP (Anexo 1)](#annex-1-mapping-nti-themes-dcatap-themes), así como entre [Temáticas DCAT-AP y Temas INSPIRE (Anexo 2)](#annex-2-mapping-inspire-themes-dcatap-themes)

!!! must organisational "Convención 10"
    
    El catálogo **DEBE** incluir como mínimo la [taxonomía de sectores primarios](https://datos.gob.es/kos/sector-publico/sector) en la propiedad `dcat:themeTaxonomy`. 
    

!!! may semantic "Convención 11"
    
    Se **PUEDEN** incluir taxonomías adicionales para mejorar la clasificación de los *datasets*: `http://publications.europa.eu/resource/authority/data-theme` o `http://inspire.ec.europa.eu/theme`

!!! info "Ejemplo de uso de taxonomías"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_catalog-dcat-themetaxonomy.ttl"
    ```

# Convenciones para `dcat:DataService` {#dataservice}

## Servicios de datos HVD (`dcat:DataService`) {#dataservice-hvd-dataservice}

Los [conjuntos de datos de alto valor (HVD) deben proporcionar acceso programático a sus datos mediante APIs](https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=CELEX:32023R0138). La especificación de servicios de datos se realiza mediante la clase `dcat:DataService` asociada a las distribuciones del dataset a través de `dcat:accessService`.

!!! must semantic "Convención 12"
    Los *datasets* catalogados como HVD **DEBEN** incluir al menos un servicio de datos (`dcat:DataService`) con las siguientes propiedades obligatorias:
    
    1. URL del endpoint (`dcat:endpointURL`)  
    2. Descripción del endpoint (`dcat:endpointDescription`)
    3. Punto de contacto (`dcat:contactPoint`)
    4. Legislación aplicable (`dcatap:applicableLegislation`)
    5. Categoría HVD (`dcatap:hvdCategory`)
    6. Documentación (`foaf:page`)
    7. *Datasets* servidos (`dcat:servesDataset`)


!!! info "Ejemplo de propiedad de acceso al servicio en una distribución"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-hvd-dataservice.ttl"
    ```

!!! info "Nota sobre implementación"
    - Sí el servicio de datos sirve al menos un *dataset* HVD, se aplican los requisitos de implementación según el reglamento HVD.
    - La descripción del endpoint debería seguir especificaciones estándar como OpenAPI.
    - Los servicios deben estar documentados al menos en español.
    - Para *datasets* no HVD, la inclusión de servicios de datos es opcional pero recomendada.

## Modelado de Servicios OGC {#dataservice-ogc-services}

Para mejorar la interoperabilidad y descripción de servicios OGC (`WMS`, `WFS`, `WMTS`, `CSW`, etc.), estos deben modelarse usando `dcat:DataService` en lugar de `dcat:Distribution`.

!!! should technical "Convención 13"
    Los servicios OGC **DEBERÍAN** modelarse como `dcat:DataService` en lugar de `dcat:Distribution`. Esto aplica a:
    
    1. Servicios WMS (Web Map Service)
    2. Servicios WFS (Web Feature Service) 
    3. Servicios CSW (Catalog Service for the Web)
    4. Otros servicios OGC estándar

!!! info "Ejemplo de modelado de servicio cartográfico"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataservice-ogc-services.ttl"
    ```

!!! warning "Importante"
    El uso de `dcat:Distribution` para servicios OGC:

    - No permite describir adecuadamente las capacidades del servicio
    - Dificulta la federación y descubrimiento automático
    - No facilita la vinculación con otros *datasets* servidos

!!! info "Nota sobre implementación"
    Al modelar servicios OGC como `dcat:DataService`:

    - Incluya la URL del `GetCapabilities` en `dcat:endpointDescription`
    - Vincule con los *datasets* servidos usando `dcat:servesDataset`
    - En `dcat:endpointURL` indicar la URL base del servicio sin parámetros.

# Convenciones para `dcat:Dataset` {#dataset}

## Publicador (`dct:publisher`) {#dataset-dct-publisher}
La trazabilidad del publicador debería venir determinada por el identificador de organismos del sector público disponible en el [Directorio Común de unidades orgánicas y oficinas (DIR3)](https://datos.gob.es/es/catalogo/e05188501-directorio-comun-de-unidades-organicas-y-oficinas-dir3) siempre y cuando este disponible.

!!! should organisational "Convención 14" 

    La información de publicador **DEBERÍA** contener un [código identificador DIR3](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) en la propiedad identificador (`dct:identifier`), por ejemplo: `EA0000000`


## Creador (`dct:creator`) {#dataset-dct-creator}
La trazabilidad del creador debería venir determinada por el identificador de organismos del sector público disponible en el [Directorio Común de unidades orgánicas y oficinas (DIR3)](https://datos.gob.es/es/catalogo/e05188501-directorio-comun-de-unidades-organicas-y-oficinas-dir3) siempre y cuando este disponible.

!!! should organisational "Convención 15" 

    La información de creador **DEBERÍA** contener un [código identificador DIR3](https://datos.gob.es/es/recurso/sector-publico/org/Organismo) en la propiedad identificador (`dct:identifier`), por ejemplo: `EA0000000`


## Cobertura geográfica (`dct:spatial`) {#dataset-dct-spatial}

La cobertura geográfica de un conjunto de datos debe describirse de la manera más precisa posible utilizando los identificadores correspondientes a los recursos geográficos del territorio español descritos en el Anexo V de la [NTI-RISP](https://www.boe.es/eli/es/res/2013/02/19/(4)).

!!! must semantic "Convención 16"
    La cobertura geográfica **DEBE** declararse utilizando las URIs del [Anexo V de la NTI-RISP para recursos geográficos del territorio español](https://datos.gob.es/es/recurso/sector-publico/territorio), siguiendo estas reglas:
    
    1. Utilizar el nivel territorial más específico que corresponda al ámbito real del dataset
    2. Evitar el uso de `España` por defecto cuando el ámbito sea más reducido.
    3. No declarar simultáneamente una Comunidad Autónoma y sus provincias.
    4. Para Comunidades Autónomas uniprovinciales, utilizar preferentemente la referencia a la Comunidad Autónoma.


!!! success "Ejemplos de uso correcto"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial_correct.ttl"
    ```

!!! failure "Ejemplos de uso incorrecto"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial_incorrect.ttl"
    ```

## Referencias espaciales geométricas (`dct:spatial` con geometrías) {#dataset-dct-spatial-geometry}

Para describir la cobertura geométrica de los *datasets* de forma interoperable se pueden utilizar diferentes propiedades y formatos estándar, en particular se recomienda utilizar `WKT` ([*Well-Known Text*](https://www.ogc.org/es/publications/standard/sfa/)) para describir la cobertura geométrica.

!!! should semantic "Convención 17"
    Cuando se especifique la cobertura geométrica, se **DEBERÍA** usar `WKT` (según [GeoSPARQL](http://www.opengeospatial.org/standards/geosparql))

!!! info "Ejemplo de uso de geometrías"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dct-spatial-geometry.ttl"
    ```

!!! info "Nota sobre implementación"
    - `dcat:bbox`: Recomendado para especificar el rectángulo delimitador o *bounding box* (`0..1`).
    - `dcat:centroid`: Recomendado para especificar el centro geográfico de un área espacial u otro punto característico (`0..1`).
    - `locn:geometry`: Para geometrías más complejas, extensas o precisas, permite expresar un conjunto de coordenadas que denotan los vértices del área geográfica.


## Distribución (`dcat:distribution`) {#dataset-dcat-distribution}

Obligatoriedad temporal de distribuciones en los datasets

!!! must semantic "Convención 23"

    Todo recurso de tipo `dcat:Dataset` **DEBE** contener al menos una instancia de `dcat:Distribution`. Esta convención tiene como objetivo asegurar la persistencia de la obligatoriedad del modelo de metadatos de la NTI-RISP 2013 hasta su depreciación conforme al nuevo DCAT-AP-ES en el federador de datos.gob.es

!!! info "Ejemplo mínimo de dataset con distribución"

    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-distribution.ttl"
    ```

## Relación explícita con metadatos fuente mediante `adms:identifier` {#dataset-metadata-relation}
La federación y migración de metadatos desde diferentes perfiles y estándares (INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.) hacia DCAT-AP-ES genera la necesidad de enlazar los metadatos fuente con los recursos DCAT-AP-ES generados. Establecer una convención clara facilita la trazabilidad, la interoperabilidad semántica y la gestión eficiente de versiones en procesos de migración y federación entre diferentes modelos de metadatos.

!!! should technical "Convención 24"
    Cuando un recurso DCAT-AP-ES derive de un metadato fuente de otro estándar (por ejemplo: INSPIRE/ISO19139, MARC21, DataCite, EML, Dublin Core, etc.), **DEBERÍA** incluirse una relación mediante la propiedad `adms:identifier` que apunte al identificador persistente del metadato fuente, utilizando un nodo de tipo `adms:Identifier`.

!!! info "Ejemplo de un dataset relacionado con un servicio geográfico"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-metadata-relation.ttl"
    ```

!!! warning "Importante"
    - La URI referenciada en la propiedad `adms:identifier` debe ser persistente y resoluble, preferentemente el identificador completo del metadato fuente.
    - La clase [`adms:Identifier`](https://www.w3.org/TR/vocab-adms/#identifier) requiere proporcionar `skos:notation`, con un tipo de dato que especifique el esquema de identificación (incluyendo el número de versión si es apropiado).
    - Esta convención no impide el uso de otras propiedades de relación (`dct:relation`, `rdfs:seeAlso`, `dcat:qualifiedRelation`) si se requiere mayor granularidad o complementariedad.
    - El uso de `adms:Identifier` como nodo informativo permite enriquecer el enlace para hacerlo más usable en vistas de metadatos de catálogos o para reutilizadores externos.

!!! info "Nota sobre implementación"
    - Usar `adms:identifier` permite incluir propiedades contextuales adicionales sobre el identificador secundario (estándar de conformidad, formato, página de visualización, etc.).
    - Referencia: [Best practices for linking DCAT-AP datasets to alternative metadata descriptions (SEMICeu/DCAT-AP#450)](https://github.com/SEMICeu/DCAT-AP/issues/450)

# Convenciones para `dcat:Distribution` {#distribution}

## Modelado de URLs de acceso en servicios OGC {#distribution-ogc-urls}

Para asegurar un acceso correcto a los servicios OGC y cumplir con los requisitos de INSPIRE, es importante modelar adecuadamente las URLs de acceso a los servicios, tanto si se modelan como `dcat:Distribution` (desaconsejado) como [si se modelan como `dcat:DataService` (recomendado)](#dataservice-ogc-services).

!!! must technical "Convención 21"
    En las distribuciones de servicios OGC, las URLs de acceso **DEBEN** modelarse de la siguiente manera: En `dcat:accessURL`: URL completa de la petición de capacidades del servicio `GetCapabilities` (ej: `http://example.org/wms?request=GetCapabilities&service=WMS`) y en `dct:conformsTo`: URL del estándar OGC correspondiente, ej: `http://www.opengeospatial.org/standards/wms`

!!! info "Ejemplo de descripción del acceso a servicios cartográficos"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_distribution-ogc-urls.ttl"
    ```

!!! warning "Importante"
    - Se recomienda modelar los servicios OGC como DataService en lugar de Distribution ([ver Convención](#dataservice-ogc-services))
    - No usar URLs base sin `GetCapabilities` en las `accessURL` de las distribuciones.

# Convenciones para dcat:contactPoint {#dcat-contactpoint}

Para facilitar la comunicación con los responsables de los *datasets* o *servicios de datos*, se debe proporcionar información de contacto estructurada utilizando la [ontología vCard](https://www.w3.org/TR/vcard-rdf/) para la descripción de personas y organizaciones y no referir directamente a IRIs de la taxonomía como por ejemplo: (`dcat:contactPoint <http://datos.gob.es/recurso/sector-publico/org/Organismo/A00000000>`)

!!! must semantic "Convención 18"
    
    Los *servicios de datos HVD* **DEBEN** incluir al menos un punto de contacto (`dcat:contactPoint`) con alguna de las siguientes propiedades:
    
    1. Correo electrónico (`vcard:hasEmail`) o URL del formulario de contacto (`vcard:hasURL`)

!!! should semantic "Convención 19"
    
    El punto de contacto **DEBERÍA** incluir:
    
    1. Nombre (`vcard:organization-name`)
    2. Número de teléfono (`vcard:hasTelephone`)
    3. Identificador del organismo (`vcard:hasUid`)
    4. Correo electrónico (`vcard:hasEmail`)
    5. URL del formulario de contacto (`vcard:hasURL`)

!!! must organisational "Convención 20"
    
    Los puntos de contacto recogidos en la taxonomía del portal **DEBEN** describirse como un `vcard:Kind` y no directamente con la URI del organismo.


!!! success "Ejemplo de uso correcto"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-contactpoint_correct.ttl"
    ```

!!! failure "Ejemplo de uso incorrecto"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_dataset-dcat-contactpoint_incorrect.ttl"
    ```

!!! warning "Importante"
    
    Todos los valores proporcionados se recomienda que sean de carácter público y persistente, ^^evitando referencias a datos personales^^ o temporalmente inestables, y preferiblemente lo más cercanos al origen del conjuntos de datos.


# Anexo 1. Tabla de mapeo de sectores primarios a Temáticas de datos DCAT-AP {#annex-1-mapping-nti-themes-dcatap-themes}

| Sector primario (NTI) | URI NTI | Temática DCAT-AP | URI DCAT-AP |
|----------------------|---------|------------------|-------------|
| Ciencia y tecnología | http://datos.gob.es/kos/sector-publico/sector/ciencia-tecnologia | Science and Technology | http://publications.europa.eu/resource/authority/data-theme/TECH |
| Comercio | http://datos.gob.es/kos/sector-publico/sector/comercio | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Cultura y ocio | http://datos.gob.es/kos/sector-publico/sector/cultura-ocio | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Demografía | http://datos.gob.es/kos/sector-publico/sector/demografia | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Deporte | http://datos.gob.es/kos/sector-publico/sector/deporte | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Economía | http://datos.gob.es/kos/sector-publico/sector/economia | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Educación | http://datos.gob.es/kos/sector-publico/sector/educacion | Education | http://publications.europa.eu/resource/authority/data-theme/EDUC |
| Empleo | http://datos.gob.es/kos/sector-publico/sector/empleo | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Energía | http://datos.gob.es/kos/sector-publico/sector/energia | Energy | http://publications.europa.eu/resource/authority/data-theme/ENER |
| Hacienda | http://datos.gob.es/kos/sector-publico/sector/hacienda | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Industria | http://datos.gob.es/kos/sector-publico/sector/industria | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Legislación y justicia | http://datos.gob.es/kos/sector-publico/sector/legislacion-justicia | Justice | http://publications.europa.eu/resource/authority/data-theme/JUST |
| Medio ambiente | http://datos.gob.es/kos/sector-publico/sector/medio-ambiente | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Medio Rural | http://datos.gob.es/kos/sector-publico/sector/medio-rural-pesca | Agriculture | http://publications.europa.eu/resource/authority/data-theme/AGRI |
| Salud | http://datos.gob.es/kos/sector-publico/sector/salud | Health | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| Sector público | http://datos.gob.es/kos/sector-publico/sector/sector-publico | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Seguridad | http://datos.gob.es/kos/sector-publico/sector/seguridad | Justice | http://publications.europa.eu/resource/authority/data-theme/JUST |
| Sociedad y bienestar | http://datos.gob.es/kos/sector-publico/sector/sociedad-bienestar | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Transporte | http://datos.gob.es/kos/sector-publico/sector/transporte | Transport | http://publications.europa.eu/resource/authority/data-theme/TRAN |
| Turismo | http://datos.gob.es/kos/sector-publico/sector/turismo | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Urbanismo e infraestructuras | http://datos.gob.es/kos/sector-publico/sector/urbanismo-infraestructuras | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Vivienda | http://datos.gob.es/kos/sector-publico/sector/vivienda | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |


# Anexo 2. Tabla de mapeo entre Temas INSPIRE y Temáticas DCAT-AP {#annex-2-mapping-inspire-themes-dcatap-themes}

| Tema INSPIRE | URI INSPIRE | Temática DCAT-AP | URI DCAT-AP |
|-------------|-------------|------------------|-------------|
| Direcciones (AD) | http://inspire.ec.europa.eu/theme/ad | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Unidades administrativas (AU) | http://inspire.ec.europa.eu/theme/au | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Sistemas de referencia (RS) | http://inspire.ec.europa.eu/theme/rs | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Cuadrículas geográficas (GG) | http://inspire.ec.europa.eu/theme/gg | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Parcelas catastrales (CP) | http://inspire.ec.europa.eu/theme/cp | Regions, Economy | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/ECON |
| Nombres geográficos (GN) | http://inspire.ec.europa.eu/theme/gn | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Hidrografía (HY) | http://inspire.ec.europa.eu/theme/hy | Environment, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Lugares protegidos (PS) | http://inspire.ec.europa.eu/theme/ps | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Redes de transporte (TN) | http://inspire.ec.europa.eu/theme/tn | Transport | http://publications.europa.eu/resource/authority/data-theme/TRAN |
| Elevación (EL) | http://inspire.ec.europa.eu/theme/el | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Geología (GE) | http://inspire.ec.europa.eu/theme/ge | Regions, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Cubierta terrestre (LC) | http://inspire.ec.europa.eu/theme/lc | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Ortoimágenes (OI) | http://inspire.ec.europa.eu/theme/oi | Regions, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/REGI, http://publications.europa.eu/resource/authority/data-theme/TECH |
| Instalaciones agrícolas (AF) | http://inspire.ec.europa.eu/theme/af | Agriculture | http://publications.europa.eu/resource/authority/data-theme/AGRI |
| Monitorización ambiental (AM) | http://inspire.ec.europa.eu/theme/am | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Condiciones atmosféricas (AC) | http://inspire.ec.europa.eu/theme/ac | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Regiones biogeográficas (BR) | http://inspire.ec.europa.eu/theme/br | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Edificios (BU) | http://inspire.ec.europa.eu/theme/bu | Regions | http://publications.europa.eu/resource/authority/data-theme/REGI |
| Recursos energéticos (ER) | http://inspire.ec.europa.eu/theme/er | Energy | http://publications.europa.eu/resource/authority/data-theme/ENER |
| Instalaciones de observación (EF) | http://inspire.ec.europa.eu/theme/ef | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Hábitats y biotopos (HB) | http://inspire.ec.europa.eu/theme/hb | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Salud y seguridad (HH) | http://inspire.ec.europa.eu/theme/hh | Health | http://publications.europa.eu/resource/authority/data-theme/HEAL |
| Uso del suelo (LU) | http://inspire.ec.europa.eu/theme/lu | Economy, Environment | http://publications.europa.eu/resource/authority/data-theme/ECON, http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Recursos minerales (MR) | http://inspire.ec.europa.eu/theme/mr | Economy, Environment, Energy | http://publications.europa.eu/resource/authority/data-theme/ECON, http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/ENER |
| Zonas de riesgos naturales (NZ) | http://inspire.ec.europa.eu/theme/nz | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Oceanográficos (OF) | http://inspire.ec.europa.eu/theme/of | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Distribución de la población (PD) | http://inspire.ec.europa.eu/theme/pd | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Instalaciones de producción (PF) | http://inspire.ec.europa.eu/theme/pf | Economy | http://publications.europa.eu/resource/authority/data-theme/ECON |
| Especies de distribución (SR) | http://inspire.ec.europa.eu/theme/sr | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Suelo (SO) | http://inspire.ec.europa.eu/theme/so | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Distribución de especies (SD) | http://inspire.ec.europa.eu/theme/sd | Environment | http://publications.europa.eu/resource/authority/data-theme/ENVI |
| Servicios de utilidad pública (SU) | http://inspire.ec.europa.eu/theme/su | Society | http://publications.europa.eu/resource/authority/data-theme/SOCI |
| Servicios gubernamentales (US) | http://inspire.ec.europa.eu/theme/us | Government | http://publications.europa.eu/resource/authority/data-theme/GOVE |
| Instalaciones meteorológicas (MF) | http://inspire.ec.europa.eu/theme/mf | Environment, Science and Technology | http://publications.europa.eu/resource/authority/data-theme/ENVI, http://publications.europa.eu/resource/authority/data-theme/TECH |


# Anexo 3. Mapeo de identificadores organizativos {#annex-3-mapping-org-identifiers}

Este anexo proporciona guías para el mapeo entre diferentes sistemas de identificación de organismos, [ver convención](#general-dir3). En el ecosistema de datos abiertos español coexisten diferentes sistemas de identificación de organismos:

1. Códigos DIR3 (oficiales)
2. NIF (identificación fiscal)
3. Códigos internos de ministerios y organismos
4. Identificadores históricos heredados

Esto puede generar inconsistencias al:

* Relacionar *datasets* entre diferentes catálogos
* Vincular organizaciones publicadoras y creadoras
* Mantener la trazabilidad histórica de los datos

**Tabla de equivalencias**

| Tipo ID | Formato | Ejemplo | Uso | Notas |
|---------|---------|---------|-----|-------|
| DIR3 | `EAXXXXXXX` | `EA0000000` | Organismos públicos activos | Identificador principal recomendado |
| NIF | `PAXXXXXXX` | `P28000000` | Organismos privados | Usar como prefijo P + NIF |
| Código interno | Variable | `INE-INT-001` | Uso histórico | Desaconsejado para nuevos *datasets* |


# Anexo 4. Espacios de nombres utilizados en el documento {#annex-4-document-namespaces}

Este anexo proporciona una referencia completa de los espacios de nombres ([*namespaces*](https://www.w3.org/TR/xml-names11/)) utilizados en el perfil DCAT-AP-ES y en los ejemplos de este documento. Los espacios de nombres son fundamentales para:

1. Identificar unívocamente los elementos y propiedades utilizados
2. Evitar conflictos entre vocabularios diferentes
3. Facilitar la validación y procesamiento del RDF

**Ejemplo de declaración de namespaces**
=== "RDF/XML"
    ```xml linenums="1"
    --8<-- "examples/rdf/Conventions_annex-4.rdf"
    ```

=== "TTL"
    ```turtle linenums="1"
    --8<-- "examples/ttl/Conventions_annex-4.ttl"
    ```

Los prefijos listados son los más comúnmente utilizados, aunque técnicamente se podrían usar otros siempre que se declaren correctamente.

| Prefijo | URI | Nombre | Descripción |
|---------|-----|---------|-------------|
| `adms` | `http://www.w3.org/ns/adms#` | Asset Description | Descripción de activos semánticos |
| `cnt`  | `http://www.w3.org/2011/content#` | Representing Content in RDF | Representación de contenidos en RDF |
| `dcat` | `http://www.w3.org/ns/dcat#` | Data Catalog Vocabulary | Vocabulario para describir catálogos de datos |
| `dcatap` | `http://data.europa.eu/r5r/` | DCAT-AP | Extensiones específicas del perfil DCAT-AP |
| `dct` | `http://purl.org/dc/terms/` | Dublin Core Terms | Metadatos básicos para describir recursos |
| `eli` | `http://data.europa.eu/eli/ontology#` | European Legislation Identifier | Identificación de legislación europea |
| `foaf` | `http://xmlns.com/foaf/0.1/` | Friend of a Friend | Vocabulario para describir personas y organizaciones |
| `geo` | `http://www.opengis.net/ont/geosparql#` | GeoSPARQL Ontology | Lenguaje de consulta geográfica de datos RDF |
| `locn` | `http://www.w3.org/ns/locn#` | Location Core | Vocabulario para ubicaciones y direcciones |
| `odrl` | `http://www.w3.org/ns/odrl/2/` | Open Digital Rights Language | Expresión de derechos digitales |
| `prov` | `http://www.w3.org/ns/prov#` | Provenance Ontology | Trazabilidad y procedencia de datos |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` | RDF Schema | Vocabulario básico para definir recursos RDF |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` | RDF Schema | Extensión de RDF para definir clases y propiedades |
| `schema` | `http://schema.org/` | Schema.org | Vocabulario para estructurar datos en la web |
| `skos` | `http://www.w3.org/2004/02/skos/core#` | SKOS | Sistema de organización del conocimiento |
| `spdx` | `http://spdx.org/rdf/terms#` | Software Package Data Exchange | Licencias y paquetes de software |
| `time` | `http://www.w3.org/2006/time#` | Time Ontology | Conceptos temporales y duraciones |
| `vcard` | `http://www.w3.org/2006/vcard/ns#` | vCard Ontology | Ontología para información de contacto |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` | XML Schema | Tipos de datos XML Schema |
