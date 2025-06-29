import paho.mqtt.client as mqtt
import time

respuesta = ""

def on_connect(client, userdata, flags, rc):
    print("Conectado con el codigo {}".format(rc))

def on_message(client, userdata, msg):
    global respuesta
    respuesta = msg.payload.decode("utf-8")
    print("Respuesta: {}".format(respuesta))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Suscrito con QoS {}".format(granted_qos))

def on_unsubscribe(client, userdata, rc):
    if rc != 0:
        print("Ha ocurrido desconexión inesperada")

# -----------------------------------------------------------
# CLASS CLIENTE MQTT
# -----------------------------------------------------------
class ClienteMQTT():
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_subscribe = on_subscribe
        self.client.on_unsubscribe = on_unsubscribe
        
        self.broker = "localhost"
        self.port = 1883
        
        self.topics_subscribir = [("Recamara/Luz",0),("Recamara/Temperatura",0)]
        self.topic_publicar = ["Peticion/Luz", "Peticion/Temperatura"]
        
        self.client.connect(self.broker, port=1883, keepalive=60)
        time.sleep(0.1)
        self.client.loop_start()
        self.client.subscribe(self.topics_subscribir)
        time.sleep(0.1)

def publicar(self, instruccion):
    if (instruccion == "encender") or (instruccion == "apagar"):
        self.client.publish(self.topic_publicar[0], instruccion)
    elif (instruccion == "temperatura"):
        self.client.publish(self.topic_publicar[1], instruccion)

def regresar_respuesta(self):
    return respuesta