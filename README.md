CI smoke testS
# Mission Control sistema

Mission Control sistema automatiškai veda projektus per Discovery fazę: užduoda 20 klausimų, atlieka realybės patikrą, sugeneruoja pritaikytus klausimus ir laukia patvirtinimo prieš bet kokius diegimus. Sistema saugo visus įrodymus ir kuria portfolio.

## Kaip vyksta procesas

1. **Discovery** - užduodami 20 bazinių klausimų
2. **Reality check** - tikrinamas laikas, pinigai, techninė aplinka
3. **Custom klausimai** - sugeneruojami 10 pritaikytų klausimų (+3 jei reikia)
4. **Understanding Gate** - laukiamas TAIP/NE patvirtinimas
5. **MVP implementacija** - tik po patvirtinimo

## Struktūra

- `templates/` - šablonai projektams (PROJECT_BRIEF.md, EVIDENCE_MANIFEST.md, PROJECT_PORTFOLIO.md)
- `projects/` - realūs projektai (kiekvienas projektas `projects/<project_name>/`)
- `tools/` - įrankiai (repo_doctor.py)
- `gates/` - patikrinimo vartai (fact_check_gate.py)
- `.github/workflows/` - CI workflow failai

## Portfolio

Portfolio failas `PROJECT_PORTFOLIO.md` yra root kataloge. Jame saugomi visų projektų santraukos. Kiekvienas projektas turi savo įrašą su statusu (BAIGTA / VYKDOMA / ATIDĖTA) ir nuoroda į EVIDENCE_MANIFEST.
