#!/usr/bin/env python3
"""
Repo Doctor - tikrina repo struktūrą ir semantines patikras.
"""

import sys
from pathlib import Path

def check_file_exists(filepath, name):
    """Tikrina, ar failas egzistuoja."""
    if filepath.exists() and filepath.is_file():
        return True, None
    return False, f"Trūksta: {name}"

def check_dir_exists(dirpath, name):
    """Tikrina, ar katalogas egzistuoja."""
    if dirpath.exists() and dirpath.is_dir():
        return True, None
    return False, f"Trūksta katalogo: {name}"

def check_template_headers(template_path):
    """Tikrina, ar PROJECT_BRIEF.md turi privalomas antraštes."""
    required_headers = ["Tikslas", "Rezultatai", "Sėkmės kriterijai", "Draudžiama", "Įrodymai"]
    
    if not template_path.exists():
        return False, "templates/PROJECT_BRIEF.md neegzistuoja"
    
    try:
        content = template_path.read_text(encoding='utf-8')
        missing = []
        for header in required_headers:
            if header not in content:
                missing.append(header)
        
        if missing:
            return False, f"Trūksta antraščių templates/PROJECT_BRIEF.md: {', '.join(missing)}"
        return True, None
    except Exception as e:
        return False, f"Klaida skaitant templates/PROJECT_BRIEF.md: {e}"

def main():
    """Pagrindinė funkcija - tikrina repo struktūrą."""
    root = Path(".")
    errors = []
    warnings = []
    
    # Tikriname root failus
    root_files = [
        (root / "README.md", "README.md"),
        (root / "ARCHITECT_HANDOFF.md", "ARCHITECT_HANDOFF.md"),
        (root / "DISCOVERY_QUESTIONS.md", "DISCOVERY_QUESTIONS.md"),
        (root / "PROJECT_PORTFOLIO.md", "PROJECT_PORTFOLIO.md"),
    ]
    
    for filepath, name in root_files:
        exists, error = check_file_exists(filepath, name)
        if not exists:
            errors.append(error)
    
    # Tikriname katalogus
    dirs = [
        (root / "templates", "templates/"),
        (root / "projects", "projects/"),
        (root / "tools", "tools/"),
        (root / "gates", "gates/"),
        (root / ".github" / "workflows", ".github/workflows/"),
    ]
    
    for dirpath, name in dirs:
        exists, error = check_dir_exists(dirpath, name)
        if not exists:
            errors.append(error)
    
    # Tikriname templates failus
    template_files = [
        (root / "templates" / "PROJECT_BRIEF.md", "templates/PROJECT_BRIEF.md"),
        (root / "templates" / "EVIDENCE_MANIFEST.md", "templates/EVIDENCE_MANIFEST.md"),
        (root / "templates" / "PROJECT_PORTFOLIO.md", "templates/PROJECT_PORTFOLIO.md"),
    ]
    
    for filepath, name in template_files:
        exists, error = check_file_exists(filepath, name)
        if not exists:
            errors.append(error)
    
    # Tikriname tools ir gates failus
    tool_files = [
        (root / "tools" / "repo_doctor.py", "tools/repo_doctor.py"),
        (root / "gates" / "fact_check_gate.py", "gates/fact_check_gate.py"),
    ]
    
    for filepath, name in tool_files:
        exists, error = check_file_exists(filepath, name)
        if not exists:
            errors.append(error)
    
    # Tikriname workflow failą
    workflow_file = root / ".github" / "workflows" / "mvp_checks.yml"
    exists, error = check_file_exists(workflow_file, ".github/workflows/mvp_checks.yml")
    if not exists:
        errors.append(error)
    
    # Semantinė patikra: templates/PROJECT_BRIEF.md antraštės
    brief_template = root / "templates" / "PROJECT_BRIEF.md"
    exists, error = check_template_headers(brief_template)
    if not exists:
        errors.append(error)
    
    # Išvedame rezultatus
    print("=" * 60)
    print("REPO DOCTOR - STRUKTŪROS PATIKRA")
    print("=" * 60)
    
    if errors:
        print("\n❌ RASTOS KLAIDOS:\n")
        for error in errors:
            print(f"  • {error}")
        print("\n" + "=" * 60)
        print("REZULTATAS: FAIL")
        print("=" * 60)
        sys.exit(1)
    else:
        print("\n✅ Visi patikrinimai praeiti sėkmingai!")
        print("\nPatikrinta:")
        print("  • Root failai (README.md, ARCHITECT_HANDOFF.md, DISCOVERY_QUESTIONS.md, PROJECT_PORTFOLIO.md)")
        print("  • Katalogai (templates/, projects/, tools/, gates/, .github/workflows/)")
        print("  • Template failai (PROJECT_BRIEF.md, EVIDENCE_MANIFEST.md, PROJECT_PORTFOLIO.md)")
        print("  • Tool failai (repo_doctor.py, fact_check_gate.py)")
        print("  • Workflow failas (mvp_checks.yml)")
        print("  • Semantinė patikra (PROJECT_BRIEF.md privalomos antraštės)")
        print("\n" + "=" * 60)
        print("REZULTATAS: PASS")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    main()
