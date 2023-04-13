### MQTT sýnidæmi 

- [ESP32 + RPi Broker uppsetning](https://github.com/VESM3/IOT/blob/main/Efni/MQTT/MQTTBroker.md) 
   - ESP32 notar DHT22/11 og PubSubClient. _C++_
   - RPi er Broker og Subscriber.  _Python_
- [RPI með test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI) _python_
   1. Client (RPi) tenging við MQTT Broker (test.mosquitto)
   2. Publisher (RPi) telemetry (birtugildi) með JSON sniðmáti.
   3. Subscriber (fartölva) server kóði og birtir gildin.
   4. Publisher (fartölva) server kóði með commands með JSON snimáti til Broker.
   5. Subscriber (RPi) er actuator, kveikir á LED við ákveðin skilyrði.

---

#### ESP32 MQTT client
- [PubSubClient](https://www.arduino.cc/reference/en/libraries/pubsubclient/)
- [EspMQTTClient](https://www.arduino.cc/reference/en/libraries/espmqttclient/)
