## Tímaverkefni 3

- Námsmat 20% af heildareinkunn
- MQTT

---

### 1 Náttljós með RPi (20%)

1. Tengdu ljósnema BH1750 við RPi og kannaðu birtustigsgildin. Sjá t.d. [hér](https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/)
   - bættu við 0.5 - 1 ms time.sleep() t.d. í main() neðst, til að leyfa skynjaranum að stara og muna að enable i2C í RPI
   - SDA (SDI) = GPIO21
   - SCL (SCK) = GPIO22 
1. Útbúðu náttljós með BH1750 ljósnemanum, LED og RPi. Það duga að hafa on/off stöðu á LED við ákveðið birtuskilyrði.

_Það má nota DHT11 í staðinn, notið þá raka- eða hitagildi sjá [tutorial](https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/)_
   - sleppa: `git clone https://github.com/adafruit/Adafruit_Python_DHT.git`
   - sleppa: `sudo python3 setup.py install`
   - Gera í staðinn:  `sudo pip3 install Adafruit_DHT`

---

### 2 MQTT með RPi (30%)

1. Lestu eftirfarandi um [MQTT](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#introduction). 
1. Fylgdu svo leiðbeiningum þar sem snúa að **Single-board computer - Raspberry Pi** (ekki Arduino - Wio Terminal) þar sem þú:
   1.  tengir náttljósið (IoT hlut úr 3.1) sem MQTT client við [Eclipse Mosquitto](https://test.mosquitto.org/) sem er open-source test MQTT broker. 
   1.  RPi Sendir birtugildin í JSON sniði til MQTT broker.
   1.  Python app á tölvunni þinni (server code) hlustar (subscribe) á MQTT broker.
   1.  Tölva þín (server code) sendir skipun (publish) um að kveikja eða slökkva á náttljósinu (LED) útfrá ákveðnum birtugildum.

Nánar um [How to Use The Paho MQTT Python Client for Beginners](http://www.steves-internet-guide.com/into-mqtt-python-client/)

_Það má nota DHT11 í staðinn, notið þá raka- eða hitagildi_


---

### 3. MQTT með ESP32 (20%) 

1. Kynntu þér vel MQTT grunnskipanir.
1. Gerðu sambærilegt og í 3.2 en núna með ESP32 sem MQTT client (í staðinn fyrir RPi). 
   - Notaðu [BH1750](https://www.arduino.cc/reference/en/libraries/bh1750/) með ESP32, [sýnidæmi](https://github.com/claws/BH1750#example)
   - Tengdu ESP32 við Wifi.
   - Notaðu MQTT Client fyrir ESP32, [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/) (eða [PubSubClient](https://github.com/knolleary/pubsubclient))
   - Notaðu [Eclipse Mosquitto Broker](https://test.mosquitto.org/)
   - Notaðu [Arduino JSON](https://arduinojson.org/) _það má líka senda beint streng_

_Það má nota DHT11 í staðinn, notið þá raka- eða hitagildi_

<!--
**Bjargir til viðmiðunar:**
- [ESP32 MQTT client: Publish and Subscribe. HiveMQ and BME280 example](https://www.survivingwithandroid.com/esp32-mqtt-client-publish-and-subscribe/) 
- [MQTT](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#introduction), skoða lauslega Arduino útfærslu.
- Ef þú vilt frekar nota python: [MicroPython – Getting Started with MQTT on ESP32](https://randomnerdtutorials.com/micropython-mqtt-esp32-esp8266/)
-->

<!--
---

### 4 MQTT með ESP32, RPi, tölvu og MQTT Eclipse Mosquitto Broker (20%)

1. Tengdu DHT11 við ESP32 og sendu hita- og rakastigsmælingarnar til [Eclipse Mosquitto](https://test.mosquitto.org/) MQTT Broker.
1. Tengdu Raspberry Pi við LED og tengdu við [Eclipse Mosquitto](https://test.mosquitto.org/) MQTT Broker.
1. Tölvan þín (server code) á að fá upplýsingarnar sem koma frá ESP32.
1. Tölvan þín (server code) sendir skipun (publish) til RPi um að kveikja á LED þegar ákveðið hita- og rakastig er náð.

---
-->

---

### 4. Eigin MQTT Broker (30%)

Einn eða tveir nemendur saman.

1. Settu RPi upp sem MQTT Broker 
2. ESP32 er client og á að senda telemetry (skynjari að eigin vali) til MQTT Broker. 
3. ESP32 (annar) sem actuator (t.d. LED) á að taka við skipunum (subscribe to commands).
4. Tölvan þín (server code) hlustar (subscribe) á MQTT broker.
5. Tölvan þín (server code) sendir skipun skipun (publish) á actuator útfrá ákveðnum skilyrðum (frjáls útfærsla) frá telemetry.
 
**Sýnidæmi veðurstöð:**  
- [Send data from ESP32 to Raspberry Pi (Broker) via MQTT](https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/)
- [Lausn frá kennara](https://github.com/eirben/VESM2_V22/blob/main/verkefni5/verkefni5.4.md)

<!--
- Home Automation: [part 1](https://www.youtube.com/watch?v=kRvNlSJs0Hg&ab_channel=BorisDusnoki) og [part 2](https://www.youtube.com/watch?v=menuVmKz-mc&t=0s&ab_channel=BorisDusnoki) _(youtube)_. ESP32 er tengt við DHT11, IR transmitter og tæki og RPi: Mosquitto Broker, Node Red, DietPi OS, SQL Lite.
-->

---

### Námsmat

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnum.

