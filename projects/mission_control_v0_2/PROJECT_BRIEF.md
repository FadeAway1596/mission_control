# PROJECT_BRIEF

## Tikslas

Sukurti Mission Control v0.2 sistemos kaulus: Context Pack (viena tiesa), Policy (external content = untrusted + leidimai), ir Run Ledger (įrodymai po kiekvieno darbo). Visi PR'ai turi būti priversti laikytis disciplinos per Repo Doctor automatines patikras.

## Rezultatai

- CONTEXT_PACK.md (root) - 10-20 eilučių apie sistemą, kanoną, draudimus, PR darbo būdą
- policy/POLICY.md - Network default OFF, allowed sources, draudžiamos veiklos
- runs/RUN_LEDGER.md - šablonas įrašams su Date, branch, PR link, CLAIM → EVIDENCE → DECISION, Actions link, commit hash
- Atnaujintas tools/repo_doctor.py - tikrina, ar egzistuoja visi 3 failai
- projects/mission_control_v0_2/EVIDENCE_MANIFEST.md - su nuorodomis į visus 3 failus

## Sėkmės kriterijai

- CONTEXT_PACK.md egzistuoja root kataloge ir aprašo sistemą, kanoną, draudimus, PR darbo būdą
- policy/POLICY.md egzistuoja su Network default OFF, allowed sources, draudžiamomis veiklomis
- runs/RUN_LEDGER.md egzistuoja su šablonu įrašams
- Repo Doctor tikrina visus 3 failus ir grąžina FAIL, jei trūksta
- EVIDENCE_MANIFEST.md turi bent 3 eilutes su nuorodomis į visus 3 failus
- GitHub Actions MVP Checks praeina su visais naujais patikrinimais

## Draudžiama

- Auto-execute be patvirtinimo
- Rašymas už projekto ribų
- Interneto įjungimas be leidimo (Policy default OFF)
- Scraping be explicit leidimo
- Fakto išradimas (invent facts)
- Liesti slaptus raktus / secrets

## Įrodymai

- Projekto failai: CONTEXT_PACK.md, policy/POLICY.md, runs/RUN_LEDGER.md
- Atnaujintas tools/repo_doctor.py su naujais patikrinimais
- Pakeitimų istorija (git commit)
- CI patikros rezultatas (GitHub Actions)
- EVIDENCE_MANIFEST.md su nuorodomis
