import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client()
client.connect("127.0.0.1", 1883)

print("Capteur MQTT actif...")

while True:
    temp = round(random.uniform(20, 30), 2)
    client.publish("iot/sensors/temp", temp, qos=1)
    print("MQTT Publish :", temp)
    time.sleep(5)
