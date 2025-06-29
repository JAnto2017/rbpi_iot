import threading
import time

#[1,1,2,2,3,3,4,4,5,5]
mi_lista = []

def cuenta(numero):
    for i in range(1, numero+1):
        mi_lista.append(i)
        # print(mi_lista)
        time.sleep(1)

if __name__ == "__main__":
    h1 = threading.Thread(target=cuenta, args=(10,))
    h1.start()
    
    h2 = threading.Thread(target=cuenta, args=(10,))
    h2.start()
    
    # no pasar de esta línea de código hasta que hilo termina de ejecutarse
    h1.join()
    # no pasar de esta línea de código hasta que hilo termina de ejecutarse
    h2.join()

    print("Hilos activos: {}".format(threading.activeCount()))
    # time.sleep(1.8)
    print(mi_lista)
