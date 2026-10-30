Arenduspäevik – Labor 2: Rõhuanduri signaali võimendamine

Kuupäev: 24.10.2026
Õppeaine: Andmehõive
Teema: MPX5700AP rõhuanduri signaali võimendamine LM358N operatsioonivõimendiga

Töö eesmärk

Laboritöö eesmärk oli koostada analoogsignaali võimendamise skeem, mis võimaldaks MPX5700AP rõhuanduri väljundpinget paremini kasutada AtomS3R mikrokontrolleri 3,3 V analoogsisendiga. Soovisime vähendada signaali nihkepinge mõju ja suurendada mõõtmiseks kasutatavat pingevahemikku.

Töö käik

Alustasime LM358N operatsioonivõimendi paigaldamisest makettplaadile. Ühendasime mikroskeemi AtomS3R toiteallikaga ning kontrollisime multimeetriga, et toitepinge oleks 5 V.

Seejärel ühendasime MPX5700AP rõhuanduri. Anduri toiteklemmile ühendasime 5 V, maanduse ühendasime ühise GND-ga ning väljundsignaali suunasime operatsioonivõimendi sisendisse.

Signaali võimendamiseks kasutasime 10 kΩ ja 27 kΩ takisteid. Koostasime tagasisideahela ning ühendasime anduri signaali võimendi mitteinverteeriva sisendiga takistite kaudu.

Järgmisena ehitasime võrdluspinge jaguri. Kasutasime kolme takistit: 100 kΩ, 51 kΩ ja 10 kΩ. Nende abil saime 5 V toitepingest ligikaudu 0,311 V võrdluspinge.

Mõõtmised ja tulemused

Kontrollisime ühendusi ja mõõtsime erinevates punktides pinget ning takistust.

| Mõõdetud suurus | Tulemus |

| --- | --- |

| LM358N toitepinge | 5,0 V |

| MPX5700AP väljundpinge | 0,83 V |

| Võrdluspinge ilma koormuseta | 0,311 V |

| Võrdluspinge pärast ühendamist | 0,50 V |

| LM358N sisendpinge (+) | 0,70 V |

| LM358N sisendpinge (−) | 0,70 V |

| LM358N väljundpinge | 0,019–1,25 V |

| 10 kΩ takisti mõõdetud väärtus | 9,82–9,86 kΩ |

| 27 kΩ takisti mõõdetud väärtus | 26,52–26,66 kΩ |

Mõõtmiste käigus selgus, et andur töötas ja andis korrektset väljundpinget. Ka takistite väärtused olid ootuspärased. Probleem tekkis operatsioonivõimendi ühenduste ja võrdluspinge stabiilsusega.

Probleemid ja lahenduste otsimine

Skeemi koostamise ajal muutsime mitu korda juhtmete ja takistite asukohti. Alguses oli anduri väljund ühendatud vale võimendisisendiga. Pärast selle parandamist tekkisid probleemid võimenduse ja võrdluspingega.

Märkasime, et võrdluspinge muutus koormuse ühendamisel 0,311 V-lt 0,50 V-ni. Proovisime probleemi lahendada LM358N teise operatsioonivõimendi kasutamisega pingepuhvrina. Selleks ühendasime mikroskeemi klemmid 6 ja 7 ning suunasime võrdluspinge klemmile 5.

Ühenduste muutmise käigus katkes aga pingejaguri maandusühendus. Selle tulemusena langes mõõdetud võrdluspinge 0 V-ni. Edasised parandused muutsid skeemi järjest keerulisemaks ning kõigi ühenduste kontrollimine muutus raskeks.

Kokkuvõte ja edasine tegevus

Laboritöö käigus õppisime kasutama makettplaati, ühendama operatsioonivõimendit ja rõhuandurit ning mõõtma pingeid ja takistusi multimeetriga. Saime praktiliselt teada, kui oluline on ühine maandus, õige tagasisideühendus ja stabiilne võrdluspinge.

Lõpptulemusena ei õnnestunud meil koostada usaldusväärselt töötavat võimendusskeemi. Mitmete ümberühenduste ja juhiste käigus tekkis segadus ning me ei saanud enam kindlad olla kogu skeemi õigsuses.

Seetõttu otsustasime alustada skeemi koostamist uuesti nullist. Järgmisel korral kontrollime esmalt kogu elektriskeemi, määrame kindlaks komponentide asukohad ja ühendame need järjest, kontrollides iga etappi multimeetriga.

Seekordne töö oli kasulik praktiline kogemus, mis näitas, et elektroonikas on süsteemne töökorraldus ja täpne dokumenteerimine sama olulised kui komponentide ühendamine.
