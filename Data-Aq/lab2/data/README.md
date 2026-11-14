# Labor 2 — mõõteandmed (data)

**Oluline:** `pressure_20261025_legacy.csv` on olemasolevast [25.10.2026 tekstlogist](../logs/Tool_logs25102026.md) **ilma muutmata arvudeta** taastatud 145 mõõterida. Fail genereeriti skriptiga [`../src/convert_tool_log.py`](../src/convert_tool_log.py).

- `sample_index` on ainult järjekorranumber (alates 0); see ei ole aeg.
- `source_line` viitab algse Markdown-logi rea numbrile.
- `adc` ja `voltage_mv` on vanast monitorist loetud mõõtetulemused.
- `reported_p_abs_kpa`, `reported_p_gauge_kpa` ja `air_status` on **vana püsivara arvutatud/tähistatud väärtused**, mitte sõltumatult kontrollitud rõhk.
- `config=unverified` tähendab, et selles logis ei olnud konfiguratsiooni `raw` või `opamp` märgitud. Väärtust **ei tohi ilma originaaltõenduseta muuta**.
- `t_ms` ning `pump_state` on tühjad, sest algses tekstis ei olnud neid andmeid. Aega ega ON/OFF olekut ei tohi taastada oletuse või võltsitud ajatempliga.

**Tähtis kalibratsiooni viga:** algne logi ütleb `Atmospheric reference = 41.3 kPa`, kuid varem mõõdetud atmosfäärirõhk oli ligikaudu 97 kPa. Võimendi väljundi kasutamisel tuleb kontrollida ka tagasiteisendust anduri pingeks.

**Nüüd on ka Labor 1 raw andmete koopiad:** [`lab1_raw_20260912_154318.csv`](lab1_raw_20260912_154318.csv) (129 rida) ja [`lab1_raw_20260912_164737.csv`](lab1_raw_20260912_164737.csv) (983 rida). Need pärinevad algsetest ajatempleid sisaldavatest Nutilahendused logidest ning säilitavad arvuti vastuvõtuaja; `config=raw` tähendab Labor 1 otsest anduriühendust, kuid `host_elapsed_ms` ei ole ADC täpne proovivõtuaeg. Graafikud ja analüüs: [`../docs/signal_analysis.md`](../docs/signal_analysis.md).

**Võrdluskatse puuduvad andmed:** 100 Hz ajatemplitega `raw/opamp` võrdlus-CSV, vähemalt 30 impulssi kummagi konfiguratsiooni kohta, katsefaasid, pump ON/OFF ja tegelikult mõõdetud SNR pole sellest failist taastatavad. Varasemad Lab 1 ajatempleid sisaldavad failid on algkujul alles [Nutilahendused/lab1/sketch_sep12a/logs/](../../../Nutilahendused/lab1/sketch_sep12a/logs/) kaustas. Need on Labor 1 ajaloolised mõõtmised, mitte automaatselt Lab 2 `opamp` mõõtmised.

Edasiseks mõõtmiseks on [`../src/log_serial_lab2.py`](../src/log_serial_lab2.py), mis salvestab ainult seadme tegelikke järjestikusi lugemeid. **Vana püsivara ei väljasta 100 Hz mõõteandmeid**, seega 100 Hz nõude täitmiseks on vaja eraldi püsivara ning katse kontrolli.
