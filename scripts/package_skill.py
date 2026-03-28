#!/usr/bin/env python3
"""
Skill Packaging Script

This script packages the spec-driven development skill into a zip file
for distribution and installation.
"""

import os
import sys
import zipfile
import shutil
import json
from pathlib import Path
from datetime import datetime

class SkillPackager:
    def __init__(self, skill_path: str = "."):
        self.skill_path = Path(skill_path).resolve()
        self.skill_name = self.skill_path.name
        
        # Output directory and filename
        self.output_dir = self.skill_path / "dist"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.zip_filename = f"{self.skill_name}_{timestamp}.zip"
        self.zip_path = self.output_dir / self.zip_filename
        
        # Files to include
        self.include_patterns = [
            "SKILL.md",
            "templates/**/*",
            "references/**/*",
            "scripts/**/*",
        ]
        
        # Files to exclude
        self.exclude_patterns = [
            "__pycache__",
            "*.pyc",
            "*.pyo",
            ".DS_Store",
            "Thumbs.db",
        ]
        
        # Required files
        self.required_files = [
            "SKILL.md",
            "templates/PROJECT.md",
            "templates/ROADMAP.md",
            "templates/PLAN.md",
            "templates/SUMMARY.md",
            "templates/REQUIREMENTS.md",
            "templates/STATE.md",
            "templates/config.json",
        ]
    
    def validate_skill_structure(self) -> bool:
        """Validate that the skill has all required files."""
        print("🔍 Validating skill structure...")
        
        missing_files = []
        for file_path in self.required_files:
            full_path = self.skill_path / file_path
            if not full_path.exists():
                missing_files.append(file_path)
                print(f"  ❌ Missing: {file_path}")
            else:
                print(f"  ✅ Found: {file_path}")
        
        if missing_files:
            print(f"\n❌ Missing required files: {', '.join(missing_files)}")
            return False
        
        # Check SKILL.md for required sections
        skill_md_path = self.skill_path / "SKILL.md"
        if skill_md_path.exists():
            content = skill_md_path.read_text(encoding='utf-8')
            required_sections = [
                "## Core Workflow",
                "## Templates",
                "## Implementation Examples",
            ]
            
            missing_sections = []
            for section in required_sections:
                if section not in content:
                    missing_sections.append(section)
            
            if missing_sections:
                print(f"⚠️  SKILL.md missing sections: {', '.join(missing_sections)}")
        
        return True
    
    def create_output_directory(self) -> bool:
        """Create the output directory if it doesn't exist."""
        try:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            print(f"✅ Created output directory: {self.output_dir}")
            return True
        except Exception as e:
            print(f"❌ Failed to create output directory: {e}")
            return False
    
    def collect_files(self) -> list:
        """Collect all files to be included in the package."""
        print("\n📦 Collecting files...")
        
        all_files = []
        
        # Add SKILL.md
        skill_md = self.skill_path / "SKILL.md"
        if skill_md.exists():
            all_files.append(skill_md)
            print(f"  ✅ Added: SKILL.md")
        
        # Add template files
        templates_dir = self.skill_path / "templates"
        if templates_dir.exists():
            for template_file in templates_dir.rglob("*"):
                if template_file.is_file():
                    # Check if file should be excluded
                    should_exclude = False
                    for pattern in self.exclude_patterns:
                        if pattern in str(template_file):
                            should_exclude = True
                            break
                    
                    if not should_exclude:
                        all_files.append(template_file)
                        rel_path = template_file.relative_to(self.skill_path)
                        print(f"  ✅ Added: {rel_path}")
        
        # Add reference files
        references_dir = self.skill_path / "references"
        if references_dir.exists():
            for ref_file in references_dir.rglob("*"):
                if ref_file.is_file():
                    # Check if file should be excluded
                    should_exclude = False
                    for pattern in self.exclude_patterns:
                        if pattern in str(ref_file):
                            should_exclude = True
                            break
                    
                    if not should_exclude:
                        all_files.append(ref_file)
                        rel_path = ref_file.relative_to(self.skill_path)
                        print(f"  ✅ Added: {rel_path}")
        
        # Add script files
        scripts_dir = self.skill_path / "scripts"
        if scripts_dir.exists():
            for script_file in scripts_dir.rglob("*"):
                if script_file.is_file():
                    # Check if file should be excluded
                    should_exclude = False
                    for pattern in self.exclude_patterns:
                        if pattern in str(script_file):
                            should_exclude = True
                            break
                    
                    if not should_exclude:
                        all_files.append(script_file)
                        rel_path = script_file.relative_to(self.skill_path)
                        print(f"  ✅ Added: {rel_path}")
        
        print(f"\n📊 Total files collected: {len(all_files)}")
        return all_files
    
    def create_zip_package(self, files: list) -> bool:
        """Create a zip file with all collected files."""
        print(f"\n📁 Creating zip package: {self.zip_path.name}")
        
        try:
            with zipfile.ZipFile(self.zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file_path in files:
                    # Calculate relative path within the zip
                    arcname = file_path.relative_to(self.skill_path)
                    
                    # Add file to zip
                    zipf.write(file_path, arcname)
                    print(f"  📄 Added to zip: {arcname}")
            
            # Get file size
            file_size = self.zip_path.stat().st_size
            size_mb = file_size / (1024 * 1024)
            
            print(f"\n✅ Package created successfully!")
            print(f"   📁 Package: {self.zip_path}")
            print(f"   📊 Size: {file_size:,} bytes ({size_mb:.2f} MB)")
            print(f"   📦 Files: {len(files)}")
            
            return True
        except Exception as e:
            print(f"❌ Failed to create zip package: {e}")
            return False
    
    def create_manifest(self) -> bool:
        """Create a manifest file describing the package."""
        try:
            manifest_path = self.output_dir / f"{self.skill_name}_manifest.json"
            
            manifest = {
                "skill_name": self.skill_name,
                "version": "1.0.0",
                "package_date": datetime.now().isoformat(),
                "package_file": self.zip_filename,
                "files_included": len(self.collect_files()),  # Re-collect to count
                "description": "Spec-Driven Development Skill - A systematic approach to building software through specification-first development",
                "author": "Spec-Driven Development Team",
                "requirements": {
                    "python": ">=3.8",
                    "platform": "any"
                },
                "usage": {
                    "initialize_project": "python scripts/init_project.py <project_name>",
                    "validate_project": "python scripts/validate_project.py [project_path]",
                    "documentation": "See SKILL.md for detailed usage instructions"
                }
            }
            
            with open(manifest_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2)
            
            print(f"✅ Created manifest: {manifest_path.name}")
            return True
        except Exception as e:
            print(f"⚠️  Failed to create manifest: {e}")
            return False
    
    def package(self) -> bool:
        """Main packaging method."""
        print(f"🚀 Packaging skill: {self.skill_name}")
        print(f"📁 Skill path: {self.skill_path}")
        
        # Step 1: Validate structure
        if not self.validate_skill_structure():
            print("❌ Skill structure validation failed")
            return False
        
        # Step 2: Create output directory
        if not self.create_output_directory():
            return False
        
        # Step 3: Collect files
        files = self.collect_files()
        if not files:
            print("❌ No files to package")
            return False
        
        # Step 4: Create zip package
        if not self.create_zip_package(files):
            return False
        
        # Step 5: Create manifest
        self.create_manifest()
        
        # Step 6: Summary
        print(f"\n{'='*50}")
        print(f"✅ PACKAGING COMPLETE!")
        print(f"{'='*50}")
        print(f"📦 Skill: {self.skill_name}")
        print(f"📁 Package: {self.zip_path}")
        print(f"📊 Size: {self.zip_path.stat().st_size:,} bytes")
        print(f"📄 Files: {len(files)}")
        print(f"{'='*50}")
        print(f"\n📋 Installation Instructions:")
        print(f"1. Extract the zip file to your skills directory")
        print(f"2. The skill will be available as '{self.skill_name}'")
        print(f"3. Use 'spec-skill' to start a new project")
        
        return True

def main():
    """Command-line entry point."""
    import argparse
    parser = argparse.ArgumentParser(description="Package a Trae skill into a zip file.")
    parser.add_argument("skill_dir", nargs="?", default=".", help="Path to the skill directory (default: current directory)")
    
    args = parser.parse_args()
    
    # Run the packager
    packager = SkillPackager(args.skill_dir)
    success = packager.package()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
