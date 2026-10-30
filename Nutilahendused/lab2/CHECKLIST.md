# Nutikad Lahendused — Labor 2: tööde nimekiri

Koostatud [`README.md`](README.md) põhjal. Üks linnuke iga konkreetse väljundi või testi kohta.

**Töömaht:** 28 tundi · **Hindamine:** 20 punkti · **Meeskond:** 3-4 tudengit
**Teine kaitsmine:** toimub **12.11.26** · **Materjalid õppejõule:** hiljemalt **10.11.26**, GitHubi lingina

Siin kehtivad reeglid (vt [`AGENTS.md`](../AGENTS.md)):

- Valmis ei tähenda "kood on olemas", vaid "töötab ja on läbi proovitud päris riistvaral".
- Numbrit ei mõelda välja. Teadmata väärtus jääb kujule `TODO: mõõta`.
- Vanad mõõtmised jäävad alles, uued lisatakse kuupäeva ja põhjendusega.

---

## Tähtajad ja esitamine (uuendatud 29.10.26)

Teine kaitsmine lükkub edasi ja toimub **12.11.26**.

- [ ] Saada materjalid õppejõule **hiljemalt 10.11.26**, GitHubi lingina.
- [ ] Repositoorium peab sisaldama **Fusion 360 tööfaile `.f3z` arhiivi formaadis** (mitte ainult `.f3d` ega `.stl`).
- [ ] Kontrolli enne 10.11, et link avaneks õigustega kontolt, mitte ainult sinu brauseris, ja et tag `smart-solutions-lab2` on pushitud.

---

## 0. Enne kõike muud (sisendid ja blokeerijad)

- [ ] Kogu kokku Labori 1 sisendid: jaam, MG400 baaspakett, [`data/positions.json`](../lab1/data/positions.json), Atomi püsivara ja leht, aadressiplaan.
- [ ] Küsi õppejõult droplet (üks meeskonna kohta, õppejõu konto pealt).
- [ ] Küsi Andmehõive L2 meeskonnaliikmelt rõhuanduri ja op-ampi kalibratsioonikonstandid (need lähevad Atomi lehele).
- [ ] Küsi 3D printimise L2 meeskonnaliikmelt: laua kaamera post (kaamera robotist kõrgemal), tööriista kaamera kinnitus iminapa tööriistahoidiku külge koos toitega, ja Gridfinity laud, kus iga hoidiku koha juures on ruudu nimi.
- [ ] Kontrolli riiulit: USB veebikaamera (UHD), USB pikenduskaabel, Seeed Studio XIAO ESP32S3 Sense kaameramoodul (113991115).
- [ ] Otsusta ja kirjuta üles kausta struktuur: README nõuab `smart-solutions/lab2/{server,src,firmware,docs}`, aga siin repos on praegu `Nutilahendused/lab2/`. Üks neist peab jääma kehtima.
- [ ] Jaga töö piirkondadeks (droplet / postkontor / kaamerad + Atomi leht / ohutus + dokumendid) ja kirjuta jaotus arenduspäevikusse.

---

## 1. Droplet (SSH, tulemüür, HTTPS)

### 1.1 Võtmed (üks arvuti kohta, tehtud selles arvutis)

- [ ] Igas arvutis, millega dropletisse minnakse: `ssh-keygen -t ed25519 -C "meeskond-N kelle-arvuti"`.
- [ ] Pane igale privaatvõtmele parool.
- [ ] Kontrolli, et avalik rida algab sõnaga `ssh-ed25519`, enne kui saadad.
- [ ] Kontrolli failinime lõppu `.pub` — kui saadad kogemata privaatse poole, on see võti läbi ja tuleb uus teha.
- [ ] Saada üks kiri aadressile kaspar.kallas@ut.ee: meeskonna number, kõigi arvutite avalikud read ja iga rea juures, kelle või mis arvuti see on.
- [ ] Kirjuta üles saatmise kuupäev ja mis täpselt saadeti (mitte privaatvõtmed).
- [ ] Hiljem lisanduv arvuti: saada tema avalik võti samamoodi kohe järele.

### 1.2 Esimene sisselogimine

- [ ] Võta õppejõult vastu dropleti aadress, link (nimi) ja kasutajanimi.
- [ ] Kontrolli, et link viitab dropleti aadressile (nimi ja aadress peavad kokku minema) — ise DNS-i seadistama ei pea.
- [ ] `ssh kasutajanimi@aadress` töötab **igast** arvutist, mille võtme saatsid.
- [ ] Kontrolli, et paroolisisselogimine on keelatud ja sisse saab ainult võtmega.

### 1.3 Turvaseadistus (kõik kolm enne kõike muud)

- [ ] Tulemüür püsti nii, et lahti on **ainult** need pordid, mida päriselt kasutad; jäta SSH port lahti *enne*, kui tulemüüri sisse lülitad.
- [ ] Iga lahtise pordi kohta kirjuta üles, mis teenus selle taga on.
- [ ] Uuendused peale.
- [ ] Kirjuta üles: dropleti aadress ja link, millised võtmed on sees ja mis kuupäeval lisatud, millised pordid on lahti ja mis igaühe taga on.

### 1.4 HTTPS

- [ ] Pöördproksi, mis võtab sertifikaadi ise ja uuendab seda ise (Caddy + Let's Encrypt).
- [ ] Leht avaneb õppejõult saadud lingi peal `https://`-iga ja ilma brauseri hoiatuseta.
- [ ] Kirjuta üles, miks ilma selleta ei saa (parool ja võti käiksid üle interneti loetavalt).

### 1.5 Korratavuse test

- [ ] Ehita kogu dropleti seadistus **üks kord meelega uuesti**, ainult oma märkmete järgi.
- [ ] Kirjuta üles, kaua uuesti ehitamine võttis ja mis märkmetest puudu oli.
- [ ] Kirjuta dropleti samm-sammult ehitus `docs/`-i (hindamistabelis nõutud).

**Märkmete fail:** `TODO: dropleti märkmete faili asukoht`

---

## 2. Postkontor (sõnum kasutajalt robotini)

### 2.1 Kõigepealt kokkulepe

- [ ] Leppige kokku sõnumi formaat (näide README-s: `{"job":"letter","arg":"K"}`, `{"device":"team-2-atom","robot":"ready","p":-52.3}`, `{"msg":17,...}`, `{"msg":17,"result":"done"}`).
- [ ] Kirjuta `docs/server_api.md`: iga aadress, kes seda kutsub, mis sisse läheb, mis välja tuleb, ja veavastused.
- [ ] Kinnita lubatud tööde nimekiri (vähemalt üks täht Laborist 1 ja üks teine töö; arvesta "näita pilti Atomi ekraanil" ja "tõsta proovitükk allikast valmis pessa").
- [ ] Kirjuta üles, mis juhtub sõnumiga, mida nimekirjas ei ole.
- [ ] Otsusta ja kirjuta üles, kui vana sõnum veel kehtib, ja mis aegunud sõnumiga juhtub.
- [ ] Otsusta ja kirjuta üles küsimisvahed, mida mõõdad (nt 1 s ja 10 s).
- [ ] Otsusta ja kirjuta üles, kui kaua on "liiga kaua" Atomi vaikimise kohta, ja mida kasutaja siis lehel näeb.

### 2.2 Serveripool (Flask dropletis, pöördproksi taga)

- [ ] Kasutaja leht: näitab, kas robot on kohal, mis eelmisest sõnumist sai, ja laseb uue sõnumi jätta.
- [ ] Kasutaja leht on parooli taga.
- [ ] Aadress: kasutaja jätab töö (nimekirja kontroll, sisendi suuruse ja tüübi kontroll).
- [ ] Aadress: Atom teatab oleku ja küsib sõnumeid (Atomi võtmega autenditud).
- [ ] Aadress: Atom teatab tulemuse (`done` / `refused` + `why`).
- [ ] Sõnumitele antakse ID-d ja need saadetakse vastuses tagasi, et tulemust saaks siduda.
- [ ] Nimekirjast väljas sõnum tagastab `refused` koos põhjusega; midagi ei liigu.
- [ ] Aegumine on jõustatud serveris ja ka Atomis/jaamas (kaks kaitset).
- [ ] Vaikiva Atomi tuvastus: server hoiab viimase külastuse aega ja leht ütleb seda ausalt.
- [ ] Avalike aadresside lihtne kuritarvitamise piiramine (päringute sagedus).
- [ ] Server ei ava kunagi ühendust labori võrgu poole (roboti poole ei helistata).
- [ ] Midagi väljast tulnut ei käivitata (ei `eval`, ei shelli, ei failiteid sisendist).

### 2.3 Atomi pool (püsivara)

- [ ] Atom liitub labori WiFi-ga Labori 1 lehe seadete järgi.
- [ ] Atom käib postil iga N sekundi tagant: saadab oleku ja küsib, kas sõnumeid on.
- [ ] Atom annab iga kord kaasa oma võtme (võti elab Atomi lehe seadetes, **mitte repos**).
- [ ] Atom kontrollib, et räägib õige serveriga (HTTPS / serveri identiteet).
- [ ] Sõnum läheb jaamale edasi sama kanalit mööda, mida mööda täht Laboris 1 läks.
- [ ] Jaam teeb töö algusest lõpuni; Atom viib tulemuse serverisse tagasi.
- [ ] Kui ühendus kaob keset tööd, ootab vastus Atomi sees ja läheb teele, kui ühendus tagasi tuleb.
- [ ] Server ei vasta: proovi uuesti pikema vahega ja näita ekraanil, et ühendust ei ole.
- [ ] Keelatud või aegunud töö: vastus `refused` koos põhjusega; robot ei liigu.

### 2.4 Jaama pool (Python)

- [ ] Võtab töö vastu Labori 1 kanali kaudu.
- [ ] Seob töö olemasoleva Labori 1 rutiiniga (tähe joonistamine ja teine töö).
- [ ] Teeb töö lõpuni ka siis, kui võrk kadus; pooleli ei katkestata.
- [ ] Saadab õnnestumise/ebaõnnestumise kanali kaudu tagasi.
- [ ] Robotile saadab korraga ainult üks programm (Labori 1 reegel).

### 2.5 Väline ja pahatahtlik testimine

- [ ] Telefonitest: **lülita WiFi välja**, ava leht mobiilse andmesidega, jäta sõnum, vaata, et töö tehakse ja vastus ilmub lehele.
- [ ] Ekraanipilt telefonist, kus on näha, et WiFi on väljas, `docs/`-i.
- [ ] Jäta sõnum, mida nimekirjas ei ole → midagi ei liigu, leht ütleb miks.
- [ ] Jäta korrektne sõnum, kui Atom on vooluta, oota üle aegumispiiri, lülita Atom sisse → seda ei täideta.
- [ ] Katkesta ühendus keset tööd (ruuteri WiFi välja või dropleti kaabel), kui robot juba joonistab; robot teeb töö lõpuni ja vastus jõuab kohale, kui ühendus taastub. Korda **3 korda**.
- [ ] Tõmba Atom vooluta ja kontrolli, et leht näitab ausalt viimast postilkäiku kokkulepitud aja jooksul.
- [ ] Proovi Atomi aadressi ilma võtme või vale võtmega → tagasi lükatud.

### 2.6 Latentsuse mõõtmine

- [ ] 30 sõnumit küsimisvahega **1 s**: aeg kasutaja vajutusest roboti esimese liigutuseni. Kirjuta üles iga mõõtmine.
- [ ] 30 sõnumit küsimisvahega **10 s**: sama mõõtmine.
- [ ] Arvuta mõlema vahe keskmine ja maksimum.
- [ ] Kirjuta üles postilkäike tunnis mõlema vahe korral.
- [ ] Vali üks vahe ja kirjuta põhjus README-sse.
- [ ] Pane kõrvale Labori 1 number (täht tuli otse Atomi nupult) — vahe on postkontori hind.
- [ ] Salvesta toorandmed CSV-na `docs/`-i (`TODO: failinimi`).

---

## 3. Kaamerad ja Atomi leht

### 3.1 Laua kaamera (USB UHD veebikaamera)

- [ ] Kinnita 3D-prinditud posti otsa, robotist kõrgemale, jaama külge USB pikenduskaabli kaudu.
- [ ] Kaadri kontroll: kogu laud — Gridfinity ruudustik servast servani — ja robot on pildil.
- [ ] Otsusta väiksem pilt, mille pealt ruudu nimi on veel loetav.

### 3.2 Tööriista kaamera (XIAO ESP32S3 Sense)

- [ ] Kinnita iminapa kõrvale tööriistahoidikule (koos toitega) 3D-prinditud kinnitusega.
- [ ] Vii ta Labori 1 aadressiplaani.
- [ ] Kaadri kontroll: otsik ja detail otse selle all.
- [ ] Ära jäta voogu lahti kõigile; pildi toob jaam.

### 3.3 Mõlemad pildid jaama lehel (ainult labori võrgus)

- [ ] Jaama leht näitab mõlemat voogu kõrvuti (MJPEG või muu `<img>`-iga töötav voog).
- [ ] Kirjuta üles, kuidas tööriista kaamera pilt jaamani jõuab.
- [ ] Kaamerapildid jäävad labori võrku — dropletisse neid selles laboris ei saadeta.
- [ ] Üks pilt kummastki kaamerast samal hetkel, `docs/`-i.

### 3.4 Mõõtmised kummagi kaamera kohta

Iga kaamera kohta: viide (sündmus → nähtav), kaadrid sekundis, ribalaius.

- [ ] Laua kaamera: viide, kaadrisagedus, ribalaius — `TODO: mõõta`
- [ ] Tööriista kaamera: viide, kaadrisagedus, ribalaius — `TODO: mõõta`
- [ ] Vaatamise lahutus ja mõõtmise täislahutus eraldi kirjas.
- [ ] Juhtimise latentsus ilma kaamerateta — `TODO: mõõta`
- [ ] Juhtimise latentsus ühe kaameraga — `TODO: mõõta`
- [ ] Juhtimise latentsus mõlema kaameraga — `TODO: mõõta`
- [ ] Kui juhtimise latentsus kasvas: vali väiksem pilt / vähem kaadreid / üks kaamera korraga / aeglasem juhtimine ja kirjuta põhjus välja.

### 3.5 Atomi lehe täiendused (sama leht, uut lehte ei tehta)

- [ ] Rõhuanduri kalibratsioonikonstandid Andmehõive L2-st, lehe seadetes muudetavad.
- [ ] Testinupp, mis näitab korraga toorest ADC lugemit, pinget ja kPa.
- [ ] Serveri aadressi väli.
- [ ] Atomi võtme väli (seadetes, mitte repos).
- [ ] Küsimisvahe väli.
- [ ] Testinupp, mis teeb ühe päris kõne ja näitab, mida server vastas.
- [ ] Uuenda `docs/atom_page.md`: kõigi seadete ja testinuppude nimekiri.

---

## 4. Ohutuskokkulepe

- [ ] Kirjuta meeskonna kokkulepe (`TODO: faili nimi docs/`-is) **enne**, kui postkontor esimest korda robotit liigutab.
- [ ] Selles: kes tohib sõnumeid jätta ja mida ta peab enne seda tegema.
- [ ] Selles: robot võtab sõnumeid vastu ainult siis, kui ruumis on inimene, kes ulatub hädastopini ja kes on roboti lubanud.
- [ ] Selles: kui ruumis ei ole kedagi, on robot välja lülitatud, mitte ainult keelatud.
- [ ] Selles: lubamist postkontori kaudu ei tehta.
- [ ] Tööd ainult nimekirjast; koordinaate, kiirust ega pumba otsejuhtimist postkontori kaudu ei saadeta.
- [ ] Iga nimekirjas olev töö on enne laboris kohapeal läbi proovitud 20 % kiirusel.
- [ ] Aegunud sõnum ei liiguta kunagi robotit.
- [ ] Avalik server on avalik: parool, HTTPS, lahti ainult vajalikud pordid.
- [ ] Server ei helista robotile; ainus suund on Atomi enda tulek.
- [ ] Võõras sisend on vaenulik: pildil suuruse ülempiir ja pildifaili tüüp, tähel üks täht, midagi sisselaekunud ei käivitata.
- [ ] Atomi võti ei ole repos — kui ta sinna sattus, tee uus.
- [ ] Privaatne SSH võti ei lahku sülearvutist (ei meili, ei vestlusse, ei reposse); õppejõule läheb ainult `.pub`.
- [ ] Kaamerapildid jäävad labori võrku.
- [ ] Labori 1 MG400 reeglid korratud: käed ei ole laual, kui robot on sisse lülitatud; uue jada esimene jooks 20 % kiirusel; korraga ainult üks programm saadab käsklusi.
- [ ] Kui Atom laborist välja läheb, vaheta WiFi parool vaikimisi omast ära.
- [ ] Kõik meeskonnaliikmed on kokkuleppe läbi lugenud; kirjuta üles, kes ja millal.

---

## 5. Tellimus (`docs/bom.md`)

- [ ] Droplet ja link tulevad õppejõult — neid tellimusse ei panda.
- [ ] Lisa iga laua juures puuduv osa, üks rida iga osa kohta.
- [ ] Iga rea juurde üks lause, milline osa seda küsib.
- [ ] Kontrolli enne tellimist praktilised küsimused:
  - [ ] Kas veebikaamera kaadri laius on posti kõrguselt piisav?
  - [ ] Kas USB kaabel ulatub posti otsast jaamani?
  - [ ] Kas kaameramoodul on olemas ja kas labori WiFi ulatub temani ja Atomini laua peal ja käe otsas?
- [ ] Kanna read ühisesse tellimistabelisse Moodles **enne 16.10.26** (mida tabelis ei ole, seda ei tellita).
- [ ] Commiti `docs/bom.md` põhjendusena.

---

## 6. Dokumentatsioon ja repo väljundid

- [ ] `README.md`: täida kõik `KAARDISTA ISE` kohad — numbrid, ühikud, kus fail asub, ja tegemata asja kohta üks rida, miks.
- [ ] `README.md`: skeemid ja simulatsioonid pildina **pluss link elavale failile**, et teine saaks edasi muuta.
- [ ] `docs/server_api.md` valmis ja vastab jooksvale koodile.
- [ ] `docs/atom_page.md` valmis ja vastab jooksvale püsivarale.
- [ ] Ohutuskokkulepe commititud.
- [ ] Dropleti ehitus samm-sammult commititud.
- [ ] Süsteemi skeem draw.io-s: `.drawio` + `.png`, README-st lingitud.
- [ ] Fusion 360 tööfailid `.f3z` arhiivina repos (kaamerate kinnitused ja muu selle labori jaoks tehtud CAD) — vaata, mis on juba olemas, nt [`MG 400 rakis.f3z`](../../3d-printing/lab2/models/MG%20400%20rakis.f3z), ja lisa ülejäänud samasse vormingusse.
- [ ] Latentsuse CSV(d) `docs/`-is.
- [ ] Ekraanipildid ja fotod (telefon WiFi väljas, mõlemad kaamerapildid, lehe olekud) `docs/`-is.
- [ ] `docs/bom.md` commititud.
- [ ] Repo struktuur vastab kokkulepitud paigutusele (`server/`, `src/`, `firmware/`, `docs/`, `README.md`, `AGENTS.md`).
- [ ] `AGENTS.md` uuendatud Labori 2 kohta (uus arhitektuur, uued liidesed, uued reeglid).
- [ ] Arenduspäevik: üks sissekanne iga töösessiooni kohta, lisatakse mitte ei muudeta, formaat "kes olid kohal / tegime / juhtus (numbrid) / otsustasime ja miks / lahti järgmiseks korraks".
- [ ] Tag `smart-solutions-lab2` loodud ja pushitud.
- [ ] Täidetud "mida sa päriselt kasutasid" nimekiri (README `KAARDISTA ISE` koht).

---

## 7. Kaitsmise proov

- [ ] Ava leht telefonist mobiilse andmesidega (WiFi väljas), jäta sõnum; robot joonistab tähe ja vastus ilmub lehele.
- [ ] Jäta sõnum, mida nimekirjas ei ole, ja näita, mis sellest sai.
- [ ] Tõmba Atom vooluta ja näita, mida leht siis ütleb (ja mitme sekundi pärast).
- [ ] Näita jaama lehel mõlemat kaamerat: kogu laud ja otsik.
- [ ] Ava arenduspäevik ja oska iga sissekannet seletada.
- [ ] Valmis vastama umbes viiele küsimusele, kuidas sa selle tegid (droplet, API, aegumine, võti, kaamerapildi teekond).
- [ ] Tee enne kaitsmist üks täisproov algusest lõpuni ja kirjuta tulemus üles.
- [ ] Teine kaitsmine: **12.11.26**; materjalid saadetud hiljemalt **10.11.26** GitHubi lingina, repos `.f3z` tööfailid olemas.

---

## 8. Enesekontroll hindamistabeli järgi

| Kategooria | Punktid | Tehtud |
| :--- | :--- | :--- |
| Tööfailid — dropleti seadistus kirjas ja korratav, serveri kood, Atomi püsivara postilkäimisega, jaama kood, kahe kaamera vood, Atomi lehe uued osad | 5 p | [ ] |
| Analüüs — latentsus sõnumist liigutuseni kahe küsimisvahega ja Labori 1 number kõrval, kummagi kaamera viide/kaadrisagedus/ribalaius, juhtimise latentsus kaameratega ja ilma | 5 p | [ ] |
| Prototüüp — leht avaneb telefonist mobiilse andmesidega HTTPS-i peal, sõnum paneb roboti tööd tegema ja vastus tuleb tagasi, aegunud ja lubamata sõnum ei liiguta midagi, leht näitab ausalt, kui Atom on vait, üks kaamera näitab kogu lauda ja teine otsikut | 5 p | [ ] |
| Dokumentatsioon — README, arenduspäevik, `server_api.md`, `atom_page.md`, ohutuskokkulepe, `bom.md`, `AGENTS.md` | 5 p | [ ] |

---

## 9. Lahtised küsimused õppejõu ja meeskonnaga

- [ ] Kumb repo paigutus jääb kehtima: `Nutilahendused/lab2/` või README nõutud `smart-solutions/lab2/`?
- [ ] Kas lubatud tööde nimekirja tohib pärast esimest kaitsmist veel muuta?
- [ ] Kelle käes on kasutaja lehe parool ja kuidas seda meeskonnas jagatakse?
- [ ] Kus hoiab Atom oma võtit püsivara flash'imise ajal, et see kunagi git'i ei jõuaks?
- [ ] Millised Fusion 360 failid peavad `.f3z`-ina repos olema: ainult selle labori kaamerakinnitused, või ka Labori 1 ja 3D printimise L2 mudelid?
- [ ] Kas `.f3z` arhiivid lähevad repo juurde, `models/`-i või `3d-printing/lab2/models/`-i?
