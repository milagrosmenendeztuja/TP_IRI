from Funciones import volumen_vent

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

def grafica_seno():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y, label="Seno")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Gráfica de la función Seno")
    plt.legend()
    plt.show()
    input("Presione Enter para volver al menú...")

def grafica_coseno():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y, label="Coseno", color="orange")
    plt.xlabel("x")
    plt.ylabel("cos(x)")
    plt.title("Gráfica de la función Coseno")
    plt.legend()
    plt.show()
    input("Presione Enter para volver al menú...")

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Graficar Seno")
        print("2. Graficar Coseno")
        print("Presione 'Enter' para salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            grafica_seno()
        elif opcion == "2":
            grafica_coseno()
        elif opcion == "":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor intente de nuevo.")

# Llamada al menú
menu()




