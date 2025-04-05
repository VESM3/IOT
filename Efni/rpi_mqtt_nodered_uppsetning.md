# Uppsetning á RPi, MQTT og NodeRed

## Raspberry Pi

### Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið í tölvuna þína.
1. Settu microSD kortið með usb lykli í tölvuna.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34).
    1. Veldu **Raspberry Pi 4** og **RASPBERRY PI OS (64 bit)** stýrikerfið og veldu usb portið með microSD kortinu, smelltu svo á *Next*..
    2. Veldu Edit Settings til að gera efirfarandi [stillingar (mynd)](https://github.com/VESM3/IOT/blob/main/Myndir/RPi_uppsetning.png) í GENERAL flipanum:
        - Veldu í Image customization options `to always use`
        - hostname í `v25vesmX` þar sem X er tala sem þú færð frá kennara (ekk nota sérstafi/íslenska) 
        - Ekki breyta **pi** user og notaðu lykilorðið **Verksm1dja** 
        - Configure wifi: TskoliVESM
        - Password: Fallegurhestur
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
    3. Veldu svo SERVICES flipann og hakaðu í *Enable SSH* og veldu *Use password authentication*.
    4. Farðu svo í OPTIONS flipann og hakaðu út *Enable telemetry*. Smelltu svo á *Save*.
1. Veldu svo **YES** og aftur **YES** og hinkraðu þangað þetta er búið (c.a. 15 mín). 
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn og settu það í RaspberryPi og tengdu því næst RaspberryPi við rafmagn.

### Tengjast með SSH

Eftir að RaspberryPi hefur verið tengdur rafmagni þarf að gefa honum tvær til þrjár mínútur til að ræsa í fyrsta skipti.

Að því loknu skaltu opna *terminal* á fartölvunni þinni (PowerShell á Windows, Terminal á MacOS) og gefa þar eftirfarandi skipun:
```bash
ssh pi@v25vesmX.tskoli.vesm
```
Því næst slærðu inn lykilorðið (Verksm1dja) og þá ætti að vera komin á tenging við RaspberryPi.

:information_source: (MacOS) ef þú færð:
```bash
The authenticity of host '...'
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
þá þarft þú að skrifa `yes`.

Þegar þú hefur náð að tengja þig við RaspberryPi skaltu keyra:
```bash
sudo apt update && sudo apt upgrade -y
```

## Mosquitto MQTT broker

Til að setja upp MQTT broker-inn á RaspberryPi þarf að gera eftirfarandi:
- Setja upp mosquitto og mosquitto-clients:
    ```bash 
    sudo apt install mosquitto mosquitto-clients -y
    ```
- Búa til nýja skrá með stillingum á MQTT broker:
    ```bash
    sudo nano /etc/mosquitto/conf.d/mosquitto.conf
    ```
    - Skrifa þessar tvær línur í skrána:
        ```bash
        allow_anonymous true
        listener 1883 0.0.0.0
        ```
    - Smella svo á Ctrl-X og síðan á y.
- Setja mosquitto sem þjónustu sem ræsir alltaf:
    ```bash
    sudo systemctl enable mosquitto.service
    sudo systemctl restart mosquitto.service
    ```

## NodeRed





