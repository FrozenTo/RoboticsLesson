# 3D printimine ja CAD — Labor 1 checklist

## Projekti algus

- [O] Loo meeskonnale üks Git repo.
- [O] Loo kaust `3d-print/lab1/`.
- [O] Kopeeri labori ülesanne faili `3d-print/lab1/README.md`.
- [O] Veendu, et repo juurkaustas on `AGENTS.md`.
- [O] Pane README-sse kirja meeskonnaliikmed.
- [O] Lisa esimene arenduspäeviku sissekanne.
- [O] Pane kirja, milliseid printereid, materjale ja tööriistu tegelikult kasutate.

Esimene kuup, mis oli välja prinditud, oli silindriga kinni jäänud ja jäi üks tervikuks.

---

## 1. Kuup — printeri lõtku test

- [O] Tee Fusion 360-s 50 × 50 × 50 mm kuup.
- [O] Tee kuubi sisse silinder raadiusega 20 mm.
- [O] Tee silindri ja ümbritseva osa vaheline lõtk Fusionis parameetriks. (tehtud 0.1 mm) Oli vaja 0.2mm
- [O] Salvesta Fusioni lähtefail.
- [O] Ekspordi STL.
- [O] Tee PrusaSliceris `.3mf`.
- [O] Prindi esimene lõtkuvariant.
- [O] Kontrolli, kas silinder:
  - [O] on täiesti kinni;
  - [O] liigub suure jõuga;
  - [O] liigub normaalselt;
  - [O] pöörleb vabalt.
- [O] Vajadusel muuda lõtku ja prindi uus variant.
- [O] Leia väikseim lõtk, millega silinder liigub.
- [O] Leia lõtk, mille juures detail veel kinni sulab.
- [O] Pane kõik testitud lõtkuväärtused README-sse mm-des.
- [O] Pane kirja kasutatud printer.
- [O] Pane kirja kasutatud materjal.
- [O] Pane kirja olulised sliceri seaded.
- [O] Salvesta iga prinditud variandi STL ja `.3mf`.

### Kuubi tulemus

- [O] Sobiv lõtk on teada.
- [0] Kinni sulamise piir on teada.
- [0] Mõlemad väärtused on README-s koos ühikutega.

---

## 2. Paindlik tükk

- [O] Mõtle välja lihtne painduv testdetail.
- [O] Pane kirja detaili mõõdud:
  - [O] pikkus;
  - [O] laius;
  - [O] paksus.
- [O] Salvesta CAD lähtefail.
- [O] Ekspordi STL.
- [O] Tee `.3mf`.
- [O] Prindi detail.
- [O] Testi, kui palju saab detaili painutada nii, et see tuleb tagasi.
- [O] Pane kirja elastse painde piir.
- [O] Painuta rohkem ja leia koht, kus detail jääb kõveraks.
- [O] Pane kirja plastilise painde piir.
- [O] Painuta kuni murdumiseni.
- [O] Pane kirja, kus ja kuidas detail murdus.
- [O] Märgi paine mm-des ja/või kraadides.
- [O] Tee vajadusel uus versioon.
- [O] Salvesta kõik versioonid eraldi failidena.
- [O] Kirjuta README-sse, mida igas versioonis muutsid ja miks.

### Paindliku tüki tulemus

- [O] Elastse painde piir on teada.
- [O] Plastilise painde piir on teada.
- [O] Murdumise koht/piir on teada.
- [O] Kõik tulemused on README-s koos ühikutega.

---

## 3. Pastakahoidiku planeerimine

- [O] Vaata üle MG400 kinnitus/flants.
- [O] Ava antud MG400 mount Fusion 360 fail.
- [O] Mõõda kuulpastakas nihikuga.
- [O] Mõõda:
  - [O] pastaka läbimõõt;
  - [O] kinnituseks vajalik pikkus;
  - [O] pastaka otsa asukoht;
  - [O] MG400 kinnituse vajalikud mõõdud.
- [O] Otsusta, kuidas pastakas hoidikusse kinnitub.
- [O] Otsusta, kuidas hoidik Z-suunas järele annab.
- [O] Kasuta kuubi testist saadud lõtku.
- [O] Kasuta painduva detaili testist saadud tulemusi.
- [O] Tee esimene CAD-versioon.

---

## 4. Pastakahoidiku prototüübid

### v01

- [O] Salvesta fail nimega näiteks `pen_holder_v01`.
- [O] Ekspordi STL.
- [O] Tee `.3mf`.
- [O] Prindi.
- [O] Kontrolli, kas pastakas mahub hoidikusse.
- [O] Kontrolli, kas hoidik sobib MG400 külge.
- [O] Kontrolli, kas painduv osa annab Z-suunas järele.
- [O] Kontrolli, kas hoidik tuleb pärast vajutamist tagasi algasendisse.
- [O] Pane kirja probleemid.
- [O] Pane kirja, mida järgmises versioonis muuta.

### Järgmised versioonid

- [O] Tee `v02`.
- [O] Dokumenteeri, mis muutus ja miks.
- [O] Tee vajadusel `v03`, `v04` jne.
- [O] Ära kirjuta vanu versioone üle.
- [O] Säilita iga versiooni lähtefail.
- [O] Säilita iga prinditud versiooni STL.
- [O] Säilita iga prinditud versiooni `.3mf`.
- [O] Testi umbes mõnemillimeetrist Z-viga.
- [O] Veendu, et pastakas jääb terveks.
- [O] Veendu, et joon jääb paberile.

### Pastakahoidiku lõpptulemus

- [O] Pastakas püsib kindlalt hoidikus.
- [O] Hoidik kinnitub kindlalt MG400 külge.
- [O] Hoidik annab Z-suunas järele.
- [O] Hoidik taastab pärast vajutamist oma asendi.
- [O] Väike Z-kõrguse viga ei riku pastakat ega joonistamist.

---

## 5. MG400 test

- [O] Kinnita hoidik MG400 külge.
- [O] Pane paber tööalale.
- [O] Kinnita paber vajadusel maalriteibiga.
- [O] Hoia hädastopp käeulatuses.
- [O] Tee esimene robotijooks väikese kiirusega.
- [O] Õpeta/kinnita kirjutamise Z-kõrgus.
- [O] Kontrolli, et hoidiku painduv osa kompenseeriks väikest Z-viga.
- [O] Kontrolli, et pastakale ei tuleks liiga suurt survet.
- [O] Pane robot joonistama üks lihtne täht.

---

## 6. ESP32 + robot

- [ ] ESP32 näitab ekraanil tähte.
- [ ] Robot saab info, millist tähte joonistada.
- [ ] MG400 joonistab sama tähe, mida ESP32 näitab.
- [ ] Demo töötab algusest lõpuni.

---

## 7. Tellimus — hiljemalt 22.09.2026

- [ ] Vaata pärast esimesi katseid üle, mis jäi reaalselt puudu.
- [ ] Kontrolli, kas vaja on juurde:
  - [ ] PLA;
  - [ ] PETG;
  - [ ] M5 polte;
  - [ ] M5 mutreid;
  - [ ] M3 kuumsisestusi;
  - [ ] magneteid;
  - [ ] muid komponente.
- [ ] Pane vajalikud asjad jagatud Google Sheeti.
- [ ] Lisa kogused.
- [ ] Lisa võimalusel mõõdud/tüüp.
- [ ] Veendu, et tellimus on valmis enne 22.09.2026.

---

## 8. Arenduspäevik

Iga töösessiooni järel:

- [O] Lisa kuupäev.
- [O] Lisa kohal olnud meeskonnaliikmed.
- [O] Kirjuta, mida tegite.
- [O] Kirjuta mõõdetud numbrid koos ühikutega.
- [O] Kirjuta, mis juhtus.
- [O] Kirjuta, mida otsustasite.
- [O] Kirjuta, miks nii otsustasite.
- [O] Kirjuta, mis jäi järgmiseks korraks.
- [O] Ära muuda vanu päevikusissekandeid — lisa uus sissekanne.

Soovituslik vorm:

```markdown
### PP.KK.AA — kes olid kohal

**Tegime:**
- ...

**Juhtus (numbrid):**
- ...

**Otsustasime, ja miks:**
- ...

**Lahti järgmiseks korraks:**
- ...
```

---

## 9. README

- [ ] Algne ülesande tekst on alles.
- [ ] Täidetud on „KAARDISTA ISE — eesmärk”.
- [ ] Täidetud on „KAARDISTA ISE — kuupäevad ja sinu enda sammud”.
- [ ] Täidetud on „KAARDISTA ISE — mida sa päriselt kasutasid”.
- [ ] Lisatud on enda kasutatud allikad.
- [ ] Kuubi tulemused on dokumenteeritud.
- [ ] Paindliku tüki tulemused on dokumenteeritud.
- [ ] Pastakahoidiku kõik versioonid on kirjeldatud.
- [ ] Iga versiooni juures on kirjas, mis muutus ja miks.
- [ ] Tegemata asja kohta on kirjas, miks see tegemata jäi.
- [ ] Arenduspäevik on täidetud.
- [ ] Lõpuosa „Git repo ja tag” on täidetud.
- [ ] Lõpuosa „Numbrid, mille see labor andis” on täidetud.
- [ ] Lõpuosa „Mida me teeksime teisiti” on täidetud.
- [ ] Lõpuosa „Mida järgmine labor peaks enne alustamist teadma” on täidetud.

---

## 10. Failid repos

Kaustas `3d-print/lab1/`:

- [ ] `README.md`
- [ ] kuubi CAD lähtefail
- [ ] kuubi STL-id
- [ ] kuubi `.3mf`-id
- [ ] painduva detaili CAD lähtefail
- [ ] painduva detaili STL-id
- [ ] painduva detaili `.3mf`-id
- [ ] `pen_holder_v01`
- [ ] `pen_holder_v02`
- [ ] järgmised hoidiku versioonid
- [ ] lõpliku hoidiku CAD lähtefail
- [ ] lõpliku hoidiku STL
- [ ] lõpliku hoidiku `.3mf`
- [ ] muud vajalikud skeemid või failid

Repo juurkaustas:

- [ ] `AGENTS.md`

---

## 11. Git

- [ ] Kõik vajalikud failid on repos.
- [ ] Muudatused on commititud.
- [ ] Repo on remote'i pushitud.
- [ ] Loo tag `3d-print-lab1`.
- [ ] Push tag remote'i.
- [ ] Kontrolli, et tag on nähtav.

Näiteks:

```bash
git add .
git commit -m "Complete 3D printing lab 1"
git push

git tag 3d-print-lab1
git push origin 3d-print-lab1
```

---

## 12. Kaitsmiseks — 06.10.2026

- [ ] Git repo link on olemas.
- [ ] Tag `3d-print-lab1` on olemas.
- [ ] Robot töötab.
- [ ] Pastakahoidik on MG400 küljes.
- [ ] Pastakahoidik annab Z-suunas järele.
- [ ] ESP32 näitab tähte.
- [ ] MG400 joonistab sama tähe.
- [ ] Oskad öelda printeri sobiva lõtku.
- [ ] Oskad öelda, millise lõtkuga detail kinni sulas.
- [ ] Oskad öelda painduva detaili elastse painde piiri.
- [ ] Oskad öelda plastilise painde piiri.
- [ ] Oskad kirjeldada, kus/kuidas detail murdus.
- [ ] Oskad selgitada, miks lõplik pastakahoidik on sellise kujuga.
- [ ] Oskad näidata varasemaid hoidiku versioone.
- [ ] Oskad selgitada, mida igas versioonis muutsid ja miks.
- [ ] Oskad avada ja selgitada arenduspäevikut.

---

# Hindamise kontroll

## Tööfailid — 5 p

- [ ] Kuubi lähtefail.
- [ ] Paindliku detaili lähtefail.
- [ ] Kõik olulised pastakahoidiku versioonid.
- [ ] STL-id.
- [ ] `.3mf`-id.

## Analüüs — 5 p

- [ ] Printeri lõtk on mõõdetud.
- [ ] Elastse painde piir on mõõdetud.
- [ ] Plastilise painde piir on mõõdetud.
- [ ] Murdumise piir/koht on dokumenteeritud.

## Prototüüp — 5 p

- [ ] Pastakahoidik on roboti küljes.
- [ ] Hoidik annab järele.
- [ ] Robot joonistab.
- [ ] Joonistatav täht vastab ESP32 ekraanil olevale tähele.

## Dokumentatsioon — 5 p

- [ ] `README.md` on täidetud.
- [ ] Arenduspäevik on täidetud.
- [ ] `AGENTS.md` on olemas ja uuendatud.
- [ ] Git tag `3d-print-lab1` on olemas.

---

# Lõplik „DONE”

- [ ] Kuup prinditud ja lõtk teada.
- [ ] Paindlik tükk prinditud ja mõõdetud.
- [ ] Pastakahoidik töötab.
- [ ] MG400 joonistab ESP32 näidatud tähe.
- [ ] Kõik failid on repos.
- [ ] README on valmis.
- [ ] Arenduspäevik on valmis.
- [ ] AGENTS.md on valmis.
- [ ] Tellimus on tehtud.
- [ ] Git tag on tehtud.
- [ ] Oleme kaitsmiseks valmis.
