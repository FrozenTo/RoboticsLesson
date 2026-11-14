# Andmehõive — Labor 2: kahekanalilised ostsilloskoobimõõtmised

**Kuupäev:** 14.11.2026  
**Seade:** GW Instek GDS-1072A-U, digitaalne salvestav ostsilloskoop  
**Uuritav ahel:** MPX5700AP rõhuandur ja LM358 operatsioonivõimendi, AtomS3R 5 V toide  
**Tõendus:** meeskonnaliikme tehtud kuus päris ekraanifotot (kõik pärinevad samast mõõtmissessioonist).

## Eesmärk

Jälgida rõhu muutumisel samaaegselt kahte pingesignaali ja kontrollida, kas signaalitöötluse aste reageerib anduriga kooskõlas. CH1 on ekraanil **kollane**, CH2 **helesinine**. Varasemas töökorralduses paigutati CH1 LM358 väljundile ja CH2 anduri toorväljundile, kuid enne täpset võimendusteguri arvutamist tuleb füüsilised ühenduskohad ja mõlema sondi attenuatsioon uuesti kinnitada.

## Katse tähelepanekud

- Rõhu suurenemisel tõusevad mõlema kanali jäljed. Viimasest kahest fotost esimesel on näha tõusev üleminek ja stabiilsem platoo.
- Rõhu vähenemisel langevad mõlemad jäljed. Viimasest kahest fotost teisel on näha langev üleminek ja uus platoo.
- Fotodel on ajabaas **500 ms/div**, ROLL-režiim. Vertikaalskaalad on fotoseerias muutunud. Seetõttu ei tohi eri kaadrite jälgede kõrgusi ilma skaalasid arvestamata otse võrrelda.
- Osa kaadrite CH1 lainekuju väljub nähtavalt ekraani ülaservast; see **ei tõesta** elektroonilise võimendi küllastumist, sest tegemist võib olla ka kuva skaalapiiriga.

## Oststilloskoobi ekraanilt loetud pinged

| Kuvatav suurus | CH1 (kollane) | CH2 (sinine) |
| --- | ---: | ---: |
| Vmax | 2,64 V | 1,89 V |
| Vmin | 0,00 V | 0,60 V |
| Vpp | 2,64 V | 1,29 V |

**Allikas:** fotoseeria kuues (viimane) kaader. Need on oskilloskoobi *ekraanil kuvatud* automatiseeritud mõõdud üle nähtava ajavahemiku; maksimaalse ja minimaalse taseme esinemise hetk ei pruugi kattuda. Näiteks **2,64 / 1,29 ≈ 2,05** on kuvatud Vpp-de suhe, **mitte** kinnitatud LM358 võimendustegur. Parandatud skeemi varasem arvutuslik võimendus on **1,37×**, mille väärtusega ei saa seda suhtarvu ilma sondi- ja mõõtepunktide kontrollita samastada.

## Fotoseeria

Saadud kaadrite järjestus (originaalide nimed kasutaja saadetud failidel):

1. `1000017419.jpg` — tõus, CH2 Vmax 1,22 V; CH1 ülemine osa väljub kuvast.
2. `1000017420.jpg` — langus, CH2 Vpp ligikaudu 1,01 V; CH1 ülemine osa väljub kuvast.
3. `1000017421.jpg` — väike tõus, ekraanil Vmax CH1 2,40 V ja CH2 2,00 V.
4. `1000017422.jpg` — langus, ekraanil Vpp CH1 3,20 V ja CH2 1,59 V.
5. `1000017423.jpg` — hästi nähtav tõus ja stabiliseerumine (kasulik näidisfoto).
6. `1000017424.jpg` — hästi nähtav langus ja stabiliseerumine; automaatmõõtmiste tabel pärineb sellest kaadrist.


## Mõõtmise piirangud ja ohutus

1. Sondide lüliti 1×/10× ja ostsilloskoobi vastava CH1/CH2 menüü väärtuse omavaheline vastavus on kontrollimata; CH2 menüüs esines katse käigus ka **Voltage 5X**. Seega ei saa nendest piltidest üksi kinnitada absoluutpinge täpsust ega võimendust.
2. Fotodel puudub rõhu paralleelne kPa-ajatempel ja pumba DO oleku logi. Nende alusel ei saa arvutada pumba käivituste arvu minutis ega lekke eristamise aega.
3. Need kaadripildid ei sisalda 100 Hz andmeridu iga impulsi kohta ega vähemalt **30 + 30** `raw/opamp` katset. Seetõttu ei tohi nende põhjal esitada mõõdetud FFT-d, spektrite erinevust või SNR-i.
4. Kuna LM358 saab toite 5 V-st, ei tohi väljundit ühendada AtomS3R G5 ADC sisendisse, enne kui on kinnitatud, et pinge **ei ületa üheski katseseisundis 3,3 V**. Ostsilloskoobi katse ajal oli G5 lahti ühendatud.

## Kokkuvõte

Kahekanaliline ostsilloskoobivaatlus kinnitab kahe nähtava elektrilise signaali reageerimist rõhumuutustele. Sisendi-väljundi võrdlus on kvalitatiivselt dokumenteeritud, kuid arvulise võimenduse, ADC ohutuse kogu rõhuvahemikus ning laboriülesande SNR-i tõendamiseks on tarvis täiendavat kinnitust. Varasemaid mõõteloge ja falstadi võrdlusandmeid selle sissekandega ei muudeta.
