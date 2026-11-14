# Andmehõive Labor 3 — püsivara ja tööriistad

Selles kaustas hakatakse arendama **ainult Labor 3 uut** AtomS3R püsivara, mis toetab:

- käske `{"cmd":"dispense","ms":200}`, `{"cmd":"uv","ms":5000}` ja `{"cmd":"clear"}`;
- solenoidklapi riistvarataimeriga sulgemist ning UV LED-i taimeriga automaatset kustumist;
- komparaatori IRQ-d (lühike ISR: avariiseiskamise signaal ja lipp, ülejäänud logika väljaspool ISR-i);
- lukustuvat alarmi ning `{"ev":"alarm","why":"clog"}` või `empty` sündmusi;
- rõhu 100 Hz logimist koos päris ajatempli ja katse ID-ga.

**Veel ei ole Lab 3 püsivara loodud ega riistvaral testitud.** Enne täitmist on vaja päris mähise toite- ja vooluandmeid, relee kontaktide ning õhupordi vooluta oleku mõõtmist, LED draiveri parameetreid, komparaatori ohutut väljunditaset ning vaba GPIO/IRQ viigu valikut.

Varasem [Labor 2 100 Hz püsivara kavand](../../lab2/src/atom_pressure_100hz/) jääb puutumata. **Ära kasuta vana pumbakontrolli automaatselt doseerimiseks**: fail-safe, häire lukk ja päris pumbaoleku tagasiside tuleb eraldi teostada ja kontrollida.
