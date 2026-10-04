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

**Gridfinity põhimõõdud (kõigile hoidikutele):** samm 42 mm; välismõõt = `42 · n − 0,5 mm`
(1 × 1 = 41,5 mm, 2 × 1 = 83,5 × 41,5 mm, 2 × 2 = 83,5 × 83,5 mm); nurga raadius 3,75 mm;
jalg 4,75 mm (profiil 0,8 / 1,8 / 2,15 mm); pesa lõtk 1–2 mm külje kohta + 45° kaldserv.
Üks prinditud tükk ≤ 250 × 250 mm.

## Kokkuvõte

| # | Print | Ruut | Suurus | Välismõõt (mm) | Sõltuvus | Staatus |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Kalibreerimishoidik (ristiga) | B-2 | 1 × 1 | 41,5 × 41,5 | — | [ ] |
| 2 | Klaasi sisendhoidik | A-3, B-3, A-4, B-4 | 2 × 2 | 83,5 × 83,5 | kalibreerimine | [ ] |
| 3 | Töökoha hoidik | B-2 | 1 × 1 | 41,5 × 41,5 | klaas + mannekeen | [ ] |
| 4 | AtomS3 sisendhoidik | C-3, D-3, C-4, D-4 | 2 × 2 | 83,5 × 83,5 | mõõdud | [ ] |
| 5 | Akumooduli sisendhoidik | E-3, F-3, E-4, F-4 | 2 × 2 | 83,5 × 83,5 | aku mõõdud | [ ] |
| 6 | Põhiväljundi hoidik | E+3, E+4 | 2 × 1 | 83,5 × 41,5 | — | [ ] |
| 7 | Praagi hoidik | F+5 | 1 × 1 | 41,5 × 41,5 | — | [ ] |
| 8 | Tööriista kaamera kinnitus | flantsi küljes | — | mõõta | mooduli mõõdud | [ ] |
| 9 | Laua kohal oleva kaamera kinnitus | serv / G-nurk | — | ≤ 250 pikkus | käe max kõrgus | [ ] |

---

## 0. Kontroll enne edasi printimist

- [ ] Äsja prinditud Gridfinity kast istub ruutu ja **ei loksu**.
- [ ] Kui loksub: paranda jala lõtk enne suuri printe (iga hoidik pärineb sellest jalast).
- [ ] Kui prinditud kastil ei ole teravat keskpunkti/risti, prindi osa 1.

## 1. Kalibreerimishoidik — 1 × 1

> **Sees ei hoia miski.** Kalibreerimishoidik ei ole sisendhoidik: temasse ei panda
> AtomS3-t, klaasi ega akut. Ta on tühi 1 × 1 viitepesa, mille ainus tähtis osa on
> pealispinnal olev terav keskpunkt/rist. Kaks tööd: (1) näitab, kas Gridfinity jalg
> istub päris ruudustikku ega loksu; (2) annab täpse puutepunkti roboti kalibreerimiseks.

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

- [ ] Välismõõt 83,5 × 83,5 mm (2 × 2 ruut), nurga raadius 3,75 mm, jalg 4,75 mm.
- [ ] 4 pesa, iga pesa 26–28 mm (24 + 2 × 1–2 mm lõtk), madal soon sügavusega 3–4 mm (klaas on 2 mm), 45° kaldserv ülal.
- [ ] Vähemalt 4 ühikut (4 klaasi).
- [ ] Inimene saab ligi: väljalõige servas või väljalükkeauk põhjas (2 mm klaas siledas pesas ei tule sõrmedega välja).
- [ ] Prindi ja kontrolli sobivust päris klaasiga.
- [ ] Paranda lõtku/kaldserva ja prindi uuesti, kui vaja.
- [ ] Kirjuta nominaal vs mõõdetud ja kasutatud lõtk.

## 3. Töökoha hoidik — 1 × 1

- [ ] Välismõõt 41,5 × 41,5 mm (1 × 1 ruut), nurga raadius 3,75 mm, jalg 4,75 mm.
- [ ] Atomi pesa 26 × 26 mm, 45° kaldserv, sügavus ≥ 13 mm (ekraan üles).
- [ ] Atom/mannekeen istub ainult ühte moodi, ekraan ülespoole.
- [ ] Klaasil on tema peal kindel koht.
- [ ] Peab vastu roboti survele (paar njuutonit), ülalt vaba tee.
- [ ] USB-C ja nupp jäävad ligipääsetavaks; miski ei jää iminapa teele.
- [ ] Prindi ja kontrolli istumist päris mannekeeni + klaasiga.

## 4. AtomS3 sisendhoidik — 2 × 2

- [ ] Välismõõt 83,5 × 83,5 mm (2 × 2 ruutu), nurga raadius 3,75 mm, jalg 4,75 mm.
- [ ] 4 pesa, iga pesa 26 × 26 mm (24 × 24 + 1 mm lõtk külje kohta), 45° kaldserv ülal, sügavus ≥ 13 mm (ekraan üles).
- [ ] Vähemalt 4 ühikut (4 AtomS3 pesa).
- [ ] Prindi ja kontrolli sobivust.

## 5. Akumooduli sisendhoidik — 2 × 2 (suurus selgub mõõtmisel)

- [ ] **Eeltingimus:** akumoodul nihikuga mõõdetud (mõõtu ülesandes ei anta).
- [ ] Välismõõt 83,5 × 83,5 mm (2 × 2), nurk 3,75 mm, jalg 4,75 mm — 4 pesa mahub; kui moodul on väike, võib piisata 1 × 2 või 2 × 1.
- [ ] 4 pesa, iga pesa = mooduli mõõt + 2 × 1–2 mm lõtk, sügavus ≥ mooduli kõrgus, 45° kaldserv ülal.
- [ ] Vähemalt 4 ühikut.
- [ ] Prindi ja kontrolli sobivust.

## 6. Põhiväljundi hoidik — 2 × 1

- [ ] Välismõõt 83,5 × 41,5 mm (2 × 1 ruut), nurk 3,75 mm, jalg 4,75 mm.
- [ ] 4 pesa valmis sildile (Atom + klaas), iga pesa ≈ 26–28 mm.
- [ ] Suuremad kaldservad kui sisendil: 2–3 mm, 45° (robot paneb ebatäpsemalt).
- [ ] Inimene saab detailid välja võtta (väljalõige servas või väljalükkeauk põhjas).
- [ ] Prindi ja kontrolli.

## 7. Praagi hoidik — 1 × 1

- [ ] Välismõõt 41,5 × 41,5 mm (1 × 1), nurk 3,75 mm, jalg 4,75 mm; kui praak on suurem, võta 2 × 1 (83,5 × 41,5 mm).
- [ ] Lihtne lahtine kast või renn, kuhu detail kukub (kaldservad või funnel).
- [ ] Prindi ja paiguta F+5.

## 8. Tööriista kaamera kinnitus

- [ ] Mõõda XIAO ESP32S3 Sense moodul (plaat + kaameralaiend + objektiiv + USB-C + antenn) ja olemasolev iminapa hoidik. XIAO vormitegur on nominaalselt ~21 × 17,5 mm, aga Sense laiendiga mõõda tegelik.
- [ ] Kinnitus olemasoleva hoidiku külge: moodul eemaldatav, ei ole PLA sisse ehitatud.
- [ ] Iminapp jääb vabaks (kaamera ja kinnitus ei ulatu napa otsast allapoole), kaamera näeb töökohta, USB-C ligipääsetav.
- [ ] Kaamera on iga kord samas kohas (kuju, mitte hõõrdumine).
- [ ] Prindi; kaalu tööriist enne ja pärast (piir 500 g koos tööriista ja detailiga).
- [ ] Lahenda toide (vt `bom.md`) koos prinditud juhtmekinnituse ja tõmbetõkkega.

## 9. Laua kohal oleva kaamera kinnitus

- [ ] Mõõda käe suurim kõrgus ja ulatus (kaamera ja kandur jäävad sellest välja).
- [ ] Leia kõrgus, millega kogu laud (ruudustik 294 × 420 mm + robot) jääb kaadrisse.
- [ ] Posti jäikus kujust (lai jalg, ribid, kolmnurk). Üks prinditud tükk ≤ 250 × 250 mm, seega pikem post tükkidena — ühendus ei tohi olla nõrgim koht.
- [ ] Ei ole roboti alusel ega liikumistee peal (nt nurgaruudud G-5/G+5 või laua serv); tuleb alati samasse kohta tagasi.
- [ ] USB juhe mööda posti alla ja kinni (ei ripu üle laua).
- [ ] Prindi; testi täiskiirusel, mõõda pildi värisemine (pikslites või mm laual).

---

## Järeltegevused pärast printi

- [ ] Ülaltvaate foto kõigist hoidikutest ruudustikus (joonlaud kaadris).
- [ ] Iga prindi esimese korra probleem ja parandus kirjas.
- [ ] `README.md` ja arenduspäevik uuendatud (numbrid + ühikud).
