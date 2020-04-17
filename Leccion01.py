# install conda install -c anaconda tk

# recuerda  cambiar el ambiente o workspace en el cual instalaste tkinter 

import tkinter as tk

# Dos formas de importar las librerias 
# PRIMERA ES USANDO  import ------ import tkinter as tk
# LA SEGUNRDA USANDO from tkinter import *
# veamos la diferencia 


# 1 .- Creamos la ventana 
root = tk.Tk()

# 2.- Creando un Widget 
#99ff99
label = tk.Label(root,text = 'Mi primer label' ,bg='#99ff99' , fg = '#1a53ff'  , height = 20 , width=40 , font = ("Serif", 16) )
label.pack()
root.mainloop()

#root.destroy()

