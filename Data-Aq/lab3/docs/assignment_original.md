## Andmehõive: Labor 3 — Tilk ja IRQ

**Töömaht:** 30 tundi | **Hindamine:** 20 punkti | **Meeskond:** 3 tudengit | **Välja antud:** 28.10.26 | **Tellimise kuupäev:** 06.11.26 | **Esimene kaitsmine:** 19.11.26, veebis

### Kuidas see dokument töötab

- Repo ja töökord on Laborist 1 olemas ja samad.
- Too sellest dokumendist oma projekti repo juurde see, mida vaja: selle labori kaust, `README.md`, kuhu lähevad su enda numbrid, otsused ja KAARDISTA ISE vastused, ja failid, mida kontrollnimekiri nimetab. Tervet dokumenti üle kopeerida ei ole vaja.
- Skeemid ja simulatsioonid lähevad dokumenti pildina, pildi juurde link elavale failile, et teine saaks selle lahti teha ja edasi muuta.

### Eesmärk

Seni tegi pump ühte tööd: imes, ja napp hoidis klaasi. Nüüd teeb sama pump teist tööd ka. Ta puhub süstlasse, ja süstla otsikust tuleb tilk liimi. Mõlemat korraga ta ei tee: kui ta imeb klaasi kinni, ei saa ta süstlasse puhuda. Seepärast tehakse tilk enne, kui klaas võetakse, ja puhumise ajal läheb liigne õhk lahtisest napist välja. Millal tilk algab ja lõpeb, otsustab solenoidklapp süstla ees, ja klappi juhib sinu Atom.

Liim on 3D-printeri vaik, [Anycubic Standard Resin](https://www.photopoint.ee/en/printers-accessories/5160735-anycubic-standard-resin-grey), mis kõveneb 405 nm valguse käes. Tilk läheb Atomi ekraani peale, klaas tilga peale, ja UV LED kõvendab liimi läbi klaasi.

Sellest tuleb kaks küsimust, ja need on selle labori kaks poolt.

**Kui suur on tilk?** Tilga suurus on rõhk korda aeg korda otsiku ava — ja veel see, kui palju vaiku süstlas on, kui soe on ruum, ja kui pikk on voolik. Liiga väike tilk ei hoia klaasi kinni. Liiga suur pressitakse klaasi alt välja ja Atomi külgedele. Kui suur on paras, ei tea praegu keegi; see on number, mille sina mõõdad. Tulemus on **retsept**: otsik, rõhk, impulsi pikkus, kõvendamise aeg.

**Mis siis, kui midagi läheb valesti?** Kaks asja lähevad kindlasti.

- **Otsik kõveneb kinni.** Päevavalguses on piisavalt UV-d, ja lamp on sealsamas kõrval. Kinni otsikuga süstal on suletud anum, kuhu pump puhub. Liim ei tule, rõhk tuleb.
- **Süstal saab tühjaks.** Otsikust tuleb õhk, mitte liim, ja robot paneb klaasi kuiva Atomi peale.

Mõlemal juhul peab klapp kohe tagasi minema ja robot peab teada saama. "Kohe" ei tähenda siis, kui jaam järgmine kord küsib. Jaam on sülearvuti teisel pool USB kaablit ja tal on parajasti muud teha. Otsus tehakse seal, kus on andur, ja seda ei tee programmi põhitsükkel, vaid **katkestus (IRQ)**: riistvara ise ütleb protsessorile, et nüüd, ja protsessor jätab kõik muu pooleli.

Laboris 2 lubati, et rõhu **muutumise kiirus** (dP/dt, kPa/s) on Labori 3 töö. Siin see on. Poolikut haaret eristas korralikust see, kui kiiresti rõhk langeb. Kinnist otsikut eristab lahtisest see, kuidas rõhk tõuseb. Mõlemad on tuletis, ja tuletisel on üks ebameeldiv omadus, mille sa Fourier' abil ise ära näed: ta võimendab müra, ja seda rohkem, mida kõrgem on sagedus. Seepärast tuleb filter enne tuletist, mitte pärast.

Selles laboris on neli asja:

1. **Klapp ja impulss.** Atom lülitab klappi, impulsi pikkuse loeb riistvarataimer, ja ostsilloskoop ütleb, kui pikk impulss päriselt oli.
2. **Tilga suurus.** Eri pikkusega impulsid, eri suurusega tilgad, iga tilga rõhukõver. Sealt tuleb retsept.
3. **Filter ja tuletis.** Salvestatud kõverate peal: toores muutumise kiirus, filtreeritud muutumise kiirus, ja spekter, mis ütleb, miks üks neist on kasutu.
4. **Katkestus (IRQ).** Komparaator Falstadis, siis plaadil. Kinnine otsik ja tühi süstal päriselt läbi proovitud, ja reageerimise aeg ostsilloskoobilt.

Esimesel päeval uusi osi ei ole. Ehita sellest, mis riiulil on, ja kirjuta puuduv tellimuseks, mis läheb välja 06.11.

*See on elav dokument. Uuenda eesmärke, kui need töö käigus muutuvad — uued teadmised teevad vanad eesmärgid vahel mõttetuks. Mõte on hoida meeskond kogu aeg sihil, et ei eksitaks detailide metsa ja põhiprobleem ei jääks lahendamata.*

**KAARDISTA ISE — eesmärk nii, nagu ta tegelikult välja tuli.**

### Kontrollnimekiri

**Peab olema tehtud**

- &#x20;Klapp lülitab Atomi käsu peale. Vooluta on süstal õhu peal ja pumbast lahti. Mõõdetud, mitte oletatud.
- &#x20;Impulsi pikkust loeb riistvarataimer. Käsk ja ostsilloskoobilt klapi mähisel mõõdetud pikkus kõrvuti viie pikkuse kohta.
- &#x20;UV LED lülitab Atomi käsu peale ja kustub alati ise.
- &#x20;Anduri koht voolikus valitud ja põhjendatud.
- &#x20;Tilgad: vähemalt viis impulsi pikkust, kümme tilka igaühega, iga tilk mõõdetud pildilt tilgaplaadil ja iga tilga rõhukõver salvestatud. Fail `data/drops.csv`.
- &#x20;Teine muutuja läbi proovitud: teine otsik või teine rõhk, kolme impulsi pikkusega.
- &#x20;Atomi ekraanipoole mudelid prinditud päris AtomS3 mõõtude järgi. Tilk ja klaas mudeli peal, laigu suurus ja koht mõõdetud tööriista kaamera pildilt. Tulemused ja pildid failis `data/placement.csv`.
- &#x20;Retsept kirjas failis `docs/recipe.md`: otsik, rõhk, impulss, kõvendamise aeg, ja klaas selle tilga peal läbi proovitud.
- &#x20;Toores ja filtreeritud muutumise kiirus kõrvuti samal kõveral, spektrid kõrvuti. Filter valitud numbritega.
- &#x20;Sama muutumise kiirus Labori 2 pooliku haarde logil: kas "vaakum püsib" on nüüd otsus.
- &#x20;Komparaator Falstadis: lülitub kinnise otsiku peale, ei lülitu tavalise tilga ega müra peale.
- &#x20;Komparaator plaadil, katkestus (IRQ) Atomis: klapp tagasi, alarm lukus, sündmus välja.
- &#x20;Reageerimise aeg ostsilloskoobilt, kümme korda, katkestusega ja ilma. Fail `docs/latency.csv`.
- &#x20;Kinnine otsik kümme korda ja tühi süstal kümme korda: mitu korda tabas. Tavaline tilk kolmkümmend korda: mitu valehäiret.
- &#x20;Tellimus 06.11 failis `docs/bom.md`.
- &#x20;Repo ja arenduspäevik täidetud, tag `data-acquisition-lab3`.

**KAARDISTA ISE — kuupäevad ja sinu enda sammud.**

### Sisendid

- Laborist 1 ja 2: andur koos op-ampiga, 100 Hz logija, CSV formaat, pumbajuhtimine ribaga (`pump_control.md`), pooliku haarde logid.
- Õppejõult: 3/2 solenoidklapp, [M5Stack Mini 3A Relay Unit](https://shop.m5stack.com/products/mini-3a-relay-unit) klapi lülitamiseks, kaks 4 mm Y-kiirliitmikku (napi haru ja rõhuandur), vaik [Anycubic Standard Resin](https://www.photopoint.ee/en/printers-accessories/5160735-anycubic-standard-resin-grey) (1 kg, 365–405 nm, 200–230 mPa·s), õppejõud täidab sellega 10 cc mustad süstlad [Metcal 910-B](https://www.farnell.com/datasheets/3919444.pdf), üks süstla suurus; otsikud kolmes suuruses, otsikukorgid, kaitseprillid 405 nm jaoks, nitriilkindad, isopropanool.
- Riiulilt: LM358N (tema teine pool on komparaator), takistite ja kondensaatorite komplekt, ostsilloskoop, multimeeter, nihik.
- 3D printimise L3-st: tööriist, mis hoiab süstalt, süstla õhuühendus, mis peab rõhku, ja kaamera nihe flantsi suhtes failis `tool_offsets.md`. Kuni seda ei ole, on süstal statiivis laua peal.
- Nutikate Lahenduste L3-st: Atomi leht, kuhu klapi ja LED-i seaded ja testinupud lähevad.
- Meeskonnalt endalt: 405 nm LED ja tema draiver, samad, mille valisid 3D printimise L3 jaoks. Õppejõud ostab need Mouserist ja nad tulevad tellimusega; kuni neid ei ole, proovid LED-i taimerit Atomi viigu peal ostsilloskoobiga.
- Meeskonnalt endalt: üks meelega kinni kõvendatud otsik. Teed selle ise (vt Ohutus).

### Vahendid

1. AtomS3, USB-C kaablid
2. Sinu andur ja op-amp Laborist 2
3. 3/2 solenoidklapp, M5Stack Mini 3A Relay Unit, kaitsediood, kaks 4 mm Y-kiirliitmikku
4. Anycubic Standard Resin õppejõu täidetud 10 cc mustades süstaldes (Metcal 910-B) kolbidega, otsikud, otsikukorgid
5. 405 nm LED ja draiver (sinu valitud, Mouserist); kaitseprillid, nitriilkindad, isopropanool, paberrätikud
6. LM358N, takistite ja kondensaatorite komplekt, maketeerimisplaat
7. Ostsilloskoop, kaks kanalit; multimeeter
8. Nihik; tööriista kaameramoodul (XIAO ESP32S3 Sense, 3D printimise L2-st); hele PLA tilgaplaatide jaoks
9. MG400 koos pumbakastiga
10. Arduino IDE või PlatformIO; Python 3, Jupyter Lab, numpy, pandas, scipy, matplotlib
11. Falstad; git

*Kui plaan muutub, uuenda ka vahendeid, või tee draw\.io skeem, mis näitab, kuidas asjad omavahel töötavad.*

**KAARDISTA ISE — mida sa päriselt kasutasid.**

### Taustainfo

- **ESP32 katkestus / IRQ** [https://www.youtube.com/watch?v=WVK2Wx386XE](https://www.youtube.com/watch?v=WVK2Wx386XE)
- **Schmitti triger** — komparaator, mis ei jää läve peal värisema [https://www.youtube.com/watch?v=Nrp8OgQLAlw](https://www.youtube.com/watch?v=Nrp8OgQLAlw)
- **Madalpääsfilter** [https://www.youtube.com/watch?v=OBM5T5_kgdI](https://www.youtube.com/watch?v=OBM5T5_kgdI)
- **Kõrgpääsfilter** — sama asi, mis tuletis, ainult teise nimega [https://www.youtube.com/watch?v=H30kRgI5bi0](https://www.youtube.com/watch?v=H30kRgI5bi0)
- **Mürahaldus** [https://www.youtube.com/watch?v=u40kX1DYKdA](https://www.youtube.com/watch?v=u40kX1DYKdA)
- **Kuidas op-amp töötab** — komparaator on sama kolmnurk ilma tagasisideta [https://www.youtube.com/watch?v=kbVqTMy8HMg](https://www.youtube.com/watch?v=kbVqTMy8HMg)
- **Solenoid, relee ja kaitsediood** (link puudu — YouTube: "flyback diode relay solenoid explained")
- **ESP32 riistvarataimer** (link puudu — YouTube: "ESP32 hardware timer interrupt")
- **Falstad** [https://www.falstad.com/circuit/circuitjs.html](https://www.falstad.com/circuit/circuitjs.html)

*Lisa siia oma allikaid ja kasulikku infot, mis aitaks sul projektist aru saada ka aastaid hiljem, kui selle uuesti lahti teed.*

**KAARDISTA ISE — sinu allikad.**

### Osad

#### 1. Klapp ja impulss

Klapp on mähis, ja mähis tahab rohkem voolu, kui Atomi viik annab, ja teist pinget. Vahele käib M5Stack Mini 3A Relay Unit. Atom annab talle 5 V, maa ja ühe signaali, ja moodul lülitab kontakti, mis on Atomist täiesti eraldi ahel. Klemme on kolm: COM, ON ja OFF. Relee ühendab COM-i kas ON-i või OFF-iga. Kumb neist on vooluta ühendatud, mõõda multimeetriga, ära oleta silti järgi. Loe klapi pealt, mis pinget ja voolu ta tahab, ja mooduli pealt, mida kontakt kannab, enne kui midagi ühendad.

Mähisel on üks omadus, mis teeb elektroonika katki: kui vool välja lülitatakse, tekitab mähis hetkeks pinge, mis on mitu korda suurem kui toide. Releega läheb see pinge sädemena üle avaneva kontakti, ja iga säde sööb kontakti. **Kaitsediood** klapi mähise peal võtab selle enda peale. Releemoodulil teda ei ole: moodul ei tea, mida sa kontaktiga lülitad. Diood käib klapi mähisega rööbiti ja tagurpidi, triip plussi poole; teistpidi on ta lühis. Ostsilloskoop näitab sulle seda tippu ilma dioodita ja dioodiga — tee see pilt, sond 10× peal.

**Ohutu olek.** Klapil on kolm ava: üks pumba poolt, üks süstlale, üks õhku. Voolu all ühendab ta pumba süstlaga, vooluta süstla õhuga. Napp klapi kaudu ei käi: ta on Y-liitmikuga otse pumba voolikus, enne klappi. Vedrusid on kaks. Relee on vedruga: vooluta on ta alati samas asendis. Klapp on vedruga: vooluta läheb ta tagasi ühte kindlasse asendisse. Klapp käib selle klemmi peale, mis on vooluta lahti, ja klapi vooluta asend peab olema süstal õhu peal. Siis ei tule vooluta süstlast midagi, ja tilk lõpeb kohe, kui klapp sulgub: rõhk läheb süstlast õhku, mitte ei jää sinna tilka edasi suruma. Kontrolli seda päriselt: tõmba Atomilt USB välja, pane pump puhuma ja vaata, kas süstla harus on rõhku. Ei tohi olla. See on sama reegel, mis Laboris 1: kui midagi on valesti, ei juhtu midagi.

**Impulss.** Tilk on klapi lahtioleku aeg. Kui seda aega loeb programmi põhitsükkel, mis samal ajal joonistab ekraani ja saadab ridu, on impulss iga kord natuke erineva pikkusega, ja tilk ka. Impulsi pikkuse loeb **riistvarataimer**: sa ütled talle millisekundid, ta sulgeb klapi ise, ükskõik mida ülejäänud programm sel hetkel teeb.

Taimer lülitab Atomi viiku, aga klappi lülitab relee, ja relee on mehaaniline lüliti. Tal kulub mõni millisekund, et kinni minna, ja mõni, et lahti minna, ja need kaks ei ole võrdsed. Seepärast on ostsilloskoobil kaks kanalit: üks Atomi viigul, teine klapi mähisel. Käsk oli 200 ms: kui pikk oli impulss viigul, ja kui pikk mähisel? Viis pikkust, kümme korda igaüht. Keskmine ja kõikumine. Vahe viigu ja mähise vahel on relee. Vaata sisselülitamise serva ka lähedalt: kas kontakt põrkab?

**Relee piirid.** Relee on lihtne ja annab täieliku eralduse, aga tal on piirid, ja need tuleb numbritega teada. Leia mooduli pealt relee nimi ja tema andmeleht. Kolm küsimust. Kas kontakt kannab klapi pinget ja voolu alalisvoolul, varuga? Mis on mõõdetud sisse- ja väljalülitamise aeg võrreldes andmelehega, ja mis on siis lühim tilk, mida relee üldse teha saab? Ja kui kaua ta vastu peab: andmeleht ütleb kontakti elektrilise eluea lülituste arvuna; jaga see tilkade arvuga, mida masin päevas teeb, ja saad päevad. Mähis on induktiivne koormus, ja selle all kulub kontakt kiiremini kui andmelehe takistuslikul koormusel. See on teine põhjus, miks diood peal on. Relee ei sobi ka kiireks lülitamiseks: PWM-iga mähise voolu pärast avanemist alla võtta, et klapp vähem soojeneks, ta ei saa. Hilisemates laborites tuleb sama töö jaoks MOSFET; siis on sul need numbrid, millega teda võrrelda.

Ja üks asi, mida ostsilloskoop ei näe: klapp ise on samuti mehaaniline ja tal kulub avanemiseks aega. Rõhukõver näitab seda. Kui kaua pärast käsku hakkab rõhk süstla harus tõusma? See on lühim impulss, millel on üldse mõtet.

**Kus andur istub.** Sul on üks andur. Ta võib istuda pumba voolikus enne klappi: siis näeb ta nappa ja pumba rõhku, aga tilka ainult läbi klapi. Või klapi ja süstla vahel: siis näeb ta tilka teravalt ja nappa üldse mitte, ja ta istub koos Y-ga käe otsas. Vali, ja ütle, millest sa loobusid. Õppejõult saad kaks 4 mm Y-kiirliitmikku: üks napi harule, teine andurile.

**UV LED** saab sama kohtlemise: Atom lülitab ta draiveri kaudu sisse ja taimer lülitab välja. LED ei jää põlema sellepärast, et käsk "välja" ei jõudnud kohale.

```
arvuti → Atom:  {"cmd":"dispense","ms":200}    {"cmd":"uv","ms":5000}    {"cmd":"clear"}
Atom → arvuti:  {"ev":"dispense_start","t":123456}    {"ev":"dispense_end","t":123660}

```

Kirjuta üles: klapi pinge ja kuidas ta on läbi relee ühendatud, skeem pildina; ostsilloskoobi pilt mähise pingest väljalülitamisel, dioodita ja dioodiga; mis rõhk on süstla harus, kui Atom on vooluta; impulsi pikkuse tabel: käsk, viigul mõõdetud, mähisel mõõdetud; relee viivitus sisse ja välja lülitamisel, mõõdetud ja andmelehelt; relee nimi, kontakti lubatud pinge ja vool ning eluiga päevades sinu tilkade arvuga; klapi avanemise viivitus rõhukõveralt; anduri koht ja põhjus.

#### 2. Tilga suurus

Kõigepealt see, mida sa hoiad paigal. Rõhk: Labori 1 riba hoiab pumpa kahe lülituspunkti vahel, ja see töötab ka puhumisel — kui õhk kuhugi ei kao. Doseerimise ajal on napp lahti ja õhk läheb sealt välja. Mõõda, mis rõhk süstla ette jääb, kui napp on lahti, ja kas riba jõuab üldse väljalülitusrõhuni. Kui ei jõua või rõhust ei piisa, pane napi harusse nõelventiil: ta piirab, kui palju õhku napist välja läheb, ja temaga saab rõhku seada. Mida ta imemisega teeb, mõõda samuti. Kirjuta üles, mis rõhul sa doseerid. Otsik: vaik on vedel, umbes 200 mPa·s, kümneid kordi vedelam kui tavaline UV-liim. Mida vedelam, seda lühem impulss annab sama tilga, ja kui impulss läheb liiga lühikeseks, on relee ja klapi kõikumine suur osa tilgast. Hoia impulss üle 100 ms. Selleks alusta kõige peenemast otsikust ja madalast rõhust: vool läbi otsiku käib ava raadiuse neljanda astmega, nii et peenem otsik mõjub kõige rohkem. Kui ka kõige peenema otsiku ja madalaima rõhuga tuleb tilk liiga suur või ei püsi kujus, kirjuta see numbritega üles: siis teeme tööriista, millega tilk õigesse kuju ja suurusse surutakse. Süstal: täis, ja märgi, kui täis.

Siis muuda ühte asja: impulsi pikkust. Vähemalt viis pikkust, lühimast, mis üldse midagi välja annab, kuni sellise, mis on ilmselgelt liiga suur. Kümme tilka igaühega. Nii väikest tilka nihikuga ei mõõda: serv on hägune, ja 0,1 mm viga 5 mm laigul on mitu protsenti pindalast. Tilgad mõõdetakse pildilt.

**Tilgaplaat.** Prindi hele PLA plaat, valge või kollane, et hall vaik tema peal paistaks, ja prindi plaadile mõõtkava: näiteks 10 mm ruudustik või joonlaud. Robot paneb plaadile 5 × 5 tilka. Read on impulsi pikkused, veerud kordused, nii et kümme kordust on kaks plaati. Tilkade vahe peab olema suurem kui suurim laik, muidu sulavad naabrid kokku; selle annab esimene proovikord. Siis läheb peale klaas, aga mitte otse tilkade peale, vaid **vahetükkidele**, mis hoiavad teda plaadist kindlal kõrgusel. Siis on iga laik ühepaksune kiht, ja ruumala on pindala korda kõrgus. Ilma vahetükkideta sõltub laik sellest, kui kõvasti ja kui kaua klaas peal oli, ja kaks sama tilka annavad kaks eri laiku. Tee tilgad kiiresti järjest: esimene vajub laiali ja kõveneb toavalguses natuke, kuni viimane tuleb. Kõvenda kogu plaat lambiga ja alles siis pildista.

**Pilt.** Pildistab tööriista kaamera, see sama kaameramoodul, mis 3D printimise Laboris 2 napa kõrvale läks. Robot hoiab teda iga kord täpselt samal kõrgusel ja risti plaadiga, ja viib ta iga tilga kohale: tilkade kohad on ruudustikus teada, ja kaamera nihe flantsi suhtes on failis `tool_offsets.md`. Mine nii lähedale, et kahe impulsi pikkuse tilkade vahe on pikslites kindlasti näha — aga mitte lähemale, kui kaamera teravaks saab: tema objektiivil on lähim teravuse kaugus, ja udune serv on sama halb kui nihik. Leia see kõrgus katsega ja kirjuta üles. Arvuta, mitu mm on üks piksel sellel kõrgusel ja mitu pikslit on väikseima tilga läbimõõt. Valgus on hajus või tuleb küljelt, nii et klaasi peegeldus laikude peale ei jää; UV LED pildistamise ajal ei põle. Mõõtkavast tuleb mm piksli kohta: kuna kõrgus on alati sama, piisab ühest mõõtkava pildist iga seansi alguses. Programm eraldab heleda plaadi tumedast vaigust lävega ja loeb iga laigu pikslid kokku: pikslid → mm² → ruumala. Kontrolli läve: joonista leitud laikude piirjooned pildi peale tagasi ja vaata, kas nad on seal, kus laik päriselt on. Arvuta ka, mitu protsenti pindalast teeb üks piksel laigu serval: see on su mõõtmise täpsus, ja ta peab olema palju väiksem kui kõikumine, mida sa mõõta tahad.

Iga tilga kohta salvestatakse ka rõhukõver, sama tilga numbriga. See ei ole paberitöö. Sa tahad teada, kas kõver ütleb tilga suuruse ette — kas platoo kõrgus või kõvera alune pindala käib tilga suurusega kaasas. Kui käib, saab iga tilka kontrollida ilma teda mõõtmata. Labor 5 ehitab selle peale.

Kolm asja, mida vaadata:

- **Kas sõltuvus on sirge?** Kaks korda pikem impulss, kas kaks korda suurem tilk? Kui ei ole, siis kust ta kõveraks läheb ja miks.
- **Kui palju sama impulss kõigub?** Kümme tilka sama käsuga ei ole kümme ühesugust tilka. Standardhälve jagatud keskmisega. See number ütleb, kui täpne su doseerimine on, ja ta on tähtsam kui keskmine.
- **Esimene tilk.** Kas esimene tilk pärast pausi on sama, mis kümnes? Kui ei ole, siis sellepärast on laual prügitops.

Siis muuda teist asja ja korda lühemalt: teine otsik või teine rõhk, kolm impulsi pikkust. Kumb mõjutab tilka rohkem, kas aeg või ava?

**Atomi ekraanipoole mudel.** Päris AtomS3 peale liimi ei proovita: iga liimitud tükk on kasutatud, ja selleks pole mõtet päris Atomit raisata. Tee Atomi ekraanipoolest mudel. Mõõda päris AtomS3 nihikuga: välismõõt, ekraani ava suurus ja koht, ja kui palju ekraan raamist madalamal on. Mudel on õhuke prinditud plaat, millel need kolm asja on samad, ja mis istub töökoha hoidikus nagu päris Atom. Ekraani ala märgi kontrastse joonega ära, et tilga kohta oleks näha. Prindi neid mitu, sest iga liimitud mudel jääb liimi alla.

Ja lõpuks päris katse. Tilk mudeli peale, klaas peale, vaata läbi klaasi. Liim peab katma piisavalt, et hoida, ja ei tohi jõuda servani. Mõõda pildilt, samamoodi nagu tilgaplaadil, kaks asja: kui suureks laik klaasi all vajus, ja kui kaugel ta keskpunkt on ekraani keskpunktist, x ja y eraldi. Mõõtkava on mudeli peal. Otsusta, milline tilk on paras. Kõvenda ja mõõda, kui kaua see võtab: millal klaas enam ei nihku.

Selles laboris pildistab robot ja sina loed pildid arvutis läbi. Järgmises laboris teeb sama mõõtmise masin ise, ja tagasiside läheb otse doseerimisse. Seepärast kirjuta mõõtmised üles samas kujus, mida masin hakkab hiljem võrdlema.

Kirjuta üles: tilgaplaadi ja vahetükkide mudel, vahetükkide kõrgus ja kuidas sa selle mõõtsid; read failis `data/drops.csv` (tilga number, plaat, rida, veerg, otsik, rõhk, impulss ms, pindala pikslites, mm piksli kohta, pindala mm², ruumala µl, kõvera fail, märkus); pildid koos leitud piirjoontega; mõõtmise täpsus protsentides; graafik, tilga suurus impulsi pikkuse vastu, hajuvusega; kõikumine protsentides iga pikkuse kohta; kas kõvera platoo või pindala käib tilga suurusega kaasas; mudeli mõõdud ja kust need tulid; read failis `data/placement.csv` (mudeli number, tilga number, impulss ms, laigu pindala klaasi all mm², nihe ekraani keskpunktist x ja y mm, kas jõudis servani, kuidas mõõdeti); retsept failis `docs/recipe.md` — otsik, rõhk, impulss, kõvendamise aeg, ja foto klaasist selle tilga peal.

#### 3. Filter ja tuletis

See osa käib arvutis, kõverate peal, mis sul juba on.

Võta üks tilga kõver ja arvuta rõhu muutumise kiirus kõige lihtsamal moel: `dP/dt = (P praegu − P eelmine) / 10 ms`. Joonista. See ei näe välja nagu kõvera tõus, vaid nagu müra, ja põhjus on arvutatav. Tuletis korrutab iga sageduse tema enda sagedusega: aeglane muutus, mida sa otsid, jääb väikeseks, ja kiire värin, mida sa ei otsi, kasvab suureks. Tee spekter signaalist ja spekter tuletisest ja pane kõrvuti. Suhe igal sagedusel on `2πf`. Labori 1 spektrist tead sa juba, millised tipud seal on; nüüd näed, milline neist tuletise ära rikub.

Seega filter enne. Proovi vähemalt kahte: libisev keskmine ja mediaan. Nad ei tee sama asja — keskmine määrib üksiku terava tipu laiali, mediaan viskab ta välja. Iga filtri kohta kaks numbrit: kui palju müra tuletises alles jäi, ja **kui palju filter hiljaks jääb**. Filter ei ole tasuta. Kümne punkti keskmine teab muutusest alles siis, kui see on juba pool oma akent vana. Katkestuse jaoks on see viivitus osa reageerimise ajast.

Vali üks. Põhjus on kaks numbrit kõrvuti, mitte "tundus sujuvam".

Siis tee sama asi, mille Labor 2 lubas. Võta pooliku haarde logid ja arvuta nende peal filtreeritud muutumise kiirus pärast pumba väljalülitumist. Laboris 2 küsiti, mitu sekundit kulub, enne kui poolik haare on korralikust eristatav. Nüüd on küsimus: kas on olemas muutumise kiiruse lävi, mis eristab nad ära, ja kui kiiresti? See on otsus "vaakum püsib", ja robot tõstab selle peale.

Ja lõpuks see, mille pärast osa 4 olemas on. Pane kolm kõverat kõrvuti: tavaline tilk, kinnine otsik, tühi süstal. Mis neid eristab — tõusu kiirus, platoo kõrgus, või see, kuidas rõhk pärast klapi sulgumist langeb? Seda ei tea ette keegi. Vaata oma andmeid ja vali tunnus, mille järgi katkestus lülitub.

Kirjuta üles: toores ja filtreeritud muutumise kiirus samal kõveral; spektrid kõrvuti; iga filtri müra ja viivitus, ja kumma sa valisid; muutumise kiiruse lävi korraliku ja pooliku haarde vahel ja aeg otsuseni; kolm doseerimise kõverat kõrvuti ja tunnus, mis neid eristab, numbritega.

#### 4. Katkestus

Nüüd tehakse sama otsus riistvaras.

**Falstadis enne.** Komparaator võrdleb kahte pinget ja tema väljund on üks kahest: kõrge või madal. Ühes sisendis on sinu signaal — kas op-ampi väljund ise või tema tuletis, olenevalt sellest, mille sa osas 3 valisid —, teises on lävi. Kolm sisendit, mida proovida: tavaline tilk, kinnine otsik, ja tavaline tilk, mille peal on müra. Komparaator peab lülituma teise peale ja mitte esimese ega kolmanda peale.

Kolmas on see, mis esimesel korral ei õnnestu. Kui signaal on täpselt läve juures, lülitab müra komparaatorit edasi-tagasi kümneid kordi. Lahendus on **hüsterees**: natuke väljundist tagasi sisendisse, nii et sisselülitamise lävi on kõrgemal kui väljalülitamise oma. See on Schmitti triger, ja see on sama mõte, mis Labori 1 pumbajuhtimise riba: kaks läve ühe asemel, et asi värisema ei jääks. Takistid tulevad Falstadist.

**Siis plaadil.** Komparaator on LM358N teine pool: sama kiip, mis Laborist 2 juba plaadil on, esimene pool võimendab ja teine võrdleb. Op-amp ilma tagasisideta ongi komparaator. Tema väljund läheb Atomi viiku, mis teeb katkestuse. LM358N väljund ei ole rail-to-rail: 5 V toitel jõuab ta umbes 3,5 V-ni, ja see on Atomi viigu jaoks juba liiga palju. Mõõda multimeetriga, mis pinge väljund kõrges olekus päriselt annab, ja kui see on üle 3,3 V, pane vahele jagur, enne kui ta Atomi külge läheb.

```
dispense: kui alarm on lukus → keeldu
          pump puhub, napp lahti → klapp voolu alla → taimer loeb ms → klapp vooluta, süstal õhku
katkestus: klapp kohe vooluta → alarm lukku → {"ev":"alarm","why":"clog"} välja
tühi süstal: kui rõhk ei jõua platoole ettenähtud aja sees → alarm lukku, "empty"
alarm püsib, kuni tuleb {"cmd":"clear"}

```

Katkestuse alguse paneb paika protsessor: kui komparaatori väljund viigul muutub, peatab protsessor põhitsükli riistvaraliselt mõne mikrosekundi jooksul, ükskõik mida programm parasjagu teeb. Katkestuse pikkus on aga sinu kätes, sest kuni katkestuse funktsioon käib, seisab kõik muu — põhitsükkel, ekraan, UART —, ja seepärast tehakse seal ainult see, mis ei saa oodata: klapp kinni ja lipp püsti. Lipp on üks muutuja, mida põhitsükkel igal ringil vaatab, ja kui ta on püsti, teeb põhitsükkel ülejäänu — ekraani, rea arvutile ja alarmi luku —, nii et katkestus ise jääb lühikeseks. Alarm jääb lukku. Süsteem, mis pärast ummistust ise uuesti proovib, pumpab kinnisesse süstlasse teist korda.

**Mõõda, kui kiire see on.** Ostsilloskoobi üks kanal on rõhk, teine pinge klapi mähisel, mitte Atomi viigul: relee lahtilaskmise aeg on osa reageerimise ajast. Kinnine otsik peal. Aeg hetkest, mil rõhk ületab läve, hetkeni, mil klapp lahti lastakse. Kümme korda.

Siis ehita sama kaitse ilma katkestuseta: põhitsükkel loeb iga ringiga andurit ja võrdleb lävega. Mõõda sama aeg, kümme korda. Ja siis anna põhitsüklile tööd — joonista ekraanile, saada ridu — ja mõõda uuesti. Katkestuse number ei tohiks muutuda. Põhitsükli oma muutub. Kirjuta kõrvale ka see, kui kaua kummagi tööle saamine võttis: kiirem lahendus on tavaliselt ka see, mille kallal kauem istuti, ja mõlemad numbrid kuuluvad otsuse juurde.

**Ja lõpuks päris katse.** Kinnine otsik, kümme korda: mitu korda alarm tuli. Tühi süstal, kümme korda. Tavaline tilk retsepti järgi, kolmkümmend korda: mitu korda alarm tuli siis, kui ei oleks pidanud. Kaitse, mis annab valehäireid, lülitatakse välja kolmandal päeval, ja siis ei ole kaitset.

Kirjuta üles: Falstadi skeem pildina ja lingina, takistid, lävi ja hüstereesi laius; ostsilloskoobi pilt lävest ja klapist samal ekraanil; read failis `docs/latency.csv` (katse, viis, koormus, aeg ms), keskmine ja halvim katkestusega ja ilma; kümnest kinnisest otsikust tabatud, kümnest tühjast süstlast tabatud, kolmekümnest tavalisest tilgast valehäireid; arendusaeg kummagi lahenduse kohta; üks lause, kumma sa jätad ja miks.

**KAARDISTA ISE — vastused.** Iga osa kohta: numbrid, ühikud, kus fail on. Tegemata asja kohta üks rida, miks.

### Ohutus

- **405 nm valgus ja silmad.** Valgustamine käib katte all, nii et valgus välja ei paista. 405 nm on UV ja nähtava valguse piiril: silm näeb teda tuhmi violetsena, palju nõrgemana, kui ta tegelikult on, ja võrkkest saab kahju enne, kui valgus ere tundub. LED-i ei vaadata. Kui LED on draiveri küljes, on kõigil laua ääres kaitseprillid 405 nm jaoks ees. Lamp on suunatud laua poole. LED kustub alati ise, taimeriga, ja vooluta on ta väljas.
- **Vaik.** Kõvenemata vaik ärritab nahka ja võib tekitada allergia, mis ei lähe üle. Süstlad täidab õppejõud; täis süstla otsikul on kork ja taga kolb. Nitriilkindad käes, kui süstal on lahti. Maha läinud vaik pühitakse isopropanooli ja paberiga, ja paber kõvendatakse lambi all enne prügikasti. Kõvenemata vaiku kraanikaussi ei valata.
- **Lampi ei suunata otsikule.** Kinni kõvenenud otsik on see viga, mida sa siin avastama õpid. Ummistuskatse jaoks teed ühe meelega ise, ja ainult ühe: otsik eraldi, süstlast lahti, liimi täis, katte all lambi alla, kuni liim on kõva. Märgi ta ära, et ta tavaliste otsikute sekka ei satuks.
- **Kinnine süstal on suletud anum rõhu all.** Ummistuskatse ajal on süstal hoidikus või statiivis, mitte käes. Vooluta klapp laseb süstla rõhu ise õhku: enne kui süstla ära võtad, on klapp vooluta. Kuni katkestus ei ole läbi proovitud, on iga ummistuskatse ajal inimese käsi pumba lüliti juures.
- **Otsikul on kork peal**, kui sa ei doseeri. Päevavalgus kõvendab liimi otsikus aeglaselt, aga kindlalt.
- **Mähis ja diood.** Klappi ei lülitata ilma kaitsedioodita; ainus erand on osa 1 ostsilloskoobi pilt. Klapi pinge ei ole Atomi pinge: relee kontaktide pool ja Atomi pool ei saa kokku. Võrgupinget selle releega ei lülitata.
- **ADC viik ja katkestuse viik ei kannata 5 V.** Komparaatori väljund mõõdetakse multimeetriga üle, enne kui ta Atomi külge läheb.
- USB ja toide välja, enne kui juhet liigutad. Pumbakast on 24 V.
- Lahtine voolik +110 kPa juures lendab; ära suuna kellegi poole.
- Robot: käed ei ole laual, kui robot on sisse lülitatud. Tilku mõõdad sa esialgu laual, mitte roboti otsas.
- Selles laboris ei joodeta.

### Komponendid selle labori jaoks

Tellimus läheb välja 06.11.26 ja jõuab kohale enne kaitsmist. Valmis nimekirja ei ole: meeskond paneb tellimuse ise kokku faili `docs/bom.md`, iga rea juures üks lause, milline osa või number seda küsib.

Tellimine käib ühisest tellimistabelist: [https://moodle.ut.ee/mod/url/view.php?id=1535601](https://moodle.ut.ee/mod/url/view.php?id=1535601). Kanna oma read sinna enne tellimise kuupäeva; mida tabelis ei ole, seda ei tellita. Fail `docs/bom.md` jääb sinu reposse põhjenduseks, miks sa just neid asju küsisid.

Mõtle näiteks: kas LED ja draiver, mille meeskond valis, sobivad kokku — vool, pinge, toide — ja kas mõlema Mouseri tootekood on tabelis; kas vaigu andmeleht lubab teda kõvendada sinu LED-i lainepikkusega; kas klapi mähise jaoks on kaitsediood olemas ja kas ta kannab klapi pinget ja voolu; kas lahtise napiga jääb süstla ette piisavalt rõhku, või on napi harusse vaja nõelventiili; mida LM358N andmeleht ütleb tema väljundi kohta, kui ta töötab komparaatorina; kas hüstereesi takistid, mille Falstad andis, on komplektis olemas; kas otsikuid ja korke jätkub, kui iga kinni läinud otsik on kadunud otsik; kas vaiku on viiekümne tilga ja mõne ebaõnnestumise jaoks; mis kõrguselt tööriista kaamera tilgaplaati teravalt näeb ja mitu mm on seal üks piksel; ja millest teed vahetükid, mis hoiavad klaasi kindlal kõrgusel.

### Hindamiskriteeriumid

| **Kategooria**                                                                                                                                                                               | **Punktid** |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Tööfailid — Atomi püsivara taimeri, katkestuse ja alarmi lukuga, logija, `drops.csv` koos kõveratega, analüüsi märkmik                                                                       | 5 p         |
| Analüüs — impulss käsu ja mõõdetu kõrval, tilga suurus impulsi vastu hajuvusega, toores ja filtreeritud muutumise kiirus spektritega, filtri viivitus, reageerimise aeg katkestusega ja ilma | 5 p         |
| Prototüüp — klapp vooluta laseb süstla õhku, tilk retsepti järgi hoiab klaasi ja ei jõua servani, kinnine otsik ja tühi süstal annavad alarmi, tavaline tilk ei anna                         | 5 p         |
| Dokumentatsioon — README, arenduspäevik, `recipe.md`, `latency.csv`, Falstadi eksport, `pump_control.md` uuendatud, `bom.md`, AGENTS.md                                                      | 5 p         |
| **Kokku**                                                                                                                                                                                    | **20 p**    |

### Kaitsmine

Link git repole, tag `data-acquisition-lab3`.

Kaitsmine on lihtne suuline 15 minuti jutuajamine. Teed ühe tilga retsepti järgi ja näitad selle rõhukõverat. Paned peale kinnise otsiku ja näitad ostsilloskoobil, kuidas klapp lahti lastakse ja kui kiiresti. Näitad, et teine tilk ei tule enne, kui alarm on maha võetud. Avad oma arenduspäeviku. Õppejõud küsib umbes viis küsimust selle kohta, kuidas sa selle tegid. Kui esimesel korral ei õnnestu, tuled uuesti.

Repos on kaustas `data-acquisition/lab3/`: `src/` püsivara ja logijaga, `data/` kaustas `drops.csv`, `placement.csv`, kõverad ja tilgaplaatide pildid, tilgaplaadi lähtefail ja STL, ekraanipoole mudeli lähtefail ja STL, `notebooks/` tilkade, muutumise kiiruse ja spektritega, `docs/` skeemi foto, ostsilloskoobi piltide, Falstadi ekspordi, `recipe.md`, `latency.csv`, uuendatud `pump_control.md` ja `bom.md`-ga, `README.md` selle labori kohta, ja `AGENTS.md` uuendatud.

### Arenduspäevik

**KAARDISTA ISE — päevik.** Üks sissekanne iga töösessiooni kohta, kirjutatud iseendale, nii et inimene, kes seal ei olnud, saab aru. Sissekandeid lisatakse, mitte ei muudeta.

Omadussõnad ei ole tulemused. "Tilgad olid ebaühtlased" ei ole midagi; "200 ms impulss, kümme tilka, 3,1 ± 0,4 mm" on sissekanne.

**PP.KK.AA — kes olid kohal**

- Tegime:
- Juhtus (numbrid):
- Otsustasime, ja miks:
- Lahti järgmiseks korraks:

### Väljundid ja tulemused

**Väljundid**

- Nutikad Lahendused L3: klapi ja LED-i käsud, mille seaded ja testinupud lähevad Atomi lehele; alarmi sündmus, mille peale jaam roboti peatab.
- 3D printimine L3: kui pikk tohib voolik klapi ja süstla vahel olla, ja kus andur istub.
- Andmehõive L4: retsept ja kõverad, mille peale ehitatakse sajad tsüklid; kolm märgistatud olukorda — tavaline, kinnine, tühi.
- Andmehõive L4: kaamera pildilt mõõdetud laigu suurused ja kohad failis `placement.csv` — võrdlus, mille vastu masin oma mõõtmist kontrollib, kui tagasiside automatiseeritakse.
- Andmehõive L4: relee piirid numbritena — viivitus, põrge, kontakti eluiga —, mille vastu MOSFET-i võrreldakse.

**KAARDISTA ISE, lõpus.**

- Git repo ja tag:
- Numbrid, mille see labor andis, ühikutega:
- Mida me teeksime teisiti:
- Mida järgmine labor peaks enne alustamist teadma:

### Tagasiside
