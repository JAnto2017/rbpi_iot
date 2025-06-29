import threading
import time

def funcion(nombre):
    print("{} está durmiendo...".format(nombre))
    time.sleep(1)
    print("Ahora son las 3 AM...")
    time.sleep(0.65)
    print("Ahora {} ha despertado...".format(nombre))

if __name__ == "__main__":
    t1 = threading.Thread(target=funcion, args=("Pepe",))
    # t2 = threading.Thread(target=funcion, args=("Lola",))

    t1.start()
    print("Hilos activos: {}".format(threading.activeCount()))
    time.sleep(1.8)
    print("Este es el final del programa")
    
    # t2.start()