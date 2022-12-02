### MQTT Kóðasýnidæmi 

- [RPI með test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI)
- ESP32 
  - EspMQTTClient: https://www.arduino.cc/reference/en/libraries/espmqttclient/
  - PubSubClient: https://www.arduino.cc/reference/en/libraries/pubsubclient/
- [MQTT Broker](https://github.com/VESM3/IOT/blob/main/Verkefni/Verkefni3.md#4-eigin-mqtt-broker-30) (local hosting uppsetning)
  - RPi er Broker og prentar út einnig gögn frá Telemetry.
  - ESP32 er Telemetry, notar DHT22/11 og PubSubClient. 
