#ATENCION: Para hacer funcionar este script es necesario configurar la apertura automática del formato ".pyw" con Python.exe.
from tkinter import *
root = Tk()
root.title("CBDD_By_Especialista3d.com")

#Declaramos variables dinámicas:
texto1 = StringVar()
texto1.set("texto dinámico a la espera")


#Presentación inicial:
presentac = Label(root,text="""This solution is made by a professional construction manager who wants to share his knowledge. 
              This software will help you to get easily a second opinion about 
              how accurate is a construction planning and its 
              typical parameters.""")
presentac.pack(anchor="center",ipady=15)
presentac.config(font=(15))

#Entradas de texto:
entrada1 = Entry(root)
entrada1.pack(side="right",ipadx=0) #No sé cómo separarlo del lado derecho.
entrada1_label =Label(root, text="inserte aquí su texto")
entrada1_label.pack(side="left",ipadx=20)

t1_label = Label(root)
t1_label.pack()#No sé cómo anclarlo a la parte de abajo. anchor="s" no funciona.
t1_label.config(textvariable=texto1)


##ESTO ES POR SI QUEREMOS HACER UN FRAME, PERO COMPLICA MUCHO.
#frame = Frame(root, width=600, height=320)
#frame.pack(fill='y')
#frame.config(bg="lightblue") #Color de fondo
#frame.config(relief="sunken")

root.mainloop()
