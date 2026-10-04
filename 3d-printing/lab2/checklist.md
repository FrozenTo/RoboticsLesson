# 3D printimine ja CAD — Labor 2 checklist

## 1. Projekti algus ja repo

- [O] Repo on olemas ja Labor 1 struktuur säilib.
- [O] Loo kaust `3d-print/lab2/`.
- [O] Lisa/uuenda `README.md`.
- [O] Kontrolli, et `AGENTS.md` on repo juurkaustas.
- [O] Loo `docs/` kaust.
- [O] Pane paika arenduspäeviku formaat.
- [O] Lisa projekti lähtefailid.

## 2. Detailide mõõtmine

Mõõda nihikuga:

- [O] AtomS3
- [O] Polükarbonaatklaas — 24 × 24 × 2 mm
- [ ] Akumoodul

Fusionis:

- [ ] Lisa mõõdud parameetritena.
- [ ] Dokumenteeri tegelikud mõõdud.
- [ ] Märgi üles ühikud.
- [ ] Lisa mõõtmistulemused `docs/layout.md`-i.

## 3. Protsess ja paigutus

- [ ] Kirjelda sisendid: AtomS3, klaas, akumoodul.
- [ ] Määra, mitu ühikut igast sisendist hoidikusse läheb.
- [ ] Määra töökohtade arv.
- [ ] Määra väljundid: põhiväljund ja praak.
- [ ] Otsusta, kuhu iga hoidik Gridfinity ruudustikus läheb.
- [ ] Kontrolli roboti ulatust.
- [ ] Kontrolli, et hoidikud ei blokeeriks roboti liikumist.
- [ ] Jäta ruumi järgmiste laborite moodulitele.
- [ ] Tee ülaltvaate joonis.
- [ ] Lisa kõik `docs/layout.md` faili.

### Paigutuse piirangud

- [ ] Töökoht on võimalikult täpses piirkonnas (A–C, −3…+3).
- [ ] Sisendid/väljundid võivad olla kaugemal.
- [ ] Väldi G-5, G-4, G-3, G+3, G+4, G+5 alasid.

## 4. Kalibreerimishoidik

- [ ] Modelleeri 1 × 1 Gridfinity kalibreerimishoidik.
- [ ] Prindi see.
- [ ] Kontrolli, et jalg istub ruudustikku.
- [ ] Kontrolli, et hoidik ei loksu.
- [ ] Paiguta hoidik ruutu **B-2**.
- [ ] Mõõda roboti keskpunkti koordinaadid.
- [ ] Arvuta nihe: `nihe = mõõdetud − arvutatud`.
- [ ] Kontrolli kauget ruutu, nt **E+3**.
- [ ] Kui viga > 1 mm, kontrolli telgede suunda.
- [ ] Kalibreeri Z ruudustiku pinnalt.
- [ ] Dokumenteeri nihe.

## 5. Sisendhoidikud

Tee kolm hoidikut:

- [ ] AtomS3 hoidik
- [ ] Klaasi hoidik
- [ ] Akumooduli hoidik

Iga hoidiku puhul:

- [ ] Vähemalt 4 ühikut.
- [ ] Gridfinity jalg.
- [ ] Detaili pesa olemas.
- [ ] Õige lõtk Labor 1 tulemuste põhjal.
- [ ] 45° sissejuhtiv kaldserv.
- [ ] Detailil on kindel baas/asukoht.
- [ ] Inimene saab detaili kätte.
- [ ] Üle detaili ei ulatu midagi.
- [ ] Hoidik ei loksu ruudus.
- [ ] Vajadusel magnetid.
- [ ] Testi päris detailiga.

## 6. Töökoha hoidik

- [ ] Atom saab hoidikusse ainult ühes asendis.
- [ ] Atom on ekraan ülespoole.
- [ ] Klaasil on kindel asukoht Atomi peal.
- [ ] Detail toetub stabiilselt.
- [ ] Hoidik peab vastu roboti survele.
- [ ] Tööriistal on ülalt vaba ligipääs.
- [ ] USB-C ja nupp jäävad ligipääsetavaks.
- [ ] Inimene saab vajadusel detailile ligi.
- [ ] Ükski osa ei jää iminapa teele.

## 7. Väljundhoidikud

- [ ] Põhiväljundi hoidik vähemalt **4 detailile**.
- [ ] Praagi jaoks eraldi koht.
- [ ] Põhiväljundil on piisavalt suured kaldservad.
- [ ] Praagi võib lahendada kasti/rennina.
- [ ] Inimene saab valmis detailid välja võtta.
- [ ] Hoidikud on robotile ligipääsetavad.

## 8. Printimine ja dokumentatsioon

Iga prinditava detaili kohta:

- [ ] Lähtefail repo's.
- [ ] STL olemas.
- [ ] `.3mf` olemas.
- [ ] Print tehtud.
- [ ] Print üle kontrollitud.
- [ ] Vajadusel disain parandatud ja uuesti prinditud.

Dokumentatsiooni:

- [ ] Esimese prindi probleem kirjas.
- [ ] Parandus kirjas.
- [ ] Pesa nominaalmõõt kirjas.
- [ ] Tegelik mõõt nihikuga kirjas.
- [ ] Kasutatud lõtk kirjas.
- [ ] Labor 1 lõtku number ja põhjendus kirjas.
- [ ] Foto hoidikutest Gridfinity ruudustikus.

## 9. Klaasi läbijooksu test

- [ ] Lae sisendhoidikusse 4 klaasi.
- [ ] Pane Atomi mannekeen töökohale.
- [ ] Õpeta roboti punktid.
- [ ] Robot võtab klaasi sisendist.
- [ ] Robot asetab klaasi Atomi peale.
- [ ] Robot võtab klaasi uuesti.
- [ ] Robot viib klaasi väljundisse.
- [ ] Tee 4 klaasi järjest.
- [ ] Inimene ei sekku jooksu ajal.

## 10. Hoidikute välja–tagasi test

- [ ] Võta kõik hoidikud ruudustikust välja.
- [ ] Pane kõik hoidikud tagasi.
- [ ] Lae klaasid uuesti.
- [ ] Ära muuda õpetatud punkte.
- [ ] Tee sama protsess uuesti.
- [ ] Kokku **5 ringi × 4 klaasi = 20 klaasi**.
- [ ] Dokumenteeri iga katse `docs/refit_test.csv`-s.
- [ ] Märgi iga klaasi kohta, kas:
  - [ ] võttis sisendist
  - [ ] pani töökohale
  - [ ] võttis töökohalt
  - [ ] pani väljundisse
  - [ ] õnnestus / ebaõnnestus + märkus
- [ ] Märgi ebaõnnestumised ja nende põhjus.
- [ ] Mõõda võimalusel detaili nihe.
- [ ] Kontrolli, kas hoidik töötab ka teises ruudus +42 mm sammuga.
- [ ] Pane kirja korduvtäpsuse tulemus.

## 11. Tööriista kaamera

Kasutada:

- [ ] Seeed Studio XIAO ESP32S3 Sense.

Enne disaini:

- [ ] Mõõda kaameramoodul.
- [ ] Mõõda olemasolev iminapa tööriistahoidik.
- [ ] Kontrolli, kust saab hoidiku külge kinnituda.

Kinnitus:

- [ ] Kinnitub olemasoleva iminapa hoidiku külge.
- [ ] Iminapp jääb vabaks.
- [ ] Kaamera näeb kogu töökohta.
- [ ] Kaamera asend kordub iga paigaldamisega.
- [ ] USB-C jääb ligipääsetavaks.
- [ ] Kaamera saab eemaldada ilma midagi lõhkumata.
- [ ] Kaamera ei ole PLA sisse kinni ehitatud.
- [ ] Mõõda tööriista kaal enne.
- [ ] Mõõda tööriista kaal pärast.

## 12. Kaamera toide

Vali üks lahendus:

- [ ] USB-C juhe mööda robotkätt
- [ ] Aku kaamera juures
- [ ] Roboti tööriistapordi toide

Enne roboti enda toite kasutamist:

- [ ] Mõõda pinge.
- [ ] Kontrolli kaamera lubatud pinget.
- [ ] Õppejõud vaatab ühenduse üle.

Valitud lahendusega:

- [ ] Käsi liigub sisend → töökoht → väljund.
- [ ] J4 läbib oma liikumisvahemiku.
- [ ] Juhe ei jää kinni.
- [ ] Juhe ei tõmba pistikut välja.
- [ ] Juhtme kinnitus on osa prindist.
- [ ] Tõmbetõke on olemas.
- [ ] Tee foto tööriistast.
- [ ] Tee foto kaamera vaatest töökohale.
- [ ] Dokumenteeri, miks selle toite valisid.

## 13. Laua kohal olev veebikaamera

- [ ] Mõõda roboti maksimaalne kõrgus.
- [ ] Mõõda kõige kaugem ulatus.
- [ ] Leia kaamera kõrgus, millega kogu laud jääb kaadrisse.
- [ ] Kontrolli kaamerat reaalselt laua kohal.
- [ ] Mõõda kaamera kinnituse/statiivikeere.
- [ ] Disaini kinnitus.
- [ ] Kinnitus ei asu roboti alusel.
- [ ] Kinnitus ei jää roboti liikumisteele.
- [ ] Kinnitus on piisavalt jäik.
- [ ] Vajadusel kasuta ribisid/kolmnurki/laiemat jalga.
- [ ] Kui post on liiga pikk, jaga see mitmeks prinditavaks osaks.
- [ ] Ühendused on jäigad.
- [ ] Kaamera saab alati samasse kohta tagasi.
- [ ] USB juhe on posti küljes.
- [ ] Juhe ei ripu üle laua.
- [ ] Testi roboti täiskiirusel.
- [ ] Mõõda pildi värisemist.
- [ ] Kontrolli, et pärast eemaldamist/tagasipanekut pilt säilib.
- [ ] Tee foto, kus kogu ruudustik + robot on näha.

## 14. Tellimus 16.10

Koosta `docs/bom.md`.

- [ ] PLA kogus on piisav.
- [ ] Atomi mannekeen on olemas.
- [ ] Akumooduleid on piisavalt testimiseks.
- [ ] 6 × 2 mm magnetid — kui vaja.
- [ ] Kaamera valitud toitelahenduse komponendid.
- [ ] Vajalik USB-C juhe/pikendus.
- [ ] Vajalik aku või pingemuundur.
- [ ] Veebikaamera USB-kaabel ulatub jaamani.
- [ ] Klaase on vähemalt 4 + varu.
- [ ] Iga BOM rea juures on üks lause, miks seda vaja on.

## 15. Dokumentatsioon

`3d-print/lab2/` sees:

- [ ] `README.md`
- [ ] `docs/layout.md`
- [ ] `docs/refit_test.csv`
- [ ] `docs/bom.md`
- [ ] Fotod
- [ ] Kõigi printide lähtefailid
- [ ] Kõigi printide STL-id
- [ ] Kõigi printide `.3mf` failid
- [ ] `AGENTS.md` uuendatud
- [ ] Arenduspäevik täidetud

## 16. Arenduspäevik

Iga töösessiooni kohta uus sissekanne:

- [ ] Kuupäev
- [ ] Kes kohal olid
- [ ] Mida tegime
- [ ] Mis juhtus — **numbritega**
- [ ] Mida otsustasime
- [ ] Miks otsustasime nii
- [ ] Mis jäi järgmiseks korraks

> Olemasolevaid sissekandeid ei muudeta — lisatakse uued.

## 17. Ohutuskontroll enne testimist

- [ ] Roboti alus on täiesti vaba.
- [ ] Ükski hoidik ei ulatu roboti alusele.
- [ ] Kõik hoidikud istuvad korralikult põhjas.
- [ ] Hoidikuid tõstetakse ainult siis, kui robot on keelatud.
- [ ] Esimene jooks aeglaselt.
- [ ] Hädastopp on käeulatuses.
- [ ] Uue hoidiku esimene tõstmine 20% kiirusel.
- [ ] Iminapp on esimesel tõstmisel vähemalt 20 mm kõrgusel.
- [ ] Printeri detailid võetakse välja ainult jahtunud aluselt.
- [ ] Kaamerapost ei ole roboti trajektooril.
- [ ] Kaamera juhe on kinnitatud ja tõmbekaitsega.
- [ ] Roboti tööriistapordi pinget on mõõdetud enne ühendamist.
- [ ] Küljelõikuritega töötades lõigatakse näost eemale.

# 🏁 Lõplik enne kaitsmist

- [ ] 3 detaili mõõdetud ja Fusioni parameetrites.
- [ ] Protsess + paigutus valmis.
- [ ] Kalibreerimishoidik töötab.
- [ ] Kõik 3 sisendhoidikut valmis.
- [ ] Töökoha hoidik valmis.
- [ ] Põhiväljundi hoidik 4 detailile valmis.
- [ ] Praagi hoidik valmis.
- [ ] 20 klaasi test tehtud.
- [ ] `refit_test.csv` täidetud.
- [ ] Hoidikud pärast eemaldamist tagasi pannes töötavad.
- [ ] Tööriista kaamera kinnitus valmis.
- [ ] Tööriista kaamera saab toidet.
- [ ] Kaamera + juhe läbivad roboti liikumise testi.
- [ ] Laua kohal olev veebikaamera näeb kogu lauda.
- [ ] Mõlemad kaamerad on kindlalt paigas.
- [ ] `layout.md` valmis.
- [ ] `bom.md` valmis.
- [ ] `README.md` valmis.
- [ ] Arenduspäevik valmis.
- [ ] Fotod lisatud.
- [ ] STL + 3MF failid olemas.
- [ ] `AGENTS.md` uuendatud.
- [ ] Git repo korras.
- [ ] Tag **`3d-print-lab2`** tehtud.
- [ ] Kaitsmisel saab hoidikud välja võtta ja tagasi panna.
- [ ] Robot suudab ilma punkte uuesti õpetamata 4 klaasi läbi protsessi viia.
- [ ] Tööriista kaamera töötab.
- [ ] Veebikaamera näeb kogu lauda.

## 📅 Tähtajad

- **Välja antud:** 06.10.26
- **Tellimuse tähtaeg:** 16.10.26
- **Esimene kaitsmine:** 27.10.26
- **Kaitsmine:** 15 minutit, suuline
- **Git tag:** `3d-print-lab2`
