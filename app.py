import matplotlib
matplotlib.use('Agg')
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mods import *

def option_selected(event):
    selected_option = combo.get()

    # Limpiar los frames existentes
    for widget in frame.winfo_children():
        widget.destroy()

    if selected_option == "Taylor":
        create_option1_widgets()
    elif selected_option == "Bisección":
        create_option2_widgets()
    elif selected_option == "Lagrange":
        create_option3_widgets()
    elif selected_option == "Interpolación":
        create_option4_widgets()
    elif selected_option == "Minimos Cuadrados":
        create_option5_widgets()
    elif selected_option == "Modelo a un solo termino":
        create_option6_widgets()
    elif selected_option == "Euler":
        create_option7_widgets()
    elif selected_option == "Runge-Kutta Orden 4":
        create_option8_widgets()
    elif selected_option == "Trapecio":
        create_option9_widgets()
    elif selected_option == "Simpson 1/3":
        create_option10_widgets()
    elif selected_option == "Simpson 3/8":
        create_option11_widgets()
    # Agregar más opciones según sea necesario

def create_option1_widgets():
    # Crea los widgets específicos para la Opción 1
    tk.Label(frame, text="Función (en formato lambda):").pack()
    entry1 = tk.Entry(frame)
    entry1.pack()

    tk.Label(frame, text="X0:").pack()
    entry2 = tk.Entry(frame)
    entry2.pack()

    tk.Label(frame, text="n:").pack()
    entry3 = tk.Entry(frame)
    entry3.pack()

    # Función específica para la Opción 1
    def option1_function():
        value1 = entry1.get()
        value2 = entry2.get()
        value3 = entry3.get()
        # Lógica para la Opción 1
        tk.Label(frame, text=f"{taylor(value1, value2, value3)}").pack()
    
    tk.Button(frame, text="Ejecutar", command=option1_function).pack()

def create_option2_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="Tolerancia:").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()

    
    def option2_function():
        value_option21 = entry_option21.get()
        f = lambda x: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        tol = eval(value_option24)

        tk.Label(frame, text=f"La raiz de la función f en radianes es: {biseccion(f, a, b, tol)}").pack()

    
    tk.Button(frame, text="Ejecutar", command=option2_function).pack()

def create_option3_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Ingrese el arreglo entre corchetes y separado por coma").pack()
    tk.Label(frame, text="Datos en X:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="Datos en Y:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    
    def option3_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))


        tk.Label(frame, text=f"{lagrange(xd,yd)}").pack()

    
    tk.Button(frame, text="Ejecutar", command=option3_function).pack()

def create_option4_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Ingrese el arreglo entre corchetes y separado por coma").pack()
    tk.Label(frame, text="Datos en X:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="Datos en Y:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    
    def option4_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))


        tk.Label(frame, text=f"{p_simple(xd,yd)}").pack()

    
    tk.Button(frame, text="Ejecutar", command=option4_function).pack()

def create_option5_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Ingrese el arreglo entre corchetes y separado por coma").pack()
    tk.Label(frame, text="Datos en X:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="Datos en Y:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    
    def option5_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))

        a0, a1 = mc(xd,yd)
        tk.Label(frame, text=f"el modelo es {a0} + {a1}x").pack()

    
    tk.Button(frame, text="Ejecutar", command=option5_function).pack()

def create_option6_widgets():

    tk.Label(frame, text="Ingrese el arreglo entre corchetes y separado por coma").pack()
    tk.Label(frame, text="Datos en X:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="Datos en Y:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    def option6_function():
        value_option21 = entry_option21.get()
        x = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        y  = np.array(eval(value_option22))

        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.9, hspace=0.9)
        fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))
        fig.suptitle('Análisis de Datos')

        axes[0, 0].plot(x, y, 'ob', label='datos observados')
        axes[0, 0].set_title('Datos Observados')
        axes[0, 0].set_xlabel('Peso')
        axes[0, 0].set_ylabel('Pulso Cardiaco')
        axes[0, 0].legend()

        axes[0, 1].plot(x**2, y, 'm*', label='x²')
        axes[0, 1].set_title('x²')
        axes[0, 1].set_xlabel('Peso')
        axes[0, 1].set_ylabel('Pulso Cardiaco')
        axes[0, 1].legend()

        axes[0, 2].plot(x**3, y, 'cd', label='x³') 
        axes[0, 2].set_title('x³')
        axes[0, 2].set_xlabel('Peso')
        axes[0, 2].set_ylabel('Pulso Cardiaco')
        axes[0, 2].legend()

        axes[1, 0].plot(np.sqrt(x), y, 'yp', label='√x')
        axes[1, 0].set_title('√x')
        axes[1, 0].set_xlabel('Peso')
        axes[1, 0].set_ylabel('Pulso Cardiaco')
        axes[1, 0].legend()

        axes[1, 1].plot(np.log(x), y, 'kv', label='log(x)')
        axes[1, 1].set_title('log(x)')
        axes[1, 1].set_xlabel('Peso')
        axes[1, 1].set_ylabel('Pulso Cardiaco')
        axes[1, 1].legend()

        axes[1, 2].plot(x,np.log(y), 'r*', label='log(y)')
        axes[1, 2].set_title('log(y)')
        axes[1, 2].set_xlabel('Peso')
        axes[1, 2].set_ylabel('Pulso Cardiaco')
        axes[1, 2].legend()

        axes[2, 0].plot(x,np.sqrt(y), 'g*', label='√y')
        axes[2, 0].set_title('√y')
        axes[2, 0].set_xlabel('Peso')
        axes[2, 0].set_ylabel('Pulso Cardiaco')
        axes[2, 0].legend()

        axes[2, 1].plot(np.log(x),np.log(y), 'rd', label='log(y) - log(x)')
        axes[2, 1].set_title('log(y) - log(x)')
        axes[2, 1].set_xlabel('Peso')
        axes[2, 1].set_ylabel('Pulso Cardiaco')
        axes[2, 1].legend()

        axes[2, 2].plot(x,1/np.sqrt(y), 'co', label='1/√y')
        axes[2, 2].set_title('1/√y')
        axes[2, 2].set_xlabel('Peso')
        axes[2, 2].set_ylabel('Pulso Cardiaco')
        axes[2, 2].legend()

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    tk.Button(frame, text="Ejecutar", command=option6_function).pack()

def create_option7_widgets():

    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="h").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()

    tk.Label(frame, text="Condición Inicial:").pack()
    entry_option25 = tk.Entry(frame)
    entry_option25.pack()

    def option7_function():
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))
        value_option21 = entry_option21.get()
        f = lambda t,y: eval(value_option21)
        value_option22 = entry_option22.get()
        a = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        h = eval(value_option24)
        value_option25 = entry_option25.get()
        co = eval(value_option25)
        t,e = Euler(f, a ,b,h, co)
        axes.plot(t, e, 'ob', label='Aproximación con Euler')
        axes.set_title('Datos Observados')
        axes.legend()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
    tk.Button(frame, text="Ejecutar", command=option7_function).pack()

def create_option8_widgets():
    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="h").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()

    tk.Label(frame, text="Condición Inicial:").pack()
    entry_option25 = tk.Entry(frame)
    entry_option25.pack()

    
    def option8_function():
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))
        value_option21 = entry_option21.get()
        f = lambda t,y: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        h = eval(value_option24)
        value_option25 = entry_option25.get()
        co = eval(value_option25)
        t,e = Runge4(f, a, b, h , co)
        axes.plot(t, e, 'or', label='Aproximación con RungeKutta Orden 4')
        axes.set_title('Datos Observados')
        axes.legend()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        

    
    tk.Button(frame, text="Ejecutar", command=option8_function).pack()

def create_option9_widgets():
    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="n").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()
    
    def option9_function():
        value_option21 = entry_option21.get()
        f = lambda x: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        n = eval(value_option24)
        result = Trapecio(f, a, b, n)
        tk.Label(frame, text=f"El resultado de utilizar trapecio es {result}").pack()
        
    tk.Button(frame, text="Ejecutar", command=option9_function).pack()

def create_option10_widgets():
    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="n").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()
    
    def option10_function():
        value_option21 = entry_option21.get()
        f = lambda x: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        n = eval(value_option24)
        result = sims13(f, a, b, n)
        tk.Label(frame, text=f"El resultado de utilizar Simpson 1/3 es {result}").pack()
        
    tk.Button(frame, text="Ejecutar", command=option10_function).pack()

def create_option11_widgets():
    tk.Label(frame, text="Función:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="a:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    tk.Label(frame, text="b:").pack()
    entry_option23 = tk.Entry(frame)
    entry_option23.pack()

    tk.Label(frame, text="n").pack()
    entry_option24 = tk.Entry(frame)
    entry_option24.pack()
    
    def option11_function():
        value_option21 = entry_option21.get()
        f = lambda x: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        n = eval(value_option24)
        result = sims38(f, a, b, n)
        tk.Label(frame, text=f"El resultado de utilizar Simpson 3/8 es {result}").pack()
        
    tk.Button(frame, text="Ejecutar", command=option11_function).pack()

root = tk.Tk()
root.geometry("500x500")
root.title("Formulario con Select")
comboValues = ["Seleccione una opción", "Taylor", "Bisección", "Lagrange", "Interpolación", "Minimos Cuadrados","Modelo a un solo termino", "Euler", "Runge-Kutta Orden 4", "Trapecio", "Simpson 1/3", "Simpson 3/8"]
combo = ttk.Combobox(root, values=comboValues)
combo.set("Seleccione una opción")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", option_selected)


frame = tk.Frame(root)
frame.pack(pady=10)


root.mainloop()
