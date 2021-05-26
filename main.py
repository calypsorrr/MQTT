from network import WLAN
from mqtt import MQTTClient
import machine
import time

wlan = WLAN(mode=WLAN.STA)
wlan.connect("you're welcome", auth=(WLAN.WPA2, "telenet098"), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print("Connected to Wifin")

client = MQTTClient("Lopy4", "192.168.1.206", port=1883)
client.connect()
while True:
    print("Sending ON")
    client.publish(topic="sensor/programmatic", msg="ON")
    time.sleep(1)
    print("Sending OFF")
    client.publish(topic="sensor/programmatic", msg="OFF")

    time.sleep(1)
