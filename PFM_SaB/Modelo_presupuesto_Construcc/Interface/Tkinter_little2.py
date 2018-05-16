#ATENCION: Para hacer funcionar este script es necesario 
#configurar la apertura automática del formato ".pyw" con Python.exe.
from tkinter import *
from tkinter import messagebox as mebox
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
means = pd.read_csv("../Data/protomean_CSV",index_col=0).T.reset_index()
stds = pd.read_csv("../Data/protostd_CSV",index_col=0).T.reset_index()
means=means.rename(columns = {'index':'built_area'})
stds=stds.rename(columns = {'index':'built_area'})

#FUNCIONES:

def report():
	kneighbors_prediction = kneighbors()
	logreg_prediction = logreg()
	randfor_prediction = randfor()
	mebox.showinfo("REPORT",[kneighbors_prediction,logreg_prediction,randfor_prediction])

def kneighbors():
	scaled = scaler()
	typo = typology()
	knn =KNeighborsClassifier(n_neighbors=10)
	knn.fit(X,y)	
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_kn= knn.predict(prediction)
	answer = answerer(y_pred_kn)
	return answer
	#in5.set(y_pred_kn)    
	#Label(frame3,text= answer).grid(row=5,column=0)

def logreg():
	scaled = scaler()
	typo = typology()
	logreg = LogisticRegression()
	logreg.fit(X,y)	
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_lg= logreg.predict(prediction)
	answer = answerer(y_pred_lg)
	return answer
	
def randfor():
	scaled = scaler()
	typo = typology()
	randforest = RandomForestClassifier(max_depth=2, random_state=0)
	randforest.fit(X, y)
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_rf= randforest.predict(prediction)
	answer = answerer(y_pred_rf)
	return answer

def typology():
	if in6.get() == 0:
		return [1,0,0,0]
	elif in6.get() == 1:
		return [0,1,0,0]
	elif in6.get() == 2:
		return [0,0,1,0]
	else:
		return [0,0,0,1]
	
def summing():
	totalsum = float(entrada1.get()) + float(entrada3.get()) + float(entrada2.get())
	resting()
	Label(frame3,text= totalsum).grid(row=2,column=0)

def resting():
	totalsum = float(entrada1.get()) - float(entrada3.get()) -float(entrada2.get())
	Label(frame3,text= totalsum).grid(row=1,column=0)
	
def scaler(): 
	ba_scaled = uniqscaler(float(entrada1.get()),float(means['built_area']),float(stds['built_area']))
	mp_scaled = uniqscaler(float(entrada2.get()),float(means['modul_price']),float(stds['modul_price']))
	wd_scaled = uniqscaler(float(entrada3.get()),float(means['weeks_duration']),float(stds['weeks_duration']))	
	scaled =[ba_scaled,mp_scaled,wd_scaled]
	return scaled

def uniqscaler(float_,mean_,std_):
	uniqscaled = (float_ - mean_)/std_
	return uniqscaled
	
def answerer(a):
	if a == [1]:
		return "yeah"
	else:
		return "nope"
	
	

#Frames:
frame1 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame1.grid(row=0,column=0,padx=5,pady=5)

frame_typology = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame_typology .grid(row=1,column=0,padx=5,pady=5,sticky="w")

frame2 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame2.grid(row=2,column=1,padx=5,pady=5)

frame3 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame3.grid(row=2,column=0,padx=5,pady=5)

#Ins:
in1 = DoubleVar()
in2 = DoubleVar()
in3 = DoubleVar()
in4 = DoubleVar()
in5 = DoubleVar()
in6 = IntVar()

#Entradas de texto:
entrada1_label =Label(frame1, text="Gross floor area of the building project")
entrada1_label.grid(row=0,column=0,sticky="w",padx=5,pady=5)
entrada1 = Entry(frame1,justify="center",textvariable=in1)
entrada1.grid(row=0,column=1,padx=5,pady=5)


entrada2_label =Label(frame1, text="Estimated construction cost per squared meter")
entrada2_label.grid(row=1,column=0,sticky="w",padx=5,pady=5)
entrada2 = Entry(frame1,justify="center",textvariable=in2)
entrada2.grid(row=1,column=1,padx=5,pady=5)

entrada3_label =Label(frame1, text="Construction duration estimated in weeks")
entrada3_label.grid(row=2,column=0,sticky="w",padx=5,pady=5)
entrada3 = Entry(frame1,justify="center",textvariable=in3)
entrada3.grid(row=2,column=1,padx=5,pady=5)

tipology_label = Label(frame_typology, text="Please, select the typology of the building:")
tipology_label.grid(row=3,column=0,sticky="w",padx=5,pady=5)

resultado_label = Label(frame1, text="Aquí irá el resultado")
resultado_label.grid(row=8,column=0,sticky="w",padx=5,pady=5)
resultado = Entry(frame1,justify="center",textvariable=in5)
resultado.grid(row=8,column=1,sticky="w",padx=5,pady=5)


# #Botones:
Button(frame2,text="con esto escalamos",command=report).grid(row=0,column=0,sticky="w")
Radiobutton(frame_typology,text="DETACHED HOUSING", variable= in6,value=0).grid(row=4,column=1,sticky="w")
Radiobutton(frame_typology,text="COLLECTIVE HOUSING", variable= in6,value=1).grid(row=5,column=1,sticky="w")
Radiobutton(frame_typology,text="COMMERCIAL", variable= in6,value=2).grid(row=6,column=1,sticky="w")
Radiobutton(frame_typology,text="OTHERS", variable= in6,value=3).grid(row=7,column=1,sticky="w")
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

