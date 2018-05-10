#ATENCION: Para hacer funcionar este script es necesario configurar la apertura automática del formato ".pyw" con Python.exe.
from tkinter import *
root = Tk()
root.title("CBDD_By_Especialista3d.com")

import pandas as pd
import random as rnd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt


#ML tools:
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#Load DBs:
train_file = "../Data/prototrain_CSV"
train_tab = pd.read_csv(train_file)
y = train_tab['DELAYED']
X = train_tab.loc[:,'built_area':'OTHERS']

#Fitting:
knn =KNeighborsClassifier(n_neighbors=10)
knn.fit(X,y)

#Frames:
frame1 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame1.grid(row=0,column=0,padx=5,pady=5)

frame2 = Frame(root)
frame2.grid(row=1,column=1,padx=5,pady=5)

#Ins:
in1 = StringVar()
in2 = StringVar()
in3 = StringVar()

#Entradas de texto:
entrada1_label =Label(frame1, text="inserte aquí sus numeros!")
entrada1_label.grid(row=0,column=0,sticky="w",padx=5,pady=5)
entrada1 = Entry(frame1,justify="center",textvariable=in1)
entrada1.grid(row=0,column=1,padx=5,pady=5)


entrada2_label =Label(frame1, text="inserte aquí más números")
entrada2_label.grid(row=1,column=0,sticky="w",padx=5,pady=5)
entrada2 = Entry(frame1,justify="center",textvariable=in2)
entrada2.grid(row=1,column=1,padx=5,pady=5)

entrada3_label =Label(frame1, text="inserte aquí más números")
entrada3_label.grid(row=2,column=0,sticky="w",padx=5,pady=5)
entrada3 = Entry(frame1,justify="center",textvariable=in3)
entrada3.grid(row=2,column=1,padx=5,pady=5)

# entradaResult_label =Label(frame1, text="Aquí el resultado!")
# entradaResult_label.grid(row=3,column=0,sticky="w",padx=5,pady=5)
# entradaResult= Entry(frame1,justify="center",textvariable=result)
# entradaResult.grid(row=3,column=1,padx=5,pady=5)

#FUNCIONES:
def kneighbors():
    y_pred_kn = knn.predict(input_data)
    Label(frame1,text= "y_pred_kn").grid(row=5,column=0)


def stdscaler(i,mean_,std_): 
    scaled = (i - mean_)/std_
    return scaled


def crea_label():
    Label(frame1,text= "wow! has clicado!").grid(row=3,column=0)
    
	
#Botones:
Button(frame1,text="púlsame",command=crea_label).grid(row=3,column=1)
Button(frame2,text="con esto sumas",command=kneighbors).grid(row=2,column=1)

#Variables a almacenar:
	
colnames = ['built_area', 'modul_price', 'weeks_duration', 'DETACHED', 'COLLECTIVE', 'COMMERCIAL', 'OTHERS', 'DELAYED']
#predict_tab = pd.Dataframe([XXX],columns=colnames)


means = X.loc[:,'built_area':'weeks_duration'].mean()
stds = X.loc[:,'built_area':'weeks_duration'].std()

built_ar = stdscaler(float(in1),means['built_area'],stds['built_area'])
modul_pri = stdscaler(float(in2),means['modul_price'],stds['modul_price'])
weeks_dur = stdscaler(float(in3),means['weeks_duration'],stds['weeks_duration'])
input_data =[built_ar,modul_pri,weeks_dur,0,0,0,1] #Falta tipología de edif.


#t1_label = Label(root)
#t1_label.pack()#No sé cómo anclarlo a la parte de abajo. anchor="s" no funciona.
#t1_label.config(textvariable=texto1)


##ESTO ES POR SI QUEREMOS HACER UN FRAME, PERO COMPLICA MUCHO.
#frame = Frame(root, width=600, height=320)
#frame.pack(fill='y')
#frame.config(bg="lightblue") #Color de fondo
#frame.config(relief="sunken")

root.mainloop()
