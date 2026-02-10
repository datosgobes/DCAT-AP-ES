#!/usr/bin/env python3
"""
SHACL Changelog Generator
==========================
Script para generar y actualizar el CHANGELOG de los archivos SHACL
basándose en el historial de commits de Git.

Uso:
    python generate_shacl_changelog.py [--output CHANGELOG.md] [--since COMMIT_HASH]
"""

import argparse
import subprocess
import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Tuple
import sys


class SHACLChangelogGenerator:
    """Generador de CHANGELOG para archivos SHACL."""
    
    def __init__(self, repo_path: str = ".", output_file: str = "SHACL_CHANGELOG.md"):
        self.repo_path = Path(repo_path)
        self.output_file = Path(output_file)
        self.shacl_path = "shacl/"
        
    def get_commits(self, since_commit: str = None, until_commit: str = None) -> List[Dict]:
        """
        Obtiene la lista de commits que han modificado archivos SHACL.
        
        Args:
            since_commit: Hash del commit desde el cual obtener el historial
            until_commit: Hash del commit hasta el cual obtener el historial
            
        Returns:
            Lista de diccionarios con información de commits (ordenados por fecha)
        """
        cmd = [
            "git", "log",
            "--pretty=format:%H|%ad|%an|%ae|%s",
            "--date=short",
            "--"
        ]
        
        # Agregar rango de commits si se especifica
        if since_commit and until_commit:
            cmd.insert(2, f"{since_commit}..{until_commit}")
        elif since_commit:
            cmd.insert(2, f"{since_commit}..HEAD")
        
        cmd.append(self.shacl_path)
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line:
                    continue
                    
                parts = line.split('|')
                if len(parts) >= 5:
                    commits.append({
                        'hash': parts[0],
                        'date': parts[1],
                        'author': parts[2],
                        'email': parts[3],
                        'message': '|'.join(parts[4:])  # El mensaje puede contener '|'
                    })
            
            # Ordenar por fecha y hash para determinismo
            commits.sort(key=lambda x: (x['date'], x['hash']), reverse=True)
            
            return commits
            
        except subprocess.CalledProcessError as e:
            print(f"Error ejecutando git log: {e}", file=sys.stderr)
            return []
    
    def get_changed_files(self, commit_hash: str) -> List[str]:
        """
        Obtiene la lista de archivos SHACL modificados en un commit.
        
        Args:
            commit_hash: Hash del commit
            
        Returns:
            Lista de rutas de archivos modificados
        """
        cmd = [
            "git", "diff-tree", "--no-commit-id", "--name-only", "-r",
            commit_hash, "--", self.shacl_path
        ]
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            
            files = [f for f in result.stdout.strip().split('\n') if f]
            return files
            
        except subprocess.CalledProcessError as e:
            print(f"Error obteniendo archivos del commit {commit_hash}: {e}", file=sys.stderr)
            return []
    
    def categorize_commit(self, message: str) -> str:
        """
        Categoriza un commit según su mensaje.
        
        Args:
            message: Mensaje del commit
            
        Returns:
            Categoría del commit
        """
        message_lower = message.lower()
        
        # Conventional commits
        if message.startswith('feat:') or message.startswith('feature:'):
            return 'Features'
        elif message.startswith('fix:'):
            return 'Fixes'
        elif message.startswith('refactor:'):
            return 'Refactoring'
        elif message.startswith('docs:'):
            return 'Documentation'
        elif message.startswith('style:'):
            return 'Style'
        elif message.startswith('test:'):
            return 'Tests'
        elif message.startswith('chore:'):
            return 'Chore'
        elif 'merge' in message_lower:
            return 'Merge'
        elif 'breaking' in message_lower or 'breaking change' in message_lower:
            return 'Breaking Changes'
        else:
            return 'Other Changes'
    
    def extract_conventions(self, message: str) -> List[str]:
        """
        Extrae referencias a convenciones del mensaje de commit.
        
        Args:
            message: Mensaje del commit
            
        Returns:
            Lista de convenciones encontradas
        """
        # Buscar patrones como "Convención 25", "convencion 30", etc.
        pattern = r'[Cc]onvenci[oó]n\s+(\d+)'
        matches = re.findall(pattern, message)
        return [f"Convención {m}" for m in matches]
    
    def generate_changelog_content(self, commits: List[Dict], append_mode: bool = False) -> str:
        """
        Genera el contenido del CHANGELOG.
        
        Args:
            commits: Lista de commits
            append_mode: Si es True, genera solo el contenido nuevo sin header
            
        Returns:
            Contenido del CHANGELOG en formato Markdown
        """
        if not commits:
            return ""
        
        content = []
        
        if not append_mode:
            content.append("# SHACL Changelog\n")
            content.append("Este archivo registra todos los cambios significativos en los archivos SHACL de DCAT-AP-ES.\n")
            content.append("El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).\n\n")
        
        # Agrupar commits por fecha (año-mes)
        commits_by_period = {}
        for commit in commits:
            # Formato: YYYY-MM
            date_obj = datetime.strptime(commit['date'], '%Y-%m-%d')
            period = date_obj.strftime('%Y-%m')
            
            if period not in commits_by_period:
                commits_by_period[period] = []
            commits_by_period[period].append(commit)
        
        # Ordenar períodos de más reciente a más antiguo
        sorted_periods = sorted(commits_by_period.keys(), reverse=True)
        
        for period in sorted_periods:
            period_commits = commits_by_period[period]
            date_obj = datetime.strptime(period, '%Y-%m')
            period_name = date_obj.strftime('%B %Y')
            
            # En español
            months_es = {
                'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo',
                'April': 'Abril', 'May': 'Mayo', 'June': 'Junio',
                'July': 'Julio', 'August': 'Agosto', 'September': 'Septiembre',
                'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
            }
            for eng, esp in months_es.items():
                period_name = period_name.replace(eng, esp)
            
            content.append(f"## {period_name}\n")
            
            # Agrupar por categoría
            categorized = {}
            for commit in period_commits:
                category = self.categorize_commit(commit['message'])
                
                if category not in categorized:
                    categorized[category] = []
                categorized[category].append(commit)
            
            # Ordenar categorías
            category_order = [
                'Breaking Changes', 'Features', 'Fixes', 'Refactoring',
                'Documentation', 'Style', 'Tests', 'Chore', 'Merge', 'Other Changes'
            ]
            
            for category in category_order:
                if category not in categorized:
                    continue
                
                content.append(f"### {category}\n")
                
                # Ordenar commits dentro de cada categoría por fecha y hash
                categorized[category].sort(key=lambda x: (x['date'], x['hash']), reverse=True)
                
                for commit in categorized[category]:
                    # Extraer convenciones
                    conventions = self.extract_conventions(commit['message'])
                    conv_text = ""
                    if conventions:
                        conv_text = f" ({', '.join(sorted(conventions))})"
                    
                    # Obtener archivos modificados
                    files = self.get_changed_files(commit['hash'])
                    files_summary = ""
                    if files:
                        # Mostrar solo nombres de archivos únicos (sin rutas completas)
                        unique_files = set([Path(f).name for f in files])
                        if len(unique_files) <= 3:
                            files_summary = f" - `{'`, `'.join(sorted(unique_files))}`"
                        else:
                            files_summary = f" - {len(files)} archivos modificados"
                    
                    # Limpiar mensaje (eliminar prefijo de conventional commits)
                    clean_message = re.sub(r'^(feat|fix|refactor|docs|style|test|chore|feature):\s*', '', commit['message'])
                    
                    content.append(
                        f"- {clean_message}{conv_text}{files_summary} "
                        f"([`{commit['hash'][:7]}`](../../commit/{commit['hash']})) "
                        f"- @{commit['author']}\n"
                    )
                
                content.append("\n")
            
            content.append("---\n\n")
        
        return ''.join(content)
    
    def read_existing_changelog(self) -> Tuple[str, str]:
        """
        Lee el CHANGELOG existente y extrae el último commit registrado.
        
        Returns:
            Tupla (contenido, último_commit_hash)
        """
        if not self.output_file.exists():
            return "", None
        
        content = self.output_file.read_text(encoding='utf-8')
        
        # Buscar el hash del último commit registrado
        # Formato: ([`hash`](url))
        pattern = r'\[`([a-f0-9]{7})`\]'
        matches = re.findall(pattern, content)
        
        if matches:
            # El primer match es el más reciente (si está ordenado cronológicamente)
            return content, matches[0]
        
        return content, None
    
    def update_changelog(self, since_commit: str = None):
        """
        Actualiza el CHANGELOG con nuevos commits.
        
        Args:
            since_commit: Commit desde el cual actualizar (si es None, regenera todo)
        """
        print("Obteniendo commits de archivos SHACL...")
        commits = self.get_commits(since_commit=since_commit)
        
        if not commits:
            print("No se encontraron nuevos commits para actualizar el CHANGELOG.")
            return
        
        print(f"Encontrados {len(commits)} commits")
        
        if since_commit:
            # Modo actualización: agregar al principio del changelog existente
            print("Actualizando CHANGELOG existente...")
            existing_content, _ = self.read_existing_changelog()
            
            # Generar solo el contenido nuevo
            new_content = self.generate_changelog_content(commits, append_mode=True)
            
            # Insertar después del header
            lines = existing_content.split('\n')
            header_end = 0
            for i, line in enumerate(lines):
                if line.startswith('##') and not line.startswith('###'):
                    header_end = i
                    break
            
            if header_end > 0:
                updated_content = '\n'.join(lines[:header_end]) + '\n' + new_content + '\n'.join(lines[header_end:])
            else:
                updated_content = new_content + existing_content
            
            self.output_file.write_text(updated_content, encoding='utf-8')
        else:
            # Modo generación completa
            print("Generando CHANGELOG completo...")
            content = self.generate_changelog_content(commits, append_mode=False)
            self.output_file.write_text(content, encoding='utf-8')
        
        print(f"CHANGELOG guardado en: {self.output_file}")
    
    def generate_full_changelog(self):
        """Genera el CHANGELOG completo desde el principio del historial."""
        self.update_changelog(since_commit=None)


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description='Genera o actualiza el CHANGELOG de archivos SHACL'
    )
    parser.add_argument(
        '--output', '-o',
        default='shacl/CHANGELOG.md',
        help='Archivo de salida del CHANGELOG (default: shacl/CHANGELOG.md)'
    )
    parser.add_argument(
        '--since',
        help='Commit hash desde el cual generar el changelog (opcional)'
    )
    parser.add_argument(
        '--repo-path',
        default='.',
        help='Ruta al repositorio Git (default: directorio actual)'
    )
    
    args = parser.parse_args()
    
    generator = SHACLChangelogGenerator(
        repo_path=args.repo_path,
        output_file=args.output
    )
    
    generator.update_changelog(since_commit=args.since)


if __name__ == '__main__':
    main()
