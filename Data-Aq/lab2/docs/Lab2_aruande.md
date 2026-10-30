ANDMEHÕIVE · LABOR 2

Operatsioonivõimendi aste rõhuandurile MPX5700AP

Töö kuupäevad: 24.–25.10.2026     |     Meeskonnatöö     |     Mõõtelogid: eraldi CSV-failis

## Eesmärk ja lähteandmed

Eesmärk oli teisendada MPX5700AP anduri väljundpinge operatsioonivõimendi LM358P abil AtomS3R ADC jaoks sobivamasse vahemikku. Kasutasime Labor 1 mõõtmistel põhinevat sisendvahemikku umbes 0,345–2,30 V, mitte ülesande näidisvahemikku. Esimese versiooni siht oli 0,20–3,30 V; pärast parandust 0,30–3,00 V.

## Makettplaadi ühendamine ja kontroll

Paigaldasime LM358P makettplaadi keskvahe kohale (väljund pin 1: E11; pöördsisend pin 2: E12; mittepöördsisend pin 3: E13; GND pin 4: E14; toide pin 8: F11). Toiteks kasutasime AtomS3R 5 V ja GND kontakte ning ühiseid toiterööpaid. Mõõtsime toitepingeks 5,01 V. B100K potentsiomeetri paigaldasime J20/J22/J24 ridadele; selle keskkontaktiga seadsime võrdluspinge. Anduri paigaldasime A1–A6: pin 1 väljund, pin 2 GND, pin 3 +5 V. Anduri väljundi ühendasime LM358P pin 3-ga. LM358P väljundit mõõtsime multimeetriga D11 juures.

## Võimendusahela arvutus

Kasutasime mitteinverteerivat võimendit, mille pöördsisendile jõuab võrdluspinge läbi 100 kΩ takisti ja väljundist tagasiside läbi Rf. Seos: Uväl = (1 + Rf / 100 kΩ) · Uandur − (Rf / 100 kΩ) · Uref.

| Näitaja | Esimene variant | Parandatud variant |

| --- | --- | --- |

| Tagasisidetakistid | 51 + 10 = 61 kΩ | 27 + 10 = 37 kΩ |

| Arvutuslik võimendus | 1,61× | 1,37× |

| B100K võrdluspinge | 0,590 V | 0,467 V |

| Sihitud väljundvahemik | 0,20–3,30 V | 0,30–3,00 V |

## Mõõtmistulemused

| Rõhuolukord | 1. versioon: väljund | 2. versioon: väljund |

| --- | --- | --- |

| Täisvaakum | 0,200 V | 0,300 V |

| Atmosfäärirõhk | u 0,960 V | 0,963 V |

| Puhumine | 3,124 V | 2,800 V |

Lisaks mõõtsime atmosfäärirõhul anduri pingeks 0,832–0,836 V ning hilisema puhumiskatse ajal 2,208 V. Viimast väärtust ja võimendi 2,800 V näitu ei mõõdetud samaaegselt, seetõttu ei saa nende erinevusest täpset veahinnangut teha.

## Katse käik, probleemid ja järeldus

Kontrollisime B100K tööd: selle väljund oli pööramisega muudetav ligikaudu 0–5 V. Võimendi väljund muutus samuti. Ühel hetkel langes väljund ootamatult 0,590 V-ni; põhjuseks osutus osaliselt pesast välja tulnud juhe. Pärast ühenduse parandamist taastus näit umbes 0,96 V-ni. Esimese variandi ülemises otsas saime 3,124 V, mis jäi alla 3,30 V sihi. Paranduseks vahetasime 51 kΩ takisti 27 kΩ vastu ja muutsime võrdluspinge 0,467 V-ni. Uue variandiga saime vaakumis 0,300 V ning puhumisel 2,800 V. See näitab, et aste töötab ja järgib suures osas arvutust; 3,00 V ülemise piiri täpset saavutamist ei ole veel kinnitatud samaaegsete sisend-väljundmõõtmistega.

Andmesalvestus AtomS3R kaudu tehti eraldi; toor- ja võimendatud signaali logifailid ning edasine spektri/SNR analüüs lisatakse eraldi. ADC sisendi lubatud pinge ei tohi ületada 3,3 V; seda tuleb jälgida ka järgmistes katsetes.

Kokkuvõte: valmistasime ja testisime päris komponentidega kaks võimendi versiooni, mõõtsime kolme rõhuolukorda, leidsime kontaktivea ning kohandasime ahela 0,3–3,0 V sihtvahemikule.
