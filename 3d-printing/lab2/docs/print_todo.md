# Labor 2 — prinditavate osade to-do

Tööjärjekord, milles iga prinditud osa valmib. Järjekord ei ole juhuslik: väikseim
print tuleb esimesena, sest ta kontrollib Gridfinity jalga **ja** kalibreerib roboti
enne, kui suured hoidikud filamentidele kulutavad.

Viited: [`layout.md`](layout.md) (paigutus ja ruudud), [`../MG 400 rakis.md`](../MG%20400%20rakis.md)
(jala mõõdud, koordinaadid, kalibreerimine §7), [`bom.md`](bom.md) (materjal).

> **Reegel iga printi kohta:** lähtefail + STL + `.3mf` repos, print tehtud, sobivus
> päris detailiga üle kontrollitud, pesa nominaal vs nihikuga mõõdetud ja kasutatud
> lõtk (Labor 1 number) kirjas.

**Staatus:** `[ ]` tegemata · `[-]` pooleli · `[x]` valmis

## Kokkuvõte

| # | Print | Ruut | Suurus | Sõltuvus | Staatus |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Kalibreerimishoidik (ristiga) | B-2 | 1 × 1 | — | [ ] |
| 2 | Klaasi sisendhoidik | D-5, E-5, D-4, E-4 | 2 × 2 | kalibreerimine | [ ] |
| 3 | Töökoha hoidik | B-2 | 1 × 1 | klaas + mannekeen | [ ] |
| 4 | AtomS3 sisendhoidik | B-4 | 1 × 1 | mõõdud | [ ] |
| 5 | Akumooduli sisendhoidik | B-5 | 1 × 1 | aku mõõdud | [ ] |
| 6 | Põhiväljundi hoidik | E+3, E+4 | 2 × 1 | — | [ ] |
| 7 | Praagi hoidik | F+5 | 1 × 1 | — | [ ] |
| 8 | Tööriista kaamera kinnitus | flantsi küljes | — | mooduli mõõdud | [ ] |
| 9 | Laua kohal oleva kaamera kinnitus | serv / G-nurk | — | käe max kõrgus | [ ] |

---

## 0. Kontroll enne edasi printimist

- [ ] Äsja prinditud Gridfinity kast istub ruutu ja **ei loksu**.
- [ ] Kui loksub: paranda jala lõtk enne suuri printe (iga hoidik pärineb sellest jalast).
- [ ] Kui prinditud kastil ei ole teravat keskpunkti/risti, prindi osa 1.

## 1. Kalibreerimishoidik — 1 × 1

- [ ] Modelleeri ristiga keskpunkt (või terav tipp).
- [ ] Prindi.
- [ ] Kontrolli, et jalg istub ruudustikku ega loksu.
- [ ] **Värav:** pane B-2 ruutu, vii tööriista tipp keskpunkti, kirjuta koordinaadid.
- [ ] Arvuta nihe = mõõdetud − arvutatud (§4 valem).
- [ ] Kontrolli kauget ruutu E+3; kui viga > 1 mm, on telgede suund valesti.
- [ ] Kalibreeri Z ruudustiku pinnalt.
- [ ] Dokumenteeri nihe `layout.md`-s.

> Ilma selle sammuta ei tohi suuri mitme ruudu hoidikuid printida — õpetatud punktid
> oleksid valed ja prindid läheksid raisku.

## 2. Klaasi sisendhoidik — 2 × 2

- [ ] Pesa 24 × 24 × 2 mm klaasile, lõtk + 45° kaldserv ülal.
- [ ] Vähemalt 4 ühikut.
- [ ] Prindi ja kontrolli sobivust päris klaasiga.
- [ ] Paranda lõtku/kaldserva ja prindi uuesti, kui vaja.
- [ ] Kirjuta nominaal vs mõõdetud ja kasutatud lõtk.

## 3. Töökoha hoidik — 1 × 1

- [ ] Atom/mannekeen istub ainult ühte moodi, ekraan ülespoole.
- [ ] Klaasil on tema peal kindel koht.
- [ ] Peab vastu roboti survele (paar njuutonit), ülalt vaba tee.
- [ ] USB-C ja nupp jäävad ligipääsetavaks; miski ei jää iminapa teele.
- [ ] Prindi ja kontrolli istumist päris mannekeeni + klaasiga.

## 4. AtomS3 sisendhoidik — 1 × 1

- [ ] Pesa AtomS3 mõõtude järgi, 45° kaldserv, määratud baas.
- [ ] Vähemalt 4 ühikut.
- [ ] Prindi ja kontrolli sobivust.

## 5. Akumooduli sisendhoidik — 1 × 1

- [ ] **Eeltingimus:** akumoodul nihikuga mõõdetud (mõõtu ülesandes ei anta).
- [ ] Pesa mõõtude järgi, 45° kaldserv.
- [ ] Vähemalt 4 ühikut.
- [ ] Prindi ja kontrolli sobivust.

## 6. Põhiväljundi hoidik — 2 × 1

- [ ] Vähemalt 4 detailile.
- [ ] Suuremad kaldservad kui sisendil (robot paneb ebatäpsemalt).
- [ ] Inimene saab detailid välja võtta (väljalõige servas või väljalükkeauk põhjas).
- [ ] Prindi ja kontrolli.

## 7. Praagi hoidik — 1 × 1

- [ ] Lihtne kast või renn, kuhu detail kukub.
- [ ] Prindi ja paiguta F+5.

## 8. Tööriista kaamera kinnitus

- [ ] Mõõda XIAO ESP32S3 Sense moodul ja olemasolev iminapa hoidik.
- [ ] Kinnitus olemasoleva hoidiku külge: moodul eemaldatav, ei ole PLA sisse ehitatud.
- [ ] Iminapp jääb vabaks, kaamera näeb töökohta, USB-C ligipääsetav.
- [ ] Prindi; kaalu tööriist enne ja pärast.
- [ ] Lahenda toide (vt `bom.md`) koos prinditud juhtmekinnituse ja tõmbetõkkega.

## 9. Laua kohal oleva kaamera kinnitus

- [ ] Mõõda käe suurim kõrgus ja ulatus.
- [ ] Leia kõrgus, millega kogu laud jääb kaadrisse.
- [ ] Jäikus kujust (lai jalg, ribid, kolmnurk); pikk post tükkidena.
- [ ] Ei ole roboti alusel ega liikumistee peal; tuleb alati samasse kohta tagasi.
- [ ] USB juhe mööda posti alla ja kinni.
- [ ] Prindi; testi täiskiirusel, mõõda pildi värisemine.

---

## Järeltegevused pärast printi

- [ ] Ülaltvaate foto kõigist hoidikutest ruudustikus (joonlaud kaadris).
- [ ] Iga prindi esimese korra probleem ja parandus kirjas.
- [ ] `README.md` ja arenduspäevik uuendatud (numbrid + ühikud).
