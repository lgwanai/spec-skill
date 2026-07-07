#!/usr/bin/env python3
"""
Project Validation Script for Spec-Driven Development

This script validates that a project follows the spec-driven development
structure and contains all required files.
"""

import os
import json
import sys
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple

class ProjectValidator:
    def __init__(self, project_path: str = "."):
        self.project_path = Path(project_path).resolve()
        self.planning_dir = self.project_path / ".planning"
        
        # Required files and their descriptions
        self.required_files = {
            "PROJECT.md": "Project context and goals",
            "ROADMAP.md": "Phased implementation plan",
            "REQUIREMENTS.md": "Detailed requirements",
            "STATE.md": "Project state and decisions",
            "config.json": "Project configuration",
        }

        # Canonical but migration-friendly files. Missing files should warn,
        # not fail, so existing spec-skill projects can adopt the new flow
        # incrementally.
        self.recommended_files = {
            "DOMAIN.md": "Domain concepts and vocabulary",
            "USE_CASES.md": "Actors, roles, and use cases",
        }
        
        # Required directories
        self.required_dirs = [
            "phases",
            "phases/01-project-init",
        ]
        
        # Validation results
        self.results: List[Dict] = []
        self.errors: List[str] = []
        self.warnings: List[str] = []
    
    def check_directory_exists(self, path: Path, description: str) -> bool:
        """Check if a directory exists."""
        exists = path.exists() and path.is_dir()
        self.results.append({
            "type": "directory",
            "name": str(path.relative_to(self.project_path)),
            "description": description,
            "status": "✅" if exists else "❌",
            "exists": exists
        })
        
        if not exists:
            self.errors.append(f"Missing directory: {path.relative_to(self.project_path)} - {description}")
        
        return exists
    
    def check_file_exists(self, path: Path, description: str) -> bool:
        """Check if a file exists and is not empty."""
        exists = path.exists() and path.is_file()
        empty = exists and path.stat().st_size == 0
        
        status = "✅"
        if not exists:
            status = "❌"
        elif empty:
            status = "⚠️"
        
        self.results.append({
            "type": "file",
            "name": str(path.relative_to(self.project_path)),
            "description": description,
            "status": status,
            "exists": exists,
            "empty": empty
        })
        
        if not exists:
            self.errors.append(f"Missing file: {path.relative_to(self.project_path)} - {description}")
        elif empty:
            self.warnings.append(f"Empty file: {path.relative_to(self.project_path)} - {description}")
        
        return exists and not empty

    def check_recommended_file_exists(self, path: Path, description: str) -> bool:
        """Check recommended canonical files without failing old projects."""
        exists = path.exists() and path.is_file()
        empty = exists and path.stat().st_size == 0

        status = "✅"
        if not exists:
            status = "⚠️"
        elif empty:
            status = "⚠️"

        self.results.append({
            "type": "file",
            "name": str(path.relative_to(self.project_path)),
            "description": f"{description} (recommended)",
            "status": status,
            "exists": exists,
            "empty": empty,
            "recommended": True,
        })

        if not exists:
            self.warnings.append(
                f"Recommended file missing: {path.relative_to(self.project_path)} - {description}. "
                "Create it when the project or phase involves human interaction."
            )
        elif empty:
            self.warnings.append(f"Empty recommended file: {path.relative_to(self.project_path)} - {description}")

        return exists and not empty
    
    def check_file_content(self, path: Path, expected_keywords: List[str] = None) -> bool:
        """Check if a file contains expected content."""
        if not path.exists():
            return False
        
        try:
            content = path.read_text(encoding='utf-8')
            
            if expected_keywords:
                missing_keywords = []
                for keyword in expected_keywords:
                    if keyword not in content:
                        missing_keywords.append(keyword)
                
                if missing_keywords:
                    self.warnings.append(f"File {path.relative_to(self.project_path)} missing keywords: {', '.join(missing_keywords)}")
                    return False
            
            return True
        except Exception as e:
            self.warnings.append(f"Failed to read {path.relative_to(self.project_path)}: {e}")
            return False
    
    def check_config_json(self, path: Path) -> bool:
        """Validate config.json structure."""
        if not path.exists():
            return False
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Check required fields
            required_fields = ["project", "workflow", "quality"]
            missing_fields = []
            
            for field in required_fields:
                if field not in config:
                    missing_fields.append(field)
            
            if missing_fields:
                self.errors.append(f"config.json missing required sections: {', '.join(missing_fields)}")
                return False
            
            # Check project name
            if "name" not in config.get("project", {}):
                self.warnings.append("config.json missing project name")
            
            return True
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in config.json: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading config.json: {e}")
            return False
    
    def check_phases_structure(self) -> bool:
        """Check phases directory structure."""
        phases_dir = self.planning_dir / "phases"
        if not phases_dir.exists():
            self.errors.append("Missing phases directory")
            return False
        
        # Check for at least one phase
        phase_dirs = [d for d in phases_dir.iterdir() if d.is_dir()]
        if not phase_dirs:
            self.warnings.append("No phases found in phases directory")
            return True
        
        # Check each phase directory
        for phase_dir in phase_dirs:
            phase_name = phase_dir.name
            
            # Check phase naming pattern (e.g., "01-project-init")
            if not any(c.isdigit() for c in phase_name):
                self.warnings.append(f"Phase directory '{phase_name}' doesn't follow naming convention (should start with number)")
            
            # Check for plan files
            plan_files = list(phase_dir.glob("*-PLAN.md"))
            if not plan_files:
                self.warnings.append(f"Phase '{phase_name}' has no plan files")
            else:
                # Check plan file naming
                for plan_file in plan_files:
                    if not plan_file.name.count('-') >= 2:
                        self.warnings.append(f"Plan file '{plan_file.name}' doesn't follow naming convention (should be XX-YY-PLAN.md)")
            
            # Check for summary files
            summary_files = list(phase_dir.glob("*-SUMMARY.md"))
            if not summary_files:
                self.warnings.append(f"Phase '{phase_name}' has no summary files")
        
        return True

    def check_trace_validation(self) -> bool:
        """Run trace validation when the script is available."""
        trace_script = Path(__file__).parent / "validate_trace.py"
        if not trace_script.exists():
            self.warnings.append("Trace validator not found: scripts/validate_trace.py")
            return True

        try:
            result = subprocess.run(
                [sys.executable, str(trace_script), str(self.project_path)],
                capture_output=True,
                text=True,
                check=False,
            )
        except Exception as e:
            self.warnings.append(f"Failed to run trace validator: {e}")
            return True

        if result.returncode != 0:
            self.errors.append(
                "Trace validation failed. Run `python scripts/validate_trace.py .` for details.\n"
                + result.stdout.strip()
            )
            return False

        if "WARNINGS" in result.stdout:
            self.warnings.append(
                "Trace validation passed with warnings. Run `python scripts/validate_trace.py .` for details."
            )

        return True
    
    def validate(self) -> bool:
        """Main validation method."""
        print(f"🔍 Validating spec-driven project: {self.project_path}")
        
        # Check planning directory exists
        if not self.check_directory_exists(self.planning_dir, "Planning directory"):
            print("❌ Planning directory not found. Is this a spec-driven project?")
            return False
        
        # Check required files
        print("\n📄 Checking required files...")
        for filename, description in self.required_files.items():
            file_path = self.planning_dir / filename
            self.check_file_exists(file_path, description)

        # Check recommended canonical files without blocking migration
        print("\n📄 Checking recommended files...")
        for filename, description in self.recommended_files.items():
            file_path = self.planning_dir / filename
            self.check_recommended_file_exists(file_path, description)
        
        # Check file contents
        print("\n📝 Checking file contents...")
        
        # Check PROJECT.md for placeholders
        project_path = self.planning_dir / "PROJECT.md"
        self.check_file_content(project_path, ["## What This Is", "## Core Value", "## Requirements"])

        # Check DOMAIN.md for interaction gate and core concept structure
        domain_path = self.planning_dir / "DOMAIN.md"
        if domain_path.exists():
            self.check_file_content(domain_path, ["# Domain Model:", "## Core Concepts", "Interaction Gate"])

        # Check USE_CASES.md for actor/use-case structure
        use_cases_path = self.planning_dir / "USE_CASES.md"
        if use_cases_path.exists():
            self.check_file_content(use_cases_path, ["# Use Cases:", "## Actors and Roles", "## Use Case Matrix"])
        
        # Check ROADMAP.md for placeholders
        roadmap_path = self.planning_dir / "ROADMAP.md"
        self.check_file_content(roadmap_path, ["# Roadmap:", "## Phases"])
        
        # Check config.json structure
        config_path = self.planning_dir / "config.json"
        if config_path.exists():
            self.check_config_json(config_path)
        
        # Check phases structure
        print("\n📈 Checking phases structure...")
        self.check_phases_structure()

        # Check trace consistency
        print("\n🔗 Checking trace consistency...")
        self.check_trace_validation()
        
        # Check required directories
        print("\n📁 Checking directory structure...")
        for dir_path in self.required_dirs:
            full_path = self.planning_dir / dir_path
            self.check_directory_exists(full_path, f"Required directory: {dir_path}")
        
        # Print results
        print(f"\n{'='*50}")
        print("📊 VALIDATION RESULTS")
        print(f"{'='*50}")
        
        # Group results by type
        directories = [r for r in self.results if r["type"] == "directory"]
        files = [r for r in self.results if r["type"] == "file"]
        
        if directories:
            print("\n📁 DIRECTORIES:")
            for dir_result in directories:
                print(f"  {dir_result['status']} {dir_result['name']:40} - {dir_result['description']}")
        
        if files:
            print("\n📄 FILES:")
            for file_result in files:
                status = file_result['status']
                if file_result.get('empty', False):
                    status = "⚠️ (empty)"
                print(f"  {status} {file_result['name']:40} - {file_result['description']}")
        
        # Print warnings
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")
        
        # Print errors
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")
        
        # Summary
        print(f"\n{'='*50}")
        total_checks = len(self.results)
        passed_checks = sum(1 for r in self.results if r["status"] == "✅")
        
        if self.errors:
            print(f"❌ VALIDATION FAILED")
            print(f"   {passed_checks}/{total_checks} checks passed")
            print(f"   {len(self.errors)} errors need to be fixed")
            return False
        else:
            if self.warnings:
                print(f"⚠️  VALIDATION PASSED WITH WARNINGS")
                print(f"   {passed_checks}/{total_checks} checks passed")
                print(f"   {len(self.warnings)} warnings to review")
            else:
                print(f"✅ VALIDATION PASSED")
                print(f"   {passed_checks}/{total_checks} checks passed")
                print(f"   All files and directories are properly structured")
            return True

def main():
    """Command-line entry point."""
    project_path = sys.argv[1] if len(sys.argv) > 1 else "."
    
    validator = ProjectValidator(project_path)
    success = validator.validate()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
