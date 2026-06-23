import pandas as pd
import matplotlib.pyplot as plt
import math



datos = pd.read_csv("Houses.txt", sep=r"\s+")

precios = datos["price"]
medidas = datos["size"]

# Cantidad de datos
n = len(precios)

# Regla de Sturges
k = round(1 + 3.322 * math.log10(n))

print("Cantidad de datos:", n)
print("Cantidad de bins:", k)

# Rango y ancho de clase Price
maximoPrecios = precios.max()
minimoPrecios = precios.min()
rangoPrecios = maximoPrecios - minimoPrecios
ancho_clasePrecios = rangoPrecios / k

# Rango y ancho de clase Size
maximoMedidas = medidas.max()
minimoMedidas = medidas.min()
rangoMedidas = maximoMedidas - minimoMedidas
ancho_claseMedidas = rangoMedidas / k

# Print Precios
print("Mínimo:", minimoPrecios)
print("Máximo:", maximoPrecios)
print("Rango:", rangoPrecios)
print("Ancho de clase:", ancho_clasePrecios)

# Histograma Precios
plt.figure()
plt.hist(precios, bins=k)
plt.title("Histograma de precios")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.show()
plt.close()

# 1)A) Intervalo de mayor frecuencia Precios
conteoPrecios, bins, _ = plt.hist(precios, bins=k)
indice_maxPrecios = conteoPrecios.argmax()
print("Intervalo con mayor frecuencia (precios):")
print(bins[indice_maxPrecios], "-", bins[indice_maxPrecios + 1])
print("Frecuencia:", conteoPrecios[indice_maxPrecios])

# Print Medidas
print("Mínimo:", minimoMedidas)
print("Máximo:", maximoMedidas)
print("Rango:", rangoMedidas)
print("Ancho de clase:", ancho_clasePrecios)

# Histograma Medidas
plt.figure()
plt.hist(medidas, bins=k)
plt.title("Histograma de medidas")
plt.xlabel("Medidas")
plt.ylabel("Frecuencia")
plt.show()
plt.close()

# 1)A)Intervalo de mayor frecuencia Medidas
conteoMedidas, bins, _ = plt.hist(medidas, bins=k)
indice_maxMedidas = conteoMedidas.argmax()
print("Intervalo con mayor frecuencia (medidas):")
print(bins[indice_maxMedidas], "-", bins[indice_maxMedidas + 1])
print("Frecuencia:", conteoMedidas[indice_maxMedidas])

# 1)B) Para determinar en qué intervalo es más probable encontrar el precio de una casa elegida al azar, se analiza el histograma de frecuencias.

#El intervalo con mayor probabilidad corresponde al que presenta la mayor frecuencia absoluta, es decir, la barra más alta del histograma.
#En este caso, dicho intervalo es:
#[límite inferior del bin] – [límite superior del bin]
#(el que obtengas con bins[indice_max] y bins[indice_max + 1])
#Por lo tanto, ese intervalo representa la zona donde se concentra la mayor cantidad de precios, y por ende, donde es más probable encontrar el valor de una casa seleccionada aleatoriamente.