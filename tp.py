import numpy as np
import matplotlib.pyplot as plt

# Periodo total del ciclo cardíaco
T = 0.8
tiempo = np.linspace(0, T, 1000)

# Definir los puntos de cambio en cada fase
inicio_disminucion = T / 4       # Inicio de la sístole
inicio_llenado_rapido = T / 2    # Inicio de la diástole (llenado rápido)
inicio_llenado_lento = 3 * T / 4 # Transición a llenado lento y auricular

def volumen_vent(inicio_disminucion, inicio_llenado_rapido, inicio_llenado_lento):
    # Inicializar el array del volumen ventricular
    volumen_ventricular = np.zeros_like(tiempo)

# Llenar el array 'volumen_ventricular' de acuerdo con cada fase
    for i in range(len(tiempo)):
        if tiempo[i] < inicio_disminucion:
            # Fase de volumen máximo antes de sístole
            volumen_ventricular[i] = 130
        elif inicio_disminucion <= tiempo[i] < inicio_llenado_rapido:
            # Fase de contracción ventricular (sístole) con transición suave (curva exponencial)
            volumen_ventricular[i] = 130 - (130 - 50) * (1 - np.exp(-(tiempo[i] - inicio_disminucion) * 5)) 
        elif inicio_llenado_rapido <= tiempo[i] < inicio_llenado_lento:
            # Fase de llenado rápido con una función cuadrática para suavizar el aumento
            volumen_ventricular[i] = 50 + (80) * ((tiempo[i] - inicio_llenado_rapido) / (inicio_llenado_lento - inicio_llenado_rapido))**2
        else:
            # Fase de llenado lento y auricular con una oscilación pequeña
            volumen_ventricular[i] = 90 + 5 * np.sin(10 * (tiempo[i] - inicio_llenado_lento)) 

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


def presion_aort(inicio_disminucion, inicio_llenado_rapido, inicio_llenado_lento):

    P_max = 120      # Presión máxima sistólica
    P_base = 80      # Presión diastólica (mínima)
    t_sistole = 0.3  # Duración aproximada de la sístole
    t_diastole = 0.5 # Duración aproximada de la diástole

    # Tiempo total del ciclo cardíaco
    T = t_sistole + t_diastole
    tiempo = np.linspace(0, T, 1000)

    
    def presion_aortica(t):
        if t < (t_sistole/3):
            return P_base
        elif t > (t_sistole/3) and t < t_sistole:
            return P_base + 20 * np.sin((np.pi / (t_sistole - t_sistole / 3)) * (t - t_sistole / 3))
            #return P_base + (P_max - P_base) * np.exp(-(t - t_sistole) * 5)

        else:
            return P_base 


    presion = np.vectorize(presion_aortica)(tiempo)

    
    plt.figure(figsize=(10, 6))
    plt.plot(tiempo, presion, color="red", label="Presión Aórtica Simulada")

    
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Presión (mmHg)")
    plt.title("Simulación de la Presión Aórtica")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(70, P_max + 10)
    plt.show()


presion_aort(inicio_disminucion, inicio_llenado_rapido, inicio_llenado_lento)