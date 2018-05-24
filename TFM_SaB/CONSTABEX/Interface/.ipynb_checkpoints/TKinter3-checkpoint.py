#ATENCION: Para hacer funcionar este script es necesario configurar la apertura automática del formato ".pyw" con Python.exe.
from tkinter import *
root = Tk()
root.title("CBDD_By_Especialista3d.com")

import pandas as pd
import random as rnd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
plt.style.use('ggplot')
%matplotlib inline

#ML tools:
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#Load DBs:
train_file =
test_file =
train_tab = pd.read_csv()


y = train_tab['DELAYED']
X = train_tab.loc[:,'built_area':'OTHERS']

#K-NEIGHBORS:
def kneighbors:
    knn =KNeighborsClassifier(n_neighbors=10)
    knn.fit(X,y)
    y_pred_kn = knn.predict(X_test)
    print("KNEIGHBORS REGRESSION MODEL: ")
    print("Basic scoring: " +str(knn.score(X_test,y_test)))
    print("Normalized accuracy: " +str(accuracy_score(y_test,y_pred_kn)))
    print("Net accuracy: " +str(accuracy_score(y_test,y_pred_kn, normalize = False)) + 
          " over " + str(y_test.size) + " samples.")

#Variables a almacenar:
means = X.loc[:,'built_area':'weeks_duration'].mean()
stds = X.loc[:,'built_area':'weeks_duration'].std()

def stdscaler(i): 
    scaled = (i - mean)/std
    return scaled

colnames = ['built_area', 'modul_price', 'weeks_duration', 'DETACHED', 'COLLECTIVE', 'COMMERCIAL', 'OTHERS', 'DELAYED']
predict_tab = pd.Dataframe([XXX],columns=colnames)
input_data =[list of normalized data] #Falta relacionar con los parámetros de abajo antes de meterlo en el DF.
built_ar = StringVar()
modul_pri = StringVar()
weeks_dur = StringVar()

from functions import sumar

def crea_label():
    Label(frame1,text= "wow! has clicado!").grid(row=3,column=0)
    
#Presentación inicial:
#presentac = Label(root,text="""This solution is made by a professional construction manager who wants to share his knowledge. 
#              This software will help you to get easily a second opinion about 
#              how accurate is a construction planning and its 
#              typical parameters.""")
#presentac.pack(anchor="center",ipady=15)
#presentac.config(font=(15))

#Frames, marco:
frame1 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame1.grid(row=0,column=0,padx=5,pady=5)

frame2 = Frame(root)
frame2.grid(row=1,column=1,padx=5,pady=5)



#Entradas de texto:
entrada1 = Entry(frame1,justify="center",textvariable=in1)
entrada1.grid(row=0,column=1,padx=5,pady=5)
entrada1_label =Label(frame1, text="inserte aquí sus numeros!")
entrada1_label.grid(row=0,column=0,sticky="w",padx=5,pady=5)

entrada2 = Entry(frame2,justify="center",textvariable=in2)
entrada2.grid(row=1,column=1,padx=5,pady=5)
entrada2.config(justify="center")
entrada2_label =Label(frame2, text="inserte aquí más números")
entrada2_label.grid(row=1,column=0,sticky="w",padx=5,pady=5)

entradaResult= Entry(frame2,justify="center",textvariable=result)
entradaResult.grid(row=3,column=1,padx=5,pady=5)
entradaResult_label =Label(frame2, text="Aquí el resultado!")
entradaResult_label.grid(row=3,column=0,sticky="w",padx=5,pady=5)


#Botones:
Button(frame1,text="púlsame",command=crea_label).grid(row=3,column=1)
Button(frame2,text="con esto sumas",command=sumar).grid(row=2,column=1)


#t1_label = Label(root)
#t1_label.pack()#No sé cómo anclarlo a la parte de abajo. anchor="s" no funciona.
#t1_label.config(textvariable=texto1)


##ESTO ES POR SI QUEREMOS HACER UN FRAME, PERO COMPLICA MUCHO.
#frame = Frame(root, width=600, height=320)
#frame.pack(fill='y')
#frame.config(bg="lightblue") #Color de fondo
#frame.config(relief="sunken")

root.mainloop()
