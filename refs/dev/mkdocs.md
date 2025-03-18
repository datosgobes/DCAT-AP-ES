## Uso de MkDocs

Este documento proporciona instrucciones básicas para configurar y usar [MkDocs Material](https://squidfunk.github.io/mkdocs-material/reference/) para generar documentación.

---

### Requisitos previos

- [Python](https://www.python.org/downloads/) 3.6 o superior
- [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)

### Instalación

**Clonar el repositorio:**

```sh
git clone https://github.com/datosgobes/DCAT-AP-ES.git
cd DCAT-AP-ES
```

> [!TIP]
> El archivo `pyproject.toml` se utiliza para configurar y administrar proyectos en Python, especialmente cuando se usa [`PDM`](https://pdm-project.org/en/latest/) para la gestión de dependencias y empaquetado. Aquí tienes una guía rápida sobre cómo usarlo:

#### 1. **Instalar PDM**  

Si no tienes [`PDM` instalado](https://pdm-project.org/en/latest/), sigue los pasos según tu sistema operativo:

**En Linux/Mac:**  
Ejecuta el siguiente comando en la terminal:

```bash
curl -sSL https://pdm-project.org/install-pdm.py | python3 -
```

> [!NOTA]  
> Después de la instalación, agrega `bin` al `PATH` ejecutando:  
> ```bash
> export PATH=/home/admin/.local/bin:$PATH
> ```

**En Windows:**  
Ejecuta el siguiente comando en **PowerShell**:

```powershell
(Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | python -
```

> [!IMPORTANTE]  
> Si usas Windows, agrega la ruta del ejecutable de PDM al `PATH`. Para ello:  
> 1. Abre **Panel de control** → **Sistema** → **Configuración avanzada del sistema**.  
> 2. En la pestaña **Opciones avanzadas**, haz clic en **Variables de entorno**.  
> 3. Busca la variable `Path`, edítala y agrega la ruta donde se instaló `pdm` (por ejemplo, `C:\Users\tu-usuario\AppData\Roaming\Python\Scripts`).  
> 4. Guarda los cambios y reinicia la terminal.


#### 2. **Instalar dependencias**  

Después de instalar PDM, instala las dependencias del proyecto que están en `pyproject.toml`:

```sh
pdm install
```

---

#### 3. **Activar el entorno virtual**  

Según tu sistema operativo, usa el siguiente comando:

**En Linux/Mac:**  

```bash
source .venv/bin/activate
```

**En Windows (CMD o PowerShell):**  

```powershell
.venv\Scripts\activate
```

### Estructura del proyecto

Asegúrate de que tu proyecto tenga la siguiente estructura:

```
DCAT-AP-ES/
├── docs/
│   ├── index.md
│   ├── ... (otros archivos Markdown)
├── mkdocs.yml
└── README.md
```

- **docs/**: Carpeta que contiene los archivos Markdown para la documentación.
- **mkdocs.yml**: Archivo de configuración de MkDocs.

### Configuración de MkDocs

Ejemplo de archivo `mkdocs.yml`:

```yaml
site_name: "Nombre del Sitio"
theme:
  name: "material"

nav:
  - Inicio: index.md
  - Página 1: page1.md
  - Página 2: page2.md

markdown_extensions:
  - toc:
      permalink: true
  - admonition
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.superfences
  - pymdownx.tabbed
  - pymdownx.snippets
```

### Generar y servir la documentación

1. **Navega al directorio del proyecto:**

   ```sh
   cd DCAT-AP-ES
   ```

2. **Inicia el servidor de desarrollo:**

   ```sh
   mkdocs serve -a 127.0.0.1:8088
   ```

3. **Abre tu navegador y ve a:**

   ```
   http://127.0.0.1:8088
   ```

### Construir la documentación para Producción

Para generar los archivos estáticos de la documentación:

```sh
mkdocs build
```

Los archivos generados se ubicarán en la carpeta `site/`.

### Depurar MkDocs

Para depurar MkDocs, sigue estos pasos:

```sh
cd DCAT-AP-ES
mkdocs serve -a 127.0.0.1:8088
```

### Recursos adicionales

- [Documentación oficial de MkDocs](https://www.mkdocs.org/)
- [Material para MkDocs](https://squidfunk.github.io/mkdocs-material/)
