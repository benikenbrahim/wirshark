import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print("MQTT Temp :", msg.payload.decode())

client = mqtt.Client()
client.connect("127.0.0.1", 1883)

client.subscribe("iot/sensors/temp", qos=1)
client.on_message = on_message

print("Client MQTT en attente de donnees...")
client.loop_forever()