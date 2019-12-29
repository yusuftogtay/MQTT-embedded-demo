import paho.mqtt.client as mqtt
import JSONgenerator as data


client = mqtt.Client(client_id="DEMO")
client.connect(host="185.207.37.66",port=1883,keepalive=45)

client.publish(topic="deneme",payload=data.sensorDataJSON())
