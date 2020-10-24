import paho.mqtt.client as mqtt

def chegou_mensagem(client,userdate,message):
    temperatura=float(str(message.payload.decode()))
    print("Detectei {:.2f}".format(temperatura))
def on_subscribe(clente, userdate,mid,granted_qos):
    print("Inscrito: "+str(mid)+" "+str(granted_qos))

broker="broker.hivemq.com"
port=1883
topico="par/sala01/temp"
cliente=mqtt.Client("cliente-ledor")
cliente.connect(host=broker,port=port)
cliente.subscribe(topico,qos=1)
cliente.on_message=chegou_mensagem
cliente.on_subscribe=on_subscribe
cliente.loop_forever()

