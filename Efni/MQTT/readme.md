#### MQTT kóðasýnidæmi 

- [ESP32 + RPi Broker uppsetning](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/MQTTBroker.md) _(C++ og python)_
   - ESP32 notar DHT22/11 og PubSubClient, gögn sem strengur. 
   - RPi er Broker og Subscriber.  
- [RPI með test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI) _(python)_
   1. Client (RPi) tenging við MQTT Broker (test.mosquitto)
   2. Publisher (RPi) telemetry (birtugildi) með JSON sniðmáti.
   3. Subscriber (fartölva) server kóði og birtir gildin.
   4. Publisher (fartölva) server kóði með commands með JSON snimáti til Broker.
   5. Subscriber (RPi) er actuator, kveikir á LED við ákveðin skilyrði.

---

#### MQTT client

- [PubSubClient](https://www.arduino.cc/reference/en/libraries/pubsubclient/) (by knolleary)
   - [Using the Arduino PubSub MQTT Client](http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/).
   - It can only publish QoS 0 messages. It can subscribe at QoS 0 or QoS 1.
   - The maximum message size, including header, is 256 bytes by default. This is configurable.
- [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/) (by bertmelis)
   - MQTT library that can publish with QoS 1 or 2.
   - depends on the PubSubClient Library.
- [Paho MQTT python client](https://pypi.org/project/paho-mqtt/) 
   - [How to Use The Paho MQTT Python Client for Beginners](http://www.steves-internet-guide.com/into-mqtt-python-client/)
   - `pip3 install paho-mqtt`
