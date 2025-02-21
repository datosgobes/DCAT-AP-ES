---
name: Convención técnica o semántica para DCAT-AP-ES
about: Plantilla para discutir o proponer nuevas convenciones técnicas o semánticas
  para la aplicación de DCAT-AP-ES
title: 'Convención - '
labels: convention
assignees: ''

---

### **Contexto**

Explique el contexto o la necesidad de la nueva convención técnica o semántica. ¿Por qué se considera importante esta convención? ¿Qué problema o inconsistencia resuelve?

---

### **Objetivos de la Convención**

Describa los objetivos clave que esta convención busca alcanzar, como la mejora de la interoperabilidad, la claridad en el intercambio de datos, o la alineación con otras normativas nacionales o internacionales.

#### Beneficios de la Convención

Describa los beneficios que esta convención aportaría al proyecto. Ejemplo:

- Mejora en la legibilidad e interoperabilidad.
- Reducción de errores comunes.
- Coherencia semántica.

---

### **Propuesta**

#### Tipo de Convención

Indique el tipo de convención que se está discutiendo:

- **Convención técnica**: Aspectos técnicos de implementación, como codificación, identificación de recursos y modelado de entidades.
- **Convención semántica**: Reglas que aseguran la coherencia semántica en la descripción de los recursos.

#### **Categoría de la Convención**

Indique si la convención es:

- **Obligatoria** (*MUST*): Debe cumplirse sin excepciones.
- **Recomendada** (*SHOULD*): Se recomienda su cumplimiento, aunque puede haber excepciones justificadas.
- **Opcional** (*MAY*): Es opcional y su uso es libre.

>[!CAUTION]
> **Recuerda**: Si esta convención se aprueba como "*Obligatoria*", se actualizarán las directrices de implementación de **DCAT-AP-ES** y se deberán aplicar las nuevas restricciones en los catálogos de datos abiertos.


#### Convención propuesta
Explique la convención que se propone agregar o modificar, en términos claros. Incluya ejemplos específicos de cómo debería aplicarse esta convención a los metadatos en formato **DCAT-AP-ES**. Por ejemplo:

    >- **Convención 02**: Las etiquetas de idioma, como `dct:title`, `dct:description`, `foaf:name`, etc., *DEBEN* estar al menos en idioma español (`es`) y no pueden ser literales vacíos.

    >- **Convención 06**: Los recursos *DEBEN* tener un identificador único y persistente que cumpla los siguientes requisitos: 1. Incluir la propiedad `dct:identifier` con un valor único para cada recurso. 2. Mantener la coherencia del identificador aunque el recurso se actualice. 3. Usar el mismo identificador cuando el recurso se publique en diferentes catálogos.

Añada detalles adicionales sobre cómo esta convención se ajusta al perfil **DCAT-AP-ES**.

---

### **Comentarios Adicionales**

Proporcione cualquier comentario adicional o duda sobre la propuesta, ejemplos o casos de uso que no se hayan cubierto en las secciones anteriores.
