#Lbreria
import tkinter as tk
from tkinter import ttk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from tkinter import messagebox

#instruciones para la ventana
Ventana=Tk()
Ventana.title("Graficador")
Ventana.geometry("700x300")

#Amplitud
entry_amplitud=Entry(Ventana)
entry_amplitud.place(x=50, y=50)
texto_amplitud=Label(Ventana, text="Voltaje")
texto_amplitud.place(x=200, y=50)

#Frecuencia
entry_frecuencia=Entry(Ventana)
entry_frecuencia.place(x=50, y=100)
texto_frecuencia=Label(Ventana, text="Frecuencia")
texto_frecuencia.place(x=200, y=100)

#Fase
entry_fase=Entry(Ventana)
entry_fase.place(x=50, y=150)
texto_fase=Label(Ventana, text="Fase")
texto_fase.place(x=200, y=150)

#Desplegable entrada
onda_entrada = tk.StringVar()
desplegable_entrada= ttk.Combobox(Ventana,width=17,values=["Seno","Coseno","Triangular","Cuadrada"],state="readonly",textvariable=onda_entrada)
desplegable_entrada.place(x=400, y=50)
desplegable_entrada.set("Selecciona una opción: ")
texto_fase=Label(Ventana, text="Señal")
texto_fase.place(x=555, y=50)

#Ciclos
entry_ciclo=Entry(Ventana)
entry_ciclo.place(x=400, y=100)
texto_ciclo=Label(Ventana, text="Ciclos")
texto_ciclo.place(x=555, y=100)

#Funcion
def realizarGrafica():
    datos_amplitud=entry_amplitud.get()
    datos_frecuencia=entry_frecuencia.get()
    datos_fase=entry_fase.get()
    datos_ciclos=entry_ciclo.get()
    senal=onda_entrada.get()

    # Convertir a números si es necesario
    try:
        #Parámetros
        A = float(datos_amplitud) #mplitud
        f = int(datos_frecuencia) # frecuencia en Hz   
        phi_deg = float(datos_fase) #fase
        N_ciclos= int(datos_ciclos) #número de ciclos que quieres mostrar
        if A == 0:
            messagebox.showerror("Error", "La amplitud no puede ser 0.")
            return
        if f <= 0:
            messagebox.showerror("Error", "La frecuencia debe ser mayor a 0.")
            return
        if N_ciclos <= 0:
            messagebox.showerror("Error", "El número de ciclos debe ser mayor a 0.")
            return
        if phi_deg >-360 and phi_deg < 0: 
            phi_deg=phi_deg+360
        if phi_deg <-360 or phi_deg > 360: 
            messagebox.showerror("Error", "Verifica que sean grados.") 
            return
    
        if senal=="Seno":      
            # parámetros          
            T = 1 / f                    # período de la señal
            t_max = N_ciclos * T         # duración total en segundos
            fn = 40*f   # frecuencia de muestreo
            t = np.linspace(0, t_max, fn)  # vector tiempo de 0 a 1s
            phi = np.deg2rad(phi_deg)   # conversión a radianes
            # señal 
            y = A * np.sin(2 * np.pi * f * t + phi)

        elif senal=="Coseno":
            # parámetros          
            T = 1 / f                    # período de la señal
            t_max = N_ciclos * T         # duración total en segundos
            fn = 40*f   # frecuencia de muestreo
            t = np.linspace(0, t_max,fn)  # vector tiempo de 0 a 1s
            phi = np.deg2rad(phi_deg)   # conversión a radianes
            # señal 
            y = A * np.cos(2 * np.pi * f * t + phi)

        elif senal=="Triangular":
            # parámetros          
            T = 1 / f                    # período de la señal
            t_max = N_ciclos * T         # duración total en segundos
            fn = 40*f   # frecuencia de muestreo
            t = np.linspace(0, t_max,fn)  # vector tiempo de 0 a 1s
            phi = np.deg2rad(phi_deg)   # conversión a radianes
            # señal 
            y = A * signal.sawtooth(2 * np.pi * f * t + phi, width=0.5)

        elif senal=="Cuadrada":
            # parámetros          
            T = 1 / f                    # período de la señal
            t_max = N_ciclos * T         # duración total en segundos
            fn = 40*f    # frecuencia de muestreo
            t = np.linspace(0, t_max,fn)  # vector tiempo de 0 a 1s
            phi = np.deg2rad(phi_deg)   # conversión a radianes
            # señal 
            y = A * signal.square(2 * np.pi * f * t + phi, duty=0.5)

        # gráfica
        plt.plot(t, y, label=f"{senal}: {N_ciclos} ciclos")
        plt.axhline(A, color='b', linestyle='--', label=f'Amplitud +{abs(A)}')
        plt.axhline(-A, color='r', linestyle='--', label=f'Amplitud -{abs(A)}')
        plt.xlabel("Tiempo [s]")
        plt.ylabel("Amplitud")
        plt.title(f"Señal {senal}")
        plt.grid(True)
        plt.legend(loc='lower right')
        plt.show()
    except ValueError:
        messagebox.showerror("Entrada inválida", "Verifica que todos los datos sean números válidos.")


#boton
boton_elemento =Button(Ventana, text="Comenzar" , command=realizarGrafica)
boton_elemento.place(x=400, y=150, width=100, height=30)

Ventana.mainloop()