#!/usr/bin/env python3
"""
Script Unificado de Validación DCAT-AP-ES

Realiza 3 fases complementarias de validación:
- Fase 0: Comparación Modelo-SHACL (modelo de documentación vs formas SHACL)
- Fase 1: Validación Sintáctica (validar archivos de formas SHACL)
- Fase 2: Validación Semántica (ejemplos RDF contra formas SHACL)

Este script se ejecuta dentro del contenedor Docker y genera un SUMMARY.md unificado

Uso:
    python3 validate_dcat_ap_es.py [all|model-only|syntax-only|shacl-only]
"""

import os
import sys
import argparse
import subprocess
import configparser
from pathlib import Path
from datetime import datetime
from rdflib import Graph
from pyshacl import validate

# Color codes
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'  # No Color

class Validator:
    def __init__(self, repo_root, mode='all'):
        self.repo_root = repo_root
        self.repo_url = f'https://github.com/datosgobes/DCAT-AP-ES'
        self.mode = mode
        self.report_dir = os.path.join(repo_root, 'tests/validation-reports')
        self.test_config = os.path.join(repo_root, 'tests/test.ini')
        self.shacl_dir = os.path.join(repo_root, 'shacl')
        self.examples_dir = os.path.join(repo_root, 'examples')
        
        # Initialize counters
        self.syntax_errors = 0
        self.shacl_errors = 0
        self.model_critical = 0
        self.model_warnings = 0
        self.model_info = 0
        
        # Track which phases were executed
        self.phase_0_executed = False
        self.phase_1_executed = False
        self.phase_2_executed = False
        
        # Create report directory
        os.makedirs(self.report_dir, exist_ok=True)
    
    def log_info(self, msg):
        print(f"{BLUE}[INFO]{NC} {msg}")
    
    def log_success(self, msg):
        print(f"{GREEN}[SUCCESS]{NC} {msg}")
    
    def log_warning(self, msg):
        print(f"{YELLOW}[WARNING]{NC} {msg}")
    
    def log_error(self, msg):
        print(f"{RED}[ERROR]{NC} {msg}")
    
    def print_section(self, title):
        print(f"\n{BLUE}{'='*60}{NC}")
        print(f"{BLUE}{title:^60}{NC}")
        print(f"{BLUE}{'='*60}{NC}\n")
    
    def run_command(self, cmd, shell=False):
        """Run shell command and return output."""
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True)
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            self.log_error(f"Failed to run command: {e}")
            return 1, "", str(e)
    
    def phase_0_model_shacl(self):
        """Fase 0: Comparación Modelo-SHACL - llama a compare_model_shacl.py directamente."""
        self.phase_0_executed = True
        self.print_section("Fase 0: Comparación Modelo-SHACL")
        
        self.log_info("Comparando documentación del modelo (docs/index.md) contra formas SHACL...")
        
        # Call compare_model_shacl.py directly (we're inside the container)
        cmd = ['python', '/usr/local/bin/compare_model_shacl.py']
        
        exit_code, stdout, stderr = self.run_command(cmd)
        
        # Print output
        if stdout:
            print(stdout)
        if stderr and 'ERROR' in stderr:
            print(stderr)
        
        # Check for CRITICAL issues and warnings
        model_report = os.path.join(self.report_dir, 'model-vs-shacl-report.md')
        if os.path.exists(model_report):
            with open(model_report, 'r', encoding='utf-8') as f:
                content = f.read()
                self.model_critical = content.count('🚨 CRITICAL')
                self.model_warnings = content.count('⚠️ WARN')
                self.model_info = content.count('ℹ️ INFO')
            
            self.log_success("Informe de comparación Modelo-SHACL generado")
            
            if self.model_critical > 0:
                self.log_error(f"CRÍTICO: {self.model_critical} propiedades obligatorias sin formas SHACL")
                return False
            else:
                self.log_success("Todas las propiedades obligatorias tienen formas SHACL")
                return True
        else:
            self.log_error("Error al generar informe Modelo-SHACL")
            return False
    
    def phase_1_syntax(self):
        """Fase 1: Validar sintaxis de archivos de formas SHACL."""
        self.phase_1_executed = True
        self.print_section("Fase 1: Validación Sintáctica (Formas SHACL)")
        
        if not os.path.exists(self.test_config):
            self.log_error(f"Configuración de pruebas no encontrada: {self.test_config}")
            return False
        
        # Parse test.ini to get all unique SHACL files
        config = configparser.ConfigParser()
        config.read(self.test_config)
        
        all_shapes = set()
        
        # First, get shapes from [shacl_shapes] section if it exists
        if config.has_option('shacl_shapes', 'files'):
            shapes_list = config.get('shacl_shapes', 'files')
            for shape in shapes_list.split(','):
                shape = shape.strip()
                if shape:
                    all_shapes.add(shape)
        
        # Then, get shapes from test case sections (for backward compatibility)
        for section in config.sections():
            if section in ['prefixes', 'entity_classes', 'reusable_shapes', 'shacl_shapes', 'tests']:
                continue  # Skip configuration sections
            shapes = config.get(section, 'shapes', fallback='')
            if shapes:
                for shape in shapes.split(','):
                    shape = shape.strip()
                    if shape:
                        all_shapes.add(shape)
        
        self.log_info(f"Encontrados {len(all_shapes)} archivos únicos de formas SHACL para validar")
        
        for shape in sorted(all_shapes):
            file_path = os.path.join(self.shacl_dir, '1.0.0', shape)
            
            if not os.path.exists(file_path):
                self.log_warning(f"Archivo no encontrado: {file_path} (omitiendo)")
                continue
            
            self.log_info(f"Validando: {file_path}")
            
            # Use rapper to validate syntax (without -q to get line numbers)
            exit_code, stdout, stderr = self.run_command(['rapper', '-i', 'turtle', '-c', file_path])
            
            if exit_code == 0:
                self.log_success(f"✓ {shape}")
            else:
                self.log_error(f"✗ {shape}")
                self.syntax_errors += 1
                # Show detailed error with line numbers
                if stderr:
                    # Print full stderr to show line numbers
                    error_lines = stderr.strip().split('\n')
                    for line in error_lines[:10]:  # Show first 10 error lines
                        if line.strip():
                            print(f"  {line}")
                    if len(error_lines) > 10:
                        print(f"  ... ({len(error_lines) - 10} líneas de error adicionales)")
        
        print()
        if self.syntax_errors == 0:
            self.log_success("Todos los archivos de formas SHACL son sintácticamente válidos")
            return True
        else:
            self.log_error(f"Encontrados {self.syntax_errors} error(es) de sintaxis en formas SHACL")
            return False
    
    def phase_2_semantic(self):
        """Fase 2: Validación semántica (ejemplos RDF contra SHACL) - fusiona shapes en un grafo."""
        self.phase_2_executed = True
        self.print_section("Fase 2: Validación Semántica (Ejemplos RDF contra SHACL)")
        
        if not os.path.exists(self.test_config):
            self.log_error(f"Configuración de pruebas no encontrada: {self.test_config}")
            return False
        
        config = configparser.ConfigParser()
        config.read(self.test_config)
        
        # Skip configuration sections
        config_sections = {'prefixes', 'entity_classes', 'reusable_shapes', 'shacl_shapes', 'tests'}
        
        test_num = 1
        syntax_errors = 0
        
        for section in config.sections():
            # Skip configuration sections (not test cases)
            if section in config_sections:
                continue
            
            test_name = config.get(section, 'name', fallback=section)
            test_file = config.get(section, 'file', fallback='')
            test_shapes = config.get(section, 'shapes', fallback='')
            test_expect = config.get(section, 'expect', fallback='conformant')
            
            self.log_info(f"Prueba {test_num}: {test_name} (esperado: {test_expect})")
            
            # Build data file path
            data_file = os.path.join(self.examples_dir, 'ttl', test_file)
            self.log_info(f"Archivo de datos: {data_file}")
            
            if not os.path.exists(data_file):
                self.log_error(f"Archivo de datos no encontrado: {data_file}")
                self.shacl_errors += 1
                test_num += 1
                continue
            
            # FIRST: Validate syntax of the example file using rapper
            self.log_info(f"Validando sintaxis de: {data_file}")
            exit_code, stdout, stderr = self.run_command(['rapper', '-i', 'turtle', '-c', data_file])
            
            if exit_code != 0:
                self.log_error(f"✗ Error de sintaxis en {test_name}")
                syntax_errors += 1
                self.shacl_errors += 1
                # Show detailed error
                if stderr:
                    error_lines = stderr.strip().split('\n')
                    for line in error_lines[:10]:
                        if line.strip():
                            print(f"  {line}")
                    if len(error_lines) > 10:
                        print(f"  ... ({len(error_lines) - 10} líneas de error adicionales)")
                
                # Create empty report for this failed test
                report_file = os.path.join(self.report_dir, f'{section}-report.ttl')
                Graph().serialize(destination=report_file, format='turtle')
                
                test_num += 1
                continue
            else:
                self.log_success(f"✓ Sintaxis válida")
            
            # Merge all SHACL shapes into a single graph (in memory, no temp file)
            shapes_graph = Graph()
            for shape in test_shapes.split(','):
                shape = shape.strip()
                if shape:
                    shape_path = os.path.join(self.shacl_dir, '1.0.0', shape)
                    if os.path.exists(shape_path):
                        shapes_graph.parse(shape_path, format='turtle')
            
            # Parse data graph
            data_graph = Graph()
            try:
                data_graph.parse(data_file, format='turtle')
            except Exception as e:
                self.log_error(f"Error al parsear {data_file}: {str(e)}")
                syntax_errors += 1
                self.shacl_errors += 1
                
                # Create empty report for this failed test
                report_file = os.path.join(self.report_dir, f'{section}-report.ttl')
                Graph().serialize(destination=report_file, format='turtle')
                
                test_num += 1
                continue
            
            # Run validation using pyshacl Python API
            report_file = os.path.join(self.report_dir, f'{section}-report.ttl')
            
            try:
                # Validate and get results
                conforms, report_graph, results_text = validate(
                    data_graph,
                    shacl_graph=shapes_graph,
                    inference='rdfs',
                    abort_on_first=False,
                    allow_infos=True,
                    allow_warnings=True
                )
                
                # Write TTL report from report_graph
                report_graph.serialize(destination=report_file, format='turtle')
                
                # Also keep text report for parsing
                stdout = results_text
                stderr = ''
                exit_code = 0 if conforms else 1
                
            except Exception as e:
                self.log_error(f"Error en validación: {str(e)}")
                # Write empty graph on error
                Graph().serialize(destination=report_file, format='turtle')
                stdout = ''
                stderr = str(e)
                exit_code = 1
            
            # Parse results from text report
            conforms_result = 'unknown'
            violations_count = 0
            warnings_count = 0
            
            if stdout:
                # Check conformance status
                if 'Conforms: True' in stdout:
                    conforms_result = 'true'
                elif 'Conforms: False' in stdout:
                    conforms_result = 'false'
                
                # Count violations and warnings from result types
                violations_count = stdout.count('Constraint Violation')
                warnings_count = stdout.count('Validation Result') - stdout.count('Details:')
            
            # Check if report has any results (violations OR warnings)
            has_any_results = False
            try:
                # Parse the TTL report to check for sh:result
                report_graph_check = Graph()
                report_graph_check.parse(report_file, format='turtle')
                # Check if there are any sh:result triples
                from rdflib import Namespace
                SH = Namespace("http://www.w3.org/ns/shacl#")
                has_any_results = len(list(report_graph_check.subject_objects(SH.result))) > 0
            except:
                pass
            
            # Check result
            test_pass = False
            if test_expect == 'conformant':
                # For 'conformant' examples (Full): require conforms=true AND no results (no violations, no warnings)
                if conforms_result == 'true' and not has_any_results:
                    test_pass = True
                    self.log_success(f"✓ {test_name} es totalmente conforme")
                elif conforms_result == 'true' and has_any_results:
                    self.log_error(f"✗ {test_name} tiene avisos (warnings) - debe ser totalmente conforme sin avisos")
                    self.shacl_errors += 1
                else:
                    self.log_error(f"✗ {test_name} tiene {violations_count} violación(es)")
                    self.shacl_errors += 1
            elif test_expect == 'warnings':
                # For 'warnings' examples (Minimal): allow warnings, but no violations
                if conforms_result == 'true' or violations_count == 0:
                    test_pass = True
                    self.log_success(f"✓ {test_name} es conforme (avisos permitidos)")
                else:
                    self.log_error(f"✗ {test_name} tiene {violations_count} violación(es)")
                    self.shacl_errors += 1
            
            test_num += 1
        
        print()
        if syntax_errors > 0:
            self.log_error(f"Encontrados {syntax_errors} error(es) de sintaxis en ejemplos RDF")
        
        if self.shacl_errors == 0:
            self.log_success("Todas las validaciones SHACL pasaron")
            return True
        else:
            self.log_error(f"Encontrados {self.shacl_errors} error(es) SHACL")
            return False
    
    def generate_summary(self):
        """Generate comprehensive summary report."""
        self.print_section("Resumen de Validación (Todas las Fases)")
        
        config = configparser.ConfigParser()
        config.read(self.test_config)
        
        # Skip configuration sections
        config_sections = {'prefixes', 'entity_classes', 'reusable_shapes', 'shacl_shapes', 'tests'}
        
        summary_content = f"""# Informe de Validación DCAT-AP-ES

**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Visión General de las Fases de Validación

El proceso de validación de DCAT-AP-ES consta de tres fases complementarias:

"""
        
        # Only show executed phases
        if self.phase_0_executed:
            summary_content += f"""### Fase 0: Comparación Modelo-SHACL
**Propósito:** Verificar que el modelo de documentación tiene definiciones SHACL correspondientes

- **Estado:** {'❌ BLOQUEANTE' if self.model_critical > 0 else '✅ CORRECTO'}
- **Problemas CRÍTICOS:** {self.model_critical}
- **Advertencias informativas:** {self.model_warnings} WARN, {self.model_info} INFO (no bloqueantes)

---

"""
        
        if self.phase_1_executed:
            summary_content += f"""### Fase 1: Validación Sintáctica (Formas SHACL)
**Propósito:** Verificar que los archivos de formas SHACL son RDF/Turtle sintácticamente válidos

- **Errores de sintaxis:** {self.syntax_errors}
- **Estado:** {'❌ ERROR' if self.syntax_errors > 0 else '✅ CORRECTO'}

---

"""
        
        if self.phase_2_executed:
            summary_content += """### Fase 2: Validación Semántica (Ejemplos RDF contra SHACL)
**Propósito:** Validar archivos de ejemplo RDF contra las restricciones de las formas SHACL

| Caso de Prueba | Esperado | Estado |
|----------------|----------|--------|
"""
            # Only process test cases if Phase 2 was executed
            for section in config.sections():
                # Skip configuration sections
                if section in config_sections:
                    continue
                test_name = config.get(section, 'name', fallback=section)
                test_expect = config.get(section, 'expect', fallback='conformant')
                report_file = os.path.join(self.report_dir, f'{section}-report.ttl')
                
                if os.path.exists(report_file):
                    with open(report_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        conforms = 'true' in content and 'sh:conforms true' in content
                        violations = content.count('sh:resultSeverity sh:Violation')
                        has_results = content.count('sh:result [')
                else:
                    conforms = False
                    violations = 0
                    has_results = 0
                
                expect_label = "Conformidad completa" if test_expect == "conformant" else "Avisos permitidos"
                
                if test_expect == 'conformant':
                    # For Full examples: must be conforms=true AND no results (no warnings, no violations)
                    status = "✅ CORRECTO" if (conforms and has_results == 0) else "❌ ERROR"
                else:  # warnings
                    # For Minimal examples: allow warnings, but no violations
                    status = "✅ CORRECTO" if (conforms or violations == 0) else "❌ ERROR"
                
                summary_content += f"| {test_name} | {expect_label} | {status} |\n"
            
            summary_content += "\n---\n"
        
        summary_content += """
## Estadísticas

"""
        
        if self.phase_0_executed:
            summary_content += f"- **Fase 0 (Modelo-SHACL):** Problemas CRÍTICOS: {self.model_critical}\n"
        if self.phase_1_executed:
            summary_content += f"- **Fase 1 (Sintaxis):** Errores: {self.syntax_errors}\n"
        if self.phase_2_executed:
            summary_content += f"- **Fase 2 (Semántica):** Fallos en pruebas: {self.shacl_errors}\n"
        
        summary_content += """
## Informes Detallados

>[!TIP]
> **GitHub Actions**: Informes detallados disponibles en los artefactos generados por el contenedor. Ver: **https://github.com/datosgobes/DCAT-AP-ES/actions/workflows/validate-shacl.yml**

"""
        
        if self.phase_0_executed:
            summary_content += """**Fase 0 - Comparación Modelo-SHACL:**
- `model-vs-shacl-report.md` - Formato Markdown con análisis detallado de propiedades

"""
        
        if self.phase_2_executed:
            summary_content += """**Fase 2 - Resultados de Validación SHACL (formato Turtle):**
"""
            for section in config.sections():
                # Skip configuration sections
                if section in config_sections:
                    continue
                
                test_name = config.get(section, 'name', fallback=section)
                summary_content += f"- `{section}-report.ttl` - {test_name}\n"
        
        summary_file = os.path.join(self.report_dir, 'SUMMARY.md')
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        self.log_info(f"Informe completo guardado en: {summary_file}")
    
    def run(self):
        """Run validation according to mode."""
        validation_failed = False
        
        if self.mode in ['all', 'model-only']:
            if not self.phase_0_model_shacl():
                validation_failed = True
                # In 'all' mode, stop immediately if a phase fails
                if self.mode == 'all':
                    # Generate summary before exiting so SUMMARY.md exists
                    self.generate_summary()
                    self.print_section("Validación Completa")
                    self.log_error("❌ Fase 0 falló. Deteniendo validación.")
                    return 1
        
        if self.mode in ['all', 'syntax-only']:
            if not self.phase_1_syntax():
                validation_failed = True
                # In 'all' mode, stop immediately if a phase fails
                if self.mode == 'all':
                    # Generate summary before exiting so SUMMARY.md exists
                    self.generate_summary()
                    self.print_section("Validación Completa")
                    self.log_error("❌ Fase 1 falló. Deteniendo validación.")
                    return 1
        
        if self.mode in ['all', 'shacl-only']:
            if not self.phase_2_semantic():
                validation_failed = True
                # In 'all' mode, stop immediately if a phase fails
                if self.mode == 'all':
                    # Generate summary before exiting so SUMMARY.md exists
                    self.generate_summary()
                    self.print_section("Validación Completa")
                    self.log_error("❌ Fase 2 falló. Deteniendo validación.")
                    return 1
        
        # Always generate summary for 'all' or shacl-only
        if self.mode in ['all', 'shacl-only']:
            self.generate_summary()
        
        self.print_section("Validación Completa")
        
        if validation_failed:
            self.log_error("Algunas fases de validación fallaron. Revisa los informes para más detalles.")
            return 1
        else:
            self.log_success("¡Todas las fases de validación pasaron! ✓")
            return 0


def main():
    parser = argparse.ArgumentParser(
        description='Script Unificado de Validación DCAT-AP-ES',
        epilog='Fases: 0=Modelo-SHACL, 1=Sintaxis, 2=Semántica'
    )
    parser.add_argument(
        'mode',
        nargs='?',
        default='all',
        choices=['all', 'model-only', 'syntax-only', 'shacl-only'],
        help='Modo de validación'
    )
    
    args = parser.parse_args()
    
    # When running in Docker, workspace is mounted at /workspace
    repo_root = '/workspace'
    
    validator = Validator(repo_root, mode=args.mode)
    return validator.run()


if __name__ == '__main__':
    sys.exit(main())
