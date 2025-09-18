import numpy as np

datos = np.random.rand(1000, 3) * 100

print(datos.shape)

media = np.mean(datos, axis=0) 
dst_std = np.std(datos, axis=0) 
max = np.max(datos, axis=0) 
min = np.min(datos, axis=0)

print("Características básicas") 
print("Media", media) 
print("Dst std", dst_std) 
print("Máximo", max) 
print("Mínimo", min)