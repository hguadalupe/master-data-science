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
train_file = "../Data/TRAIN_scaled_CSV"
X_train = pd.read_csv(train_file).loc[:,'built_area':'OTHERS']
y_train = pd.read_csv(train_file)['DELAYED']

#Importamos unas tablas preparadas para escalar (medias y std):
means = pd.read_csv("../Data/TRAIN_mean_CSV",index_col=0).reset_index(drop=True)
stds = pd.read_csv("../Data/TRAIN_std_CSV",index_col=0).reset_index(drop=True)

#Fitting Algorithms:
knn =KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train,y_train)
logreg = LogisticRegression()
logreg.fit(X_train,y_train)		
randforest = RandomForestClassifier(max_depth=3,max_features=3, random_state=0)
randforest.fit(X_train, y_train)

#FUNCIONES:

def report():
	voting_result = voting()
	threshold =0.3
	response = []
	#---Debugging
	y_pred_kn =kneighbors()
	y_pred_lg=logreg()
	y_pred_rf=randfor()
	#---Debugging
	if voting_result >= threshold:
		response.append(1)
	else:
		response.append(0)
		
	mebox.showinfo("REPORT",[voting(), y_pred_kn, y_pred_lg,y_pred_rf,response ])
	
def voting():
	predictions = [kneighbors(),logreg(), randfor()]
	voting_result = 0 
	
	for i in predictions:
		if i== [1]:
			voting_result +=0.33
		else:
			pass
		
	return voting_result
	
def kneighbors():
	scaled = scaler()
	typo = typology()
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_kn= knn.predict(prediction)
	y_pred_kn
	return y_pred_kn

def logreg():
	scaled = scaler()
	typo = typology()
	logreg = LogisticRegression()
	logreg.fit(X_train,y_train)		
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_lg= logreg.predict(prediction)
	return y_pred_lg
	
def randfor():
	scaled = scaler()
	typo = typology()	
	pre_predict_args = scaled + typo 
	prediction = np.asarray(pre_predict_args).reshape(1,-1)
	y_pred_rf= randforest.predict(prediction)
	return y_pred_rf

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
	ba_scaled = uniqscaler(float(entrada1.get()),
									float(means.query("var == 'built_area'")['val']),
									float(stds.query("var == 'built_area'")['val']))
	mp_scaled = uniqscaler(float(entrada2.get()),
									float(means.query("var == 'modul_price'")['val']),
									float(stds.query("var == 'modul_price'")['val']))
	wd_scaled = uniqscaler(float(entrada3.get()),
									float(means.query("var == 'weeks_duration'")['val']),
									float(stds.query("var == 'weeks_duration'")['val']))	
	scaled =[ba_scaled,mp_scaled,wd_scaled]
	return scaled

def uniqscaler(float_,mean_,std_):
	uniqscaled = (float_ - mean_)/std_
	return uniqscaled
	
	
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

