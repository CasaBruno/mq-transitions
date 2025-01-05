"""
This module handles MQTT connections and messages.
"""

import paho.mqtt.client as mqtt

# Connection success callback
def on_connect(mqtt_client, userdata, flags, rc):
    """This function is called when the client connects to the broker."""
    print('Connected with result code '+str(rc))
    mqtt_client.subscribe('bruno/#')

# Message receiving callback
def on_message(client, userdata, msg):
    """This function is called when a message is received from the broker."""
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()

# Specify callback functions
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.connect('192.168.0.32', 1883, 60)

# Publish a message
client.publish('bruno/1', 'Hello, World!')

# Keep the connection open
client.loop_forever()