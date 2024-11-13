import numpy as np
import matplotlib.pyplot as plt

#JUANPY

# Definición de las funciones para cada fase de la presión

def p1(x, est): #"x" es el tiempo relativo
        pres_media = (est["P_sist"] + est["P_diast"]) / 2
        pres_amplitud = (est["P_diast"] - est["P_sist"]) / 2

        return pres_media + pres_amplitud * np.sin(3 / 2 * np.pi * (est["Lpm"] / (60 * 3 / 8)) * x - 1 / 2 * np.pi)

def p2(x, est):
        pres_media = (est["P_sist"] + est["P_diast"]) / 2
        pres_amplitud = (est["P_diast"] - est["P_sist"]) / 2

        return pres_media + (pres_amplitud / 2) * np.sin(3 / 2 * np.pi * (est["Lpm"] / (60 * (3 / 8))) * x - 1 / 2 * np.pi)

def p3(x, est):
        pres_media = (est["P_sist"] + est["P_diast"]) / 2
        pres_amplitud = (est["P_diast"] - est["P_sist"]) / 2

        return pres_media + pres_amplitud * np.sin(-np.pi * (est["Lpm"] / (60 * (5 / 8))) * x - np.pi)

# Función para calcular la presión aórtica en cada instante de tiempo
def PRESION_AORT(est, T, F):
        
        # número de ciclos a simular
        num_ciclos = 5 
        # Fijar la semilla para reproducibilidad
        np.random.seed(0)
        # Promedio 70 lpm con variación
        lpm_variados = np.random.normal(loc=70, scale=10, size=num_ciclos)  # Promedio 70 lpm con variación
        # Tiempo total para la simulación
        tiempo_total = np.linspace(0, num_ciclos * T, num_ciclos * 1000)
        
        # Inicializo el array de la presión aórtica
        presion_aortica = np.zeros_like(tiempo_total)

        # Lleno el array 'presion_aortica' de acuerdo con cada fase en cada ciclo
        for i in range(len(tiempo_total)):

            # Ajuste del tiempo relativo al ciclo actual
            t_relativo = tiempo_total[i] % T
            
            if 0 <= t_relativo < T * 3 / 8:
                presion_aortica[i] = p1(t_relativo, est)

            elif T * 3 / 8 <= t_relativo < T * 5 / 8:
                presion_aortica[i] = p2(t_relativo, est)

            else:
                presion_aortica[i] = p3(t_relativo, est)


        # Graficar
        plt.figure(figsize=(12, 6))
        plt.plot(tiempo_total, presion_aortica, color="blue", linewidth=2, label="Presión Aórtica (Simulada)")
        plt.xlabel("Tiempo (s)", fontsize=12)
        plt.ylabel("Presión (mmHg)", fontsize=12)
        plt.title("Simulación de la Presión Aórtica en Varios Ciclos", fontsize=14)
        plt.legend(loc="upper right", fontsize=10)
        plt.grid(True, linestyle="--", alpha=0.7)
        plt.ylim(0, 200)  # Ajuste de límite del eje Y para reflejar la presión máxima y mínima
        plt.show()
        input("Presione Enter para volver al menú...")


def Principal(est):
    
    #Parametros
    T = 60 / est["Lpm"]  # periodo total en segundos
    F = est["Lpm"] / 60  # frecuencia en hz

    PRESION_AORT(est, T, F)
    
