import paho.mqtt.client as mqtt
import json
def on_message(client,userdate,message):
    dados=json.loads(str(message.payload.decode()))
    print("Detectei Temperatura de {:.2f} e Umidade de {:.2f}".format(dados['temperatura'],dados['umidade']))

def on_subscribe(clente, userdate,mid,granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

broker="broker.hivemq.com"
port=1883
topico="par/sala01"
cliente=mqtt.Client("cliente-ledor")
cliente.connect(host=broker,port=port)
cliente.subscribe(topico,qos=1)
cliente.on_message=on_message
cliente.on_subscribe=on_subscribe

cliente.loop_forever()
