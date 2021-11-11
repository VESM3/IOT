_DRÖG_

## Tímaverkefni 5 (9%)

- Einstaklingsverkefni
- Message Queueing Telemetry Transport (MQTT) 
- Að tengja Arduino við Wifi

---

### 5.1 Náttljós með RPi

1. Tengdu ljósnema [BH1750](https://www.instructables.com/BH1750-Digital-Light-Sensor/) við RPi og kannaðu birtustigið
1. Útbúðu náttljós með ljósnema og LED og RPi. Það duga að hafa on/off stöðu á LED við ákveðið birtskilyrði.

<!-- sjá td [RPi LDR tutorial](https://pimylifeup.com/raspberry-pi-light-sensor/) -->
<!-- [Build a nightlight - Raspberry Pi](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/3-sensors-and-actuators/pi-sensor.md#build-a-nightlight---raspberry-pi)
 -->
 
---

### 5.2 MQTT með RPi

[MQTT](https://mqtt.org/) is a Client Server publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed so as to be easy to implement. These characteristics make it ideal for use in many situations, including constrained environments such as for communication in Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is at a premium. 

1. Lestu eftirfarandi [Connect your device to the Internet](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#connect-your-device-to-the-internet) og fylgdu leiðbeiningum með notkun **RPi**. Tengdu náttljósið (IoT hlut) úr lið 5.1 og tölvuna við [Eclipse Mosquitto](https://test.mosquitto.org/) sem er open-source test MQTT broker. 

<!-- Fylgdu [leiðbeiningum](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/single-board-computer-mqtt.md) -->

---

### 5.3 Að tengja Arduino við netið með ESP8266 Wifi module

Tengdu Arduinio við wifi með ESP8266.

Skoðaðu t.d. [Add WiFi to Arduino UNO and use telnet on Android](https://www.instructables.com/Add-WiFi-to-Arduino-UNO/) og [ESP8266WiFi library](https://arduino-esp8266.readthedocs.io/en/latest/esp8266wifi/readme.html#quick-start)

---

### 5.4 Náttljós með Arduino 
Útbúðu náttljós; ljósnema og LED með Arduino, sjá td. [Arduino LDR tutorial](https://create.arduino.cc/projecthub/tarantula3/using-an-ldr-sensor-with-arduino-807b1c).

---

#### 5.5 MQTT með Arduino (IoT hlutur) og tölvu.
<!--  [Install the WiFi and MQTT Arduino libraries](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/wio-terminal-mqtt.md#control-your-nightlight-over-the-internet---wio-terminal) --> 
1. Sæktu og innstallaðu eftirfarandi söfn í Arduino IDE:
  ```C
  Seeed Arduino rpcWiFi @ 1.0.5
  Seeed Arduino FS @ 2.1.1
  Seeed Arduino SFUD @ 2.0.2
  Seeed Arduino rpcUnified @ 2.1.3
  Seeed_Arduino_mbedtls @ 3.0.1
  ```
This imports the Seeed WiFi libraries. The @ <number> syntax refers to a specific version number of the library.   
1. Náðu í Arduino MQTT client safnið [PubSubClient](https://github.com/knolleary/pubsubclient), leiðbeiningar [Installing Arduino Library from GitHub](https://www.baldengineer.com/installing-arduino-library-from-github.html). [API Documentation](https://pubsubclient.knolleary.net/api)
1. Tengdu Arduino við þráðlausa netið skv. [leiðbeiningum](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/wio-terminal-mqtt.md#connect-to-wifi)
1. Tengdu IoT hlut við MQTT broker [leiðbeiningar](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/wio-terminal-mqtt.md#connect-to-mqtt)
1. Fylgdu leiðbeiningum [Connect your device to the Internet](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#connect-your-device-to-the-internet) og fáðu náttljósið til að virka með Arduino.
1. Prófaðu núna að nota RPí staðinn fyrir tölvuna.
 
---
 
**MEIRA VÆNTANLEGT**
