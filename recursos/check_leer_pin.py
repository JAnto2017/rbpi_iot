import os
import sys

pin = sys.argv[1]
def leer_pin(pin):
    if not os.path.isfile("/sys/class/gpio/gpio"+str(pin)+"/value"):
        os.system("echo "+str(pin)+" > /sys/class/gpio/export")
        os.system("echo in > /sys/class/gpio/gpio"+str(pin)+"/direction")
    file_name=os.path.join("/","sys","class","gpio","gpio"+str(pin),"value")
    f = open(file_name,"r")
    valor = f.read()
    f.close()
    return valor
   
print(leer_pin(pin))