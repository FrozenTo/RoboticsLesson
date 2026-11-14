# Andmehõive Labor 3 — komponentide loend (BOM)

**Staatus:** vajaduste inventuur, **mitte ostukinnitus**. Tellimistähtaeg oli **06.11.2026**; pole kontrollitud, kas midagi telliti või kohale jõudis. Osade täpsed mudelid ja Mouseri koodid tuleb vajadusel tegelikult tarnitud osadelt/dokumentidest üle vaadata.

| Osa | Ülesanne ja kontroll | Päritolu ülesandes | Tegelik olemasolu |
| --- | --- | --- | --- |
| 3/2 solenoidklapp | Süstla ühendamine rõhuga; vooluta tagasivool atmosfääri. Kontrolli mähise DC pinget ja voolu | Õppejõult | Kinnitamata |
| M5Stack Mini 3A Relay Unit | Atomi signaali ja klapi mähise koormuse eraldamine; kontrolli COM/ON/OFF vooluta ühendust | Õppejõult | Kinnitamata |
| Kaitsediood | Klapi induktiivpinge piiramine; väärtus ja suund pärast mähise parameetrite kontrolli | Vahendite loendis | Kinnitamata |
| 2 × 4 mm Y-kiirliitmik | Napi haru ja anduri ühendus | Õppejõult | Kinnitamata |
| Anycubic Standard Resin | 405 nm kõvenev vaigumaterjal, umbes 200–230 mPa·s ülesande järgi | Õppejõult | Kinnitamata |
| Metcal 910-B 10 cc mustad süstlad | Doseerimine; täitmine õppejõu poolt | Õppejõult | Kinnitamata |
| Otsikud kolmes suuruses ja korgid | Tilga suuruse katse; kinnise otsiku juhtum | Õppejõult | Kinnitamata |
| 405 nm LED + sobiv draiver | Kõvendamine, riistvarataimeriga ohutu väljalülitus | Meeskonnalt/ühine tellimus | Täpne tootekood kinnitamata |
| LM358N, takistid, kondensaatorid | Komparaator ja Schmitti hüsterees; kontrollida tegelikku kiibi varianti ja vaba kanalit | Riiulilt | Kinnitamata |
| AtomS3R, MPX5700AP ja Lab 2 LM358P op-amp | Rõhu mõõtmine ja juhtimine | Varasematest labidest | Kasutatud varem; Lab 3 seadistus kinnitamata |
| Ostsilloskoop, multimeeter, nihik | Relee, viivituse, ADC ja mõõtkava kontroll | Riiulilt | Kinnitamata |
| MG400 pump/kast, voolik, statiivid | Suruõhk, vaakum ja doseerimise katsed | Varasematest labidest | Kasutatud varem; Lab 3 seadistus kinnitamata |
| XIAO ESP32S3 Sense kaamera | Tilkade mõõtmise fotod | 3D printimine L2 | Kaamera kalibreering kinnitamata |
| Hele PLA, vahetükid, ekraanimudelid | Tilgaplaat ja mõõdetav klaasi asend | 3D printimine L3 | Pole GitHubis kinnitatud |
| UV kaitseprillid 405 nm jaoks, nitriilkindad, isopropanool | Ohutu kõvendamine ja vaigu käsitlemine | Õppejõult | Kinnitamata |
| Nõelventiil (vajadusel) | Napi haru õhukulu piiramine, kui avatud napp takistab rõhu tekkimist | Tingimuslik | Vajadus mõõtmata |

**Enne ühendamist kontrolli:** päris solenoidklapi toitespetsifikatsioon, relee kontaktide DC induktiivkoormus, kaitsedioodi sobivus, GPIO lubatud pinge 3,3 V, LED draiveri ühendus ja ühenduste vooluta asend. Ära asenda neid mõõdetud väärtustega oletusi.

Ühine tellimistabel: https://moodle.ut.ee/mod/url/view.php?id=1535601
