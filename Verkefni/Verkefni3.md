## Tímaverkefni 3

- Námsmat 20% af heildareinkunn
- MQTT

---

### 1 Náttljós með RPi (20%)

1. Tengdu ljósnema BH1750 við RPi og kannaðu birtustigsgildin. Sjá t.d. [hér](https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/)
1. Útbúðu náttljós með BH1750 ljósnemanum, LED og RPi. Það duga að hafa on/off stöðu á LED við ákveðið birtuskilyrði.
 
---

### 2 MQTT með RPi (25%)

1. Lestu eftirfarandi um [MQTT](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#introduction). 
1. Fylgdu svo leiðbeiningum sem snúa að **Raspberry Pi** (ekki Arduino/Virtual) í greininni þar sem þú:
   1.  tengir náttljósið (IoT hlut úr 3.1) sem MQTT client við [Eclipse Mosquitto](https://test.mosquitto.org/) sem er open-source test MQTT broker. 
   1.  RPi Sendir birtugildin í JSON sniði til MQTT broker.
   1.  Python app á tölvunni þinni (server code) hlustar (subscribe) á MQTT broker.
   1.  Tölva sendir skipun (publish) um að kveikja eða slökkva á náttljósinu (LED) útfrá ákveðnum birtugildum.

---

### 3 MQTT með ESP32 (25%) 

1. Kynntu þér vel MQTT grunnskipanir.
1. Gerðu sambærilegt og í 3.2 en núna með ESP32 sem MQTT client (í staðinn fyrir RPi). 
   - Prófaðu [BH1750](https://www.arduino.cc/reference/en/libraries/bh1750/) með ESP32, [sýnidæmi](https://github.com/claws/BH1750#example)
      - SDA (SDI) = GPIO21
      - SCL (SCK) = GPIO22 
   - Tengdu ESP32 við Wifi.
   - Notaðu MQTT Client fyrir ESP32, [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/) eða [PubSubClient](https://github.com/knolleary/pubsubclient) 
   - Notaðu [Eclipse Mosquitto Broker](https://test.mosquitto.org/)
   - Notaðu [Arduino JSON](https://arduinojson.org/)


**Bjargir til viðmiðunar:**
- [ESP32 MQTT client: Publish and Subscribe. HiveMQ and BME280 example](https://www.survivingwithandroid.com/esp32-mqtt-client-publish-and-subscribe/) 
- [MQTT](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#introduction), skoða lauslega Arduino útfærslu.

---

### 4 MQTT með ESP32 og RPi (30%) - _drög_

Settu upp eigin MQTT Broker til að vinna með.

1. Tengdu DHT11 við ESP32 og sendu hita- og rakastigsmælingarnar til eign Broker [Eclipse Mosquitto Broker](https://test.mosquitto.org/).
1. Tengdu Raspberry Pi við LED og tengdu við Mosquitto Broker.
1. Tölvan þín á að fá upplýsingarnar sem koma frá ESP32.
1. Tölvan sendir skipun til RPi um að kveikja á LED þegar ákveðið hita- og rakastig er náð.

#### Sýnidæmi:
Home Automation: ESP32 (client) og RPi (broker) <br>
ESP32 er tengt við DHT11, IR transmitter og tæki og RPi: Mosquitto Broker, Node Red, DietPi OS, SQL Lite
- [part 1](https://www.youtube.com/watch?v=kRvNlSJs0Hg&ab_channel=BorisDusnoki) _youtube_
- [part 2](https://www.youtube.com/watch?v=menuVmKz-mc&t=0s&ab_channel=BorisDusnoki) _youtube_

---

### Námsmat

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnum.

