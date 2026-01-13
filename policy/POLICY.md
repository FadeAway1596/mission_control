# POLICY

## Network Default: OFF

Pagal nutylėjimą visos išorinio turinio (external content) operacijos yra **UŽDARYTOS**. Interneto prieiga, web scraping, API kvietimai - viskas reikalauja explicit leidimo.

## Allowed Sources (Allowlist)

Leidžiamos šaltinių kategorijos:

- **Official websites** - oficialūs projekto, įrankio ar dokumentacijos puslapiai (pvz. GitHub oficialus repo, dokumentacijos puslapiai)
- **Hunter** - jei naudojamas Hunter API arba panašus įrankis su explicit leidimu
- **User CSV** - vartotojo pateikti CSV failai arba duomenys
- **GitHub API** - tik oficialus GitHub API su autentifikacija (jei reikia)

## Draudžiama

- **Scraping** - web scraping be explicit leidimo ir allowlist patvirtinimo
- **Invent facts** - fakto išradimas, sugalvojimas arba netikrų duomenų naudojimas
- **Unofficial sources** - neoficialūs šaltiniai, nepatvirtinti puslapiai
- **Automated data collection** - automatinis duomenų rinkimas be leidimo
- **Third-party APIs** - trečiųjų šalių API be explicit leidimo

## Leidimo procesas

Norint naudoti external content:
1. Pridėti į PROJECT_BRIEF.md sekciją "Draudžiama" arba "Leidimai"
2. Nurodyti konkretų šaltinį ir priežastį
3. Gauti patvirtinimą per PR procesą
4. Įtraukti į EVIDENCE_MANIFEST.md kaip įrodymą
