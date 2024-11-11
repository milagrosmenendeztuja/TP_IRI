import numpy as np
import matplotlib.pyplot as plt

# Parámetros del ciclo cardíaco
lpm = 75  # latidos por minuto
F = lpm / 60  # frecuencia en Hz
T = 60 / lpm  # periodo total en segundos
tiempo = np.linspace(0, T, 1000)  # tiempo para un ciclo

# Volúmenes
vol_d = 130  # volumen diastólico
vol_s = 50   # volumen sistólico
vol_medio = vol_d - vol_s  # volumen medio (amplitud de cambio en el volumen)

# Definición de las funciones para cada fase
def v1(x):
    return vol_medio + (vol_s * np.sin((3 / 4) * np.pi * (lpm / (60 * (2/8))) * x))

def v2(x):
    return v1(T * (2/8))

def v3(x):
    return vol_s + (vol_medio + vol_s * np.sin(3 / 4 * np.pi * (lpm / (60 * 2/8)) * (T * (2/8))) - vol_s) * np.exp(-30 * (x - T * (2.5/8)))

def v4(x):
    return vol_medio - (v3(T * (5/8)) + 80) * np.exp(-30 * (x - T * (4.5/8)))

# Función para calcular el volumen ventricular en cada instante de tiempo
def volumen_vent():
    # Inicializar el array del volumen ventricular
    volumen_ventricular = np.zeros_like(tiempo)

    # Llenar el array 'volumen_ventricular' de acuerdo con cada fase
    for i in range(len(tiempo)):
        if 0 <= tiempo[i] < T * (2/8):
            
            volumen_ventricular[i] = v1(tiempo[i])
        
        elif T * (2/8) <= tiempo[i] < T * (2.5/8):

            volumen_ventricular[i] = v2(tiempo[i])
        
        elif T * (2.5/8) <= tiempo[i] < T * (5/8):

            volumen_ventricular[i] = v3(tiempo[i])
        
        elif T * (5/8) <= tiempo[i] < T:
            
            volumen_ventricular[i] = v4(tiempo[i])

    # Graficar el volumen ventricular
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, volumen_ventricular, color="purple", linewidth=2, label="Volumen Ventricular (Simulado)")
    plt.xlabel("Tiempo (s)", fontsize=12)
    plt.ylabel("Volumen (mL)", fontsize=12)
    plt.title("Simulación del Volumen Ventricular", fontsize=14)
    plt.legend(loc="upper right", fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(40, 140)  # Ajuste de límite del eje Y para reflejar el volumen máximo
    plt.show()

# Llamada a la función para ejecutar la simulación
#volumen_vent()

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de presión
pres_d = 120  # presión diastólica
pres_s = 80   # presión sistólica
pres_amplitud = (pres_d - pres_s) / 2  # 20
pres_media = (pres_d + pres_s) / 2     # 100

# Frecuencia cardíaca (latidos por minuto) y periodo de un ciclo
lpm = 75
T = 60 / lpm

# Definición de las funciones para cada fase de la presión
def q1(x):
    return pres_media + (pres_amplitud * np.sin((3 / 2) * np.pi * (lpm / 60 * (3 / 8)) * x - (1 / 2 * np.pi)))

def g2(x):
    return pres_media + ((pres_amplitud / 2) * np.sin((3 / 2) * np.pi * (lpm / 60 * (3 / 8)) * x - (1 / 2 * np.pi)))

def h(x):
    return pres_media + (pres_amplitud * np.sin(-np.pi * (lpm / 60 * (5 / 8)) * x - np.pi))

# Tiempo para un ciclo de presión
tiempo = np.linspace(0, T, 1000)

# Inicializar el array de presión aórtica
presion_aortica = np.zeros_like(tiempo)

# Llenar el array con las funciones por cada fase
for i in range(len(tiempo)):
    if 0 <= tiempo[i] < T * (3 / 8):
        presion_aortica[i] = q1(tiempo[i])
    elif T * (3 / 8) <= tiempo[i] < T * (5 / 8):
        presion_aortica[i] = g2(tiempo[i])
    elif T * (5 / 8) <= tiempo[i] < T:
        presion_aortica[i] = h(tiempo[i])

# Graficar la presión aórtica con estilo similar a la imagen
plt.figure(figsize=(10, 6))
plt.plot(tiempo, presion_aortica, color="gray", linewidth=2)

# Resaltar la sección de g2 en naranja
tiempo_g2 = tiempo[(tiempo >= T * (3 / 8)) & (tiempo < T * (5 / 8))]
presion_g2 = presion_aortica[(tiempo >= T * (3 / 8)) & (tiempo < T * (5 / 8))]
plt.plot(tiempo_g2, presion_g2, color="orange", linewidth=2)

# Marcar los puntos q1, g2 y h
plt.text(T * (3 / 8) / 4, q1(T * (3 / 8) / 4), "q₁", fontsize=12, ha='right')
plt.text(T * (3 / 8) + (T * (5 / 8) - T * (3 / 8)) / 2, g2(T * (3 / 8) + (T * (5 / 8) - T * (3 / 8)) / 2), "g₂", fontsize=12, ha='right')
plt.text(T * (5 / 8) + (T - T * (5 / 8)) / 2, h(T * (5 / 8) + (T - T * (5 / 8)) / 2), "h", fontsize=12, ha='right')

# Ajustes de la gráfica
plt.xlabel("Tiempo (s)", fontsize=12)
plt.ylabel("Presión (mmHg)", fontsize=12)
plt.title("Simulación de la Presión Aórtica", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.ylim(60, 140)
plt.show()

