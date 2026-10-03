# Nutikad Lahendused — Labor 1 checklist

## 1. Repo ja ettevalmistus

- [O] Loo kaust `smart-solutions/lab1/`
- [O] Kopeeri labori ülesanne faili `README.md`
- [O] Loo kaust `src/`
- [O] Loo kaust `firmware/`
- [O] Loo kaust `data/`
- [O] Loo kaust `docs/`
- [O] Kontrolli ja uuenda repo juurkaustas `AGENTS.md`
- [O] Loo `CHECKLIST.md`
- [/] Alusta arenduspäevikut
- [O] Pane kirja meeskonnaliikmed
- [O] Tee esialgne draw.io skeem kogu süsteemist

---

## 2. Tellimus — `docs/bom.md`

**Tähtaeg: 22.09.2026**

- [ ] Vaata üle, millised vajalikud osad on juba olemas
- [O] Kontrolli, kas sülearvutil on Ethernet-port
- [O] Vajadusel lisa USB-C → Ethernet adapter
- [O] Kontrolli LAN-kaabli olemasolu
- [O] Kontrolli USB-C kaablite olemasolu
- [O] Kontrolli markeri/pastaka olemasolu
- [O] Kontrolli paberi olemasolu
- [O] Kontrolli maalriteibi olemasolu
- [ ] Kontrolli AtomS3 jaoks vajalikke lisatarvikuid
- [ ] Pane puuduvad komponendid faili `docs/bom.md`
- [ ] Lisa iga komponendi juurde põhjendus, miks seda vaja on

---

# ROBOT

## 3. MG400 võrguühendus

- [O] Ühenda MG400 LAN-kaabliga arvutiga
- [O] Kontrolli roboti aadressi: `192.168.1.6`
- [O] Seadista arvuti Ethernet-adapter:
  - [O] IP: `192.168.1.50`
  - [O] Mask: `255.255.255.0`
  - [O] Gateway: tühi
- [O] Testi ühendust käsuga `ping 192.168.1.6`
- [ ] Pane aadressiplaan dokumentatsiooni
- [ ] Pane kirja kasutatud Ethernet-liides

---

## 4. MG400 baaspakett

- [O] Laadi/klooni `KKallas/mg400-base`
- [O] Kontrolli baaspaketi README-d
- [O] Loo Python virtual environment
- [O] Installi vajalikud Python paketid
- [O] Käivita `mg400 status`
- [O] Kontrolli, et roboti režiim kuvatakse
- [O] Kontrolli, et roboti praegune asend kuvatakse
- [O] Käivita `mg400 serve`
- [O] Ava MG400 veebiliides
- [O] Ühenda robot veebiliidesest
- [O] Luba robot veebiliidesest
- [O] Testi X liikumist
- [O] Testi Y liikumist
- [O] Testi Z liikumist
- [O] Testi R liikumist
- [O] Testi salvestatud asendeid
- [O] Esimesed liikumised tee 20% kiirusega

---

## 5. MG400 pordid

- [ ] Kontrolli porti `29999`
- [ ] Kontrolli porti `30003`
- [ ] Kontrolli porti `30004`
- [ ] Pane dokumentatsiooni:
  - [ ] `29999` — käsud / dashboard
  - [ ] `30003` — liikumiskäsud
  - [ ] `30004` — tagasiside
- [ ] Kontrolli, et robotile saadab liikumiskäske korraga ainult üks programm

---

## 6. Pump

Baaspaketi eeldus:

- `DO2` — imemine
- `DO1` — puhumine

Kontrollida enne kasutamist.

- [O] Leia pumbakasti dokumentatsioon
- [O] Kontrolli pumbakasti ühendusi
- [O] Kontrolli DO1 multimeetriga
- [O] Kontrolli DO2 multimeetriga
- [O] Tuvasta, milline DO juhib imemist
- [O] Tuvasta, milline DO juhib puhumist
- [O] Testi imemist käsurealt
- [O] Testi puhumist käsurealt
- [O] Pane õiged DO-numbrid dokumentatsiooni
- [O] Kirjelda, kuidas DO-numbrid üle kontrolliti
- [O] Märgi üles, kui baaspaketi eeldus oli vale

---

## 7. MG400 neli asendit

Õpeta robotile:

- [O] `above_source`
- [O] `source`
- [O] `above_finished`
- [O] `finished`

Seejärel:

- [O] Kontrolli iga positsiooni X
- [O] Kontrolli iga positsiooni Y
- [O] Kontrolli iga positsiooni Z
- [O] Kontrolli iga positsiooni R
- [x] Salvesta positsioonid faili `data/positions.json`
- [ ] Kontrolli, et positsioonid laaditakse failist õigesti

---

## 8. Pick-and-place test

Robot peab tõstma detaili allikast valmis pessa 10 korda järjest.

- [ ] Test 1
- [ ] Test 2
- [ ] Test 3
- [ ] Test 4
- [ ] Test 5
- [ ] Test 6
- [ ] Test 7
- [ ] Test 8
- [ ] Test 9
- [ ] Test 10
- [ ] Salvesta tulemused faili `docs/pick_test.csv`
- [ ] Märgi iga testi juurde, kas detail tõsteti
- [ ] Märgi iga testi juurde, kas detail asetati õigesti
- [ ] Lisa vajadusel märkus

---

## 9. MG400 baaspaketi kontroll

- [ ] Kontrolli, kas README juhised töötasid
- [ ] Kontrolli, kas IP-aadressid olid õiged
- [ ] Kontrolli, kas pumba DO-numbrid olid õiged
- [ ] Kontrolli, kas midagi oli puudu
- [ ] Pane leitud probleemid arenduspäevikusse
- [ ] Paranda vajadusel baaspaketti
- [ ] Tee vajadusel Pull Request õppejõu repole

---

# EKRAAN / ATOMS3

## 10. AtomS3 PlatformIO projekt

- [ ] Ava `ESP32-Image-Server`
- [ ] Ava projekt VS Code'is
- [ ] Ava PlatformIO
- [ ] Kontrolli board: `m5stack-atoms3`
- [ ] Kontrolli M5Unified kasutamist
- [ ] Ühenda AtomS3 USB-C-ga
- [O] Buildi projekt
- [O] Laadi firmware AtomS3-le
- [ ] Ava Serial Monitor
- [ ] Sea Serial Monitor kiiruseks `115200`
- [ ] Kontrolli, et AtomS3 käivitub õigesti
- [ ] Pane kirja firmware laadimise sammud
- [ ] Mõõda firmware laadimise aeg

---

## 11. AtomS3 WiFi

- [ ] Kontrolli, et AtomS3 teeb oma WiFi võrgu
- [ ] Pane kirja WiFi võrgu nimi
- [ ] Pane kirja WiFi parool
- [ ] Ühenda telefon AtomS3 WiFi-ga
- [ ] Kontrolli Atomi aadressi `192.168.4.1`
- [ ] Ava Atomi veebileht
- [ ] Pane lehe URL dokumentatsiooni
- [ ] Kontrolli, et veebileht töötab telefonist

---

## 12. Pildi saatmine ekraanile

- [ ] Ava AtomS3 veebileht
- [ ] Vali testpilt
- [ ] Crop'i pilt 128 × 128 suuruseks
- [ ] Saada pilt AtomS3-le
- [ ] Kontrolli, et pilt ilmub AtomS3 ekraanile
- [ ] Mõõda ühe 128 × 128 pildi saatmise aeg
- [ ] Pane mõõdetud aeg dokumentatsiooni

---

## 13. Captive portal

Eesmärk: pärast Atomi WiFi-ga liitumist peab veebileht avanema automaatselt.

- [ ] Lisa DNS-server
- [ ] Suuna DNS-päringud Atomi aadressile
- [ ] Kontrolli captive portalit Androidiga
- [ ] Logi Androidi kontrollaadressid
- [ ] Kontrolli captive portalit iPhone'iga, kui võimalik
- [ ] Logi iPhone'i kontrollaadressid
- [ ] Kontrolli, et telefon avab lehe ise
- [ ] Kontrolli, et kasutaja ei pea sisestama `192.168.4.1`
- [ ] Pane kontrollaadressid dokumentatsiooni

---

## 14. AtomS3 seadete ja testide leht

Lisa samale olemasolevale veebilehele seadete/testide osa.

- [ ] WiFi võrgu nime seadistus
- [ ] WiFi parooli seadistus
- [ ] Jaama aadressi seadistus
- [ ] Testinupp
- [ ] Testinupp kuvab AtomS3 ekraanil oleku
- [ ] Kontrolli, et seadete osa töötab
- [ ] Kontrolli, et hiljem saab samale lehele lisada uusi seadmeid
- [ ] Dokumenteeri leht failis `docs/atom_page.md`

Tulevaste laborite jaoks peab leht võimaldama juurde lisada:

- [ ] rõhuanduri
- [ ] UART-i
- [ ] klapi
- [ ] LED-i

---

# TÄHT

## 15. Tähe kommunikatsioonikanal

Lepi Andmehõive osaga kokku, kuidas täht AtomS3-st jaama jõuab.

- [ ] Vali kommunikatsioonimeetod
- [ ] Otsusta, kas jaam küsib Atomilt uut tähte
- [ ] Või otsusta, kas Atom saadab tähe ise jaamale
- [ ] Pane paika jaama IP-aadress
- [ ] Pane paika kasutatav port
- [ ] Pane paika HTTP endpoint, kui kasutatakse HTTP-d
- [ ] Pane paika JSON formaat

Näide:

```json
{"letter":"A"}
```

- [ ] Dokumenteeri lahendus failis `docs/letter_channel.md`

---

## 16. Jaama Python programm

Jaam = sülearvuti, mis ühendab AtomS3 ja MG400.

- [ ] Loo jaama kood kausta `src/`
- [ ] Jaam saab AtomS3-st tähe
- [ ] Jaam loeb JSON-ist välja `letter`
- [ ] Jaam lisab vastuvõtmisele ajatempli
- [ ] Kontrolli, kas robot on ühendatud
- [ ] Kontrolli, kas robot on lubatud
- [ ] Kui robot ei ole valmis, ära liiguta robotit
- [ ] Näita kasutajale põhjust, miks robot ei liigu
- [ ] Leia saadud tähele vastav punktide nimekiri
- [ ] Teisenda punktid MG400 liikumiskäskudeks
- [ ] Saada esimene liikumiskäsk robotile

---

## 17. Tähtede trajektoorid

Valmista vähemalt kolm tähte.

- [ ] Täht 1: __________
- [ ] Täht 2: __________
- [ ] Täht 3: __________
- [ ] Defineeri iga täht punktide nimekirjana
- [ ] Määra, millal pliiats on üleval
- [ ] Määra, millal pliiats on all
- [ ] Määra pliiatsi kirjutamise Z
- [ ] Pane tähepunktid faili `docs/letters.md`
- [ ] Pane pliiatsi Z faili `docs/letters.md`
- [ ] Pane kavandatud tähe suurus faili `docs/letters.md`

---

## 18. Esimesed joonistamistestid

Iga uue tähe esimene test:

- [ ] Robot 20% kiirusel
- [ ] Hädastopp käeulatuses
- [ ] Pliiats vähemalt 20 mm paberist kõrgemal
- [ ] Robot teeb trajektoori õhus
- [ ] Kontrolli X-suunalist liikumist
- [ ] Kontrolli Y-suunalist liikumist
- [ ] Kontrolli joonte järjekorda
- [ ] Kontrolli pliiatsi üles/alla loogikat
- [ ] Alles pärast õhutesti vii pliiats paberile

---

## 19. Markeri/pastakahoidiku test

Enne 3D-prinditud hoidiku valmimist:

- [ ] Kinnita marker turvaliselt flantsi külge
- [ ] Leia sobiv kirjutamise Z
- [ ] Testi joonistamist

Kui 3D-printimise hoidik on valmis:

- [ ] Paigalda 3D-prinditud pastakahoidik
- [ ] Kontrolli kinnitust
- [ ] Leia uus kirjutamise Z
- [ ] Kontrolli hoidiku järeleandmist
- [ ] Testi trajektoor õhus
- [ ] Testi trajektoor paberil

---

## 20. Tähtede mõõtmine

Iga valmis tähe puhul:

- [ ] Joonista täht paberile
- [ ] Mõõda tähe laius joonlauaga
- [ ] Mõõda tähe kõrgus joonlauaga
- [ ] Võrdle kavandatud mõõtmetega
- [ ] Pane tulemused faili `docs/letters.md`

---

## 21. Latentsuse test

Tee kokku 30 nupuvajutust.

Iga testi puhul salvesta:

- [ ] Atom saatis tähe
- [ ] Jaam sai tähe
- [ ] Jaam saatis robotile esimese käsu

Testid:

- [ ] 1
- [ ] 2
- [ ] 3
- [ ] 4
- [ ] 5
- [ ] 6
- [ ] 7
- [ ] 8
- [ ] 9
- [ ] 10
- [ ] 11
- [ ] 12
- [ ] 13
- [ ] 14
- [ ] 15
- [ ] 16
- [ ] 17
- [ ] 18
- [ ] 19
- [ ] 20
- [ ] 21
- [ ] 22
- [ ] 23
- [ ] 24
- [ ] 25
- [ ] 26
- [ ] 27
- [ ] 28
- [ ] 29
- [ ] 30

- [ ] Salvesta tulemused faili `docs/latency.csv`
- [ ] Arvuta Atom → jaam keskmine latentsus
- [ ] Arvuta Atom → jaam maksimaalne latentsus
- [ ] Arvuta jaam → robot keskmine latentsus
- [ ] Arvuta jaam → robot maksimaalne latentsus

---

# DOKUMENTATSIOON

## 22. Draw.io skeem

- [ ] Tee skeem kogu süsteemist
- [ ] Lisa AtomS3
- [ ] Lisa AtomS3 WiFi
- [ ] Lisa sülearvuti / jaam
- [ ] Lisa kasutatav protokoll
- [ ] Lisa Ethernet-ühendus
- [ ] Lisa MG400
- [ ] Lisa pump
- [ ] Lisa pastakahoidik
- [ ] Lisa paber
- [ ] Salvesta muudetav draw.io fail
- [ ] Lisa skeemist pilt dokumentatsiooni
- [ ] Lisa link originaalsele draw.io failile

---

## 23. Vajalikud failid

Kontrolli, et repos on olemas:

- [ ] `README.md`
- [ ] `CHECKLIST.md`
- [ ] `AGENTS.md`
- [ ] `src/`
- [ ] `firmware/`
- [ ] `data/positions.json`
- [ ] `docs/bom.md`
- [ ] `docs/atom_page.md`
- [ ] `docs/letter_channel.md`
- [ ] `docs/letters.md`
- [ ] `docs/pick_test.csv`
- [ ] `docs/latency.csv`
- [ ] draw.io skeem
- [ ] skeemi pilt
- [ ] vajalikud fotod
- [ ] arenduspäevik

---

## 24. Arenduspäevik

Iga töösessiooni järel lisa uus sissekanne.

- [ ] Kuupäev
- [ ] Kes olid kohal
- [ ] Mida tegime
- [ ] Mis juhtus
- [ ] Mõõdetud numbrid ja ühikud
- [ ] Probleemid
- [ ] Otsused
- [ ] Otsuste põhjendused
- [ ] Mis jäi järgmiseks korraks

Mall:

```md
## PP.KK.AA — kohal: ...

### Tegime
-

### Juhtus
-

### Otsustasime, ja miks
-

### Lahti järgmiseks korraks
-
```

Vale või aegunud mõõtmist ei kustutata. Lisa hiljem uus tulemus koos kuupäeva ja selgitusega.

---

# OHUTUS

## 25. MG400 ohutus

Enne iga uut liikumisjada:

- [ ] Robot töötab 20% kiirusel
- [ ] Hädastopp on käeulatuses
- [ ] Kõigile öeldakse enne liikumist „liigub“
- [ ] Käed on roboti tööalast väljas
- [ ] Roboti 440 mm ulatuses ei ole inimest
- [ ] Robotit juhib ainult üks programm
- [ ] Esimene test tehakse ilma proovitükita
- [ ] Pliiats või iminapp on vähemalt 20 mm pinnast kõrgemal
- [ ] Alles pärast õnnestunud testi kasutatakse päris Z-kõrgust

Pumba juures:

- [ ] Robot on keelatud enne DO juhtmete ühendamist
- [ ] Pumbakast on vooluvõrgust väljas enne juhtmete ühendamist
- [ ] Arvesta, et pumbakast kasutab 24 V

AtomS3:

- [ ] Laborist välja viimisel muuda vaikimisi WiFi parool

---

# LÕPPDEMO

## 26. Robot

- [ ] `mg400 status` töötab
- [ ] `mg400 serve` töötab
- [ ] Veebileht liigutab robotit
- [ ] Imemine töötab käsurealt
- [ ] Puhumine töötab käsurealt
- [ ] Neli positsiooni on salvestatud
- [ ] 10 järjestikust pick-and-place testi on tehtud

---

## 27. AtomS3

- [ ] Firmware käivitub
- [ ] Atom teeb oma WiFi võrgu
- [ ] Telefon saab WiFi-ga ühenduda
- [ ] Captive portal avaneb automaatselt
- [ ] Pildi saab lehelt AtomS3-le saata
- [ ] Pilt ilmub ekraanile
- [ ] Seadete osa töötab
- [ ] Testinupp töötab

---

## 28. Täht

- [ ] Lühike AtomS3 nupuvajutus valib tähe
- [ ] Pikk nupuvajutus saadab tähe
- [ ] Jaam saab JSON-i kätte
- [ ] Jaam lisab ajatempli
- [ ] Jaam leiab õige tähe trajektoori
- [ ] MG400 joonistab esimese tähe
- [ ] MG400 joonistab teise tähe
- [ ] MG400 joonistab kolmanda tähe
- [ ] Tähed on mõõdetud
- [ ] 30 latentsuse testi on tehtud

---

# ENNE KAITSMIST

## 29. Repo kontroll

- [ ] Kõik vajalikud failid on GitHubis
- [ ] README on täidetud
- [ ] KAARDISTA ISE osad on täidetud
- [ ] Arenduspäevik on ajakohane
- [ ] Mõõtmistel on ühikud
- [ ] Failinimed dokumentatsioonis vastavad päris failidele
- [ ] Fotod on lisatud
- [ ] Draw.io skeem on lisatud
- [ ] Kood töötab värskelt kloonitud repost
- [ ] Vajalikud commit'id on tehtud
- [ ] Kõik muudatused on pushitud

---

## 30. Git tag

- [ ] Tee tag:

```bash
git tag smart-solutions-lab1
```

- [ ] Push tag:

```bash
git push origin smart-solutions-lab1
```

- [ ] Kontrolli GitHubist, et tag on olemas

---

# Kaitsmiseks valmis

- [ ] Git repo link olemas
- [ ] Tag `smart-solutions-lab1` olemas
- [ ] AtomS3 demo töötab
- [ ] MG400 demo töötab
- [ ] Pump töötab
- [ ] Telefon avab Atomi captive portali
- [ ] Pilt jõuab Atomi ekraanile
- [ ] Atomil valitud täht jõuab jaama
- [ ] MG400 joonistab tähe
- [ ] Vähemalt kolm tähte töötavad
- [ ] Arenduspäevik on näitamiseks valmis
- [ ] Oskame selgitada, kuidas Atom → jaam → MG400 ahel töötab
