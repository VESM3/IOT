# Grein: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/single-board-computer-mqtt.md
# Kóði: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/code-mqtt/pi/nightlight/app.py

# MQTT client allows your app to communicate over MQTT. 
import paho.mqtt.client as mqtt  # pip3 install paho-mqtt

# Replace <ID> with a unique ID that will be used the name of this device client. 
# and later for the topics that this device publishes and subscribes to. Also used for server code.
id = '<ID>'

# unique name for this MQTT client on the broker.
client_name = id + 'test_client'

# to create an MQTT client object
mqtt_client = mqtt.Client(client_name)

# connect to the MQTT broker
mqtt_client.connect('test.mosquitto.org') 

# Start a processing loop that runs in a background thread 
# listening for messages on any subscribed topics.
mqtt_client.loop_start()
