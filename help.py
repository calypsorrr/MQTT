import paho.mqtt.client as mqtt #import the client1
import time
import mysql.connector
import random
mydb = mysql.connector.connect(
  host="10.6.121.161",
  user="root",
  password="telenet098",
  database="php",
  port= 3305
)
broker_address="10.6.121.161"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
while True:
	getal3 = client.publish("sensor","69")#publish
	time.sleep(5)
	getal4 = client.publish("sensor","420")#publish
	time.sleep(5)
	mycursor = mydb.cursor()
	getal1 = 35
	var = getal1
	sql = f"INSERT INTO mqtt (id, waarde, tijdstip) VALUES (UUID(), {var}, CURRENT_TIMESTAMP())"
	mycursor.execute(sql)

	mydb.commit()
