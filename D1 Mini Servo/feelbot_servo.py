
# Code to run in MicroPython on a Wemos D1 mini with servo on pin D5

from secrets import secrets

import time
from machine import Pin, PWM

import network
from umqtt.simple import MQTTClient

WiFi_SSID = secrets['ssid']
WiFi_PASS = secrets['password']
mqtt_server = "node02.myqtthub.com"
client_id = "FeelBot"
client = MQTTClient(client_id, mqtt_server,user='feelbot',password='feelbot')

low_range=18
high_range=122

servo = PWM(Pin(14), freq=50, duty=low_range)

expressions={"happy":low_range,"angry":low_range+(high_range-low_range)/3,"scared":high_range-(high_range-low_range)/3,"sad":high_range}


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        print(WiFi_SSID)
        wlan.connect(WiFi_SSID, WiFi_PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
    
 
def sub_cb(topic, msg):
    msg_str=(msg.decode("utf-8"))
    print(msg_str)
    emo=(expressions.get(msg_str))
    if emo !=None:
      servo.duty(int(emo))

      
      
      
    




do_connect()
client.set_callback(sub_cb)
client.connect()
client.subscribe(b"feelbot")

while True:
  client.wait_msg()

client.disconnect()

