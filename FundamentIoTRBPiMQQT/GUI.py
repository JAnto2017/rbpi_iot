from tkinter import *
from PIL import ImageTk, Image
import cliente_mqtt
import time

class PanelDeControl():
    def __init__(self, ventana):
        self.ventana = ventana
        self.lista_imagenes = ["Imagenes/on.jpg","Imagenes/off.jpg","Imagenes/termostato.jpg"]
        self.imagenes_cargadas = []
        self.cargar_imagenes()
        self.crear_botones()
        self.campo_temperatura()
        self.cliente = cliente_mqtt.ClienteMQTT()
    
    def cargar_imagenes(self):
        for i in range(len(self.lista_imagenes)):
            self.imagenes_cargadas.append(ImageTk.PhotoImage(Image.open(self.lista_imagenes[i])))
        for idx, value in enumerate(self.imagenes_cargadas):
            label = Label(self.ventana, image=value).grid(row=0, column=idx)

    def crear_botones(self):
        Button(self.ventana, text="ON", bg="black", fg="white", command=lambda:self.cliente.publicar("encender")).grid(row=1, column=0)
        Button(self.ventana, text="OFF", bg="black", fg="white", command=lambda:self.cliente.publicar("apagar")).grid(row=1, column=1)
        Button(self.ventana, text="TEMPERATURA", bg="black", fg="white", command=self.reportar_temperatura).grid(row=1, column=2)

    # crea un EDIT sirve para escribir en la ventana
    def campo_temperatura(self):
        self.campo_temperatura = Entry(self.ventana, bg="black", fg="white", width=30)
        self.campo_temperatura.grid(row=2, column=2)
    
    def reportar_temperatura(self):
        self.cliente.publicar("temperatura")
        time.sleep(0.1)
        temperatura = self.cliente.regresar_respuesta()
        self.actualizar_temperatura(temperatura)
    
    def actualizar_temperatura(self, temperatura):
        self.campo_temperatura.delete(0, END)
        self.campo_temperatura.insert(0, "La temperatura es: " + temperatura + " ºC")
            
# ---------------------------------------------------------------------------------

if __name__ == "__main__":
    ventana = Tk()
    ventana.config(bg="black")
    controlador = PanelDeControl(ventana)
    ventana.mainloop()