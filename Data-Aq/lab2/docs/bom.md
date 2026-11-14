# Andmehõive — Labor 2: komponentide loend (BOM)

**Labor:** Op-amp, lihtne aga keeruline  
**Katsete kuupäevad:** 24.–25.10.2026  
**Dokumendi koostamine:** 14.11.2026  
**Alus:** [Lab 2 mõõtmisaruanne](Lab2_aruande.md), [arenduspäevik](development-log.md) ja [Labor 1 vahendite kirjeldus](../../lab1/README.md).

## 1. Eesmärk

BOM (*Bill of Materials*) on katsetes kasutatud komponentide ning järgmiste katsete jaoks vajalike vahendite loend. Laboris 2 ehitasime MPX5700AP rõhuanduri signaali jaoks LM358P operatsioonivõimendi astme, et kasutada AtomS3R ADC sisendvahemikku paremini.

Allolev loend on **tagantjärele koostatud tegeliku prototüübi dokumentatsioon**, mitte tõend selle kohta, et ostutellimus esitati 16.10.2026. Aruannetes ei ole kinnitatud tarnijaid, hindu ega ostutellimuse numbrit; neid andmeid ei ole välja mõeldud.

## 2. Prototüübis kasutatud elektroonikakomponendid

| Komponent | Kogus prototüübis | Milleks seda vaja oli | Staatus |
| --- | ---: | --- | --- |
| MPX5700AP absoluutrõhuandur | 1 | Mõõdab pumbasüsteemi rõhku ja annab võimendile analoogpinge. | Kasutatud ja mõõdetud |
| LM358P, kahe operatsioonivõimendiga mikroskeem | 1 | Teisendab rõhuanduri väljundpinge ADC jaoks sobivamasse vahemikku. | Kasutatud ja mõõdetud |
| B100K potentsiomeeter, 100 kΩ | 1 | Võimaldab seada võimendusahela võrdluspinget. | Kasutatud; 0,590 V ja 0,467 V |
| Takisti 100 kΩ | 1 | Ühendab võrdluspinge LM358P pöördsisendiga ja määrab koos tagasisidetakistiga võimenduse. | Kasutatud mõlemas variandis |
| Takisti 51 kΩ | 1 | Moodustas koos 10 kΩ takistiga esimese variandi 61 kΩ tagasisidetakistuse. | Kasutatud esimeses variandis |
| Takisti 27 kΩ | 1 | Asendas paranduse ajal 51 kΩ takisti, andes koos 10 kΩ takistiga 37 kΩ tagasisidetakistuse. | Kasutatud parandatud variandis |
| Takisti 10 kΩ | 1 | Oli tagasisideahelas koos 51 kΩ või 27 kΩ takistiga. | Kasutatud mõlemas variandis |
| AtomS3R mikrokontroller | 1 | Andis prototüübile 5 V ja GND ühendused ning võimaldab mõõta signaali ADC abil. | Kasutatud |
| Makettplaat (*breadboard*) | 1 | Võimaldas katsetada ja parandada ühendusi ilma jootmiseta. | Kasutatud |
| Ühendusjuhtmed | Kogus täpsustamata | Ühendasid anduri, LM358P, takistid, potentsiomeetri ja toite. | Kasutatud; täpne arv dokumenteerimata |

**Märkus versioonide kohta:** esimesel variandil oli tagasiside takistus 51 + 10 = **61 kΩ** ja arvutuslik võimendus **1,61×**. Parandatud variandil oli tagasiside takistus 27 + 10 = **37 kΩ** ja arvutuslik võimendus **1,37×**. Neid variante katsetati järjest; tabeli koguseid ei tohi liita kahe samaaegselt vajaliku komplektina.

## 3. Mõõtevahendid ja süsteemi ülejäänud osad

| Vahend | Milleks seda vaja on | Lab 2 tõendatud seis |
| --- | --- | --- |
| Multimeeter | Kontrollib 5 V toidet, võrdluspinget ning anduri ja võimendi väljundpinget. | Kasutatud; LM358P toide 5,01 V |
| Kahe kanaliga ostsilloskoop | Näitab anduri toorsignaali ja võimendi väljundit sama pumba impulsi ajal. | Nõutud; samaaegne mõõtepilt tuleb veel tõendada |
| Arvuti, USB-C ühendus ja logimistarkvara | Loeb AtomS3R mõõtmisi ning salvestab need edasiseks analüüsiks. | Tarkvara ja logid asuvad repos; Lab 2 võrdlus-CSV vajab kontrolli |
| Dobot MG400 ja pumbakast | Võimaldavad mõõta rõhku imemise ning puhumise ajal ja katsetada pumba juhtimist. | Labor 1 süsteemi osa; Lab 2 lõppkatsed vajavad eraldi kinnitust |
| 4 mm pneumovoolik ja T-liitmik | Ühendavad rõhuanduri pumba ning iminapa rõhuliiniga. | Labor 1 vahendite hulgas; tegelik kogus kontrollida |
| Iminapp ning polükarbonaatklaas | On vajalikud korraliku ja pooliku haarde võrdluskatseks. | Labor 1 vahendite hulgas; Lab 2 pooliku haarde katse tõendamata |

Falstad on simulatsioonitarkvara, mitte ostetav elektroonikakomponent; simulatsiooni pildid on kaustas [images/](images/).

## 4. Tellimisvajadus ja põhjendus

Ülesande järgi pidi meeskond koostama puuduolevate osade tellimuse **16.10.2026**. Olemasolevad aruanded kinnitavad, et loetletud elektroonikakomponentidega ehitati ja testiti prototüüp, kuid **ei kinnita, kas osad võeti labori riiulilt, telliti juurde või kui palju neid laos alles on**.

Seetõttu ei saa tagantjärele ausalt märkida ühtegi neist osadest 16.10 esitatud ostutellimusena. Enne uut tellimust tuleb üle kontrollida:

- kas jätkukatseteks on olemas vähemalt üks töökorras LM358P ja MPX5700AP;
- kas 100 kΩ, 51 kΩ, 27 kΩ ja 10 kΩ takistid ning B100K potentsiomeeter on alles;
- kas pneumovoolikut, T-liitmikke, ühendusjuhtmeid ja iminappasid on katseteks piisavalt;
- kas kahel kanalil mõõtev ostsilloskoop ning MG400 pumbakast on katse ajal saadaval.

**Tellimus 16.10.2026:** dokumenteeritud osturidu ei leitud.  
**Tarnijad, tootenumbrid, hinnad ja tegelik tellitud kogus:** ei ole allikates kirjas.  
**Otsus:** prototüübi jaoks kasutatud osad on dokumenteeritud; uue ostutellimuse vajadus tuleb määrata pärast olemasolevate osade kontrolli.

## 5. Seos mõõtmistulemustega ja ohutus

Prototüübi esimese variandi mõõdetud väljundpinge oli täisvaakumis **0,200 V** ja puhumisel **3,124 V**; parandatud variandil vastavalt **0,300 V** ja **2,800 V**. Need tulemused on kirjas [mõõtmisaruandes](Lab2_aruande.md).

**Ohutus:** LM358P saab 5 V toite, kuid AtomS3R ADC sisendile ei tohi anda üle **3,3 V**. Enne ADC ühendamist ja pärast iga takisti või võrdluspinge muutmist tuleb võimendi väljund mõõta multimeetriga. Elektriühendusi muudetakse ainult väljalülitatud toitega; MG400 pumbakasti 24 V ühendusi ei muudeta töötava roboti juures.
