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

print("-----------------------------")
print("CANTIDAD DE DATOS Y BINS:")
print("Cantidad de datos:", n)
print("Cantidad de bins:", k)
print("-----------------------------")

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
print("PRECIOS DATOS HISTOGRAMA:")
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
print("-----------------------------")

# Print Medidas
print("MEDIDAS DATOS HISTOGRAMA")
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
print("-----------------------------")

# 1)B) Para determinar en qué intervalo es más probable encontrar el precio de una casa elegida al azar, se analiza el histograma de frecuencias.

#El intervalo con mayor probabilidad corresponde al que presenta la mayor frecuencia absoluta, es decir, la barra más alta del histograma.
#En este caso, dicho intervalo es:
#[límite inferior del bin] – [límite superior del bin]
#(el que obtengas con bins[indice_max] y bins[indice_max + 1])
#Por lo tanto, ese intervalo representa la zona donde se concentra la mayor cantidad de precios, y por ende, donde es más probable encontrar el valor de una casa seleccionada aleatoriamente.


plt.figure()
plt.boxplot(precios)
plt.title("Boxplot de precios")
plt.show()
plt.close()

plt.figure()
plt.boxplot(medidas)
plt.title("Boxplot de size")
plt.show()
plt.close()


#Precios (cuartiles, mediana y limites)
q1Precios = precios.quantile(0.25)
medianaPrecios = precios.quantile(0.50)
q3Precios = precios.quantile(0.75)
iqrPrecios = q3Precios - q1Precios
lim_infPrecios = q1Precios - 1.5 * iqrPrecios
lim_supPrecios = q3Precios + 1.5 * iqrPrecios

print("PRECIOS BOXPLOT")
print("Q1:", q1Precios)
print("Mediana:", medianaPrecios)
print("Q3:", q3Precios)
print("IQR:", iqrPrecios)
print("Límite inferior:", lim_infPrecios)
print("Límite superior:", lim_supPrecios)
print(f"Entre {q1Precios} y {q3Precios} esta el 50 % de los valores centrales")
print("--------------------------")


#Medidas (cuartiles, mediana y limites)
q1Medidas = medidas.quantile(0.25)
medianaMedidas = medidas.quantile(0.50)
q3Medidas = medidas.quantile(0.75)
iqrMedidas = q3Medidas - q1Medidas
lim_infMedidas = q1Medidas - 1.5 * iqrMedidas
lim_supMedidas = q3Medidas + 1.5 * iqrMedidas

print("MEDIDAS BOXPLOT")
print("Q1:", q1Medidas)
print("Mediana:", medianaMedidas)
print("Q3:", q3Medidas)
print("IQR:", iqrMedidas)
print("Límite inferior:", lim_infMedidas)
print("Límite superior:", lim_supMedidas)
print(f"Entre {q1Medidas} y {q3Medidas} esta el 50 % de los valores centrales")
print("--------------------------")


#Bigotes Precios
outliers_precios = precios[
    (precios < lim_infPrecios) |
    (precios > lim_supPrecios)
]
print("VALORES ATIPICOS PRECIOS:")
print(outliers_precios)
print("--------------------------")


#Bigotes Medidas
outliers_medidas = medidas[
    (medidas < lim_infMedidas) |
    (medidas > lim_supMedidas)
]
print("VALORES ATIPICOS MEDIDAS:")
print(outliers_medidas)
print("--------------------------")
print("El histograma es más útil para observar cómo se distribuyen las frecuencias en distintos intervalos de valores. En cambio, el gráfico de cajas resume la distribución mediante los cuartiles, la mediana y los valores atípicos, permitiendo comparar conjuntos de datos y detectar outliers de forma más sencilla.")