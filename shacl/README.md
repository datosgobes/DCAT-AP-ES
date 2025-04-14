# Guía de Validación SHACL para DCAT-AP-ES

Este directorio contiene los archivos de validación SHACL ([Shapes Constraint Language](https://www.w3.org/TR/shacl/)) para [comprobar la conformidad](https://datos.gob.es/es/blog/shacl-un-lenguaje-para-validar-grafos-rdf) con el perfil de aplicación [DCAT-AP-ES](https://github.com/datosgobes/DCAT-AP-ES).

>[!TIP]
> Más información sobre la validación de [DCAT-AP-ES](https://github.com/datosgobes/DCAT-AP-ES/validacion)  y sus ficheros SHACL.

## Contenido

El repositorio incluye los siguientes archivos SHACL:

- `shacl_common_shapes.ttl`: Restricciones comunes para todas las entidades
- `shacl_catalog_shape.ttl:` Restricciones para catálogos
- `shacl_dataservice_shape.ttl`: Restricciones para servicios de datos
- `shacl_dataset_shape.ttl`: Restricciones para conjuntos de datos
- `shacl_distribution_shape.ttl`: Restricciones para distribuciones
- `shacl_dataservice_shape.ttl`: Restricciones para servicios de datos
- `shacl_mdr-vocabularies.shape.ttl`: Vocabularios controlados y sus restricciones
- `shacl_imports.ttl`: Definiciones de importación para ontologías externas
- `shacl_mdr_imports.ttl`: Definiciones de importación para vocabularios MDR

`hvd/`: Directorio con restricciones adicionales para conjuntos de datos de alto valor (HVD):

- `shacl_common_hvd_shapes.ttl`: Restricciones comunes para todas las entidades
- `shacl_catalog_shape.ttl:` Restricciones para catálogos
- `shacl_dataservice_hvd_shape.ttl`: Restricciones para servicios de datos
- `shacl_dataset_hvd_shape.ttl`: Restricciones para conjuntos de datos
- `shacl_distribution_hvd_shape.ttl`: Restricciones para distribuciones

## Cómo usar los validadores SHACL

### Prerrequisitos

Para ejecutar la validación SHACL necesitarás una de las siguientes herramientas:

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

- **Validación exitosa**: El archivo cumple con todas las restricciones
- **Violaciones**: Errores que deben corregirse para cumplir con NTI-RISP
- **Advertencias**: Problemas no críticos pero que se recomienda solucionar
- **Información**: Sugerencias para mejorar la calidad de los datos

Cada informe de error incluirá:
1. La forma (shape) que ha fallado
2. El valor que ha causado la violación
3. La restricción específica que no se ha cumplido

## Ejemplos de validación

### Validación de un conjunto de datos

```bash
shacl validate --shapes shacl_dataset_shape.ttl --data ejemplo_dataset.ttl
```

### Validación de un catálogo completo

```bash
shacl validate --shapes shacl_catalog_shape.ttl --data ejemplo_catalogo.ttl
```

### Validación de uso de vocabularios controlados

```bash
shacl validate --shapes shacl_vocabularies.shape.ttl --data ejemplo_dataset.ttl
```

## Resolución de problemas comunes

- **Error de sintaxis RDF**: Verifica la sintaxis del archivo a validar usando herramientas como `rapper` o `riot`
- **Prefijos no declarados**: Asegúrate de declarar todos los prefijos usados en tu archivo
- **Valores no conformes**: Revisa los vocabularios controlados para usar exactamente los valores permitidos

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

>[!TIP] 
> ### Consejos para la depuración de RDF
>1. **Validación por etapas**: Valida primero la sintaxis con Rapper o RIOT antes de intentar la validación SHACL
>2. **Fragmentación**: Si tienes un archivo grande, divídelo en partes más pequeñas para identificar mejor los errores
>3. **Prefijos**: Asegúrate de que todos los prefijos estén correctamente definidos
>4. **Valores literales**: Comprueba que los tipos de datos y etiquetas de idioma sean correctos
>5. **IRIs**: Verifica que todas las IRIs sean válidas y resolubles cuando sea posible
