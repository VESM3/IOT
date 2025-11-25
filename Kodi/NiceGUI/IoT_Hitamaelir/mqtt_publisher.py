import json
import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

# MQTT Configuration
MQTT_BROKER = "broker.hivemq.com"  # Public MQTT broker
MQTT_PORT = 1883
MQTT_TOPIC = "iot/temperature/sensor001"

def generate_sensor_data():
    """Generate realistic temperature sensor data"""
    base_temp = 22.0  # Base temperature in Celsius
    variation = random.uniform(-3.0, 3.0)
    temperature = round(base_temp + variation, 2)
    
    data = {
        "sensor_id": "TEMP_SENSOR_001",
        "temperature": temperature,
        "unit": "celsius",
        "location": "Room A",
        "timestamp": datetime.now().isoformat()
    }
    return data

def on_connect(client, userdata, flags, rc, properties=None):
    pass

def main():
    # Initialize MQTT client
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    
    try:
        # Connect to broker
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
        
        count = 0
        while True:
            # Generate and publish sensor data
            sensor_data = generate_sensor_data()
            message = json.dumps(sensor_data)
            
            result = client.publish(MQTT_TOPIC, message)
            
            # Wait before sending next reading
            time.sleep(2)
            
    except KeyboardInterrupt:
        client.loop_stop()
        client.disconnect()
    except Exception as e:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
