#ATENCION: Para hacer funcionar este script es necesario 
#configurar la apertura automática del formato ".pyw" con Python.exe.
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

#Importamos unas tablas preparadas para escalar (medias y std):
means = pd.read_csv("../Data/protomean_CSV")
stds = pd.read_csv("../Data/protostd_CSV")

#FUNCIONES:

def kneighbors():
	y_pred_kn = knn.predict(input_data)
	in5.set(y_pred_kn)    
	Label(frame1,text= "y_pred_kn").grid(row=5,column=0)

def summing():
	in5.set(float(entrada1.get()) + float(entrada3.get()) + float(entrada2.get()) +float(entrada4.get()))
	#Label(frame3,text= totalsum).grid(row=4,column=0)

def scaler(): 
	# ba_scaled = uniqscaler(float(entrada1.get()),float(means['built_area']),float(stds['built_area']))
	#in5.set(stds['built_area
	Label(frame3,text= type(means['built_area'])).grid(row=0,column=0)

def uniqscaler(float_,mean_,std_):
	uniqscaled = (float_ - mean_)/std_
	return uniqscaled
	

#Fitting:
def fitting():
	knn =KNeighborsClassifier(n_neighbors=10)
	knn.fit(X,y)

#Frames:
frame1 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame1.grid(row=0,column=0,padx=5,pady=5)

frame2 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame2.grid(row=1,column=1,padx=5,pady=5)

frame3 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame3.grid(row=1,column=0,padx=5,pady=5)

#Ins:
in1 = DoubleVar()
in2 = DoubleVar()
in3 = DoubleVar()
in4 = DoubleVar()
in5 = DoubleVar()

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

entrada4_label =Label(frame1, text="inserte aquí más números")
entrada4_label.grid(row=3,column=0,sticky="w",padx=5,pady=5)
entrada4 = Entry(frame1,justify="center",textvariable=in4)
entrada4.grid(row=3,column=1,padx=5,pady=5)

resultado_label = Label(frame1, text="Aquí irá el resultado")
resultado_label.grid(row=4,column=0,sticky="w",padx=5,pady=5)
resultado = Entry(frame1,justify="center",textvariable=in5)
resultado.grid(row=4,column=1,sticky="w",padx=5,pady=5)

# #Botones:
Button(frame2,text="con esto escalamos",command=scaler).grid(row=0,column=0)
# Button(frame1,text="con esto sumas",command=entrada1.get()).grid(row=3,column=0)

 #Variables de cálculo:
# means = X.loc[:,'built_area':'weeks_duration'].mean()
# stds = X.loc[:,'built_area':'weeks_duration'].std()


#Esto hay que meterlo en una función. Acabarás anidando funciones dentro de funciones.
#Pero merece la pena, porque no debes de confiar en el orden del script.

#modul_pri = stdscaler(entrada2.get(),means['modul_price'],stds['modul_price'])
#weeks_dur = stdscaler(entrada3.get(),means['weeks_duration'],stds['weeks_duration'])
#input_data =[built_ar,modul_pri,weeks_dur,0,0,0,1] #Falta tipología de edif.

# ent1 = entrada1.get()
# entrada1.set(ent1)

# -----------------------------------------------------
# -----------------------------------------------------

# Label(frame2,text= 'woooh').grid(row=0,column=0)

# -----------------------------------------------------
# -----------------------------------------------------

root.mainloop()

