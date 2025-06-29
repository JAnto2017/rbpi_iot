import threading
import time

def cuenta(numero):
    for i in range(1, numero+1):
        print(i)
        time.sleep(1)

if __name__ == "__main__":
    # se crean tres hilos
    for _ in range(2):
        t = threading.Thread(target=cuenta, args=(10,))
        t.start()
    
    print("Hilos activos: {}".format(threading.activeCount()))
    time.sleep(1.8)
    print("Este es el final del programa")