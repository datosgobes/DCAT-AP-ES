#!/bin/bash
set -euo pipefail

# entrypoint.sh - pyshacl Docker wrapper
# Simplifies validation with multiple shapes files

if [ "$#" -eq 0 ] || [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    echo "Usage: docker run [docker-opts] dcat-ap-es/shacl-validation:latest [OPTIONS|COMMAND]"
    echo ""
    echo "Commands:"
    echo "  validate [MODE]           Run unified DCAT-AP-ES validation (default: all)"
    echo "                            Modes: all, model-only, syntax-only, shacl-only"
    echo "  compare-model-shacl       Run model-SHACL comparison validation only"
    echo ""
    echo "PyShacl Options:"
    echo "  -d, --data FILE           Data file to validate (required)"
    echo "  -s, --shapes FILE         Shapes file (can be repeated)"
    echo "  -df, --data-format FMT    Data file format (turtle, xml, json-ld, etc.)"
    echo "  -f, --format FMT          Output format (turtle, human, json-ld)"
    echo "  -a, --advanced            Enable SHACL Advanced Features"
    echo "  -w, --web                 Enable web ontology loading"
    echo "  --help, -h                Show this help"
    echo ""
    echo "Example (Unified validation - all phases):"
    echo "  docker run --rm -v \$PWD:/workspace -w /workspace \\"
    echo "    dcat-ap-es/shacl-validation:latest validate all"
    echo ""
    echo "Example (PyShacl direct):"
    echo "  docker run --rm -v \$PWD/data:/data -v \$PWD/shapes:/shapes \\"
    echo "    dcat-ap-es/shacl-validation:latest \\"
    echo "    -d /data/catalog.ttl \\"
    echo "    -s /shapes/shape1.ttl \\"
    echo "    -s /shapes/shape2.ttl \\"
    echo "    -df turtle -f turtle"
    exit 0
fi

# Handle validate command
if [ "$1" = "validate" ]; then
    shift
    MODE="${1:-all}"
    exec python /usr/local/bin/validate_dcat_ap_es.py "$MODE"
fi

# Handle compare-model-shacl command
if [ "$1" = "compare-model-shacl" ]; then
    shift
    exec python /usr/local/bin/compare_model_shacl.py "$@"
fi

# If first argument is 'pyshacl', pass all arguments directly
if [ "$1" = "pyshacl" ]; then
    exec "$@"
fi

# Otherwise, assume wrapper mode and build pyshacl command
exec pyshacl "$@"
