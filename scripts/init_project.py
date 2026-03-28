#!/usr/bin/env python3
"""
Project Initialization Script for Spec-Driven Development

This script creates the standard directory structure and template files
for a new spec-driven development project.
"""

import os
import sys
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional

class ProjectInitializer:
    def __init__(self, project_name: str, project_path: str = "."):
        self.project_name = project_name
        self.project_path = Path(project_path).resolve()
        self.planning_dir = self.project_path / ".planning"
        self.phases_dir = self.planning_dir / "phases"
        
        # Template paths (relative to this script)
        self.template_dir = Path(__file__).parent.parent / "templates"
        
        # Required files and their destinations
        self.required_files = {
            "PROJECT.md": self.planning_dir / "PROJECT.md",
            "ROADMAP.md": self.planning_dir / "ROADMAP.md",
            "REQUIREMENTS.md": self.planning_dir / "REQUIREMENTS.md",
            "STATE.md": self.planning_dir / "STATE.md",
            "config.json": self.planning_dir / "config.json",
        }
        
        # Phase structure templates
        self.phase_template_files = {
            "PLAN.md": None,  # Will be placed in phase directories
            "SUMMARY.md": None,  # Will be placed in phase directories
        }
    
    def validate_project_name(self) -> bool:
        """Validate the project name."""
        if not self.project_name or not self.project_name.strip():
            print("❌ Project name cannot be empty")
            return False
        
        # Check for invalid characters
        invalid_chars = ['<', '>', ':', '"', '|', '?', '*', '\\', '/']
        for char in invalid_chars:
            if char in self.project_name:
                print(f"❌ Project name contains invalid character: {char}")
                return False
        
        return True
    
    def check_existing_structure(self) -> bool:
        """Check if project structure already exists."""
        if self.planning_dir.exists():
            print(f"⚠️  Planning directory already exists: {self.planning_dir}")
            response = input("Do you want to overwrite? (y/N): ").strip().lower()
            if response != 'y':
                print("❌ Aborting initialization")
                return False
            # Backup existing directory
            backup_dir = self.project_path / ".planning.backup"
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
            shutil.move(self.planning_dir, backup_dir)
            print(f"📦 Backed up existing planning directory to: {backup_dir}")
        
        return True
    
    def create_directory_structure(self) -> bool:
        """Create the directory structure."""
        try:
            # Create main directories
            self.planning_dir.mkdir(parents=True, exist_ok=True)
            self.phases_dir.mkdir(parents=True, exist_ok=True)
            
            # Create .gitignore in planning directory
            gitignore_path = self.planning_dir / ".gitignore"
            gitignore_path.write_text("# Git ignore for planning directory\n*\n!*.md\n!*.json\n")
            
            print(f"✅ Created directory structure at: {self.planning_dir}")
            return True
        except Exception as e:
            print(f"❌ Failed to create directory structure: {e}")
            return False
    
    def copy_template_file(self, template_name: str, dest_path: Path) -> bool:
        """Copy a template file to its destination."""
        try:
            template_path = self.template_dir / template_name
            if not template_path.exists():
                print(f"❌ Template not found: {template_path}")
                return False
            
            # Read template content
            content = template_path.read_text(encoding='utf-8')
            
            # Replace placeholders for specific files
            if template_name == "PROJECT.md":
                content = content.replace("[Project Name]", self.project_name)
            elif template_name == "ROADMAP.md":
                content = content.replace("[Project Name]", self.project_name)
            elif template_name == "STATE.md":
                content = content.replace("[Project Name]", self.project_name)
            elif template_name == "config.json":
                # Parse JSON and update project name
                config = json.loads(content)
                config["project"]["name"] = self.project_name
                config["project"]["description"] = f"{self.project_name} - Spec-driven development project"
                content = json.dumps(config, indent=2)
            
            # Write to destination
            dest_path.write_text(content, encoding='utf-8')
            print(f"✅ Created: {dest_path.relative_to(self.project_path)}")
            return True
        except Exception as e:
            print(f"❌ Failed to create {dest_path}: {e}")
            return False
    
    def create_initial_phase(self) -> bool:
        """Create the initial phase structure."""
        try:
            phase_name = "01-project-init"
            phase_dir = self.phases_dir / phase_name
            phase_dir.mkdir(parents=True, exist_ok=True)
            
            # Create phase-specific directories
            (phase_dir / "assets").mkdir(exist_ok=True)
            (phase_dir / "references").mkdir(exist_ok=True)
            
            # Copy PLAN.md template
            plan_template = self.template_dir / "PLAN.md"
            if plan_template.exists():
                plan_content = plan_template.read_text(encoding='utf-8')
                # Update phase name in the template
                plan_content = plan_content.replace("XX-name", phase_name)
                plan_content = plan_content.replace("plan: NN", "plan: 01")
                plan_content = plan_content.replace("wave: N", "wave: 1")
                
                plan_path = phase_dir / "01-01-PLAN.md"
                plan_path.write_text(plan_content, encoding='utf-8')
                print(f"✅ Created initial plan: {plan_path.relative_to(self.project_path)}")
            
            # Copy SUMMARY.md template
            summary_template = self.template_dir / "SUMMARY.md"
            if summary_template.exists():
                summary_content = summary_template.read_text(encoding='utf-8')
                # Update phase name in the template
                summary_content = summary_content.replace("XX-name", phase_name)
                summary_content = summary_content.replace("plan: YY", "plan: 01")
                
                summary_path = phase_dir / "01-01-SUMMARY.md"
                summary_path.write_text(summary_content, encoding='utf-8')
            
            return True
        except Exception as e:
            print(f"❌ Failed to create initial phase: {e}")
            return False
    
    def create_readme(self) -> bool:
        """Create a README.md file in the project root."""
        try:
            readme_path = self.project_path / "README.md"
            readme_content = f"""# {self.project_name}

Spec-Driven Development Project

## Project Structure

```
{self.project_name}/
├── .planning/          # Planning and documentation
│   ├── PROJECT.md     # Project context and goals
│   ├── ROADMAP.md     # Phased implementation plan
│   ├── REQUIREMENTS.md # Detailed requirements
│   ├── STATE.md       # Project state and decisions
│   ├── config.json    # Project configuration
│   └── phases/        # Phase plans and summaries
│       └── 01-project-init/
│           ├── 01-01-PLAN.md
│           └── 01-01-SUMMARY.md
├── src/               # Source code (to be created)
└── README.md          # This file
```

## Getting Started

1. Review the planning documents in `.planning/`
2. Start with Phase 1: Project Initialization
3. Follow the spec-driven development workflow

## Workflow

This project follows the spec-driven development methodology:

1. **Plan**: Define requirements and create detailed plans
2. **Execute**: Implement according to specifications
3. **Verify**: Validate against success criteria
4. **Document**: Record decisions and outcomes

## Next Steps

- Review `.planning/PROJECT.md` for project context
- Check `.planning/ROADMAP.md` for implementation phases
- Start with Phase 1 in `.planning/phases/01-project-init/`
"""
            
            readme_path.write_text(readme_content, encoding='utf-8')
            print(f"✅ Created: {readme_path.relative_to(self.project_path)}")
            return True
        except Exception as e:
            print(f"❌ Failed to create README.md: {e}")
            return False
    
    def initialize(self) -> bool:
        """Main initialization method."""
        print(f"🚀 Initializing spec-driven project: {self.project_name}")
        print(f"📁 Project path: {self.project_path}")
        
        # Step 1: Validate inputs
        if not self.validate_project_name():
            return False
        
        # Step 2: Check for existing structure
        if not self.check_existing_structure():
            return False
        
        # Step 3: Create directory structure
        if not self.create_directory_structure():
            return False
        
        # Step 4: Copy template files
        print("\n📄 Creating template files...")
        all_success = True
        for template_name, dest_path in self.required_files.items():
            if not self.copy_template_file(template_name, dest_path):
                all_success = False
        
        if not all_success:
            print("⚠️  Some template files failed to create")
        
        # Step 5: Create initial phase
        print("\n📈 Creating initial phase...")
        if not self.create_initial_phase():
            print("⚠️  Failed to create initial phase")
        
        # Step 6: Create README
        print("\n📖 Creating README...")
        if not self.create_readme():
            print("⚠️  Failed to create README")
        
        # Step 7: Summary
        print(f"\n{'='*50}")
        print(f"✅ Project initialization complete!")
        print(f"📁 Project: {self.project_name}")
        print(f"📍 Location: {self.project_path}")
        print(f"\n📋 Next steps:")
        print(f"1. Review `.planning/PROJECT.md`")
        print(f"2. Update `.planning/ROADMAP.md` with your phases")
        print(f"3. Define requirements in `.planning/REQUIREMENTS.md`")
        print(f"4. Start with Phase 1: `.planning/phases/01-project-init/01-01-PLAN.md`")
        print(f"{'='*50}")
        
        return True

def main():
    """Command-line entry point."""
    if len(sys.argv) < 2:
        print("Usage: python init_project.py <project_name> [project_path]")
        print("\nExample:")
        print("  python init_project.py my-awesome-project")
        print("  python init_project.py my-project ./projects/")
        sys.exit(1)
    
    project_name = sys.argv[1]
    project_path = sys.argv[2] if len(sys.argv) > 2 else "."
    
    initializer = ProjectInitializer(project_name, project_path)
    success = initializer.initialize()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()