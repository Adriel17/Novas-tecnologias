import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import time
import json
import configparser
import pygame 


def mplay():
    pygame.mixer.init()
    pygame.mixer.music.load("arquivox.mp3")
    pygame.mixer.music.play()
    #pygame.time.wait(1000)
def mstop():
    pygame.mixer.music.stop()

def on_message(client,userdate,message):
   
    dados=json.loads(str(message.payload.decode()))
    print("Valor = {0} ".format(dados['field1']))
    print(" {0} ".format(dados['field2']))
    if dados['field2'] == "ABRIU":
        mplay()
    elif dados['field2'] == "fechado":
        mstop()


broker="mqtt.thingspeak.com"
port=1883
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_SUBSCRIBE']
username=config['THINGSPEAK']['USERNAME']
password=config['THINGSPEAK']['MQTT_API_KEY']
subscribe.callback(on_message,qos=0,topics=topico,hostname=broker,port=port,client_id="clisub",auth={'username':username,'password':password})
while (True):
    time.sleep(20)
#python submqtt-thingspeak.py