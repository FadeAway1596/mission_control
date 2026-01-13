# RUN LEDGER

Įrodymų registras po kiekvieno darbo. Kiekvienas įrašas dokumentuoja, kas buvo padaryta, kokie buvo įrodymai ir koks buvo sprendimas.

## Šablonas įrašui

```markdown
## [YYYY-MM-DD] - [Projekto pavadinimas / veiksmas]

**Branch:** `branch-name`  
**PR link:** `https://github.com/user/repo/pull/123`  
**Commit hash:** `abc123def456...`

### CLAIM
[Ką teigėme, kad padarysime]

### EVIDENCE
[Kokie įrodymai buvo pateikti - failai, URL, commit hash, CI rezultatai]

### DECISION
[Koks buvo sprendimas - PASS/FAIL, kas buvo patvirtinta, kas atmesta]

### Actions Run
[GitHub Actions workflow link arba Actions run link]
```

---

## Pavyzdys

## [2026-01-14] - Mission Control v0.2: Context Pack + Policy + Run Ledger

**Branch:** `mission-control-v0-2`  
**PR link:** `[PR link bus pridėtas po PR sukūrimo]`  
**Commit hash:** `[commit hash bus pridėtas po commit]`

### CLAIM
Sukurti Mission Control v0.2 sistemos kaulus: CONTEXT_PACK.md, policy/POLICY.md, runs/RUN_LEDGER.md ir atnaujinti Repo Doctor, kad tikrintų šiuos failus.

### EVIDENCE
- `./CONTEXT_PACK.md` - aprašo sistemą, kanoną, draudimus, PR darbo būdą
- `./policy/POLICY.md` - Network default OFF, allowed sources, draudžiamos veiklos
- `./runs/RUN_LEDGER.md` - šablonas įrašams
- `./tools/repo_doctor.py` - atnaujintas su patikrinimais
- `./projects/mission_control_v0_2/EVIDENCE_MANIFEST.md` - su nuorodomis

### DECISION
[Bus užpildyta po PR patvirtinimo]

### Actions Run
[GitHub Actions workflow link bus pridėtas po PR sukūrimo]
