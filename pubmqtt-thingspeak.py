import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser
broker="mqtt.thingspeak.com" #broker ThingSpeak
port=1883 #porta
config=configparser.ConfigParser()
config.read('conf')
topico=config['THINGSPEAK']['TOPICO_PUBLISH']
valor_temperatura=0
valor_umidade=0
#Documentação API MQTT https://www.mathworks.com/help/thingspeak/publishtoachannelfeed.html
while(True):
    valor_temperatura=(random.random()+0.0001)*100
    valor_umidade=(random.random()+0.001)*200
    dados="field1={:.2f}&field2={:.2f}&status=MQTTPUBLISH".format(valor_temperatura,valor_umidade)
    publish.single(payload=dados,topic=topico,port=port,hostname=broker)
    print(dados)
    time.sleep(20)
