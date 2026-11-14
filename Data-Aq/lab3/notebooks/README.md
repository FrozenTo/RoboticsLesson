# Andmehõive Labor 3 — andmeanalüüs

Kui olemas on vähemalt üks **päriselt 100 Hz ajatemplitega** doseerimise rõhukõver, koostada analüüs:

1. Ajatemplite kontroll ja rõhu teisendus kPa ühikusse; valed või puuduvad ajad lükata tagasi.
2. `dP/dt` algne diskreetne tuletis `(P[i] - P[i-1]) / (t[i]-t[i-1])`, kus aeg on **sekundites**.
3. Libisev keskmine ja mediaanfilter enne tuletist. Võrrelda mõlema müra (nt stabiilse lõigu std) ja viivitust päris rõhukõveral.
4. Salvestatud rõhu ja tuletise sagedusspektrid; diskreetse FFT ja Welch PSD arvutus ainult siis, kui tegelik proovivõtuaeg kinnitatud.
5. Tavalise tilga, kinnise otsiku ja tühja süstla rõhukõverate võrdlus; valitud lävi peab eristama neid ilma valehäireteta.
6. Joonistada tilga pindala/ruumala impulsi pikkuse vastu, 10 korduse keskmine ja hajuvus ning seos rõhukõvera pindalaga.

**Praegune seis:** vajalikud Lab 3 ajatempliga tilga-, ummistuse- ja tühja süstla logid puuduvad. Labor 1 umbes 1,35 rida sekundis või Labor 2 ajatemplita logid ei tõenda 100 Hz dP/dt või IRQ reageerimiskiirust. Kunstlikke tulemusi ei genereerita.
