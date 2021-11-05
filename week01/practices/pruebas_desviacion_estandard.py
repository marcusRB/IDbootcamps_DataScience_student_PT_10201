try:
     import numpy as np
except Exception as e:
     print(e)
import statistics
lista = [2, 3, 5, 6]
# media = np.mean(lista)
media = sum(lista)/len(lista)

# sd = np.std(lista)
# print(round(sd,2))

sd2 = statistics.stdev(lista)
print(round(sd2,2))

suma_cuads = 0
for index in range(len(lista)):
     resta = lista[index] - media
     cuad = resta ** 2
     suma_cuads += cuad
sd3 = round((suma_cuads / (len(lista))) ** 0.5, 2)
print(sd3)

