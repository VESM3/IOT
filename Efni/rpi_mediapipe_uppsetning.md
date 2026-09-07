# Uppsetning á RPi, SSH, RPi Desktop og Mediapipe 

### 1. Uppsetning á RPi

Sækja, setja upp og ræsa [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

Velja viðeigandi Raspberry Pi 

![alt text](../Myndir/rpi/RPi_H26_1.png)

Skruna svo niður þar til "Raspberry Pi OS (other)" finnst og velja það.

![alt text](../Myndir/rpi/RPi_H26_2.png)

Skruna svo aftur niður þar til "Raspberry Pi OS (Legacy, 64-bit) finnst og velja það (Bookworm).

![alt text](../Myndir/rpi/RPi_H26_3.png)

Veldu svo SD kortið.

![alt text](../Myndir/rpi/RPi_H26_4.png)

Skráðu svo "hostname", það á að vera hYXX þar sem YXX er númer sem kennarinn úthlutar þér.

![alt text](../Myndir/rpi/RPi_H26_5.png)

Stilltu svo "Localisation" á eftirfarandi hátt:

![alt text](../Myndir/rpi/RPi_H26_6.png)

Hafður notendanafnið `pi` og lykilorðið `Verksm1dja` (ath. 1 í stað i).

![alt text](../Myndir/rpi/RPi_H26_7.png)

Í "Choose Wi-Fi", hafðu SSID `TskoliVESM` og lykilorðið `Fallegurhestur`.

![alt text](../Myndir/rpi/RPi_H26_8.png)

Í "SSH authentication" virkjaðu "Enable SSH" og hafðu hakað í "Use password authentication".

![alt text](../Myndir/rpi/RPi_H26_9.png)

Smelltu að lokum á "WRITE" og veldu "I UNDERSTAND ...."
![](../Myndir/rpi/RPi_H26_10.png)
![](../Myndir/rpi/RPi_H26_11.png)

Uppsetningin tekur um það bil 15 mínútur.

---

### 2. Tengjast RPi með SSH 

:warning: Til að geta tengst RPi með SSH þá þarf fartölvan þín að vera tengd ```TskoliVESM``` þráðlausa netinu (lykilorð ```Fallegurhestur```) :warning:

Settu SSD kortið í RPi og tengdu svo RPi við rafmagn. Eftir að RaspberryPi hefur verið tengdur rafmagni þarf að gefa honum tvær til þrjár mínútur til að ræsa í fyrsta skipti.

Tengstu RPi með SSH með því að slá eftirfarandi inn í Terminal (PowerShell á Windows, Terminal á Apple):

```bash
ssh pi@vesmhYXX
```

Lykilorðið er ```Verksm1dja``` (ath. 1 (einn) í stað i).

Þar sem Y er hópurinn sem þú ert í og XX númerið á SSD kortinu sem þú fékkst.

---

#### 3. Að tengjast RPi desktop (viðmót) frá fartölvu

Hægt er að tengjast **RPi desktop** viðmóti þráðlaust frá fartölvunni þinni.

Byrjaðu á því að virkja þjónustuna ```RPi Connect``` með að skrifa eftirfarandi í terminal.

```bash
sudo raspi-config
```

Veldu svo ```Interface Options```. Notaður örvatakkana til að færa þig upp/niður og síðan Tab takkann til að velja ```<Select>``` þar sem þú smellir að Enter.

![raspi-config-main](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/raspi_config_main.png)

Farðu svo í RPi Connect og veldu ```<Yes>``` og gerðu svo það sama fyrir ```VNC```

![raspi-config-interface](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/raspi_config_interface.png)

Að lokum velur þú svo ```<Finish>``` til að komast út úr ```raspi-config```

Virkjaðu næst RPi Connect með því að gefa eftirfarandi skipun:

```bash
rpi-connect on
```

Næst þarftu að skrá þig inn með því að gefa eftirfarandi skipu:

```bash
rpi-connect signin
```

Þá færðu slóð sem þú þarft að fara inn á með vafranum þínum.

```
Complete sign in by visiting https://connect.raspberrypi.com/verify/XXXX-XXXX
```

```bash
https://connect.raspberrypi.com/verify/XXXX-XXXX
```
Þar þarftu svo að búa þér til reikning (Raspberry Pi ID). Að lokum þarftu svo að gefa Pi-inum nafn (host name) og þá ættir þú að geta tengst honum með gluggaumhverfi með því að velja **Screen Sharing** úr **Connect via**.

Núna getur þú tengst bæði Terminal og gluggaumhverfi án þess að fartölvan þín sé tengd við TskoliVESM þráðlausa netið.

Til að tengjast þessu seinna getur þú farið inn á [þessa](https://connect.raspberrypi.com/) slóð.

---

### 4. Mediapipe uppsetning

Á RPi keyrðu eftirfarandi til að sækja uppsetningarskriftu:
```bash
wget https://raw.githubusercontent.com/VESM3/IOT/main/Kodi/setup_pi.sh
```

Næst þarf að gera skriftuna keyranlega.

```bash
chmod +x setup_pi.sh
```

Og loks að keyra hana.

```bash
./setup_pi.sh
```

#### Prófun

Tengstu RPi með VNC, opnaðu þar terminal og keyrðu eftirfarandi:
```bash
cd ~/mediapipe_test
source venv/bin/activate
python test_mediapipe.py
```
