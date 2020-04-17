""" 
tipos de Widgets 

Widget classes

Tkinter supports 15 core widgets:

Button : LLAMR EVENTOS GENERALMENTE O CALLBACKS 

Canvas : GRAFICAR 

Checkbutton : REPRESENTAR VARIABLES O HACER EL TOGGLE

Entry : TEXT BOX DE ENTRADA

Frame : CONTAINER SIRVE PARA AGRUPAR MAS WIDGETS

Label : MUESTRA UNA IMAGEN O TEXTO

Listbox : UNA LISTA DE ALTERNATIVAS 

Menu : PUEDE CREAR UN MENU

Message : AGRUPA CANTIDADES DE TEXTO MAS PROPIEDADES

Radiobutton : SELECCIONAR VARIABLES

Scale : MAS CONOCIDO COMO SLIDER 

Scrollbar : PERMITE DESLIZAR LAS PANATALLAS SE USA CON OTROS WIDGETS 


Toplevel : GENERA UNA VENTANA ESPECIAL FUERA DE LA QUE TENEMOS EN EL MASTER
"""
import tkinter  as tk
master = tk.Tk()
counter = 0 
def callback():
    global counter
    counter= counter+1
    print("aqui han presionado ",counter)

button = tk.Button(master,fg='blue', bg='green' , text="Pulsame " , width = 10, height=5,command = callback)
button.pack()






master.mainloop()