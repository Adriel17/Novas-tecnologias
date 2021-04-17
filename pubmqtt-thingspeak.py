import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import random
import time
import configparser

broker = "mqtt.thingspeak.com"
port = 1883
config = configparser.ConfigParser()
config.read('conf')
topico = config['THINGSPEAK']['TOPICO_PUBLISH']
detectar_movimento = 0
estado = "fechado"

while(True):
    detectar_movimento = random.randint(0, 1)
    #dados="field1={:.2f}&status=MQTTPUBLISH".format(detectar_movimento)
    if detectar_movimento == 0:
        estado = "fechado"
        dados="field1={:.2f}&field2={}&status=MQTTPUBLISH".format(detectar_movimento,estado)
    elif detectar_movimento == 1:
        estado = "ABRIU"
        dados="field1={:.2f}&field2={}&status=MQTTPUBLISH".format(detectar_movimento,estado)
    publish.single(payload=dados, topic=topico, port=port, hostname=broker)
    print(dados)
    time.sleep(2)
#python pubmqtt-thingspeak.py