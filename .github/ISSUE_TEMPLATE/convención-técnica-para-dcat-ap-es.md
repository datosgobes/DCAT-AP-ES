---
name: Convención técnica para DCAT-AP-ES
about: Plantilla para discutir o proponer nuevas convenciones técnicas para la aplicación
  de DCAT-AP-ES
title: 'Convención - '
labels: convention, technical
assignees: ''

---

### **Contexto**
Explique el contexto o la necesidad de la nueva convención técnica. ¿Por qué se considera importante esta convención? ¿Qué problema o inconsistencia resuelve?

>[!TIP]
> **Convención técnica**: Aspectos técnicos de implementación, como codificación, identificación de recursos y modelado de entidades.

#### Objetivos de la Convención
Describa los objetivos clave que esta convención busca alcanzar, como:

- Mejorar la interoperabilidad técnica entre sistemas y plataformas.
- Asegurar la correcta identificación y codificación de los recursos para evitar errores.
- Facilitar la integración de los metadatos con otros sistemas y plataformas a través de estándares técnicos comunes.

---

### **Propuesta**
#### Aplicabilidad
Indique la aplicabilidad de la convención y su motivación.

- **Obligatoria** (*MUST*): Debe cumplirse sin excepciones.
- **Recomendada** (*SHOULD*): Se recomienda su cumplimiento, aunque puede haber excepciones justificadas.
- **Opcional** (*MAY*): Es opcional y su uso es libre.

>[!CAUTION]
> **Recuerda**: Si esta convención se aprueba como "*Obligatoria*", se actualizarán las directrices de implementación de **DCAT-AP-ES** y se deberán aplicar las nuevas restricciones en los catálogos de datos abiertos.


#### Convención propuesta
Explique la convención que se propone agregar o modificar, en términos claros. Incluya ejemplos específicos de cómo debería aplicarse esta convención a los metadatos en formato **DCAT-AP-ES**. Por ejemplo:

>**Convención 02**
>
>Sí están definidas las etiquetas de idioma de `dct:title`, `dct:description`, `vcard:organization_name `, `vcard:fn`, `foaf:name`, `dcat:keyword` y `adms:versionNotes` **DEBEN** al menos estar en idioma español `es` y no pueden ser literales vacíos.

>**Convención 06**
>
>Los recursos **DEBEN** tener un identificador único y persistente que cumpla los siguientes requisitos:
>
>1. Incluir la propiedad `dct:identifier` con un valor único para cada recurso.
>2. Mantener la coherencia del identificador aunque el recurso se actualice.
>3. Usar el mismo identificador cuando el recurso se publique en diferentes catálogos.
>
>```turtle
>@prefix dcat: <http://www.w3.org/ns/dcat#> .
>@prefix dct: <http://purl.org/dc/terms/> .
>
># Dataset en el catálogo de datos abiertos 
><http://datos.comunidad.es/dataset/medioambiente/calidad-aire-2024>
>    a dcat:Dataset ;
>    dct:identifier "MA-AIRE-2024" ;
>    dct:title "Calidad del aire 2024"@es .
>
># El mismo dataset en el catálogo CSW (conforme a GeoDCAT-AP)
><https://ide.comunidad.es/catalogo/dataset/calidad-aire-2024> 
>    a dcat:Dataset ;
>    dct:identifier "MA-AIRE-2024" ;
>    dct:title "Calidad del aire 2024"@es .
>```

Añada detalles adicionales sobre cómo esta convención se ajusta al perfil **DCAT-AP-ES**.

---

### **Comentarios Adicionales**
Proporcione cualquier comentario adicional o duda sobre la propuesta, ejemplos o casos de uso que no se hayan cubierto en las secciones anteriores.
