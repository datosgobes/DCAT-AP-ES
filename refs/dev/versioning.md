# Versionado de MKDocs (`mike`)
Para aplicar versionado con [mike](https://github.com/jimporter/mike) y Material for MkDocs en tu proyecto, puedes seguir estos pasos básicos:

1. Instala “mike”:  
   Asegúrate de incluir “mike” en tus dependencias. Por ejemplo, en la sección de instalación de tu [`pyproject.toml`](../../pyproject.toml) o en tu entorno personalizado con pip:
   ```sh
   pip install mike
   ```

2. Configura MkDocs para usar “mike”:  
   En tu mkdocs.yml, agrega la sección “version” dentro de “extra”:
   ````yaml
   ```yaml
   # filepath: mkdocs.yml
   # ...existing code...
   extra:
     version:
       provider: mike
   # ...existing code...
   ```
   ````

## Uso Local de Mike para Pruebas

Puedes probar el versionado localmente con estos comandos:

```bash
# Instalar mike si aún no está instalado
pip install mike

# Generar una versión específica (sin hacer push)
mike deploy 1.0 latest

# Establecer la versión predeterminada (sin hacer push)
mike set-default latest

# Servir localmente las versiones
mike serve
```

## Gestión de Versiones

### Publicar una Nueva Versión

Cuando quieras publicar una nueva versión:

```bash
# Para versión 1.1 por ejemplo
mike deploy --push --update-aliases 1.1 latest

# Si es una versión estable y quieres marcarla como "stable"
mike deploy --push --update-aliases 1.1 latest stable
```

### Configurar Alias Personalizados

Puedes usar múltiples alias para cada versión:

```bash
# Ejemplo para una versión beta
mike deploy --push 2.0-beta dev
```

### Advertencia de Versión Obsoleta

Si quieres mostrar una advertencia cuando los usuarios no están viendo la última versión, crea un archivo main.html con:

```html
{% extends "base.html" %}

{% block outdated %}
  No estás viendo la última versión.
  <a href="{{ '../' ~ base_url }}">
    <strong>Haz clic aquí para ir a la última versión.</strong>
  </a>
{% endblock %}
```

## Estructura de URLs resultante

Con esta configuración, tus documentos estarán disponibles en URLs con la siguiente estructura:

- https://datosgobes.github.io/DCAT-AP-ES/1.0/ (versión específica)
- https://datosgobes.github.io/DCAT-AP-ES/latest/ (alias para la última versión)

La URL raíz (https://datosgobes.github.io/DCAT-AP-ES/) redirigirá automáticamente a la versión predeterminada.

## Consideraciones Multilingüe

Como tu proyecto usa `mkdocs-static-i18n`, la estructura de URLs incluirá idiomas y versiones:

- https://datosgobes.github.io/DCAT-AP-ES/1.0/es/ (versión 1.0, español)
- https://datosgobes.github.io/DCAT-AP-ES/1.0/en/ (versión 1.0, inglés)

Con esto tendrás un sistema de versionado completo para tu documentación.