import paho.mqtt.client as mqtt
import random
import time

broker="broker.hivemq.com" #broker público - http://www.mqtt-dashboard.com/
port=1883 #porta
topico="par/sala01/temp" #Tópico

cliente=mqtt.Client("cliente01")
cliente.connect(host=broker,port=port)
valor_temperatura=0 #Vamos simular aqui o valor de leitura de uma temperatura
while(True):
    valor_temperatura=(random.random()+0.0001)*100
    cliente.publish(topic=topico,payload=str(valor_temperatura),qos=1)
    print("Enviei {:.2f}".format(valor_temperatura))
    time.sleep(30)


