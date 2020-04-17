import tkinter  as tk
from PIL import Image , ImageTk
master = tk.Tk()

canvas = tk.Canvas(master,height = 500 , width = 500)
file1 = Image.open("Image.bmp")
render = ImageTk.PhotoImage(file1)
canvas.create_image((256, 256),image = render)
canvas.pack()
master.mainloop()