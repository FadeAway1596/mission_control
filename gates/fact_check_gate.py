#!/usr/bin/env python3
"""
Fact-check Gate - tikrina, ar visi teiginiai turi įrodymus.
"""

import sys
import re
from pathlib import Path

def find_evidence_manifests():
    """Suranda visus EVIDENCE_MANIFEST.md failus projects/ kataloge."""
    projects_dir = Path("projects")
    if not projects_dir.exists():
        return []
    
    manifests = list(projects_dir.glob("**/EVIDENCE_MANIFEST.md"))
    return manifests

def has_url_or_path_or_commit(line):
    """Tikrina, ar eilutėje yra URL, kelias arba commit hash."""
    line = line.strip()
    if not line or line.startswith("#"):
        return False
    
    # URL patikrinimas (http://, https://)
    if re.search(r'https?://', line):
        return True
    
    # Kelio patikrinimas (./, /, projects/)
    if re.search(r'(\./|/|projects/)', line):
        return True
    
    # Commit hash patikrinimas (commit: abc123, abc123, #abc123)
    if re.search(r'commit:\s*[a-f0-9]+', line, re.IGNORECASE):
        return True
    if re.search(r'[#\s][a-f0-9]{6,}', line, re.IGNORECASE):
        return True
    
    return False

def check_manifest(manifest_path):
    """Tikrina vieną EVIDENCE_MANIFEST.md failą."""
    try:
        content = manifest_path.read_text(encoding='utf-8')
    except Exception as e:
        return False, f"Klaida skaitant failą: {e}"
    
    # Tikriname, ar yra "Įrodymai" skyrius
    evidence_section_pattern = r'^##+\s+Įrodymai'
    if not re.search(evidence_section_pattern, content, re.MULTILINE | re.IGNORECASE):
        return False, "Trūksta skyriaus 'Įrodymai'"
    
    # Surandame "Įrodymai" skyrių ir eilutes po juo
    lines = content.split('\n')
    in_evidence_section = False
    evidence_lines = []
    
    for i, line in enumerate(lines):
        # Tikriname, ar tai "Įrodymai" antraštė
        if re.match(r'^##+\s+Įrodymai', line, re.IGNORECASE):
            in_evidence_section = True
            continue
        
        # Jei radome kitą antraštę po "Įrodymai", sustabdom
        if in_evidence_section and re.match(r'^##+\s+', line):
            break
        
        # Jei esame "Įrodymai" skyriuje, renkame eilutes
        if in_evidence_section:
            evidence_lines.append(line)
    
    # Tikriname, ar yra bent viena ne tuščia eilutė
    non_empty_lines = [line for line in evidence_lines if line.strip() and not line.strip().startswith('#')]
    if not non_empty_lines:
        return False, "Skyriuje 'Įrodymai' nėra nei vienos eilutės"
    
    # Tikriname kiekvieną eilutę
    failed_lines = []
    for line in non_empty_lines:
        if not has_url_or_path_or_commit(line):
            failed_lines.append(line.strip())
    
    if failed_lines:
        return False, f"Eilutės be įrodymų:\n  " + "\n  ".join(failed_lines[:5])  # Rodo pirmas 5
    
    return True, None

def main():
    """Pagrindinė funkcija - tikrina visus EVIDENCE_MANIFEST.md failus."""
    manifests = find_evidence_manifests()
    
    print("=" * 60)
    print("FACT-CHECK GATE - ĮRODYMAI PATIKRA")
    print("=" * 60)
    
    # Jei nėra jokių manifestų
    if not manifests:
        print("\nℹ️  Nerasta jokių EVIDENCE_MANIFEST.md failų projects/ kataloge.")
        print("   Tai normalu, jei dar nėra pirmo projekto.")
        print("\n" + "=" * 60)
        print("REZULTATAS: PASS (nėra ką tikrinti dar)")
        print("=" * 60)
        sys.exit(0)
    
    # Tikriname kiekvieną manifestą
    print(f"\nRasta {len(manifests)} EVIDENCE_MANIFEST.md failų:\n")
    
    all_passed = True
    failed_manifests = []
    
    for manifest in manifests:
        print(f"  Tikrinama: {manifest}")
        passed, error = check_manifest(manifest)
        
        if passed:
            print(f"    ✅ PASS")
        else:
            print(f"    ❌ FAIL: {error}")
            all_passed = False
            failed_manifests.append((manifest, error))
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("REZULTATAS: PASS")
        print("=" * 60)
        sys.exit(0)
    else:
        print("REZULTATAS: FAIL")
        print("=" * 60)
        print("\nKlaidingi failai:")
        for manifest, error in failed_manifests:
            print(f"  • {manifest}: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()
