# Andmehõive: Labor 3 — Tilk ja IRQ

**Töömaht:** 30 tundi · **Hindamine:** 20 punkti · **Meeskond:** 3 tudengit  
**Ülesanne väljastatud:** 28.10.2026 · **Tellimistähtaeg:** 06.11.2026 · **Esimene kaitsmine:** 19.11.2026 veebis

> **Staatus 14.11.2026:** labori ettevalmistus. Käesolevas kaustas ei ole veel uusi füüsilisi mõõtmisi ega kinnitatud klapi, LED-i, komparaatori või IRQ katseid. **Algne õppejõu dokument on täielikult säilitatud:** [`docs/assignment_original.md`](docs/assignment_original.md). Kõik tehtud ja tegemata asjad hoitakse eraldi. Teiste ainete ja varasemate laborite faile ei muudeta.

## Projekti eesmärk

Sama MG400 pumbakast peab täitma kahte vastastikku välistavat tööd: enne klaasi haaramist annustatakse **Anycubic Standard Resin** 10 cc süstlast, hiljem kasutatakse vaakumit klaasi hoidmiseks. 3/2 solenoidklapp eraldab süstla pumbast ja peab vooluta olekus suunama süstla õhku. Klaas vajutatakse mudel-Atomi peale ja 405 nm LED kõvendab vaigu. Ohtudeks on **ummistunud otsik** ja **tühi süstal**; need peavad andma usaldusväärse alarmi ning katkestama doseerimise.

## Neli tööplokki

| Plokk | Ülesanne | Tõendus / väljund | Staatus |
| --- | --- | --- | --- |
| 1. Klapp ja impulss | 3/2 klapi vooluta asendi kontroll; relee ja kaitsediood; Atomi riistvarataimer; LED automaatne väljalülitus | Viis käsu pikkust, kümme kordust igaühe kohta; ostsilloskoobi mõõdetud impulsid ja viivitused | **Pole dokumenteeritud** |
| 2. Tilga suurus | Vähemalt viis impulsi pikkust × kümme tilka; teise otsiku või rõhu katse; kaamera mõõtkava, vahetükid, ekraanimudelid | [`data/drops.csv`](data/drops.csv), [`data/placement.csv`](data/placement.csv), pildid, rõhukõverad ja [`docs/recipe.md`](docs/recipe.md) | **Mõõtmised puuduvad** |
| 3. Filter ja dP/dt | Toores tuletis, libisev keskmine ja mediaanfilter, spektrid ning filtri müra ja viivitus | [`notebooks/`](notebooks/), samade 100 Hz rõhukõverate kontrollitud analüüs | **Vajab 100 Hz katseandmeid** |
| 4. Komparaator ja IRQ | Lävi + hüsterees Falstadis; LM358N komparaator; Atom IRQ; klapi väljalülitus, lukustatud alarm, `clear` | [`docs/latency.csv`](docs/latency.csv): 10× IRQ, 10× polling, 10 ummistust, 10 tühja süstalt, 30 normaalset tilka | **Pole mõõdetud** |

## Sõltuvused ja olemasolevad lähtefailid

- [Andmehõive Lab 2](../lab2/README.md): MPX5700AP, parandatud LM358P skeem, [pumbajuhtimise ülevaade](../lab2/docs/pump_control.md), [100 Hz püsivara kavand](../lab2/src/atom_pressure_100hz/). **100 Hz püsivara ei ole veel füüsiliselt kontrollitud**; puudu on võrreldavad `raw/opamp` logid ja pooliku haarde ajatemplid.
- [Nutilahendused Lab 2](../../Nutilahendused/lab2/README.md): side ja veebiliidese kontekst. Lab 3 Atomi lehe nupud ning alarmi kaudu roboti peatamine tuleb veel kooskõlastada.
- 3D printimine: süstlahoidik, rõhukindel õhuühendus, kaamera nihe `tool_offsets.md`, mõõteskaalaga tilgaplaat ja päris mõõtudega Atomi ekraanimudel. **Lab 3 faile ega kinnitatud mudeleid repo hetkeülevaates ei olnud**; seni kasutada laual olevat statiivi vaid juhul, kui see on füüsiliselt ohutu.
- Riistvara: klapi mähise pinge/vool, relee kontaktide ühendus vooluta olekus, LED draiveri parameetrid ja vaba ADC/IRQ viik **tuleb mõõta/kinnitada enne skeemi ja püsivara lõplikku valikut**.

## Tööfailid

- [`checklist.md`](checklist.md) — nõuded, kontrollid ja tegelik täitmise seis.
- [`src/`](src/) — eraldi Lab 3 püsivara, riistvarataimer, käsud, IRQ ja logija; esialgu alles planeeritud.
- [`data/`](data/) — ainult päistega tabelimallid; katsetulemusi ei ole sisestatud.
- [`notebooks/`](notebooks/) — filtreerimise, tuletise, FFT ja katseandmete võrdlemise ülesanded.
- [`docs/bom.md`](docs/bom.md), [`docs/recipe.md`](docs/recipe.md), [`docs/latency.csv`](docs/latency.csv), [`docs/development-log.md`](docs/development-log.md) — dokumentatsioon ja mõõtmisvormid.

## Esimene mõistlik tööjärjekord

1. **Fikseeri olemasolevad osad ja nende andmelehed.** Klapi täpne tähis, alalisvoolupinge ja -vool; relee COM/ON/OFF tegelik ühendus vooluta olekus; UV LED/driver; kaitsediood ja suruõhu ühendused. Vanas Lab 2 võimendis kasutati **LM358P**; algne Lab 3 ülesanne mainib **LM358N**. Kontrolli, milline mikroskeem ja mitu vaba kanalit päriselt on.
2. **Kavanda ohutu väljalülitus enne doseerimist.** Vooluta on klapp süstla õhku laskvas asendis; vooluta LED on kustunud. 5 V tasemed ei tohi pääseda Atomi 3,3 V viikudele.
3. Seejärel alusta taimeri ja IRQ **kuiva pingetesti** ilma vaigu, rõhu ja UV kiirguseta, kuni klapi ning LED-i elektriline töö on kontrollitud. Füüsilise klapi juhtimine eeldab eraldi riistvarakinnitust.
4. Alles pärast seda doseerimiskatsed, kaameramõõtmised ning 100 Hz rõhukõverad ja dP/dt analüüs.

**Ohutus:** ära suuna 405 nm valgust silmadesse, käsitle kõvenemata vaiku kaitsevahenditega, ära jäta ummistunud süstalt rõhu alla ega ühenda Atomi GPIO-le üle 3,3 V. Pumba- ja UV-katsed toimuvad ainult juhendatud füüsilise seadistusega.

**Git tag kaitsmiseks:** `data-acquisition-lab3` — **ei ole loodud**; lisada alles siis, kui kontrollitud tulemused on valmis.
