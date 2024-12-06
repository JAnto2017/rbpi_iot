from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor.get_available_sensors()


for i in range(0,len(sensor)):
        print('Temperatura: 'sensor[i].get_temperature()+' Id':sensor[i].id})
