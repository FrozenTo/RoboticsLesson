# Labor 2 — analüüs (notebooks)

Avamiseks käivita Jupyter Lab / Notebook ja ava [`pressure_analysis.ipynb`](pressure_analysis.ipynb). Nüüd sisaldab notebook ka **12.09.2026 Labor 1 mõlema ajatempliga logi tegelikke graafikuid** ning kirjeldavat pinge standardhälbe analüüsi. Vahetult GitHubis vaatamiseks on olemas valmis SVG graafikud: [Lab 1 15:43](lab1_raw_154318.svg), [Lab 1 16:47](lab1_raw_164737.svg) ja [Lab 2 25.10](lab2_25102026_sequence.svg). Täpsed tulemused ja SNR-i piirangud: [`../docs/signal_analysis.md`](../docs/signal_analysis.md).

Notebook teeb praegu kolm asja: (1) kontrollib säilitatud 145 mõõterida; (2) joonistab logitud **pinge mõõterea numbri järgi**, ilma väljamõeldud ajateljeta; (3) arvutab nominaalse ADC sammu ning valmistab ette päris `raw/opamp` katsete 100 Hz, 30 impulsi ja ajatempli kontrolli.

**See ei esita eksitavat SNR-i ega FFT-d:** kui `../data/pressure_comparison_verified.csv` puudub, jätab notebook võrreldavad spektrid ja SNR arvutamata. Kui hiljem lisatakse tõestatud ja ajatemplitega fail, teeb notebook esmased kontrollid ning koostab pingeühikutes SNR-i/PSD diagrammid. Õppejõu nõutud kPa-ühikutes SNR jaoks peab mõlema konfiguratsiooni kalibratsioon enne kinnitatud olema.

Vanad arvulised logid on teise aine kaustas alles. Neid ei tohi automaatselt ümber nimetada Labor 2 tugevdatud signaali mõõtmisteks. `data/README.md` kirjeldab taastatud CSV päritolu.

**Sõltuvused:** `pip install numpy pandas matplotlib scipy jupyterlab`. Notebook ei juhi füüsilist robotit ega muuda väljaspool Labor 2 kausta faile.
