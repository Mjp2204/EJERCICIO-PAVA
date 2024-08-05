from tkinter import *

root = Tk()
root.title = "TRAVELER"
root.geometry = ('10000*1000')

def bienvenida():
    print("Bienvenido a Travelers")

"""boton = Button(root, text="Bienvenida", command=bienvenida)"""
boton = Button(root, text='Bienvenida', command=bienvenida)

root.mainloop()