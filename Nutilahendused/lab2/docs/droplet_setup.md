# Nutikad Lahendused — Labor 2: DigitalOcean Dropleti seadistamine

**Meeskond:** Failed Cube  
**Töökuupäev:** 14.11.2026  
**Seadistaja:** Toomas  
**Staatus:** esmane SSH- ja turvaseadistus tehtud; veebiserver ja HTTPS veel seadistamata  
**Soovituslik asukoht repos:** `Nutilahendused/lab2/docs/droplet_setup.md`

## 1. Serveri andmed

Õppejõud andis meeskonnale Ubuntu 24.04 serveri, kuhu algselt sai sisse `root`-kasutajana SSH-võtmega.

| Andmed | Väärtus |
| --- | --- |
| Teenus | DigitalOcean Droplet |
| Domeeninimi (õppejõu antud) | `narva3.roboarena.org` |
| Staatiline / Reserved IP | `143.198.250.135` |
| Põhiline avalik IPv4 (`eth0`) | `174.138.3.104` |
| Privaatne IPv4 (`eth0`) | `10.18.0.7` |
| Süsteem | Ubuntu 24.04.5 LTS (kontrollimise ajal) |
| Masina hostname | `Narva-VPN3` |
| Serveri ED25519 sõrmejälg | `SHA256:045m2+z3QfBRLjEXq207k/zuZC9Ks5uRw7V58IxRtQU` |
| Tavapärane SSH-kasutaja | `toomas` |
| SSH-port | TCP 22 |

Õppejõu antud serveri sõrmejälg vastas esimesel ühendusel näidatule. IP-aadresside erinevus kontrolliti DigitalOceani metaandmete abil: Reserved IP oli aktiivne ning selle aadress oli `143.198.250.135`. Domeeninime DNS-vastavust ei ole selles tööetapis veel eraldi kontrollitud.

## 2. Esimene SSH-ühendus

Windows PowerShellis:

```powershell
ssh root@143.198.250.135
```

Esimesel ühendusel võrreldi serveri ED25519 sõrmejälge õppejõu antud väärtusega ning SSH lisas serveri lokaalsesse `known_hosts` faili. Autentimiseks kasutati arvuti olemasolevat paroolifraasiga kaitstud ED25519 privaatvõtit. Privaatvõtit serverisse ega reposse ei kopeeritud.

Serveris kontrolliti kasutajat, masinat ja võrguliidest:

```bash
whoami
hostname
ip -4 addr show eth0
```

Saadud kasutaja oli `root`, hostname `Narva-VPN3` ja võrguliidese avalik IP `174.138.3.104`. Et selgitada, miks SSH-ühendus käis teise aadressi kaudu, kasutati DigitalOceani metaandmete teenust:

```bash
curl -s http://169.254.169.254/metadata/v1/reserved_ip/ipv4/active; echo
curl -s http://169.254.169.254/metadata/v1/reserved_ip/ipv4/ip_address; echo
```

Vastused olid `true` ja `143.198.250.135`.

## 3. Isikliku halduskasutaja loomine

Algne ligipääs oli ainult `root`-kasutajale. Loodi isiklik kasutaja `toomas` ning anti talle võimalus käivitada halduskäske `sudo` abil.

**Algse root-kasutaja terminalis:**

```bash
adduser toomas
usermod -aG sudo toomas
install -d -m 700 -o toomas -g toomas /home/toomas/.ssh
```

`adduser` käigus määrati Linuxi kasutajale parool. Parooli dokumenti ega reposse ei salvestata.

**Windows PowerShellis:**

```powershell
scp "$env:USERPROFILE\.ssh\id_ed25519.pub" root@143.198.250.135:/home/toomas/.ssh/authorized_keys
```

See edastas **ainult avaliku võtme** (`.pub`).

**Root-terminalis määrati õigused:**

```bash
chown toomas:toomas /home/toomas/.ssh/authorized_keys
chmod 600 /home/toomas/.ssh/authorized_keys
```

**Windows PowerShellis kontrolliti uut ühendust:**

```powershell
ssh toomas@143.198.250.135
```

**Uue kasutaja terminalis:**

```bash
whoami
sudo -v
```

Tulemus: `whoami` näitas `toomas` ning `sudo -v` õnnestus. Uus SSH-ühendus avati enne vana root-seansi sulgemist.

## 4. Tulemüüri seadistamine (UFW)

Enne muutmist kontrolliti tulemüüri ja kuulavaid porte:

```bash
sudo ufw status verbose
sudo ss -lntup
```

Esialgne UFW olek oli `inactive`. Avalikul liidesel kuulas SSH teenus TCP pordil 22. DNS-resolveri port 53 kuulas üksnes kohalikel loopback-aadressidel `127.0.0.53` ja `127.0.0.54`.

Tulemüür seadistati järgmises järjekorras, **lubades SSH enne tulemüüri sisselülitamist**:

```bash
sudo ufw allow 22/tcp
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
sudo ufw status verbose
```

Kontrolli tulemus:

- UFW `active` ja käivitub automaatselt koos süsteemiga.
- Vaikimisi keelatakse sissetulevad ühendused ja lubatakse väljaminevad ühendused.
- Lubatud sissetulev port: **22/tcp**, nii IPv4 kui IPv6 jaoks.
- SSH-port 22 on vajalik serveri haldamiseks; muid avalikke teenuseporte praegu avatud ei ole.
- Teisest PowerShelli aknast tehtud uus SSH-ühendus `toomas` kasutajana õnnestus.

## 5. SSH turvaseadistus

Pärast isikliku kasutaja SSH- ja `sudo`-ühenduse kontrollimist keelati otsene root-kasutaja SSH-sisselogimine.

```bash
echo "PermitRootLogin no" | sudo tee /etc/ssh/sshd_config.d/00-disable-root-login.conf
sudo sshd -t
sudo sshd -T | grep permitrootlogin
sudo systemctl reload ssh
```

Konfiguratsioonikontroll näitas `permitrootlogin no`. Pärast SSH teenuse taaslaadimist sai `toomas` uuest terminalist endiselt sisse, kuid uus root SSH-sisselogimine lükati tagasi.

Täiendav kontroll:

```bash
sudo sshd -T | grep -E '^(passwordauthentication|kbdinteractiveauthentication|pubkeyauthentication|permitrootlogin) '
```

Tegelik väljund:

```text
permitrootlogin no
pubkeyauthentication yes
passwordauthentication no
kbdinteractiveauthentication no
```

Parooliga SSH-sisselogimine ja keyboard-interactive autentimine olid juba keelatud; neid ei olnud vaja eraldi muuta. `root`-konto ise jäi alles, kuid otse SSH-ga sellesse sisse ei saa. Vajadusel saab `toomas` kasutaja avada haldusshelli käsuga `sudo -i`.

## 6. Süsteemiuuendused ja taaskäivitus

Käivitati:

```bash
sudo apt update
apt list --upgradable
sudo apt upgrade
```

`apt update` järel näidati 18 uuendatavat paketti. `apt upgrade` pakkus 15 paketi uuendamist ja jättis kolm paketti faasitud väljalaske tõttu ootele (`distro-info`, `python3-distro-info`, `snapd`). Ühtegi paketti ei pakutud eemaldamiseks. Ubuntu versiooni ei tõstetud 26.04 peale.

Pärast uuendamisetappi taaskäivitati server käsuga:

```bash
sudo reboot
```

Taaskäivitus katkestas kõik vanad SSH-seansid, sealhulgas algse root-seansi. Serveriga ühendati uuesti:

```powershell
ssh toomas@143.198.250.135
```

Taaskäivituse järel kontrolliti:

```bash
whoami
uptime
sudo ufw status
```

**Tulemus:** `toomas` sai sisse, serveri tööaeg oli ligikaudu 1 minut ja UFW oli endiselt aktiivne; lubatud oli ainult TCP 22 IPv4 ja IPv6 jaoks. Uuenduse lõplikku pakettide loendit ei salvestatud — vajadusel kontrollida hiljem uuesti käsuga `apt list --upgradable`.

## 7. Praegune olukord ja pooleliolevad tööd

| Töö | Seis 14.11.2026 |
| --- | --- |
| Õige serveri ja SSH-sõrmejälje kontroll | Tehtud |
| Isiklik `toomas`-kasutaja ja `sudo` | Tehtud ja kontrollitud |
| SSH avaliku võtmega sisselogimine | Tehtud ja kontrollitud |
| Root SSH-sisselogimise keelamine | Tehtud ja kontrollitud |
| Parooliga SSH-sisselogimise keelu kontroll | Tehtud |
| UFW, lubatud vaid 22/tcp | Tehtud ja kontrollitud ka pärast restarti |
| Süsteemi uuendamine ja taaskäivitus | Uuendamise käik läbitud, server pärast restarti töökorras |
| Sergei ja Danieli isiklikud kontod ja võtmed | Ootab nende avalikke võtmeid |
| Domeeni DNS-vastavuse kontroll | Veel kontrollimata |
| Flask-rakendus / postkontor | Veel seadistamata |
| HTTPS ja pöördproksi (nt Caddy) | Veel seadistamata |
| Portide 80/tcp ja 443/tcp avamine veebiteenuse jaoks | Veel tegemata; avada alles teenuse seadistamisel |
| Taastamise / uuesti ehitamise katse märkmete järgi ja ajamõõtmine | Veel tegemata |

**Oluline:** server on nüüd haldamiseks turvalisemalt seadistatud, kuid **Lab 2 rakendus ei ole veel valmis**. HTTPS-i, teenuse käivitumist ja labori robotiga suhtlust ei ole veel testitud. Kaameravooge ei tohi selles laboris avalikule dropletile suunata — need jäävad labori võrku.

## 8. Kuidas järgmine kord serverisse ühenduda

Windowsi PowerShellis:

```powershell
ssh toomas@143.198.250.135
```

Serveris saab halduskäske käivitada prefiksiga `sudo`, näiteks:

```bash
sudo ufw status verbose
```

Kui on vaja root-shelli:

```bash
sudo -i
```

**Ära salvesta GitHubi ega dokumentatsiooni:** privaatseid SSH-võtmeid, paroolifraase, Linuxi kasutajaparoole, Atomi API-võtmeid või muid saladusi. Avalikud SSH-võtmed tuleb meeskonnaliikmetelt eraldi küsida ja paigaldada isikupõhiselt.

## 9. Arenduspäeviku sissekanne (kopeerimiseks)

**14.11.2026 — kohal: Toomas (ülejäänud meeskonna osalemine täpsustamata)**

**Tegime:** Ühendasime õppejõu DigitalOcean Dropletiga SSH kaudu; kontrollisime serveri sõrmejälge, Reserved IP-d ning võrguaadresse. Lõime `toomas`-kasutaja, määrasime `sudo`-õigused ja SSH avaliku võtme. Seadistasime UFW tulemüüri, keelasime root SSH-sisselogimise ning kontrollisime, et parooliga SSH-autentimine on keelatud. Käivitasime süsteemiuuendused ja taaskäivitasime serveri.

**Juhtus (numbrid):** Reserved IP `143.198.250.135`, põhiline avalik IP `174.138.3.104`, privaatne IP `10.18.0.7`. Tulemüüri lubatud sisenev port on 22/tcp (IPv4 ja IPv6). Uuendamise eel kuvati 18 uuendatavat paketti, neist 15 pakuti kohe uuendamiseks ja kolm olid faasitud. Pärast reboot'i õnnestus uus SSH-ühendus; UFW jäi aktiivseks.

**Otsustasime ja miks:** Kasutame igapäevaseks haldamiseks eraldi `toomas`-kontot; otse root-kasutajaga sisse ei logi. SSH-ühendused käivad avalike võtmetega, sest parooliga internetist sisselogimine on suurem risk. UFW avab praegu ainult halduseks vajaliku pordi; veebiteenuse pordid avame alles rakenduse paigaldamisel.

**Lahti järgmiseks korraks:** Lisada Sergei ja Danieli avalikud SSH-võtmed ja kontod; kontrollida DNS-i; paigaldada Flask ja HTTPS-i pöördproksi; dokumenteerida API; mõõta serveri taastamise aeg. Kontrollida vajadusel uuenduste järelejäänud nimekirja.
