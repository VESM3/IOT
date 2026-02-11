# Uppsetning á Raspberry Pi og MQTT Broker

## Raspberry Pi

#### Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið í tölvuna þína.
1. Settu microSD kortið með usb lykli í tölvuna.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34).
    1. Veldu viðeigandi **Raspberry Pi** ásamt stýrikerfi og veldu usb portið með microSD kortinu, smelltu svo á *Next*..
    2. Veldu Edit Settings til að gera efirfarandi stillingar í GENERAL flipanum:
        - hostname í `vesmhX` þar sem X er tala sem þú færð frá kennara (ekk nota sérstafi/íslenska) 
        - Ekki breyta **pi** user og notaðu lykilorðið **Verksm1dja** (ath. 1 (einn) í stað i)
        - Configure wifi: TskoliVESM
        - Password: Fallegurhestur
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
    3. Veldu svo SERVICES flipann og hakaðu í *Enable SSH* og veldu *Use password authentication*.
    4. Farðu svo í OPTIONS flipann og hakaðu út *Enable telemetry*. Smelltu svo á *Save*.
1. Veldu svo **YES** og aftur **YES** og hinkraðu þangað þetta er búið (c.a. 15 mín). 
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn og settu það í RaspberryPi og tengdu því næst RaspberryPi við rafmagn.

#### Tengjast RPi með SSH 

:warning: Til að geta tengst RPi með SSH þá þarf fartölvan þín að vera tengd ```TskoliVESM``` þráðlausa netinu (lykilorð ```Fallegurhestur```) :warning:

Eftir að RaspberryPi hefur verið tengdur rafmagni þarf að gefa honum tvær til þrjár mínútur til að ræsa í fyrsta skipti.

Tengstu RPi með SSH með því að slá eftirfarandi inn í Terminal (PowerShell á Windows, Terminal á Apple):

```bash
ssh pi@vesmhYXX
```

Lykilorðið er ```Verksm1dja``` (ath. 1 (einn) í stað i).

Þar sem Y er hópurinn sem þú ert í og XX númerið á SSD kortinu sem þú fékkst.

Uppfærðu svo stýrikerfið á Pi með því að gefa þessa skipun:

```bash
sudo apt update && sudo apt full-upgrade -y
```

Sæktu svo fulla útgáfu af python.

```bash
sudo apt install python3-full
```

:exclamation: ef þú færð:
```bash
The authenticity of host '...'
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
þá þarft þú að skrifa `yes`.

Uppfærslan tekur 10 til 15 mínútur.

---

#### Að tengjast RPi desktop (viðmót) frá fartölvu 

<details>
<summary>leið 1: Að tengjast með RPi Connect</summary>
<br>
    
Næst þarf að virkja tvær þjónustur en það eru ```RPi Connect``` og ```VNC```.

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
Þar þarftu svo að búa þér til reikning (Raspberry Pi ID). Að lokum þarftu svo að gefa Pi-inum nafn og þá ættir þú að geta tengst honum með gluggaumhverfi með því að velja **Screen Sharing** úr **Connect via**.

Núna getur þú tengst bæði Terminal og gluggaumhverfi án þess að fartölvan þín sé tengd við TskoliVESM þráðlausa netið.

Til að tengjast þessu seinna getur þú farið inn á [þessa](https://connect.raspberrypi.com/) slóð.

</details>

<details>
<summary>leið 2: Að tengjast RPi með VNC</summary>
<br>

Að keyra VNC server á Raspberry Pi leyfir þér að tengjast **RPi desktop** viðmóti þráðlaust frá fartölvu. Ath. fartölvan þarf að vera á sama wifi og RPi.

1. VNC server þarf að vera **enable** á RPi.
    ```bash
    sudo raspi-config
    ```
    Veldu svo ```Interface Options```. Notaður örvatakkana til að færa þig upp/niður og síðan Tab takkann til að velja ```<Select>``` þar sem þú smellir að Enter.
    ![raspi-config-main](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/raspi_config_main.png)
    Farðu svo í VNC og veldu ```<Yes>```. Að lokum velur þú svo ```<Finish>``` til að komast út úr ```raspi-config```.
1. Náðu í [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/) í fartölvuna, búðu til reikning.
    1. Búðu til VNC tengingu (New Connection) í File.
       ```
       VNC Server:  hostname    # eða iptala 
       user:  pi
       lykilorð: Verksm1dja        
       ```
    1. Tvísmelltu á tenginguna, notendafnið er `pi` (ekki breyta) og lykilorð. 
1. Núna getur þú tengst RPi með fartölvunni 

</details>

<!--
#### Hugsanleg vandamál  
- Ef þú nærð ekki VNC (_eða SSH_) samband við RPi (fartölva þarf að vera á sama wifi og RPi): 
     - nota nmap í terminal: 10.201.48.0/24 -sn -Pn.
     - keyra skipunina `nslookup hostname.tskoli.vesm` til að fá `IP` töluna sem þú getur þá notað í staðinn fyrir `hostaname.tskoli.vesm`  (virkar ekki alltaf)
- SSH. Ef permission denied (publickey) á rpi. Þá hreinsa út eldra key úr tölvunni `$ ssh-keygen -R [hostname-or-IP]`
- port 22: Connection timed out. SSH lokað útaf firewall í tölvu [windows fix](https://www.windowscentral.com/how-open-port-windows-firewall) 
- Ef þú færð svartan skjá  gerðu þá eftirfarandi breytingu í skrá (með SSH tengingu á RPi): `/boot/config.txt`. Taktu commentið út (`#`) af `hdmi_force_hotplug=1`.
-->


---

## Mosquitto MQTT broker

Til að setja upp MQTT broker-inn á RaspberryPi þarf að gera eftirfarandi:
1. Setja upp mosquitto og mosquitto-clients:
    ```bash 
    sudo apt install mosquitto mosquitto-clients -y
    ```
1. Búa til nýja skrá með stillingum á MQTT broker:
    ```bash
    sudo bash -c "echo -e 'allow_anonymous true\nlistener 1883 0.0.0.0' > /etc/mosquitto/conf.d/mosquitto.conf"
    ```
    - :exclamation: **Ef** það kemur villa á þetta, gera eftirfarandi:
  
      ```bash
      sudo nano /etc/mosquitto/conf.d/mosquitto.conf
      ```
    
      Skrifa svo inn:
      ```bash
      allow_anonymous true
      listener 1883 0.0.0.0
      ```
    
      Ýta svo á Ctrl+x síðan á Y og loks Enter til að vista og hætta í nano.
    
1. Setja mosquitto sem þjónustu sem ræsir alltaf:
    ```bash
    sudo systemctl enable mosquitto.service
    ```
    og síðan:
    ```bash
    sudo systemctl restart mosquitto.service
    ```
Til að skoða hvað er að gerast á broker-num má keyra eftirfarandi skipun, sem sýnir allt sem er sent á broker-inn:

```bash
mosquitto_sub -h localhost -F '@H:@M:@S, topic: %t, message: %p' -t '#'
```
<!--

## NodeRed

Setja inn viðeigandi hugbúnað sem notaður verður í uppsetningunni:
```bash
sudo apt install build-essential git -y
```

Setja svo upp node-red (setur líka upp Node.js):
```bash
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Svaraðu með **y** við spurningunum tveimur sem koma upp.

Uppsetningin tekur nokkrar mínútur.

Þegar `Node-RED Settings File initialisation` fer í gang, velja eftirfarandi:
```
Node-RED Settings File initialisation
=====================================
This tool will help you create a Node-RED settings file.

? Settings file ‣ /home/pi/.node-red/settings.js [ENTER]

User Security
=============
? Do you want to setup user security? …  [N]
  Yes
▸ No

Projects
========
The Projects feature allows you to version control your flow using a local git repository.

? Do you want to enable the Projects feature? … [N]
  Yes
▸ No

Flow File settings
==================
✔ Enter a name for your flows file · flows.json [ENTER]
✔ Provide a passphrase to encrypt your credentials file · [ENTER]

Editor settings
===============
? Select a theme for the editor. To use any theme other than "default", you will need to install @node-red-contrib-themes/theme-collection in your Node-RED user directory. … 
▸ default [ENTER]

? Select the text editor component to use in the Node-RED Editor … 
▸ monaco (default) [ENTER]
  ace

Node settings
=============
? Allow Function nodes to load external modules? (functionExternalModules) … 
▸ Yes [ENTER]
  No
```

Setja NodeRed sem þjónustu sem ræsir alltaf.
```bash
sudo systemctl enable nodered.service
````
og síðan:
```bash
sudo systemctl restart nodered.service
```

Að endingu er svo best að endurræsa RaspberryPi tölvuna:

```bash
sudo reboot
```

-->





