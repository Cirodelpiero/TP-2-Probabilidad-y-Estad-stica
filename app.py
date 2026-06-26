import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import numpy as np

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


# Ejercicio 3: Supongamos que la ciudad de Florida decide sortear una casa. ¿Cuál es la probabilidad aproximada, estimada a partir de la 
# información que tenemos de que el ganador reciba una casa que valga entre 200 y 300 mil dólares? Dar un intervalo con una confianza del
# 95 % para la probabilidad verdadera. Justificar cada paso realizado.
# Rta: La probabilidad estimada de que el ganador reciba una casa valuada entre 200/300 mil dólares es del 34 %. Con un nivel de confianza del
# 95 %, se estima que la probabilidad verdadera se encuentra entre 24.72 % y 43.28 

# 1. Carga de datos desde el github
#url = "https://raw.githubusercontent.com/Cirodelpiero/TP-2-Probabilidad-y-Estad-stica/master/Houses.txt"
#df_casas = pd.read_csv(url, sep=r'\s+')
#n_casas = len(df_casas)  # Tamaño 

# Filtramos: precios entre 200 y 300 inclusive
casas_en_rango = datos[(datos['price'] >= 200) & (datos['price'] <= 300)]
na = len(casas_en_rango)

# Se calcula la probabilidad empírica como: casos favorables / casos totales
# Se filtran los precios en el intervalo inclusivo 200, 300 mil dólares
n_casas = len(datos)
# Se Calcula  el estimador puntual de la proporción muestral (p1)
p1 = na / n_casas # Resultado de proporción


# Para aproximar a la Distribución Normal por el teorema central del límite, se verifica:
# 1. Muestra grande: n = 100 >= 30 //// Éxitos/Fracasos esperados: n*p1 = 34 >= 5  y  n*(1-p1) = 66 >= 5
# Si se cumplen ambos, queda justificado el uso de la variable tipificada Z

# Para un nivel de confianza del 95% (1 - alfa = 0.95), se busca en la tabla normal el valor crítico acumulado para una probabilidad de 0.975


# Se aplica la fórmula matemática: p1 +/- Z_(alfa/2) * sqrt( (p1 * (1 - p1)) / n )
z_critico = stats.norm.ppf(0.975)  # El Z aprox. es 1.96

# Error estándar e Intervalo según fórmula exacta de la página 11 de la Clase 7
# Error Estándar de la proporción muestral
error_estandar = math.sqrt((p1 * (1 - p1)) / n_casas)
# Margen de error global (Z * error estándar)
margen_error = z_critico * error_estandar
# Límites finales del intervalo (restando y sumando el margen a p1)
lim_inferior = p1 - margen_error
lim_superior = p1 + margen_error

print(f"Casas en rango: {na}")
print(f"Probabilidad estimada (p1): {p1:.4f} ({p1*100:.2f}%)")
print(f"Intervalo de Confianza (95%): [{lim_inferior:.4f} ; {lim_superior:.4f}]\n")



# Ejercicio 4: Realizar un gráfico de precios en función de la superficie. ¿Nota alguna relación entre estas variables?. 
# Estimar el coeficiente de correlación lineal entre ambas. ¿Qué significa su valor?

# Se nota una relación entre las variables, el gráfico de dispersión muestra una relación lineal positiva y directa, a mayor superficie en metros cuadrados, el precio de la propiedad tiende a aumentar

# Coeficiente de correlación lineal: Su valor es de 0.8522

# Su valor, al ser un valor positivo y muy cercano a 1, significa que existe una asociación lineal fuerte y directa entre el tamaño de la vivienda y su precio

#  Variables continuas a analizar según la consigna (Acá las definimos)
X = datos['size']   # Variable en el eje X: Superficie (en metros cuadrados)
Y = datos['price']  # Variable en el eje Y: Precio (en miles de dólares)


# Para el gráfico de dispersión: Graficamos la nube de puntos para evaluar visualmente si existe
# Justificación: Graficamos la nube de puntos para evaluar visualmente si hay alguna tendencia o relación geométrica entre ambas variables
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color='purple', alpha=0.7)

# Formato del gráfico
plt.title('Gráfico de Dispersión: Precio en función de la Superficie')
plt.xlabel('Superficie (en metros cuadrados)')
plt.ylabel('Precio (en miles de dólares)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


# Para el Coeficiente de Correlación de Pearson:
# Calculamos el coeficiente 'r' de Pearson para cuantificar la fuerza y la dirección de la asociación lineal entre X e Y
r, p_valor = stats.pearsonr(X, Y)


print(f"Coeficiente de correlación lineal de Pearson (r): {r:.4f}\n")


# Ejercicio 5: Encontrar los coeficientes β0 y β1 por mínimos cuadrados de la recta que mejor ajusta a estas
#variables (precio vs superficie).

# Calculamos covarianza y varianza para obtener la pendiente (Beta_1) y la ordenada (Beta_0)
covarianza = datos['size'].cov(datos['price'])
varianza_x = datos['size'].var()
beta_1 = covarianza / varianza_x
beta_0 = datos['price'].mean() - beta_1 * datos['size'].mean()
# Printeamos los resultados obtenidos
print("PUNTO 5: ")
print(f"Beta_1 (Pendiente): {beta_1:.4f}")
print(f"Beta_0 (Ordenada al origen): {beta_0:.4f}")
print(f"Ecuación estimada: Y = {beta_0:.4f} + {beta_1:.4f} * X\n")

#Ejercicio 5a:  Agregar la recta al gráfico hecho en el inciso anterior.
plt.figure(figsize=(8, 5))
plt.scatter(datos['size'], datos['price'], color='purple', alpha=0.7, label='Datos reales')

# Buscamos los extremos de la superficie para trazar una recta continua
x_min = datos['size'].min()
x_max = datos['size'].max()
x_recta = np.array([x_min, x_max])
y_recta = beta_0 + beta_1 * x_recta

# Graficamos la recta
plt.plot(x_recta, y_recta, color='red', linewidth=2, label='Recta de ajuste')
plt.title('Gráfico de Dispersión: Precio en función de la Superficie con Recta de Regresión')
plt.xlabel('Superficie (m²)')
plt.ylabel('Precio (en miles de dólares)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
plt.close()

#Ejercicio 5b: Estimar un precio para una propiedad cuya superficie sea de 5000 m2. ¿Qué tanta confianza tengo en esta estimación?

superficie_test = 5000
precio_estimado = beta_0 + beta_1 * superficie_test

print("PUNTO 5b: ")
print(f"Precio estimado para 5000 m²: {precio_estimado:.2f} miles de dólares.\n") #Confianza: muy baja. Es una extrapolación, ya que el valor máximo de la lista es menor.


# Ejercicio 5c: Calcular el coeficiente de determinación. ¿Qué significa su valor?

# Elevamos al cuadrado el coeficiente de correlación r de Pepy arson para obtener el R²
r_cuadrado = datos['size'].corr(datos['price']) ** 2

print("PUNTO 5c: ")
print(f"R²: {r_cuadrado:.4f} (o {r_cuadrado*100:.2f}%)")
print(f"El {r_cuadrado*100:.2f}% de la variabilidad de los precios es explicada por la superficie.\n")


# Ejercicio 6: Si yo quisiera deparar o estimar el precio de una propiedad a partir de otra característica de
# la misma (superficie o impuestos), ¿a partir de cuál me conviene estimarla? ¿Por qué?

X1 = datos['size']   # Superficie
X2 = datos['taxes']  # Impuestos
precio_dependiente = datos['price'] # Precio

# Calculamos los coeficientes de correlación r de Pearson
resultado_superficie = stats.pearsonr(X1, precio_dependiente)
resultado_impuestos = stats.pearsonr(X2, precio_dependiente)
# Nos quedamos con la primera posición [0], que es donde está el coeficiente de correlación (r)
r_superficie = resultado_superficie[0]
r_impuestos = resultado_impuestos[0]

print("PUNTO 6: ")
print(f"Coeficiente de correlación lineal - Precio vs Superficie (r1): {r_superficie:.4f}")
print(f"Coeficiente de correlación lineal - Precio vs Impuestos (r2): {r_impuestos:.4f}")
#Conviene estimar el precio de una propiedad a partir de la Superficie porque el valor obtenido para la superficie (r1= 0.8338)
#es mayor que el de los impuestos (r2 = 0.6267). Esto demuestra que hay una con menor dispersión entre el precio y la superficie