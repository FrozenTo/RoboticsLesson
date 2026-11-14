# Andmehõive — Labor 2: pumba juhtimine ja katsete taastatud dokumentatsioon

**Õppeaine:** Andmehõive  
**Labor:** 2 — Op-amp, lihtne aga keeruline  
**Dokument koostatud:** 14.11.2026  
**Staatus:** olemasolevate koodifailide, logide ja mõõtmisaruande põhjal taastatud; osa katsete arvandmeid ei ole säilinud.

> **Andmete päritolu.** Meeskonna kinnitusel tehti pumbaga katsed, kuid kõigi katseolukordade käivituste arvu, seisuaega ja pooliku haarde eristamise aega ei kirjutatud toona eraldi kokkuvõttesse. Siin ei esitata hiljem oletatud numbreid mõõdetud tulemustena. Allpool on eristatud **koodis määratud seadistused**, **säilinud mõõtmised**, **arvutuslikud väärtused** ja **puuduv tõendus**.

## 1. Süsteem ja olemasolevad failid

Süsteemis kasutati MPX5700AP absoluutrõhuandurit, AtomS3R-i, Dobot MG400 robotit ja pumbakasti. Laboris 1 jõudis anduri signaal otse ADC-sse. Laboris 2 lisasime LM358P operatsioonivõimendi astme, mis parandatud versioonis oli seatud ligikaudu 0,30–3,00 V sihtvahemikku.

Seotud lähtefailid samas repositooriumis:

- [Pumba juhtimise Pythoni programm](../../../Nutilahendused/lab1/sketch_sep12a/tools/suck_until_pressure.py) — rõhupiirini imemine, valikuline rõhu hoidmine ja DO juhtimine.
- [AtomS3R püsivara](../../../Nutilahendused/lab1/sketch_sep12a/src/main.cpp) — ADC, pinge ja rõhu kuvamine ning jadaliidese väljund.
- [Jadaliidese logija](../../../Nutilahendused/lab1/sketch_sep12a/tools/log_serial.py) — ajatempliga tekstlogid.
- [MG400 kohalik veebiliides](../../../MG400%20python%20apps/mg400_grid_website_v18/server.py) — roboti ja pumba DO-juhtimine.
- [Lab 1 ülevaade](../../lab1/README.md) ja [Lab 2 võimendi mõõtmisaruanne](Lab2_aruande.md).
- [Varasem rõhulog](../../../Nutilahendused/lab1/sketch_sep12a/logs/Latest_Log.md) ja [25.10.2026 rõhujälg](../logs/Tool_logs25102026.md).

Need programmid asuvad ajaloolistel põhjustel mitmes projekti kaustas. Nende olemasolu **ei tõenda iseenesest**, et kõik Labor 2 nõutud võrdluskatsed salvestati.

## 2. Pumba ühendus ja juhtimisloogika

Olemasoleva `suck_until_pressure.py` lähtekoodi järgi:

- MG400 vaikimisi IP-aadress on `192.168.1.6`; juhtimine toimub roboti dashboard-liidese kaudu või valikulise veebiserveri kaudu.
- **DO2** juhib imemist (*suck*) ja **DO1** puhumist (*blow*).
- Imemisel aktiveeritakse DO2 ja DO1 lülitatakse välja; puhumisel vastupidi; `off` lülitab mõlemad välja.
- Programm loeb AtomS3R-i jadaliidese väljundist `P_gauge` väärtust.
- Kui mõõdetud rõhk saavutab seatud sihi (on sihiga võrdne või väiksem), lülitab programm pumba välja.
- Kui käivitatud on täiendav jälgimisrežiim `--monitor-after-target`, lülitab programm vajaduse korral imemise uuesti sisse pärast seda, kui rõhk tõuseb üle taaskäivitamise piiri.

### Koodis olevad vaikimisi väärtused — mitte mõõdetud katsetulemused

| Parameeter | Väärtus koodis | Tähendus |
| --- | ---: | --- |
| `--target` | −20,0 kPa | Imemise seiskamise sihtrõhk |
| `--hold-band` | 2,0 kPa | Rõhu tõusu lubatud vahemik enne uut imemist |
| Arvutuslik taaskäivitamise piir | −18,0 kPa | −20 + 2 kPa; rakendub ainult hoidmisrežiimis |
| `--timeout` | 20 s | Esialgse rõhu saavutamise ooteaja piir |
| `--monitor-after-target` | 0 s | Vaikimisi programm pärast sihi saavutamist rõhku edasi ei hoia |
| `--pulse-on` | 0 s | Impulsirežiim pole vaikimisi kasutusel |
| `--pulse-off` | 0,8 s | Impulsirežiimi paus, kui see režiim on eraldi sisse lülitatud |

**Tähtis:** need on lähtekoodi vaikeseaded. Käsurea argumendid võisid tegelikus katses erineda; säilinud failid ei kinnita kõiki katse ajal kasutatud käske.

Näide ainult tööloogika selgitamiseks: kui siht on −20 kPa ja hoidmisrežiim on aktiivne, peatub imemine rõhul ≤ −20 kPa ning taastub rõhul > −18 kPa. See kirjeldab **programmi tingimusi**, mitte mõõdetud pumbatsüklit.

## 3. Säilinud mõõtmised

| Allikas | Säilinud näit | Mida saab sellest järeldada |
| --- | --- | --- |
| Lab 1/AtomS3R varasem rõhulog | Atmosfääri lähedal umbes 0,83–0,85 V, `P_abs` ligikaudu 97 kPa | Anduri algne otsemõõtmine töötas vähemalt nendes mõõtmisolukordades |
| Sama varasem logi | Imemise piirkonnas leidub näiteks `P_gauge = −26,2 … −27,0 kPa` näite | Vaakumi mõõtmine toimus; sellest ei saa ilma pumba oleku ja katseajatemplita lugeda käivitusi minutis |
| Lab 2 võimendi aruanne, esimene versioon | Täisvaakumis 0,200 V; atmosfääril umbes 0,960 V; puhumisel 3,124 V | Võimendi esimene variant mõõdeti kolmes olukorras |
| Lab 2 võimendi aruanne, parandatud versioon | Täisvaakumis 0,300 V; atmosfääril 0,963 V; puhumisel 2,800 V | Parandatud võimendi andis kasutatava pingemuutuse; samal ajal mõõdetud sisend-väljundpaare ei ole kõigis otspunktides kinnitatud |

**Logi piirang.** Failis `Tool_logs25102026.md` on pärast käivitumist `Atmospheric reference = 41.3 kPa (LOW)`. Selline tulemus ei sobi kokku varem mõõdetud ~97 kPa atmosfääriga. Üks võimalik põhjus on võimendatud pinge tõlgendamine otseanduri teisendusvalemiga, kuid täpne põhjus vajab kontrollimist. Selle faili `P_gauge` väärtustest ei tohi ilma kalibreerimist kontrollimata teha järeldusi pumba tööaja või lekke kohta.

## 4. Labor 1 ja Labor 2 juhtimise võrdlus

| Näitaja | Labor 1 / toorsignaal | Labor 2 / LM358P |
| --- | --- | --- |
| Signaalitee | MPX5700AP → AtomS3R ADC | MPX5700AP → LM358P → AtomS3R ADC |
| Signaali skaleerimine | Anduri algne väljund | Parandatud skeemi arvutuslik võimendus 1,37× |
| Näit atmosfääril | Anduril umbes 0,832–0,836 V | Võimendi väljund 0,963 V |
| Vaakumi- ja puhumisnäidud | Vt varasemaid logisid ning Lab 2 lähteandmeid | 0,300 V ja 2,800 V parandatud variandis |
| ON/OFF rõhupiirid | Käsitletud Lab 1 juhtimiskoodis; tegelikud katseargumendid taastamata | Uue signaali jaoks kasutatud piirid pole logis eraldi fikseeritud |
| Pumba käivitused minutis | Täpne mõõtetulemus pole säilinud | Täpne mõõtetulemus pole säilinud |
| Minimaalne seisuaeg | Eraldi kaitsepiirangut olemasolevas `suck_until_pressure.py` failis ei ole | Rakendamine ja katse tuleb kontrollida |
| Maksimaalne käivituste arv minutis | Eraldi piirangut olemasolevas failis ei ole | Rakendamine ja katse tuleb kontrollida |

**Teoreetiline ADC lahutusvõime:** 12-bitise 0–3,3 V ADC nominaalne pingeaste on 3,3 / 4096 ≈ 0,806 mV. MPX5700AP nimelise tundlikkuse ja ~5,06 V anduritoite korral on toorsignaali arvutuslik lahutusvõime umbes **124 Pa/ADC samm**, parandatud 1,37× astmega umbes **90 Pa/ADC samm**. Need on **arvutused**, mitte ADC tegeliku täpsuse või SNR paranemise mõõtmised. Võimendi ei vähenda automaatselt anduri enda müra.

## 5. Katseolukorrad ja seni taastamata tulemused

Meeskonna kinnitusel tehti pumbakatsed, kuid allpool toodud **mõõdikute lõppväärtusi ei saa säilinud failidest usaldusväärselt taastada**.

| Olukord | Katse eesmärk | Säilinud arvuline tulemus |
| --- | --- | --- |
| Iminapp klaasil (*napp klaasil*) | Kontrollida vaakumi tekkimist ja püsivust pärast pumba seiskamist | Hoidmisaja ja käivituste/min arvestus puudub |
| Iminapp õhus (*napp õhus*) | Kontrollida, et püsiva lekke korral ei tekiks ohtlikku lühitsüklit | Käivituste/min arvestus puudub |
| Suletud voolik (*voolik korgiga*) | Kontrollida süsteemi tihendust ja rõhu püsivust | Hoidmisaja arvestus puudub |
| Poolik haare (*poolik haare*) | Võrrelda korras ja lekkiva haarde eristamise aega toor- ja võimendatud signaaliga | Eristamise aeg sekundites mõlema konfiguratsiooni kohta puudub |

Füüsikaliselt võib eeldada, et korralikult tihendatud ühendus hoiab vaakumit kauem ja poolik haare laseb rõhul kiiremini atmosfäärirõhu suunas tõusta. **See on oodatav käitumine, mitte nendest katsetest taastatud mõõtmistulemus.**

## 6. Koodist ilmnenud piirangud ja ohutus

- `suck_until_pressure.py` ei sisalda eraldi **500 ms sideta oleku taimerit**, minimaalset pumba seisuaega ega maksimaalset käivitussageduse piirangut. Seetõttu ei saa neid kaitseid üksnes selle faili põhjal töötavaks lugeda.
- Tavalise käivitamise korral kasutatakse `--monitor-after-target 0`: programm lõpetab tegevuse pärast esimest sihtrõhuni jõudmist. Automaatne hoidmine nõuab eraldi jälgimisaega.
- `finally` haru püüab sisselülitatud imemise programmist väljumisel peatada; ühendusvea korral ei saa selle põhjal garanteerida, et füüsiline pump kindlasti seiskus.
- AtomS3R ADC sisendile ei tohi anda rohkem kui **3,3 V**. LM358P töötab 5 V toitega, mistõttu tuleb väljund enne ADC ühendamist ja pärast ühenduste muutmist mõõta.
- Pooliku haarde katset ja klaasi tõstmist ei tohi käsitada tõstmiseks ohutu haarde tõendina enne, kui rõhu püsimise kontroll ja tõrke korral ohutusse olekusse minek on päriselt katsetatud.

## 7. Kokkuvõte

Laboris 2 ehitati ja mõõdeti MPX5700AP signaali jaoks kaks LM358P võimendusahela versiooni. Meeskonna varasemates failides on olemas pumba juhtimise Pythoni programm, AtomS3R rõhumõõtmise kood ja rõhulogid. Nende põhjal saab taastada ühendused, olemasoleva juhtimisloogika ning mitmeid mõõdetud rõhu- ja pingeväärtusi.

**Täpseid käivitusi minutis, minimaalset seisuaega, lekke eristamise aega ja Lab 2 samaaegset `raw`/`opamp` võrdlust ei olnud säilinud andmetes.** Need jäetakse ausalt dokumenteerimata mõõtetulemustena, mitte ei asendata oletuslike arvudega. Käesolev fail aitab olemasolevat tööd kaitsmiseks lahti seletada ja näitab selgelt, milline tõendus vajab täiendamist.
