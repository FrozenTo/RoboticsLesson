# Andmehõive Labor 2 — eraldi AtomS3R 100 Hz püsivara

**See ei asenda ega muuda Nutilahendused Labor 1 programmi.** Failid on üksnes `Data-Aq/lab2/src/atom_pressure_100hz/` sees. Füüsilise seadmega ei ole uut püsivara veel kompileeritud ega mõõdetud.

## Mis muutub

- Mõõtmine toimub `micros()` ajastiga kavandatud **10 ms intervalliga (100 Hz)**, mitte 12 näidu keskmisena koos 500 ms pausiga. Tegelik sagedus ning jadaliidese kaod tuleb riistvaraga mõõta.
- `DATA,t_ms,seq,config,adc,voltage_mv,p_abs_kpa,p_gauge_kpa,cal_ok` väljastatakse igal proovivõtuhetkel (kahekanalilises režiimis kaks rida ühe järjestusnumbri kohta).
- `raw`: MPX5700AP väljundi otsene mõõtmine; `opamp`: parandatud LM358P skeemi väljund, pöördteisendus **Rf=37 kΩ, Rg=100 kΩ, Vref=0,467 V**.
- Rõhu nullimiseks mõõdetakse pärast alustamist **50 lugemit**, eeldusel, et pump on välja lülitatud ja andur näeb atmosfäärirõhku. Kui arvutatud atmosfäär ei jää vahemikku 80–110 kPa, on `cal_ok=0` ning rõhuväärtusi ei tohi lugeda kehtivateks.
- Säilitatud on `GET_CHAR`, `CHAR=`, `PRINT=` protokoll ja lühike/kahekordne/pikk nupuvajutus koos Preferences salvestusega. Ekraani uuendatakse harvemini, et 100 Hz väljastamist vähem takistada.
- **Ei ole automaatset pumbajuhtimist** ega tõrkeohutuse garantiid. Vanad pumbaskriptid on eraldi ega muutu.

## Ühendused enne esimest katset

`platformio.ini` määrab `RAW_ADC_PIN=5` ja `OPAMP_ADC_PIN=-1`.

**Üks kanal:** senine GPIO5 saab ühenduse vastavalt füüsilisele katserežiimile kas toore anduri väljundilt (`CONFIG RAW`) või parandatud võimendi väljundilt (`CONFIG OPAMP`). Ära ühenda kahte väljundit ühe viigu külge. Ühenda vool välja enne juhtmete ümbertõstmist.

**Kaks kanalit:** `CONFIG DUAL` on **vaikimisi keelatud**. Selle lubamiseks tuleb esmalt kontrollida AtomS3R dokumentatsioonist ja reaalselt mõõta **teine vaba ADC-võimeline viik**, määrata selle number `OPAMP_ADC_PIN`-na ning ühendada mõlemad väljundid eraldi viikudele ühise GND-ga. Kaks kanalit loetakse järjestikku ühe 10 ms tsükli jooksul, mitte täpselt samal hetkel. Võrdlustesti puhul kontrolli tegelik ajanihe.

**Ohutus:** Atomi ADC viigule ei tohi anda üle **3,3 V**. LM358P töötab 5 V toitega; viga, halb kontakt või vale potentsiomeetri asend võib anda lubamatult kõrge pinge. Enne Atomi ühendamist mõõda mõlemad väljundid multimeetriga läbi kavandatud rõhuvahemiku ja kasuta vajadusel eraldi piiramist/kaitset. Ära eelda, et tarkvaraline kontroll kaitseb viiku füüsilise ülepinge eest.

## Koostamine ja käsud

```powershell
# Data-Aq/lab2 juurest, kui PlatformIO on arvutis olemas:
pio run -d src/atom_pressure_100hz
pio run -d src/atom_pressure_100hz -t upload
```

Firmware'i jadaliidese kiirus on **230400 baud**. Kui see on käivitatud ning **pump on OFF**, saab serial monitorile saata:

```text
STATUS
CONFIG RAW
CONFIG OPAMP
CAL
GET_CHAR
```

Iga `CONFIG` muutus alustab rõhu baasväärtuse kalibreerimist uuesti; **ära vaheta konfiguratsiooni nime ilma vastava füüsilise ühenduseta**. `CONFIG DUAL` annab vea, kuni teine viik on paigaldatud ja kinnitatud. `READY,...cal_ok=1` ja `STATUS` aitavad kontrollida käivitust.

## CSV salvestamine

Uus CSV-logija on [`../capture_100hz.py`](../capture_100hz.py) (paigalda `pyserial`).

```powershell
python src/capture_100hz.py --port COM4 --expect-config raw --trial-id raw_01 --phase unknown --duration 30 --output data/raw_01.csv
```

`--expect-config` peab vastama tegelikule mõõteahelale. `t_ms` pärineb AtomS3R tarkvarast, mitte arvuti kellaajast. `trial_id` ja `phase` määratakse käsitsi; neid ei tohi nimetada automaatselt mõõdetud omadusteks. `pump_state` jääb tühjaks, kuni päris DO oleku salvestamine on eraldi tehtud.

**Kontroll:** 10 sekundi stabiilses testis peab olema ligikaudu 1000 järjestikust mõõtetakti, `t_ms` vahed ligikaudu 10 ms ning `STATUS`-s `missed_intervals=0` või selgitatud kõrvalekalle. USB või monitori ühendus võib tekitada kadusid, mistõttu loenda ka `seq` lünki. See on katse **eesmärk**, mitte kinnitatud tulemus.

**Oluline:** olemasolev [`log_serial_lab2.py`](../log_serial_lab2.py) kuulub **vanale tekstiprotokollile** ja ei loe uusi `DATA` ridu; uue püsivaraga kasuta ainult `capture_100hz.py`.
