## Tímaverkefni 4 _drög_

- Námsmat 20% af heildareinkunn
- Viðfangsefni: [MQTT](https://github.com/VESM3/IOT/wiki/MQTT)

---

### Bjargir (tutorials)
- [MQTT kóðasýnidæmi](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/readme.md#mqtt-s%C3%BDnid%C3%A6mi) 
- [Tutorial: MicroPython – MQTT Publish/Subscribe using ESP32/ESP8266](https://www.donskytech.com/micropython-mqtt-esp32-esp8266/)
- [Tutorial: umqtt.simple library in MicroPython](https://www.donskytech.com/umqtt-simple-micropython-tutorial/)
- [MicroPython – Getting Started with MQTT on ESP32](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/)
- [Install Mosquitto MQTT Broker on Raspberry Pi](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/)

---

### 1. Mosquitto test Broker (30%) 
Grunnaðgerðir í MQTT með ESP32 (client), fartölvu (subscriber) og Moquitto test Broker (broker)

1. Notaðu ESP32 (Publisher) fyrir telemetry (random gildi/streng). 
   1. Tengdu ESP32 við Wifi.
   1. Notaðu `umqtt.simple` safn fyrir MQTT client. _er þegar installed með MicroPython_
1. Notaðu [Mosquitto test broker](https://test.mosquitto.org/).
1. Birtu gildin/streng í fartölvu (subscriber).

---

### 2. Local Broker (30%)
1. Tengdu ljósnema LDR við ESP32 (Publisher) og útbúðu náttljós. LED er í on/off stöðu við ákveðið birtuskilyrði.  
1. Notaðu fartölvu sem Broker.
1. Subscriber (sama fartölva) birtir gildin. 
1. Actuator (annar ESP32) kveikir á LED við ákveðin birtuskilyrði (myrkur).

---

### 3. Pottaplanta. (40%)

Verkefnið er að sinna pottaplöntu. Við notum [jarðvegsmælir](https://github.com/VESM3/IOT/blob/main/Efni/soilsensor.md) (e. soil sensor) til að kanna rakastig jarðvegs svo við getum áttað okkur hvenær við þurfum að vökva plöntuna. Við notum ljósnema (LDR) til að kanna birtuþörf plöntunar. Við kveikjum á gróðurlampa (led pera) við ákveðin skilyrði (myrkur) og vökvum með solenoid vökvadælu ef jarðvegsmælir gefur tilefni til þess (þurrkur). 

1. Publisher (ESP32), telemetry með JSON sniðmáti.
1. Notaðu fartölvu sem Broker.
1. Subscriber (fartölva) prentar út gildin og vinnur úr telemetry og sendri skipanir á Actuator.
1. Actuator (annar ESP32) vökvar plöntu þegar jarðvegur er of þurr og kveikir á LED þegar það er of dimmt. 
1. Actuator (publisher) sendir notification til fartölvu (subscriber) þegar hann hefur framkvæmt aðgerðir.

> Hægt er að nota RaspberryPi sem broker í staðinn fyrir fartölvu.

<!--
https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/3-automated-plant-watering/README.md
-->

---

### Námsmat og skil

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
