### MQTT sýnidæmi 

- ESP32 client
  - EspMQTTClient: https://www.arduino.cc/reference/en/libraries/espmqttclient/
  - PubSubClient: https://www.arduino.cc/reference/en/libraries/pubsubclient/
- RPi MQTT Broker (local hosting uppsetning)
  - RPi er Broker og prentar út einnig gögn frá Telemetry.
  - ESP32 er Telemetry, notar DHT22/11 og PubSubClient. 
  - Sýnidæmi veðurstöð: [Send data from ESP32 to Raspberry Pi (Broker) via MQTT](https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/) og [lausn frá kennara](https://github.com/eirben/VESM2_V22/blob/main/verkefni5/verkefni5.4.md)
- [RPI með test.mosquitto](https://github.com/VESM3/IOT/tree/main/Efni/MQTT/RPI)
