import matplotlib
matplotlib.use('Agg')
import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x=sp.symbols('x')
X = sp.symbols('x')
def taylor(f,x0,n):
    x = sp.symbols('x')
    p = 0
    for k in range(0,n+1):
        df    = sp.diff(f,x,k)
        df_x0 = df.evalf(subs={x:x0})
        T     = (df_x0*(x-x0)**k)/factorial(k)
        p     = p+T
    return p

def biseccion(f, a, b, tol):
  if(f(a)*f(b)>0):
    return '', 'La función no cumple el teorema en el intervalo'
  else:
    i=0
    while(np.abs(b-a>tol)):
      c = (a+b)/2
      if(f(a)*f(c)<0):
        b=c
        i += 1
      else:
        a=c
        i +=1

  return c,i

def p_simple(xd, yd):
  N= len(xd)
  M = np.zeros([N,N])
  P = 0

  for i in range(N):
    M[i,0] = 1
    for j in range(1, N):
      M[i,j]=M[i,j-1]*xd[i]
  ai=np.linalg.solve(M,yd)
  for i in range(N):
    P=P+ai[i]*X**i
  return f"El polinomio interpolante es: P(X)= ',{P}"


def lagrange(xd,yd):
  N= len(xd)
  P = 0
  for i in range(N):
    T = 1
    for j in range(N):
      if j != i:
        T = T*((X-xd[j])/(xd[i]-xd[j]))
    P=P+T*yd[i]
  return f"El polinomio es P(x): ', {sp.expand(P)}"

def mc(xd, yd):
  m = len(xd)
  sy = sum(yd)
  sx = sum(xd)
  sxy = sum(xd*yd)
  dsx = sum(xd**2)
  sx2 = sx**2
  a0 = ((sy*dsx)-(sx*sxy))/((m*dsx)-sx2)
  a1 = ((m*sxy)-(sx*sy))/((m*dsx)-sx2)
  return a0,a1

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
    # Botón para ejecutar la función
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

    # Función específica para la Opción 2
    def option2_function():
        value_option21 = entry_option21.get()
        f = lambda x: eval(value_option21)
        value_option22 = entry_option22.get()
        a  = eval(value_option22)
        value_option23 = entry_option23.get()
        b  = eval(value_option23)
        value_option24 = entry_option24.get()
        tol = eval(value_option24)

        # Lógica para la Opción 2
        tk.Label(frame, text=f"La raiz de la función f en radianes es: {biseccion(f, a, b, tol)}").pack()

    # Botón para ejecutar la función
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

    # Función específica para la Opción 2
    def option3_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))


        # Lógica para la Opción 2
        tk.Label(frame, text=f"{lagrange(xd,yd)}").pack()

    # Botón para ejecutar la función
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

    # Función específica para la Opción 2
    def option4_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))


        # Lógica para la Opción 2
        tk.Label(frame, text=f"{p_simple(xd,yd)}").pack()

    # Botón para ejecutar la función
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

    # Función específica para la Opción 2
    def option5_function():
        value_option21 = entry_option21.get()
        xd = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        yd  = np.array(eval(value_option22))

        a0, a1 = mc(xd,yd)
        # Lógica para la Opción 2
        tk.Label(frame, text=f"el modelo es {a0} + {a1}x").pack()

    # Botón para ejecutar la función
    tk.Button(frame, text="Ejecutar", command=option5_function).pack()

def create_option6_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Ingrese el arreglo entre corchetes y separado por coma").pack()
    tk.Label(frame, text="Datos en X:").pack()
    entry_option21 = tk.Entry(frame)
    entry_option21.pack()

    tk.Label(frame, text="Datos en Y:").pack()
    entry_option22 = tk.Entry(frame)
    entry_option22.pack()

    # Función específica para la Opción 2
    def option6_function():
        value_option21 = entry_option21.get()
        x = np.array(eval(value_option21))
        value_option22 = entry_option22.get()
        y  = np.array(eval(value_option22))
        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.9, hspace=0.9)
        plt.figure(figsize=(12,12))

        plt.subplot(331)
        plt.plot(x,y, 'ob', label='datos observados')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()


        plt.subplot(332)
        plt.plot(x**2,y, 'm*', label='x²')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()


        plt.subplot(333)
        plt.plot(x**3,y, 'cd', label='x³')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(334)
        plt.plot(np.sqrt(x),y, 'yp', label='√x')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(335)
        plt.plot(np.log(x),y, 'kv', label='log(x)')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(336)
        plt.plot(x,np.log(y), 'r*', label='log(y)')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(337)
        plt.plot(x,np.sqrt(y), 'g*', label='√y')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(338)
        plt.plot(np.log(x),np.log(y), 'rd', label='log(y) - log(x)')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

        plt.subplot(339)
        plt.plot(x,1/np.sqrt(y), 'co', label='1/√y')
        plt.xlabel('Peso')
        plt.ylabel('Pulso Cardiaco')
        plt.legend()

    # Botón para ejecutar la función
    tk.Button(frame, text="Ejecutar", command=option6_function).pack()

# Crear la ventana principal
root = tk.Tk()
root.geometry("500x500")
root.title("Formulario con Select")

# Crear el Combobox (Select)
combo = ttk.Combobox(root, values=["Seleccione una opción", "Taylor", "Bisección", "Lagrange", "Interpolación", "Minimos Cuadrados","Modelo a un solo termino"])
combo.set("Seleccione una opción")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", option_selected)

# Crear un marco para los widgets dinámicos
frame = tk.Frame(root)
frame.pack(pady=10)

# Iniciar el bucle principal
root.mainloop()
import tkinter as tk
from tkinter import ttk

def option_selected(event):
    selected_option = combo.get()

    # Limpiar los frames existentes
    for widget in frame.winfo_children():
        widget.destroy()

    if selected_option == "Opción 1":
        create_option1_widgets()
    elif selected_option == "Opción 2":
        create_option2_widgets()
    # Agregar más opciones según sea necesario

def create_option1_widgets():
    # Crea los widgets específicos para la Opción 1
    tk.Label(frame, text="Campo 1:").pack()
    entry1 = tk.Entry(frame)
    entry1.pack()

    tk.Label(frame, text="Campo 2:").pack()
    entry2 = tk.Entry(frame)
    entry2.pack()

    # Función específica para la Opción 1
    def option1_function():
        value1 = entry1.get()
        value2 = entry2.get()
        # Lógica para la Opción 1
        print(f"Opción 1 seleccionada. Valores: {value1}, {value2}")

    # Botón para ejecutar la función
    tk.Button(frame, text="Ejecutar", command=option1_function).pack()

def create_option2_widgets():
    # Crea los widgets específicos para la Opción 2
    tk.Label(frame, text="Campo único para la Opción 2:").pack()
    entry_option2 = tk.Entry(frame)
    entry_option2.pack()

    # Función específica para la Opción 2
    def option2_function():
        value_option2 = entry_option2.get()
        # Lógica para la Opción 2
        print(f"Opción 2 seleccionada. Valor: {value_option2}")

    # Botón para ejecutar la función
    tk.Button(frame, text="Ejecutar", command=option2_function).pack()

# Crear la ventana principal
root = tk.Tk()
root.title("Formulario con Select")

# Crear el Combobox (Select)
combo = ttk.Combobox(root, values=["Seleccione una opción", "Opción 1", "Opción 2"])
combo.set("Seleccione una opción")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", option_selected)

# Crear un marco para los widgets dinámicos
frame = tk.Frame(root)
frame.pack(pady=10)

