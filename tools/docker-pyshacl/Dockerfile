# Dockerfile para validador SHACL con pyshacl
# Base: Python Alpine para imagen ligera
FROM python:3.12-alpine

LABEL org.opencontainers.image.source=https://github.com/datosgobes/DCAT-AP-ES
LABEL maintainer=contacto@datos.gob.es
LABEL org.opencontainers.image.description="SHACL validator using pyshacl for DCAT-AP-ES"

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instalar dependencias del sistema necesarias para RDFLib y rapper
RUN apk add --no-cache \
    tini=0.19.0-r3 \
    bash=5.2.37-r0 \
    raptor2=2.0.16-r1 \
    && rm -rf /var/cache/apk/*

# Crear directorio de trabajo
WORKDIR /app

# Instalar pyshacl y dependencias
RUN pip install --no-cache-dir \
    pyshacl==0.30.1 \
    rdflib==7.2.1 \
    && pip list

# Copiar scripts de validación
COPY compare_model_shacl.py /usr/local/bin/compare_model_shacl.py
COPY validate_dcat_ap_es.py /usr/local/bin/validate_dcat_ap_es.py
RUN chmod +x /usr/local/bin/compare_model_shacl.py /usr/local/bin/validate_dcat_ap_es.py

# Copiar script entrypoint
COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Usar tini como init para manejar señales correctamente
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/entrypoint.sh"]

# Por defecto mostrar ayuda
CMD ["--help"]
