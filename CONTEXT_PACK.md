# CONTEXT PACK

## Kas yra sistema

Mission Control yra automatinė projekto valdymo sistema, kuri veda projektus per Discovery fazę: užduoda klausimus, atlieka realybės patikrą, sugeneruoja pritaikytus klausimus ir laukia patvirtinimo prieš bet kokius diegimus. Sistema saugo visus įrodymus ir kuria portfolio.

## Kas yra kanonas

Kanonas yra vienintelė tiesa apie sistemą. Visi dokumentai, kodas ir procesai turi atitikti šį kanoną. Kanonas apibrėžiamas per CONTEXT_PACK.md, PROJECT_BRIEF.md failus ir patvirtinamas per PR procesą.

## Draudžiama

- Automatinis vykdymas be patvirtinimo
- Rašymas už projekto ribų
- Interneto įjungimas be explicit leidimo (žr. policy/POLICY.md)
- Scraping be leidimo
- Fakto išradimas (invent facts)
- Slaptų raktų / secrets kopijavimas į repo

## Kaip dirbame per PR

Visi pakeitimai vyksta per Pull Request procesą:
1. Sukuriamas branch su projekto vardu
2. Atliekami pakeitimai ir užpildomi dokumentai
3. Sukuriamas PR į main
4. Repo Doctor tikrina struktūrą ir discipliną
5. Fact-check gate tikrina įrodymus
6. Tik po visų patikrų (MVP Checks = PASS) galimas merge
