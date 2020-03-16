# Code to run in MicroPython on a Wemos D1 mini with OLED shield

from secrets import secrets

import network
from umqtt.simple import MQTTClient
from machine import Pin,I2C
import ssd1306

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000) 

lcd=ssd1306.SSD1306_I2C(64,48,i2c)

WiFi_SSID = secrets['ssid']
WiFi_PASS = secrets['password']
mqtt_server = "node02.myqtthub.com"
client_id = "FeelBot"
client = MQTTClient(client_id, mqtt_server,user='feelbot',password='feelbot')

expressions={"happy":"bender_happy.bin","sad":"bender_sad.bin",}

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WiFi_SSID, WiFi_PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
    
 
def sub_cb(topic, msg):
    msg_str=(msg.decode("utf-8"))
    exp_file=expressions.get(msg_str)
    if exp_file !=None:
      display(exp_file)
    


def display(myfile):
  file=open(myfile,"rb")
  data = bytearray(file.read())

  lcd.fill(0)

  for index, pix in enumerate(data):
    for bit in range(0,8):
      if (pix & 2**(bit)) != 0:
        lcd.pixel((((index%8)+1)* 8)-bit-1,index // 8,1)

          
  lcd.invert(True)
  lcd.show()
  file.close()


do_connect()
client.set_callback(sub_cb)
client.connect()
client.subscribe(b"feelbot")

while True:
  client.wait_msg()

client.disconnect()




