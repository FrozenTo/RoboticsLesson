# Andmehõive Labor 2 — üleandmine 14.11.2026 (CSV logimine)

**Jätkamise koht:** 100 Hz CSV logija USB-proov töötab; järgmine samm on kontrollida kohalikku CSV-d ning valmistada ette **ohutud pärisandmete** mõõtmised (raw ja opamp). See dokument kirjeldab 14.11.2026 tööseanssi, mitte lõplikke katsetulemusi.

## Täna tehtud

1. AtomS3R Arduino IDE-s: ESP32 by Espressif Systems paigaldatud; kasutati ESP32S3 Dev Module / COM4. **Uut püsivara EI laaditud** (säilitati olemasolev programm).
2. Serial Monitoris nähti kirjeid kujul `DATA,t_ms,seq,config,adc,voltage_mv,p_abs_kpa,p_gauge_kpa,cal_ok`, nt `DATA,122287,12064,raw,22,0,-31.109,nan,0`. Seade saatis ligikaudu iga 10 ms järel. Märkus: G5 oli mõõteseadme küljest lahti, seega need ei ole kehtivad rõhumõõtmised.
3. Arvutis `python -m pip install pyserial` → **pyserial 3.5**, Python 3.14 kasutajapaigaldus.
4. COM-portide kontroll: **COM4**, Espressif USB `VID:PID=303A:1001`; COM3 on Intel AMT SOL, seda ei kasutata.
5. `python -m serial.tools.miniterm COM4 230400` näitas `DATA` ridu. Samuti toimis lihtne Python-proov: `serial.Serial('COM4',230400,timeout=2)` ja `readline()`.
6. Olemasolev `src/capture_100hz.py` andis esialgu `ClearCommError failed (PermissionError(13, 'The device does not recognize the command.', None, 22))`. Probleem ilmnes nii 115200 kui 230400 baud juures; ühendus ise töötas.
7. **Kohalikus VS Code failis** `Data-Aq/lab2/src/capture_100hz.py` asendati:
   ```python
   with serial.Serial(args.port, args.baud, timeout=0.2, dsrdtr=False, rtscts=False) as port:
       port.dtr = False
       port.rts = False
   ```
   järgmisega:
   ```python
   with serial.Serial(args.port, args.baud, timeout=2) as port:
   ```
   Kasutaja kinnitas seejärel rõõmsalt, et CSV test **õnnestus**. Viimati käivitatud käsk:
   ```powershell
   python Data-Aq/lab2/src/capture_100hz.py --port COM4 --baud 230400 --expect-config raw --trial-id usb_test_04 --phase unknown --duration 5 --output Data-Aq/lab2/logs/usb_test_04.csv
   ```
   **Täpne salvestatud ridade arv ei ole vestluses fikseeritud.** Kontrolli kohalikku faili ja väljundit; testfaili ei tohi käsitleda tegeliku rõhu ega SNR-i mõõtmisena.

## Oluline: kohalik muudatus vs GitHub

- **Tänase töö logi on GitHubis siin dokumendis.**
- `src/capture_100hz.py` **parandus tehti kasutaja lokaalses töökaustas `C:\RoboticsLesson`**, mitte GitHubi kaudu. Selle faili GitHubi versioonis võivad veel olla vanad DTR/RTS käsud. Enne `git pull` / sünkroonimist kontrolli `git status` ja võrdle diff'i; **ära kirjuta kohalikku töötavat muudatust üle**.
- `logs/usb_test_04.csv` asub **lokaalselt**, kui fail tekkis edukalt. Seda pole siinse dokumentatsiooni loomisega GitHubi üles laaditud.
- Sama nimega CSV-d logija ei kirjuta üle (`Refusing to replace existing data`). Järgmise proovi korral kasuta uut nime. Sulge Arduino IDE Serial Monitor ja miniterm enne Pythoniga COM4 avamist.
- Ära pühenda katse-CSV-d pärisandmete hulka ega arvuta sellest SNR-i.

## Elektriline olukord ja ohutus

- Töötav MPX5700AP + LM358 võimendiahel on makettplaadil olemas; 14.11 tehti kahekanalilised ostsilloskoobifotod. Vaata `docs/oscilloscope_2026-11-14.md`.
- **AtomS3R G5 juhe jäeti lahti!** Seepärast tähis `raw` väljuvas DATA-s on püsivara konfiguratsiooninimi, **mitte tõend tegelikust ühendatud andurisignaalist**.
- LM358 töötab 5 V pealt; **ära ühenda võimendi väljundit G5 ADC-ga enne, kui on kontrollitud, et sisendi pinge püsib igas katseolukorras ohutult 0…3,3 V vahemikus**. Vajadusel tuleb projekteerida sobiv kaitse/skaleerimine. Muuda juhtmeid ainult väljalülitatud toitega.
- 24 V pumbaklappi ei ühendatud selle CSV-testi käigus. Ära sega 24 V pumba juhtimist Atomi ADC sisendiga.

## Järgmise töökorra sammud

1. Ava `C:\RoboticsLesson` VS Code'is ja vaata `git status` ning `git diff -- Data-Aq/lab2/src/capture_100hz.py`; säilita töötav lokaalne parandus ja loo sellele eraldi commit, kui see on üle kontrollitud.
2. Kontrolli kohalikku `Data-Aq/lab2/logs/usb_test_04.csv`: mitu rida, kas `t_ms` vahed on ~10 ms ja `config` sisaldab `raw`; märgista prooviandmed **invalid/disconnected ADC**. Vajadusel tee eraldi puhas ühendustest.
3. Enne päris mõõtmisi määra ning dokumenteeri Atomi ADC füüsiline sisend ja mõlema konfiguratsiooni tegelik ühendus; kontrolli LM358 väljundpinget multimeetriga, nii et **G5 ei saaks üle 3,3 V**. Alles pärast seda ühenda ja kogu päris mõõtmised.
4. Salvestada Labor 2 nõude järgi sama pumba tingimustega **vähemalt 30 impulssi raw- ja 30 opamp-konfiguratsioonis**, ajatemplite ja õigete `config` väärtustega. Ära nimeta lahtist G5-proovi päris `raw` andmeteks. Säilita algsed CSV-d muutmata.
5. Arvuta ja dokumenteeri spektrid (Labor 1 kõrval), `Pa/ADC samm`, mõõdetud SNR enne/pärast; seejärel pumbajuhtimise 3 olukorra testid ja `poolik haare` eristamise aeg. Uuenda `docs/pump_control.md`, `README.md` ja arenduspäevikut; lõpuks tag `data-acquisition-lab2`.

**Veel puudub:** kinnitatud 30+30 pärisimpulsi CSV, võrreldavad spektrid, mõõdetud SNR, pumba uued mõõtetulemused, osalise haarde võrdlusaeg. Need on päris ülesanded, mitte juba valminud tulemused.

_Seansi kokkuvõte koostatud olemasoleva koodi, GitHubi README ning kasutaja 14.11.2026 terminalitulemuste alusel._
