
## MQTT sýnidæmi með eigin Broker 
Publisher er með DHT22/11 raka- og hitamæli og sendir gildin til Broker. Subscriber fær svo gildin frá Broker.

- ESP32 (C/C++) er **Publisher**
- RaspberryPi (python) er **Broker** og **Subscriber**. 

Byggt á [Send data from ESP32 to Raspberry Pi (Broker) via MQTT](https://diyi0t.com/microcontroller-to-raspberry-pi-wifi-mqtt-communication/) tutorial. 


<details>
<summary>Kóði publisher (ESP32 C/C++)</summary>
<br>
  
``` c
#include "DHT.h"          // safn frá Adafruit
#include "PubSubClient.h" // Connect and publish to the MQTT broker

// Code for the ESP32
#include "WiFi.h" // Enables the ESP32 to connect to the local network (via WiFi)
#define DHTPIN 4  // Pin connected to the DHT sensor


#define DHTTYPE DHT11  // DHT11 or DHT22
DHT dht(DHTPIN, DHTTYPE);

// WiFi
const char* ssid = "";                 // Your personal network SSID
const char* wifi_password = "";        // Your personal network password

// MQTT
const char* mqtt_server = "192.168.1.100";  // IP of the MQTT broker
const char* humidity_topic = "home/livingroom/humidity";
const char* temperature_topic = "home/livingroom/temperature";
const char* mqtt_username = "eirben"; // MQTT username
const char* mqtt_password = "eirben"; // MQTT password
const char* clientID = "client_livingroom"; // MQTT client ID

// Initialise the WiFi and MQTT Client objects
WiFiClient wifiClient;
// 1883 is the listener port for the Broker
PubSubClient client(mqtt_server, 1883, wifiClient); 


// Custom function to connet to the MQTT broker via WiFi
void connect_MQTT(){
  Serial.print("Connecting to ");
  Serial.println(ssid);

  // Connect to the WiFi
  WiFi.begin(ssid, wifi_password);

  // Wait until the connection has been confirmed before continuing
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  // Debugging - Output the IP Address of the ESP8266
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Connect to MQTT Broker
  // client.connect returns a boolean value to let us know if the connection was successful.
  // If the connection is failing, make sure you are using the correct MQTT Username and Password (Setup Earlier in the Instructable)
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
    Serial.println("Connected to MQTT Broker!");
  }
  else {
    Serial.println("Connection to MQTT Broker failed...");
  }
}


void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  connect_MQTT();
  Serial.setTimeout(2000); //  maximum milliseconds to wait for serial data
  
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.println(" %");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C");

  // PUBLISH to the MQTT Broker (topic = Temperature, defined at the beginning)
  // .c_str() converts a string to an array of characters and terminates this array with a null character at the end.
  if (client.publish(temperature_topic, String(t).c_str())) { 
    Serial.println("Temperature sent!");
  }
  // Again, client.publish will return a boolean value depending on whether it succeded or not.
  // If the message failed to send, we will try again, as the connection may have broken.
  else {
    Serial.println("Temperature failed to send. Reconnecting to MQTT Broker and trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
    client.publish(temperature_topic, String(t).c_str());
  }

  // PUBLISH to the MQTT Broker (topic = Humidity, defined at the beginning)
  if (client.publish(humidity_topic, String(h).c_str())) {
    Serial.println("Humidity sent!");
  }
  // Again, client.publish will return a boolean value depending on whether it succeded or not.
  // If the message failed to send, we will try again, as the connection may have broken.
  else {
    Serial.println("Humidity failed to send. Reconnecting to MQTT Broker and trying again");
    client.connect(clientID, mqtt_username, mqtt_password);
    delay(10); // This delay ensures that client.publish doesn't clash with the client.connect call
    client.publish(humidity_topic, String(h).c_str());
  }
  client.disconnect();  // disconnect from the MQTT broker
  delay(1000*60);       // print new values every 1 Minute
}
```
</details>


<details>
<summary>Kóði subscriber (Raspberry Pi)</summary>
<br>

``` python
import paho.mqtt.client as mqtt

MQTT_ADDRESS = 'iptala broker'
MQTT_USER = 'username'
MQTT_PASSWORD = '*****'
MQTT_TOPIC = 'home/+/+'


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    print(msg.topic + ' ' + str(msg.payload))


def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('MQTT tenging við broker')
    main()

```

</details>

---

### Uppsetning á broker (Raspberry Pi)
Broker getur verið hvaða vél sem er nettengd, í þessu tilviki er Broker raspberryPi Zero.

1. Finna ip tölu á broker (raspberrypi)
1. Finna WiFi SSID og WiFi password
1. Install á raspberrypi
   * `sudo apt update && sudo apt upgrade`
   * `sudo apt install mosquitto mosquitto-clients` 
1. Gerið `sudo nano /etc/mosquitto/mosquitto.conf` og breytið, sjá !["mynd"](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/mosquitto_conf_h24.PNG)
1. Keyrið svo `sudo systemctl enable mosquitto.service` og síðan `sudo systemctl restart mosquitto.service`.
<!--
1. Stofnaðu user (username: vesm3) og lykilorð (password: vesm3)
1. Búa til notanda og lykilorð (publisher) sudo mosquitto_passwd -c /etc/mosquitto/pwfile ***username***
   * Til að eyða notanda *sudo mosquitto_passwd -d /etc/mosquitto/pwfile username*
   * Til að sjá stöðu brokera **sudo systemctl status mosquitto**
   * Til að ræsa Mosquitto **sudo systemctl start mosquitto**
   * Til að stoppa Mosquitto **sudo systemctl stop mosquitto**
   * Til að endurræsa Mosquitto **sudo systemctl restart mosquitto**
   * Til að Mosquitto ræsi sjálkrafa við ræsingu vélar **sudo systemctl enable mosquitto**
-->


