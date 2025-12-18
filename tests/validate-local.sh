#!/bin/bash

################################################################################
# Orquestador de Validación Local DCAT-AP-ES
# 
# Wrapper simple que:
# 1. Verifica prerequisitos (Docker, rapper - opcional para uso local)
# 2. Construye la imagen Docker de pyshacl si es necesario
# 3. Llama al contenedor Docker con el comando 'validate'
#
# Uso:
#   ./tests/validate-local.sh [all|model-only|syntax-only|shacl-only] [--rebuild|-r]
#
# Opciones:
#   all             : Ejecutar todas las fases de validación (default)
#   syntax-only     : Solo Fase 0 (sintaxis de formas SHACL)
#   model-only      : Solo Fase 1 (comparación Modelo-SHACL)
#   shacl-only      : Solo Fase 2 (validación semántica de ejemplos)
#   --rebuild, -r   : Forzar reconstrucción de la imagen Docker
#
# Toda la lógica de validación está en Docker: tools/docker-pyshacl/validate_dcat_ap_es.py
################################################################################

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DOCKER_IMAGE="dcat-ap-es/shacl-validation:latest"

# Parse arguments
MODE="all"
REBUILD=false

for arg in "$@"; do
    case $arg in
        --rebuild|-r)
            REBUILD=true
            ;;
        all|model-only|syntax-only|shacl-only)
            MODE="$arg"
            ;;
        --help|-h)
            echo "Uso: $0 [MODE] [OPTIONS]"
            echo ""
            echo "Modos de validación:"
            echo "  all             Ejecutar todas las fases (default)"
            echo "  syntax-only     Solo Fase 0 (sintaxis de formas SHACL)"
            echo "  model-only      Solo Fase 1 (comparación Modelo-SHACL)"
            echo "  shacl-only      Solo Fase 2 (validación semántica)"
            echo ""
            echo "Opciones:"
            echo "  --rebuild, -r   Forzar reconstrucción de imagen Docker"
            echo "  --help, -h      Mostrar esta ayuda"
            exit 0
            ;;
        *)
            log_warning "Argumento desconocido: $arg (ignorado)"
            ;;
    esac
done

# Helper functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_section() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE} $1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Check prerequisites
check_prerequisites() {
    print_section "Verificando Prerequisitos"
    
    # Check for Docker
    if ! command -v docker &> /dev/null; then
        log_error "Docker no encontrado. Instala Docker desde: https://docs.docker.com/get-docker/"
        exit 1
    fi
    log_success "Docker encontrado: $(docker --version)"
    
    # Check if rebuild is requested or image doesn't exist
    if [ "$REBUILD" = true ]; then
        log_info "Reconstrucción forzada de imagen Docker..."
        if docker build -t "$DOCKER_IMAGE" tools/docker-pyshacl; then
            log_success "Imagen Docker shacl-validation reconstruida exitosamente"
        else
            log_error "Error al reconstruir imagen Docker: $DOCKER_IMAGE"
            exit 1
        fi
    elif docker images "$DOCKER_IMAGE" | grep -q shacl-validation; then
        log_success "Imagen Docker DCAT-AP-ES shacl-validation encontrada: $DOCKER_IMAGE"
    else
        # Build shacl-validation Docker image if not exists
        log_info "Construyendo imagen Docker shacl-validation..."
        if docker build -t "$DOCKER_IMAGE" tools/docker-pyshacl; then
            log_success "Imagen Docker shacl-validation construida exitosamente"
        else
            log_error "Error al construir imagen Docker: $DOCKER_IMAGE"
            exit 1
        fi
    fi
}

# Main execution
main() {
    log_info "Validación DCAT-AP-ES - Modo: $MODE"
    
    check_prerequisites
    
    print_section "Ejecutando Validación (Modo: $MODE)"
    
    # Call Docker container with validate command
    # Mount workspace as /workspace and set it as working directory
    # The Python script inside Docker will handle all output and sections
    docker run --rm \
        -v "$PWD:/workspace" \
        -w /workspace \
        "$DOCKER_IMAGE" \
        validate "$MODE"
    
    # Capture exit code and exit with same code (no additional messages)
    exit $?
}

# Run main function
main
