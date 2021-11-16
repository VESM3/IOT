# Tímaverkefni 5 (9%)

- Einstaklingsverkefni
- Message Queueing Telemetry Transport (MQTT) 
- ESP32 

---

#### 5.1 Náttljós með RPi (20%)

1. Tengdu ljósnema BH1750 við RPi og kannaðu birtustigið.
1. Útbúðu náttljós með ljósnema og LED og RPi. Það duga að hafa on/off stöðu á LED við ákveðið birtskilyrði.

<!-- sjá td [RPi LDR tutorial](https://pimylifeup.com/raspberry-pi-light-sensor/) -->
<!-- [Build a nightlight - Raspberry Pi](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/3-sensors-and-actuators/pi-sensor.md#build-a-nightlight---raspberry-pi)
 -->
 
---

#### 5.2 MQTT með RPi (40%)

[MQTT](https://mqtt.org/) is a Client Server publish/subscribe messaging transport protocol. It is light weight, open, simple, and designed so as to be easy to implement. These characteristics make it ideal for use in many situations, including constrained environments such as for communication in Machine to Machine (M2M) and Internet of Things (IoT) contexts where a small code footprint is required and/or network bandwidth is at a premium. 

1. Lestu eftirfarandi [Connect your device to the Internet](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#connect-your-device-to-the-internet) og fylgdu leiðbeiningum með notkun **RPi**. Tengdu náttljósið (IoT hlut) úr lið 5.1 og tölvuna við [Eclipse Mosquitto](https://test.mosquitto.org/) sem er open-source test MQTT broker. 

<!-- Fylgdu [leiðbeiningum](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/single-board-computer-mqtt.md) -->


---

#### 5.3 Að tilraunast með ESP32-DevKitC WROOM-32D (40%)
1. Láttu LED blikka með ESP32 [lastminute](https://lastminuteengineers.com/esp32-arduino-ide-tutorial/)
   - notaðu pinna 2 (ekki D2), númerin á ESP32 stemma við GPIO pinna (fjólublátt) í greininni.
   - svarta snúran er eingöngu power snúra. Notaðu blá USB mircro data kapalsnúru 
1. Wifi með ESP32. Fylgdu eftir báðum tilraunum í [Create A Simple ESP32 Web Server In Arduino IDE](https://lastminuteengineers.com/creating-esp32-web-server-arduino-ide/)
 
<!--
- [IOT Made Simple: Playing With the ESP32 on Arduino IDE](https://www.instructables.com/IOT-Made-Simple-Playing-With-the-ESP32-on-Arduino-/)
-->

<!--
---

#### 5.4 Að tilraunast með Arduino og ESP8266 Wifi module 
1. Settu upp ESP8266 wifi module með Arduino og prófaðu ýmsar AT commands.
   - Uppsetning: [myndband](https://www.youtube.com/watch?v=bQ54De84Ww4)
   - ESP8266 driver: http://arduino.esp8266.com/stable/package_esp8266com_index.json
   - notaðu 115200 baud
   - AT commands; [ESP8266 AT Command Set](https://www.pridopia.co.uk/pi-doc/ESP8266ATCommandsSet.pdf) og [ESP8266 Module DataSheet with AT commands](https://cdn.sparkfun.com/datasheets/Wireless/WiFi/ESP8266ModuleV1.pdf).
1. Fylgdu [Getting Started With the ESP8266 ESP-01](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)
   - skoðaðu einnig ábendingar í comments 
1. Fáðu LED til að blikka með ESP82666 wifi module. Sjá t.d. [How to set up and configure the ESP-01 Wi-Fi module so you can connect your project to the internet.](https://maker.pro/esp8266/tutorial/how-to-program-esp8266s-onboard-gpio-pins) 
   - Haltu þið samt við sömu uppsetningu og í fyrsta liðnum.



---

#### 5.5 MQTT með Arduino (IoT hlutur) og tölvu.
[Install the WiFi and MQTT Arduino libraries](https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/wio-terminal-mqtt.md#control-your-nightlight-over-the-internet---wio-terminal) 
1. Útbúðu náttljós; ljósnema og LED með Arduino, sjá td. [Arduino LDR tutorial](https://create.arduino.cc/projecthub/tarantula3/using-an-ldr-sensor-with-arduino-807b1c).

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
1. Prófaðu núna að nota RPi staðinn fyrir tölvuna.

-->

---
 
### Námsmat

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir og ljósmyndir af verklegum tilraunum.




