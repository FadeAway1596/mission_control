# PROJECT_BRIEF

## Tikslas
Minimalus Mission Control MVP: repo struktūra + Repo Doctor + Fact-check gate + GitHub Actions CI, kad PR metu būtų aiškus PASS/FAIL.

## Rezultatai
- README.md
- PROJECT_PORTFOLIO.md (root)
- templates/PROJECT_BRIEF.md
- templates/EVIDENCE_MANIFEST.md
- templates/PROJECT_PORTFOLIO.md
- tools/repo_doctor.py
- gates/fact_check_gate.py
- .github/workflows/mvp_checks.yml
- projects/mission_control_mvp/PROJECT_BRIEF.md
- projects/mission_control_mvp/EVIDENCE_MANIFEST.md

## Sėkmės kriterijai
- Sukūrus PR į `main`, GitHub “Checks” rodo `mvp-checks = PASS`.
- Repo Doctor grąžina PASS (struktūra atitinka reikalavimus).
- Fact-check gate grąžina PASS (yra “Įrodymai” su keliu arba URL).
- Nėra “Pavyzdys”, “[...]”, “TBD” realiuose projekto failuose `projects/mission_control_mvp/`.

## Draudžiama
- Automatinis vykdymas be patvirtinimo.
- Rašymas už repo / projekto ribų.
- Interneto įjungimas be leidimo.
- Slaptų raktų / secrets kopijavimas į repo.

## Įrodymai
- Projekto failai (keliai repo viduje).
- Pakeitimų istorija (commit/PR).
- CI patikros rezultatas (GitHub Actions).
- Ekrano nuotraukos (jei reikia).
