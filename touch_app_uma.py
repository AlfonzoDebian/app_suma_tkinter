# 🐍 Importar todo el módulo Tkinter
from tkinter import *
import os


a = 0
# 🪟 Crear la ventana principal
ventana_principal = Tk()
ventana_principal.title("Colombia")         # Título de la ventana
ventana_principal.geometry("800x500")       # Tamaño de la ventana: 800px ancho x 600px alto
ventana_principal.resizable(0, 0)           # No permitir redimensionar la ventana
ventana_principal.config(bg="Black")        # Color de fondo de la ventana

a = StringVar()
b = StringVar()
c = IntVar()




# 🧱 Crear el primer Frame (una sección dentro de la ventana)
Frame_1 = Frame(ventana_principal)          # Asociar el Frame a la ventana principal
Frame_1.config(bg="White", width=780, height=240)  # Color amarillo, tamaño 800x380
Frame_1.place(x=10, y=10) 

Frame_2 = Frame(ventana_principal)          # Asociar el Frame a la ventana principal
Frame_2.config(bg="White", width=780, height=120)  # Color amarillo, tamaño 800x380
Frame_2.place(x=10, y=260) 


Frame_3 = Frame(ventana_principal)          # Asociar el Frame a la ventana principal
Frame_3.config(bg="White", width=780, height=100)  # Color amarillo, tamaño 800x380
Frame_3.place(x=10, y=390) 


logo = PhotoImage(file = "img/btn-suma.png")
label_logo = Label(Frame_1, image=logo)
label_logo.place(x=10, y=10)





# titulo = label(fr)
titulo = Label(Frame_1, text = "Colegio San Jose Guanentá")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=390, y=10)                  # Ubicar el Frame en la ventana (ligeramente hacia arriba)

titulo2 = Label(Frame_1, text = "SUMA DE ENTEROS: ")
titulo2.config(bg="ivory2", fg="blue", font=("Arial", 16))
titulo2.place(x=390, y=70)   



label_a = Label(Frame_1, text = "a = ")
label_a.config(bg="ivory2", fg="blue", font=("Arial", 16))
label_a.place(x=390, y=120)  

label_a = Label(Frame_1, text = "b = ")
label_a.config(bg="ivory2", fg="blue", font=("Arial", 16))
label_a.place(x=585, y=120)  

#Boton
img_bt_sumar = PhotoImage(file = "img/boton_sumar.png")
bt_sumar = Button(Frame_2, image = img_bt_sumar, width = 105, height = 105)
bt_sumar.place(x=116, y=7)

img_bt_borrar = PhotoImage(file = "img/boton_borrar.png")
bt_borrar = Button(Frame_2, image = img_bt_borrar, width = 105, height = 105)
bt_borrar.place(x=337, y=7)

img_bt_salir = PhotoImage(file = "img/boton_salir.png")
bt_salir = Button(Frame_2, image = img_bt_salir, width = 105, height = 105)
bt_salir.place(x=558, y=7)

# Area resultado

t_resultado = Text(Frame_3, width =50, height =3)
t_resultado.config(bg="green", fg="white", font= ("Courier", 20))
t_resultado.pack()



#el focus
entry_1 = Entry(Frame_1, width=4, textvariable=a)
entry_1.config(font=("Arial", 20), justify=CENTER)
entry_1.focus_set()
entry_1.place(x=487, y=120)

entry_2 = Entry(Frame_1, width=4, textvariable=b)
entry_2.config(font=("Arial", 20), justify=CENTER)
entry_2.focus_set()
entry_2.place(x=682, y=120)

f1 = Label(Frame_1, text = "Especialidad de Sistemas")
f1.config(bg="yellow", fg="blue", font=("Arial", 12))
f1.place(x=390, y=40)                  



# ▶️ Ejecutar el bucle principal de la ventana (mostrarla y mantenerla abierta)
ventana_principal.mainloop()
