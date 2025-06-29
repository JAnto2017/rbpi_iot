import paho.mqtt.client as mqtt
import time
from gpiozero import LED, MCP3008
import threading

luz = LED(17)
temperatura_actual = 0
respuesta = ""

# -----------------------------------------------------------
# METODOS
# -----------------------------------------------------------

def dame_temperatura():
    global temperatura_actual
    mi_adc = MCP3008(channel=0)
    while True:
        temperatura_actual = mi_adc.value*3.3*100
        return temperatura_actual

# -----------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    print("Conexión con el código {}".format(rc))

# -----------------------------------------------------------
def on_message(client, userdata, msg):
    global respuesta
    respuesta = msg.payload.decode("utf-8")
    print("Respuesta: {}".format(respuesta))
    if respuesta == "encender":
        luz.on()
    elif respuesta == "apagar":
        luz.off()
    elif respuesta == "temperatura":
        x = dame_temperatura()
        x = round(x,2)
        client.publish("Recamara/Temperatura", x)

# -----------------------------------------------------------
def on_subscribe(client, userdata, mid, granted_qos):
    print("Suscrito con QoS {}".format(granted_qos))

# -----------------------------------------------------------
def on_unsubscribe(client, userdata, mid):
    if mid != 0:
        print("Desconexión inesperada")

# -----------------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------
if __name__ == "__main__":
    
    nuevo_hilo = threading.Thread(target=dame_temperatura)
    nuevo_hilo.start()
    
    broker = "localhost"
    port = 1883
    topics_publicar = ["Recamara/Luz", "Recamara/Temperatura"]
    topics_suscribir = [("Peticion/Luz",0),("Peticion/Temperatura",0)]
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    client.on_unsubscribe = on_unsubscribe
    
    client.connect(broker, port=1883, keepalive=60)
    time.sleep(0.1)
    client.loop_start()
    client.subscribe(topics_suscribir)
    time.sleep(0.1)
    
    while True:
        if respuesta == "salir":
            break
    client.disconnect()
    client.loop_stop()