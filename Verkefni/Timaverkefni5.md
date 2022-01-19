## Tímaverkefni 5 (9%)

- MQTT

---

### 5.1 Náttljós með RPi (20%)

1. Tengdu ljósnema BH1750 við RPi og kannaðu birtustigsgildin. Sjá t.d. [hér](https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/)
1. Útbúðu náttljós með BH1750 ljósnemanum, LED og RPi. Það duga að hafa on/off stöðu á LED við ákveðið birtuskilyrði.
 
---

### 5.2 MQTT með RPi (30%)

1. Lestu eftirfarandi [Connect your device to the Internet](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#connect-your-device-to-the-internet). 
1. Fylgdu leiðbeiningum sem snúa að **Raspberry Pi** (ekki Arduino/Virtual) þar sem þú:
   1.  tengir náttljósið (IoT hlut) sem MQTT client við [Eclipse Mosquitto](https://test.mosquitto.org/) sem er open-source test MQTT broker. 
   1.  Sendir birtugildin í JSON sniði til MQTT broker.
   1.  Python app á tölvunni þinni (server code) sendir skipun um að kveikja eða slökkva á náttljósinu (LED) útfrá ákveðnum birtugildum.

---

### 5.3 MQTT með ESP32 (30%)

1. Gerðu það sama og í 5.2 en núna með ESP32 sem MQTT client.
1. Skoðaðu td:
   - [BH1750](https://www.arduino.cc/reference/en/libraries/bh1750/)
      - SDA (SDI) = GPIO21 og SCL (SCK) = GPIO22 
   - [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/) byggt ofaná [Arduino Client for MQTT](https://github.com/knolleary/pubsubclient)
   - [Arduino JSON](https://arduinojson.org/)

<!--
1. Skoða [ESP32 MQTT client: Publish and Subscribe. HiveMQ and BME280 example](https://www.survivingwithandroid.com/esp32-mqtt-client-publish-and-subscribe/)
1. Tengdu [jarðvegsmælir](https://how2electronics.com/capacitive-soil-moisture-sensor-esp8266-esp32-oled-display/) við ESP32 og kannaðu rakastigið.
-->

---

### 5.4 MQTT með ESP32 og RPi (20%)

1. Tengdu DHT11 við ESP32 og sendu hita- og rakastigsmælingarnar til [Eclipse Mosquitto Broker](https://test.mosquitto.org/).
1. Tengdu Raspberry Pi við LED og tengdu við Mosquitto Broker.
1. Tölvan þín á að fá upplýsingarnar sem koma frá ESP32.
1. Tölvan sendir skipun til RPi um að kveikja á LED þegar ákveðið hita- og rakastig er náð.


<!--
### Dæmi um lokaverkefni: Home Automation: ESP32 (client) og RPi (broker) 
- [Sýnidæmi](https://www.youtube.com/watch?v=kRvNlSJs0Hg&ab_channel=BorisDusnoki) og [part2](https://www.youtube.com/watch?v=menuVmKz-mc&t=0s&ab_channel=BorisDusnoki)
   - ESP32 er tengt við DHT11, IR transmitter og tæki 
   - RPi: Mosquitto Broker, Node Red, DietPi OS, SQL Lite
-->

---

### Námsmat

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir og ljósmyndir af verklegum tilraunum.




