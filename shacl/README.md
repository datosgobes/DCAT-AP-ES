# Guía de Validación SHACL para DCAT-AP-ES
- [Guía de Validación SHACL para DCAT-AP-ES](#guía-de-validación-shacl-para-dcat-ap-es)
  - [Contenido](#contenido)
  - [Validación para principiantes (herramientas online)](#validación-para-principiantes-herramientas-online)
    - [ITB SHACL Validator - Validador UE](#itb-shacl-validator---validador-ue)
    - [SHACL Play! - Herramientas completas](#shacl-play---herramientas-completas)
    - [Cómo validar paso a paso](#cómo-validar-paso-a-paso)
    - [Ejemplos de validación online](#ejemplos-de-validación-online)
    - [Otras herramientas online útiles](#otras-herramientas-online-útiles)
  - [Validación avanzada](#validación-avanzada)
    - [Prerrequisitos](#prerrequisitos)
    - [Validación con Apache Jena](#validación-con-apache-jena)
    - [Validación con pySHACL (Python)](#validación-con-pyshacl-python)
  - [Interpretación de resultados](#interpretación-de-resultados)
  - [Resolución de problemas comunes](#resolución-de-problemas-comunes)
- [Apéndice: Herramientas de validación RDF](#apéndice-herramientas-de-validación-rdf)
  - [Validación con Rapper (Raptor RDF Syntax Library)](#validación-con-rapper-raptor-rdf-syntax-library)
  - [Validación con RIOT (RDF I/O Technology)](#validación-con-riot-rdf-io-technology)
  - [Validación con Apache Jena](#validación-con-apache-jena-1)

---

Este directorio contiene los archivos de validación SHACL ([Shapes Constraint Language](https://www.w3.org/TR/shacl/)) para [comprobar la conformidad](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf) con el perfil de aplicación [DCAT-AP-ES](https://github.com/datosgobes/DCAT-AP-ES).

>[!TIP]
> Más información sobre la validación de [DCAT-AP-ES](https://datosgobes.github.io/DCAT-AP-ES/validacion)  y sus ficheros SHACL.

## Contenido

El repositorio incluye los siguientes archivos SHACL:

- `shacl_common_shapes.ttl`: Restricciones comunes para todas las entidades
- `shacl_catalog_shape.ttl:` Restricciones para catálogos
- `shacl_dataservice_shape.ttl`: Restricciones para servicios de datos
- `shacl_dataset_shape.ttl`: Restricciones para conjuntos de datos
- `shacl_distribution_shape.ttl`: Restricciones para distribuciones
- `shacl_mdr-vocabularies.shape.ttl`: Vocabularios controlados y sus restricciones
- `shacl_imports.ttl`: Definiciones de importación para ontologías externas
- `shacl_mdr_imports.ttl`: Definiciones de importación para vocabularios MDR

`hvd/`: Directorio con restricciones adicionales para conjuntos de datos de alto valor (HVD):

- `shacl_common_hvd_shapes.ttl`: Restricciones comunes para todas las entidades
- `shacl_catalog_shape.ttl:` Restricciones para catálogos
- `shacl_dataservice_hvd_shape.ttl`: Restricciones para servicios de datos
- `shacl_dataset_hvd_shape.ttl`: Restricciones para conjuntos de datos
- `shacl_distribution_hvd_shape.ttl`: Restricciones para distribuciones

## Validación para principiantes (herramientas online)

### ITB SHACL Validator - Validador UE

El [SHACL Validator del ITB](https://www.itb.ec.europa.eu/shacl/any/upload) es el validador oficial de la Comisión Europea, perfecto para validar catálogos DCAT-AP-ES:

**Características principales:**
- Validador oficial de la Comisión Europea
- Interfaz simple y clara
- Soporte completo para SHACL estándar
- Informes de validación detallados
- [Web and command-line application](https://github.com/ISAITB/shacl-validator)

### SHACL Play! - Herramientas completas

[SHACL Play!](https://shacl-play.sparna.fr/play/) ofrece un conjunto más amplio de herramientas para trabajar con SHACL:

**Características principales:**
- Validación RDF contra formas SHACL
- Generación de documentación y diagramas
- Conversión entre formatos RDF
- [TopBraid SHACL API](https://github.com/TopQuadrant/shacl) de TopQuadrant

### Cómo validar paso a paso

#### Opción 1: ITB SHACL Validator (recomendado)

1. **Accede al validador**: https://www.itb.ec.europa.eu/shacl/any/upload
2. **Cargar archivos SHACL**:
   - En "External shapes", selecciona "File"
   - Carga los archivos `.ttl` necesarios de este repositorio:
     - `shacl_common_shapes.ttl` (siempre necesario)
     - El archivo específico: `shacl_catalog_shape.ttl`, `shacl_dataset_shape.ttl`, etc.
     - `shacl_mdr-vocabularies.shape.ttl` (para vocabularios controlados)
3. **Cargar tu archivo a validar**:
   - En "Content to validate", selecciona "File"
   - Carga tu archivo RDF (Turtle, RDF/XML, JSON-LD, etc.)
4. **Ejecutar validación**: Haz clic en "Validate"

#### Opción 2: SHACL Play! (más funcionalidades)

1. **Accede a SHACL Play!**: https://shacl-play.sparna.fr/play/validate
2. **Ve a la sección "RDF a validar"**
3. **Cargar los archivos SHACL de DCAT-AP-ES**:
   - En "Forma (Shape)", selecciona " Cargar" 
   - Carga los mismos archivos `.ttl` que en la opción anterior
4. **Cargar tu archivo a validar**:
   - En "RDF a validar", selecciona "Cargar" y carga tu archivo RDF
5. **Ejecutar validación**: Haz clic en "Validar"

>[!TIP]
> **Para HVD (High Value Datasets)**: También carga los archivos del directorio `hvd/` correspondientes

### Ejemplos de validación online

**Validar un conjunto de datos:**
- Archivos SHACL: `shacl_common_shapes.ttl` + `shacl_dataset_shape.ttl` + `shacl_mdr-vocabularies.shape.ttl`
- Tu archivo: dataset en formato RDF/Turtle

**Validar un catálogo:**
- Archivos SHACL: `shacl_common_shapes.ttl` + `shacl_catalog_shape.ttl`
- Tu archivo: catálogo en formato RDF/Turtle

**Validar un dataset HVD:**
- Archivos SHACL: `shacl_common_shapes.ttl` + `shacl_dataset_shape.ttl` + `hvd/shacl_common_hvd_shapes.ttl` + `hvd/shacl_dataset_hvd_shape.ttl`
- Tu archivo: dataset HVD en formato RDF/Turtle

### Otras herramientas online útiles

- **[ITB SHACL Validator](https://www.itb.ec.europa.eu/shacl/shacl/upload)**: Validador oficial de la Comisión Europea
- **[SHACL Play!](https://shacl-play.sparna.fr/play/)**: Conjunto completo de herramientas SHACL
- **[RDF Translator](http://rdf-translator.appspot.com/)**: Convierte entre formatos RDF
- **[Zazuko SHACL Playground](https://shacl-playground.zazuko.com/)**: Validador de formas personalizadas.
- **[JSON-LD Playground](https://json-ld.org/playground/)**: Trabaja con JSON-LD
- **[SPARQL Playground](https://sparql.org/)**: Prueba consultas SPARQL

---

## Validación avanzada

### Prerrequisitos

Para ejecutar la validación SHACL desde línea de comandos necesitarás una de las siguientes herramientas:

- [Apache Jena](https://jena.apache.org/)
- [TopBraid SHACL API](https://github.com/TopQuadrant/shacl)
- [RDF4J SHACL](https://rdf4j.org/documentation/programming/shacl/) 
- [pySHACL](https://github.com/RDFLib/pySHACL)

### Validación con Apache Jena

1. Descarga [Apache Jena](https://jena.apache.org/download/) e instálalo

2. Ejecuta el validador SHACL con el siguiente comando:

```bash
# Sintaxis general
shacl validate --shapes {ARCHIVO_SHACL.ttl} --data {ARCHIVO_A_VALIDAR.ttl}

# Ejemplo para validar un dataset
shacl validate --shapes shacl_dataset_shape.ttl --data dataset-ejemplo.ttl

# Para validación completa con todos los archivos SHACL
shacl validate --shapes shacl_common_shapes.ttl,shacl_dataset_shape.ttl,shacl_vocabularies.shape.ttl --data dataset-ejemplo.ttl
```

3. El resultado mostrará los errores de validación si existen

### Validación con pySHACL (Python)

1. Instala [pySHACL](https://github.com/RDFLib/pySHACL):
```bash
pip install pyshacl
```

2. Ejecuta la validación:
```bash
pyshacl -s shacl_dataset_shape.ttl -e shacl_common_shapes.ttl,shacl_vocabularies.shape.ttl -df turtle -sf turtle dataset-ejemplo.ttl
```

Donde
 - `-s` es una ruta (opcional) al SHACL que se va a utilizar
 - `-e` es una ruta (opcional) a un grafo ontológico adicional que importar
 - `-f` es el formato de salida del ValidationReport (`human` = informe de validación legible por humanos)
 - m` activa la función meta-shacl
 - `-a` activa las funciones avanzadas de SHACL
 - j` habilita las características SHACL-JS (si `pyshacl[js]` está instalado)

## Interpretación de resultados

La validación SHACL generará un informe con los siguientes posibles resultados:

- **✅ Validación exitosa**: El archivo cumple con todas las restricciones
- **❌ Violaciones**: Errores que deben corregirse para cumplir con DCAT-AP-ES
- **⚠️ Advertencias**: Problemas no críticos pero que se recomienda solucionar
- **ℹ️ Información**: Sugerencias para mejorar la calidad de los datos

Cada informe de error incluirá:
1. La forma (*shape*) que ha fallado
2. El valor que ha causado la violación
3. La restricción específica que no se ha cumplido

### Ejemplos de validación avanzada

**Validación básica de un conjunto de datos:**
```bash
shacl validate --shapes shacl_dataset_shape.ttl --data ejemplo_dataset.ttl
```

**Validación de un catálogo completo:**
```bash
shacl validate --shapes shacl_catalog_shape.ttl --data ejemplo_catalogo.ttl
```

**Validación con múltiples archivos SHACL:**
```bash
# Para un dataset estándar
shacl validate --shapes shacl_common_shapes.ttl,shacl_dataset_shape.ttl,shacl_mdr-vocabularies.shape.ttl --data dataset-ejemplo.ttl

# Para un dataset HVD
shacl validate --shapes shacl_common_shapes.ttl,shacl_dataset_shape.ttl,hvd/shacl_common_hvd_shapes.ttl,hvd/shacl_dataset_hvd_shape.ttl --data dataset-hvd-ejemplo.ttl
```

## Resolución de problemas comunes

### Errores frecuentes y soluciones

- **Error de sintaxis RDF**: Verifica la sintaxis del archivo a validar usando [SHACL Play!](https://shacl-play.sparna.fr/play/), `rapper` o `riot`. Ver [Herramientas de validación RDF](#apéndice-herramientas-de-validación-rdf)
- **Prefijos no declarados**: Asegúrate de declarar todos los prefijos usados en tu archivo
- **Valores no conformes**: Revisa los vocabularios controlados para usar exactamente los valores permitidos
- **IRIs mal formadas**: Verifica que todas las IRIs sean válidas

### Consejos para una validación exitosa

1. **Empieza simple**: Valida primero con herramientas online como SHACL Play!
2. **Valida por etapas**: Primero la sintaxis RDF, luego las formas SHACL  
3. **Usa los ejemplos**: Consulta el directorio `examples/` del repositorio
4. **Revisa los vocabularios**: Usa solo valores de los vocabularios controlados especificados
5. **Documenta tu proceso**: Guarda los informes de validación para referencia futura

>[!NOTE]
> Si encuentras problemas específicos con las formas SHACL de DCAT-AP-ES, puedes [abrir un issue](https://github.com/datosgobes/DCAT-AP-ES/issues) en el repositorio.

---

# Apéndice: Herramientas de validación RDF

## Validación con Rapper (Raptor RDF Syntax Library)

[Rapper](http://librdf.org/raptor/) es una herramienta para validar y convertir entre diferentes formatos RDF.

### Instalación

```bash
# En Ubuntu/Debian
sudo apt-get install raptor2-utils

# En macOS (con Homebrew)
brew install raptor
```

### Uso básico

```bash
# Validar sintaxis RDF/Turtle
rapper -i turtle -o ntriples archivo.ttl

# Convertir entre formatos
rapper -i turtle -o rdfxml archivo.ttl > archivo.rdf
```

### Opciones comunes

- `-i formato`: Especifica el formato de entrada (turtle, rdfxml, etc.)
- `-o formato`: Especifica el formato de salida (ntriples, rdfxml, turtle, etc.)
- `-c`: Solo comprueba la sintaxis sin generar salida

## Validación con RIOT (RDF I/O Technology)

RIOT es parte de Apache Jena y proporciona validación y conversión de RDF.

### Instalación

Viene incluido con Apache Jena. [Descarga Jena](https://jena.apache.org/download/index.cgi) y extrae el paquete.

### Uso básico

```bash
# Validar un archivo RDF
riot --validate archivo.ttl

# Convertir entre formatos
riot --syntax=Turtle --output=RDF/XML archivo.ttl > archivo.rdf
```

### Opciones comunes

- `--validate`: Validar sin producir salida
- `--syntax=LANG`: Especificar el formato de entrada (Turtle, RDF/XML, etc.)
- `--output=FMT`: Especificar el formato de salida

## Validación con Apache Jena

Apache Jena proporciona un conjunto completo de herramientas para trabajar con RDF y SPARQL.

### Instalación

[Descarga Apache Jena](https://jena.apache.org/download/index.cgi) y configura las variables de entorno:

```bash
export JENA_HOME=/ruta/a/jena
export PATH=$PATH:$JENA_HOME/bin
```

### Comandos útiles

**1. Parsear y validar RDF**
```bash
riot --validate archivo.ttl
```

**2. Ejecutar consultas SPARQL**
```bash
sparql --data=archivo.ttl --query=consulta.rq
```

**3. Servidor Fuseki para SPARQL**
```bash
fuseki-server --mem /ds
# Accede en http://localhost:3030
```

**4. Validador SHACL**
```bash
shacl validate --shapes shapes.ttl --data data.ttl
```

### Consejos para una validación exitosa

1. **Validación por etapas**: Valida primero la sintaxis con Rapper o RIOT antes de intentar la validación SHACL
2. **Fragmentación**: Si tienes un archivo grande, divídelo en partes más pequeñas para identificar mejor los errores
3. **Prefijos**: Asegúrate de que todos los prefijos estén correctamente definidos
4. **Valores literales**: Comprueba que los tipos de datos y etiquetas de idioma sean correctos
5. **IRIs**: Verifica que todas las IRIs sean válidas y resolubles cuando sea posible
