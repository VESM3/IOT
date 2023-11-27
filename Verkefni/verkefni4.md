## Tímaverkefni 4 _drög_

- Námsmat 20% af heildareinkunn
- Viðfangsefni: [MQTT](https://github.com/VESM3/IOT/wiki/MQTT)

<!-- 
Sýnidæmi: [Python: RPi#1 (client) + fartölva (subscriber & publisher) + RPi#2 (actuator) + test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI)
-->

---

### 1. Mosquitto test Broker (30%) 
Grunnaðgerðir í MQTT með ESP32 (client), fartölvu (subscriber) og Moquitto test Broker (broker)

1. Notaðu ESP32 (Publisher) fyrir telemetry (random gildi/streng). 
   1. Tengdu ESP32 við Wifi.
   1. Notaðu `umqtt.simple` safn fyrir MQTT client. _(þarf ekki install, kemur með MicroPython)_
1. Notaðu [Mosquitto test broker](https://test.mosquitto.org/).
1. Birtu gildin/streng á öðrum ESP32 (subscriber).
   
> [MicroPython: Getting Started with MQTT with 2 x ESP32](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/) <br>
> [Tutorial: MicroPython – MQTT Publish/Subscribe using ESP32/ESP8266](https://www.donskytech.com/micropython-mqtt-esp32-esp8266/) <br>
> [Tutorial: umqtt.simple library in MicroPython](https://www.donskytech.com/umqtt-simple-micropython-tutorial/)

---

### 2. Local Broker (30%)
Í staðinn fyrir að nota Mosquitto test broker frá MIT þá ætlum við að setja upp okkar eigin Broker á fartölvu (eða RPi). Keyrðu lið 1. aftur en núna með eigin local Broker (þarft að vera á sama wifi og ESP32).
- [Install Mosquitto MQTT Windows](https://www.donskytech.com/install-mosquitto-mqtt-windows/) _bætið við í config skrá: lína 234: `listener 1883 0.0.0.0` og lína 532: `allow_anonymous true`, síðan þarf að opna fyrir mosquitto í Windows Firewall.
- [Install Mosquitto MQTT Broker on Raspberry Pi](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/) <br>

Gerðu svo næst eftirfarandi viðbætur:
1. Tengdu ljósnema LDR við ESP32 (Publisher) og útbúðu náttljós. LED er í off stöðu við ákveðið birtuskilyrði (bjart). Til vara: Nota random tölur.  
1. Notaðu RPi eða fartölvu sem Broker. 
1. Subscriber (sama fartölva eða RPi) birtir gildin. 
1. Actuator (annar ESP32) kveikir á LED við ákveðin birtuskilyrði (myrkur).

> [MQTT sýnidæmi með eigin Broker](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/MQTTBroker.md) _ESP32(C/C++) (publisher) og RPi (broker og subscriber)_ <br>
> [PahoMQTT client](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/PahoMQTTClient.md) <br>

---

### 3. Pottaplanta. (40%)

Verkefnið er að sinna pottaplöntu. Við notum [jarðvegsmælir](https://github.com/VESM3/IOT/blob/main/Efni/soilsensor.md) (e. soil sensor) til að kanna rakastig jarðvegs svo við getum áttað okkur hvenær við þurfum að vökva plöntuna. Við notum ljósnema (LDR) til að kanna birtuþörf plöntunar. Við kveikjum á gróðurlampa (led pera) við ákveðin skilyrði (myrkur) og vökvum með solenoid vökvadælu ef jarðvegsmælir gefur tilefni til þess (þurrkur). 

1. Publisher (ESP32), telemetry með JSON sniðmáti.
1. Notaðu fartölvu, RPi eða cloud sem Broker.
1. Subscriber (fartölva/RPi/cloud) prentar út gildin og vinnur úr telemetry og sendri skipanir á Actuator.
1. Actuator (annar ESP32) vökvar plöntu þegar jarðvegur er of þurr og kveikir á LED þegar það er of dimmt. 
1. Actuator (publisher) sendir notification til fartölvu (subscriber) þegar hann hefur framkvæmt aðgerðir.

> [Run Your Cloud MQTT Mosquitto Broker (Digital Ocean)](https://randomnerdtutorials.com/cloud-mqtt-mosquitto-broker-access-anywhere-digital-ocean/) <br>

<!--
https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/3-automated-plant-watering/README.md
-->

<!--
- [Access Node-RED Dashboard from Anywhere using Digital Ocean](https://randomnerdtutorials.com/access-node-red-dashboard-anywhere-digital-ocean/)  
- [Getting Started with Node-RED Dashboard on Raspberry Pi](https://randomnerdtutorials.com/getting-started-node-red-dashboard/)  
-->

---

## Námsmat og skil

- Skilaðu á Innu kóðalausnum.
- Yfirferð á sér stað í tíma. 
- Einkunn fyrir hvern lið: 
    - 4/4 lausn er vel útfærð.
    - 3/4 lausn er smávægilega ábótavant (vantar smá upp á).
    - 2/4 lausn er ábótavant, helmingur er vel útfærður.
    - 1/4 lausn er stórlega ábótavant, tíma og kóðavinna lögð í lausn.
    - 0/4 lausn vantar eða óunnin.

<!--
Pælingar:
- [ ] hætta að nota Mosquitto test Broker?.
- [ ] Setja upp local Broker með fartölvu og sleppa Rpi?.
-->
