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

frame2 = Frame(root, highlightbackground="blue", 
               highlightcolor="red", highlightthickness=1, 
               width=100, height=100, bd= 10)
frame2.grid(row=1,column=1,padx=5,pady=5)


# -----------------------------------------------------
# -----------------------------------------------------

Label(frame2,text= y.head(5)).grid(row=0,column=0)

# -----------------------------------------------------
# -----------------------------------------------------

root.mainloop()

