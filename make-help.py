import paho.mqtt.client as mqtt #import the client1
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.1.206",
  user="root",
  password="telenet098",
  database="php",
  port= 3305
)

def on_message(client, userdata, message):
    message_received = str(message.payload.decode("utf-8"))
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
    mycursor = mydb.cursor()
    sql = f"INSERT INTO mqtt (id, waarde, tijdstip) VALUES (UUID(), {message_received}, CURRENT_TIMESTAMP())"
    mycursor.execute(sql)
    mydb.commit()

broker_address="192.168.1.206"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
print("Subscribing to topic","iot/awesomesauce")
client.subscribe("iot/awesomesauce")
client.loop_forever()
