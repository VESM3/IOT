Með fyrirvara: _FRUM DRÖG_

## Tímaverkefni 5 (9%)

- Einstaklingsverkefni
- Message Queueing Telemetry Transport (MQTT) 
- Að tengja Arduino við Wifi

---

### 5.1 Náttljós með RPi

1. Tengdu ljósnema BH1750 við RPi og kannaðu birtustigið
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

**MEIRA VÆNTANLEGT**
