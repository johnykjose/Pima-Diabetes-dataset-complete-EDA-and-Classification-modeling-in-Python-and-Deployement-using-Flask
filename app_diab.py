# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:12:03 2020

@author: johny.jose
"""
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('RF_model_final.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    prediction_texts='em ra ravatle'
    if request.method == 'POST':
        pregnant=int(request.form['pregnant'])
        bp=float(request.form['bp'])
        insulin=float(request.form['insulin'])
        tricep=float(request.form['tricep'])
        glucose=float(request.form['glucose'])
        bmi=float(request.form['bmi'])
        age=float(request.form['age'])
        dpf=float(request.form['dpf'])
        
        prediction=model.predict([[pregnant,glucose,bp,tricep,insulin,bmi,dpf,age]])
        output=prediction
#        if (pregnant>0 & age<10):
#            return(render_template('index.html',prediction_texts='how could you be pregnant at this age enter correct details ')
        if output==1:
            return render_template('index.html',prediction_texts="You are diabetic, Please start medication")
        else:
            return render_template('index.html',prediction_texts="No need to worry, your not diabetic")
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=False)