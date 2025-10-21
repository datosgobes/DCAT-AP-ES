# DCAT-AP-ES: Tests and Validation
[![ES](https://img.shields.io/badge/lang-ES-yellow.svg)](README.md) [![EN](https://img.shields.io/badge/lang-EN-blue.svg)](README.en.md)

Automated DCAT-AP-ES validation system with 3 phases: model-SHACL comparison, syntax validation, and semantic conformance.

## Quick Start

```bash
# Validate everything (recommended)
./tests/validate-local.sh all

# Validate individual phases
./tests/validate-local.sh model-only    # Phase 0 only
./tests/validate-local.sh syntax-only   # Phase 1 only
./tests/validate-local.sh shacl-only    # Phase 2 only
```

**Requirement**: Docker installed

**Generated reports**: `tests/validation-reports/SUMMARY.md`

## Validation Phases

### Phase 0: Model-SHACL Comparison
Verifies that all MANDATORY properties from the model (`docs/index.md`) have corresponding SHACL shapes.

**Technology**: Python + rdflib  
**Output**: `model-vs-shacl-report.md` and `.csv`

### Phase 1: Syntax Validation
Validates Turtle syntax of SHACL files defined in `test.ini`.

**Technology**: Raptor rapper  
**Files**: Listed in `tests/test.ini` under `[shacl_shapes]`

**Error example**:
```
rapper: Error - URI file:///workspace/shacl/1.0.0/file.ttl:123 - syntax error
```
The number `:123` indicates the exact error line.

### Phase 2: Semantic Validation
Validates RDF examples against SHACL shapes using pySHACL.

**Technology**: pySHACL  
**Test cases**: Defined in `tests/test.ini` under `[tests]`

| Test Case | Description |
|-----------|-------------|
| `E_DCAT-AP-ES_minimal.ttl` | Mandatory properties only |
| `E_DCAT-AP-ES_full.ttl` | Mandatory + recommended |
| `E_DCAT-AP-ES_Catalog_HVD.ttl` | Minimal HVD |
| `E_DCAT-AP-ES_Catalog_HVD_full.ttl` | Complete HVD |

## test.ini File

Defines which SHACL files and test cases are validated:

```ini
[shacl_shapes]
# SHACL files to validate syntactically (Phase 1)
shacl_catalog_shape.ttl
shacl_dataset_shape.ttl
hvd/shacl_dataset_hvd_shape.ttl

[tests]
# Semantic test cases (Phase 2)
dcatapes_minimal = E_DCAT-AP-ES_minimal.ttl
dcatapes_full = E_DCAT-AP-ES_full.ttl
```

**Base shapes** (loaded automatically):
- `shacl_mdr-vocabularies.shape.ttl` - Controlled vocabularies
- `shacl_common_shapes.ttl` - Reusable shapes

## GitHub Actions

The workflow `.github/workflows/validate-shacl.yml` automatically runs `validate-local.sh all` on:
- Pull Requests modifying `shacl/**/*.ttl`, `examples/**/*.{rdf,ttl}` files, or the workflow
- Pushes to `main` and `develop` branches

**Artifacts**: Reports uploaded as artifacts (30-day retention)  
**PR Comments**: `SUMMARY.md` content published automatically

## Troubleshooting

**Syntax error with line number**:
```sh
[ERROR] ✗ shacl_mdr-vocabularies.shape.ttl
    rapper: Parsing URI file:///workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl with parser turtle
    rapper: Error - URI file:///workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl:139 - syntax error, unexpected a
    rapper: Failed to parse file /workspace/shacl/1.0.0/shacl_mdr-vocabularies.shape.ttl turtle content
    rapper: Parsing returned 93 triples
```
→ Check line 139 of the file (URIs, commas, periods, literals)

**SHACL violation**:
```
sh:resultMessage "Missing required property dcat:distribution"
```
→ Add mandatory property or verify its reference

**Unrecognized class**:
```
sh:resultMessage "Value does not have class Y"
```
→ Check explicit `rdf:type` declaration

## Running Tests Locally

### Prerequisites

The `validate-local.sh` script handles everything automatically:
- Verifies Docker installation
- Builds validation Docker image if needed
- Runs all validation phases
- Generates reports in `tests/validation-reports/`

**Single requirement**: Docker installed
```bash
# Install Docker
# Follow instructions at: https://docs.docker.com/get-docker/
```

### Unified Validation Script

```bash
# Run all phases (recommended)
./tests/validate-local.sh all

# Or run specific phases
./tests/validate-local.sh model-only      # Phase 0: Model-SHACL Comparison
./tests/validate-local.sh syntax-only     # Phase 1: SHACL Syntax Validation
./tests/validate-local.sh shacl-only      # Phase 2: Semantic Validation

# Without arguments = 'all'
./tests/validate-local.sh
```

**Reports location**: `tests/validation-reports/`
- `SUMMARY.md` - Executive summary of all phases
- `model-vs-shacl-report.md` - Detailed Model-SHACL comparison
- `model-vs-shacl-report.csv` - Excel-exportable format
- `*-report.ttl` - SHACL reports in Turtle format

## Understanding Validation Results

### SHACL Severity Levels

- **Violation** (`sh:Violation`): Failed mandatory constraint → **Build fails**
- **Warning** (`sh:Warning`): Missing recommended property → **Build passes with warnings**
- **Info** (`sh:Info`): Missing optional property → **Build passes**

### Expected Results

```md
### Phase 0: Model-SHACL Comparison
**Purpose:** Verify that the documentation model has corresponding SHACL definitions

- **Status:** ✅ PASSED
- **CRITICAL Issues:** 0
- **Informational Warnings:** 29 WARN, 0 INFO (non-blocking)

---

### Phase 1: Syntax Validation (SHACL Shapes)
**Purpose:** Verify that SHACL shape files are syntactically valid RDF/Turtle

- **Syntax Errors:** 1
- **Status:** ❌ ERROR

---

### Phase 2: Semantic Validation (RDF Examples against SHACL)
**Purpose:** Validate RDF example files against SHACL shape constraints

| Test Case | Expected | Status |
|-----------|----------|--------|
| DCAT-AP-ES Minimal Example | Warnings allowed | ✅ PASSED |
| DCAT-AP-ES Full Example | Full conformance | ✅ PASSED |
| DCAT-AP-ES HVD Minimal Example | Warnings allowed | ✅ PASSED |
| DCAT-AP-ES HVD Full Example | Full conformance | ✅ PASSED |

## Statistics

- **Phase 0 (Model-SHACL):** CRITICAL Issues: 0
- **Phase 1 (Syntax):** Errors: 1
- **Phase 2 (Semantic):** Test Failures: 0
```

## Continuous Integration

The GitHub Actions workflow runs automatically on:

- **Pull Requests** affecting:
    - `shacl/**/*.ttl`
    - `examples/**/*.rdf`
    - `examples/**/*.ttl`
    - `.github/workflows/validate-shacl.yml`

- **Changes to main/develop branches**

### Workflow Artifacts

Validation reports uploaded as artifacts:
- Retention: 30 days
- Name: `shacl-validation-reports`
- Contents:
    - `minimal-report.ttl`
    - `full-report.ttl`
    - `hvd-report.txt`
    - `hvd-full-report.ttl`
    - `SUMMARY.md`

### Pull Request Comments

The workflow automatically comments on PRs with:
- Test results summary table
- Pass/warning/fail indicators
- Link to detailed artifact reports

## References

- **DCAT-AP-ES**: https://datosgobes.github.io/DCAT-AP-ES/
- **SHACL Spec**: https://www.w3.org/TR/shacl/
