## MQTT kóðasýnidæmi 
- ESP32 (micropython) + fartölva/RPi Broker uppsetning
   - Vantar!
- [RPI með test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI) _(python)_
   1. Client (RPi) tenging við MQTT Broker (test.mosquitto)
   2. Publisher (RPi) telemetry (birtugildi) með JSON sniðmáti.
   3. Subscriber (fartölva) server kóði og birtir gildin.
   4. Publisher (fartölva) server kóði með commands með JSON snimáti til Broker.
   5. Subscriber (RPi) er actuator, kveikir á LED við ákveðin skilyrði.
- [ESP32 (C++) + RPi Broker uppsetning](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/MQTTBroker.md) _(C++ og python)_
   - ESP32 notar DHT22/11 og PubSubClient, gögn sem strengur. 
   - RPi er Broker og Subscriber.  

---

## MQTT clients

#### MQTT clients (Micropython)
- umqtt.simple

#### MQTT clients (python)
- [Paho MQTT python client](https://pypi.org/project/paho-mqtt/) _fyrir RPi og fartölvu_
   - `pip3 install paho-mqtt`
   - [How to Use The Paho MQTT Python Client for Beginners](http://www.steves-internet-guide.com/into-mqtt-python-client/)
   - [Python MQTT Client Connections – Working with Connections](http://www.steves-internet-guide.com/client-connections-python-mqtt/)

#### MQTT cleints (C++)

- [PubSubClient](https://www.arduino.cc/reference/en/libraries/pubsubclient/) (by Nick O'Leary) _fyrir ESP32 (C++)_
   - [Using the Arduino PubSub MQTT Client](http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/).
   - It can only publish QoS 0 messages. It can subscribe at QoS 0 or QoS 1.
   - The maximum message size, including header, is 256 bytes by default. This is configurable.
- [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/) (by bertmelis) (C++)
   - MQTT library that can publish with QoS 1 or 2.
   - depends on the PubSubClient Library.

---
