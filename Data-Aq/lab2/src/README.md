# Labor 2 — lähtekood (src)

See kaust sisaldab **eraldi koopiaid ja uusi abiprogramme ainult Andmehõive Labor 2 jaoks**. Ühegi teise aine ega Labor 1 algset faili ei muudeta.

## Failid

- [`atom_pressure_100hz/`](atom_pressure_100hz/) — **uus, eraldi Lab 2 püsivara** AtomS3R jaoks, 10 ms proovivõtuajastiga; algne tähevalik ja `GET_CHAR` / `PRINT` protokoll on säilitatud. Sisaldab `raw` ja `opamp` režiime, kalibreerimist ning valikulist kahe kanali lugemist (teine ADC viik vaikimisi keelatud). **Riistvaral testimata.**
- [`capture_100hz.py`](capture_100hz.py) — arvutipoolne CSV logija just uue püsivara `DATA`-ridade jaoks, salvestab seadme enda `t_ms`, `seq` ja `config` väärtused. Pumba olekut ei mõelda juurde.
- `atom_pressure_original/src/main.cpp` ja `atom_pressure_original/platformio.ini` — **muutmata koopiad** AtomS3R rõhumonitorist, mis asub kaustas [Nutilahendused/lab1/sketch_sep12a](../../../Nutilahendused/lab1/sketch_sep12a). Need on lähtepunkt, **mitte valmis Lab 2 püsivara**: vanas koodis on umbes 12 mõõtmist × 20 ms ja 500 ms paus, üks ADC kanal ning ilma op-amp teisenduse või `config` andmeväljata.
- `convert_tool_log.py` — ekspordib olemasoleva 25.10.2026 monitorilogi kontrollitavaks CSV-ks kausta `../data/`, jättes puuduva aja ja pumba oleku tühjaks ning konfiguratsiooni `unverified`.
- `log_serial_lab2.py` — **uus arvutipoolne ettevalmistatud logija**, mis loeb olemasoleva Atomi tekstiväljundit ja lisab käsitsi kinnitatud `--config raw|opamp` ning `--trial-id`. Nõuab Python `pyserial` paketti. Ei juhi robotit ega pumpa. Füüsilise katsesüsteemiga kontrollimata.

## Taaskasutatavad olemasolevad programmid (originaale ei muudetud)

- [Nutilahendused: pumba rõhu järgi juhtimine](../../../Nutilahendused/lab1/sketch_sep12a/tools/suck_until_pressure.py)
- [Nutilahendused: algne jadaliidese tekstlogija](../../../Nutilahendused/lab1/sketch_sep12a/tools/log_serial.py)
- [MG400 veebirakenduse server.py](../../../MG400%20python%20apps/mg400_grid_website_v18/server.py)
- [MG400 veebirakenduse seaded](../../../MG400%20python%20apps/mg400_grid_website_v18/config.json)

## Kasutamine

Projekti `Data-Aq/lab2` kaustast:

```powershell
python src/convert_tool_log.py
python src/log_serial_lab2.py --port COM4 --config raw --trial-id raw_01 --output data/raw_01.csv --duration 60
```

**Oluline:** teises käsus tähistab `raw` kasutaja kinnitatud füüsilist ühendust. Seda ei tuletata pingest. Vana püsivara väljastab umbes 1,35 mõõterida sekundis, nii et logija ei saa sellega täita õppejõu 100 Hz nõuet. Arvuti `host_elapsed_ms` on saabumise, mitte mõõtmise täpne aeg. Kõrvutatavaks spektri/SNR analüüsiks tuleb püsivara muuta nii, et mõõtmise aeg `t_ms`, mõlema signaali sama impulss ning katsefaasid oleksid usaldusväärselt salvestatud. Kahe ADC kanali tegelikud viigud ja nende elektriline ohutus tuleb enne uue püsivara katset kinnitada.

**Uus 100 Hz variant:** vaata [eraldi seadistusjuhendit](atom_pressure_100hz/README.md). Pärast kinnitatud ühendust kasuta `python src/capture_100hz.py --port COM4 --expect-config raw --trial-id raw_01 --phase unknown --duration 30 --output data/raw_01.csv`. See on **uus DATA protokoll**, mida vana `log_serial_lab2.py` ei oska lugeda. Tegelik 100 Hz ja kalibratsioon vajavad riistvaral mõõtmist.

**ADC ohutus:** LM358P toide on 5 V; AtomS3R ADC sisendi pinge ei tohi ületada 3,3 V. Mõõda op-amp väljund multimeetriga enne ühendamist.
