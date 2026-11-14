# Andmehõive — Labor 3 kontrollnimekiri

**Alus:** [õppejõu originaalne laboriülesanne](docs/assignment_original.md).  
**Seisuga 14.11.2026:** allpool ükski füüsiline nõue ei ole repo tõendusmaterjaliga kinnitatud. Ruudud on seetõttu märkimata. Valmis mall või kood **ei ole mõõdetud tulemus**.

## 1. Klapp, taimer, UV LED

- [ ] Klapi 3/2 asend on multimeetriga ja pneumaatiliselt kontrollitud: vooluta süstal õhku, pump eraldatud.
- [ ] Klapi mähise pinge/vool, relee kontaktide lubatud DC koormus ning kaitsediood kontrollitud; skeem olemas.
- [ ] Riistvarataimer lülitab klapi välja, viie impulsi pikkuse võrdlus kümne kordusega (käsk, Atomi viik, klapi mähis).
- [ ] Relee sisse-/väljalülituse viivitus, kontaktipõrge ja eluea arvutus dokumenteeritud.
- [ ] UV LED juhtimine draiveriga ja iseseisev ajaline väljalülitus kontrollitud; ohutuskate ning prillid olemas.
- [ ] Anduri asukoht voolikus valitud ja põhjendatud; klapi väljalülitumisel rõhu kadumine kinnitatud.

## 2. Tilk ja kaamera

- [ ] Vähemalt viis impulsi pikkust × 10 tilka; iga tilga rõhukõver salvestatud ning `data/drops.csv` täidetud.
- [ ] Teine muutuja (otsik või rõhk) testitud kolme impulsi pikkusega.
- [ ] Prinditud mõõtkavaga tilgaplaadid ja vahetükid; kaamera kalibreeritud mm/piksel; kontuuripildid olemas.
- [ ] Atomi ekraanipoole mõõtude järgi mudelid; `data/placement.csv` koos x/y nihete ja pindaladega.
- [ ] `docs/recipe.md` sisaldab kinnitatud otsikut, rõhku, impulssi, UV aega ning mudelile liimitud klaasi katset.

## 3. Filtreerimine ja dP/dt

- [ ] Kontrollitud 100 Hz rõhukõverate ajatelg ning kalibreeritud rõhk kPa-des olemas.
- [ ] Arvutatud toores dP/dt, filtreeritud dP/dt, spektrid (fft/PSD) ning võrreldud libisevat keskmist ja mediaani.
- [ ] Filtri müra ja viivitus mõõdetud, lõplik filter valitud kahe arvulise põhjendusega.
- [ ] Labor 2 pooliku haarde pärislogi põhjal leitud dP/dt lävi ja otsuse aeg; kui logi puudub, puudus välja toodud.
- [ ] Normaalse tilga, kinnise otsiku ja tühja süstla rõhukõverad ning eristav tunnus numbritega.

## 4. Komparaator ja IRQ

- [ ] Falstadi skeemis komparaatori lävi ja hüsterees tõendatud kolme sisendiga (normaalne, kinnine, müra).
- [ ] Füüsilise komparaatori kõrge väljund on enne Atom GPIO ühendust kontrollitud (mitte üle 3,3 V).
- [ ] IRQ sulgeb klapi ja lukustab alarmi; uus dispense keeldub kuni `clear` käsuni; sündmus väljastatakse.
- [ ] `docs/latency.csv`: 10× IRQ, 10× polling ja põhitsükli koormusega võrdlus, mõõdetud mähiselt.
- [ ] 10 kinnise otsiku katset, 10 tühja süstla katset ja 30 normaalse tilga valehäirekatset.

## 5. Dokumentatsioon, tarvikud ja kaitsmine

- [ ] `docs/bom.md` kontrollitud ja tegeliku 06.11 tellimuse esitamise seis tõendatud (kuupäev on juba möödunud).
- [ ] `docs/development-log.md` täiendatud pärast iga päris töösessiooni, kus on numbrid ja põhjused.
- [ ] Vajalikud `src/`, `data/`, `notebooks/`, `docs/`, `README.md`, Falstadi eksport, foto- ja ostsilloskoobitõendid olemas.
- [ ] Pumbajuhtimise seosed [Labor 2 dokumendiga](../lab2/docs/pump_control.md) läbi kontrollitud.
- [ ] Kaitsmise demo ja Git tag `data-acquisition-lab3` valmis.

**Esimene kaitsmine:** 19.11.2026 veebis. **Hindamine:** 5 p tööfailid, 5 p analüüs, 5 p prototüüp, 5 p dokumentatsioon.
