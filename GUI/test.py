from flask import Flask, render_template, request
import numpy as np
import pickle 
model = pickle.load(open('crop.pkl', 'rb'))

test = Flask(__name__)


@test.route("/home")
def home():
    return render_template('main.html')

@test.route('/predict', methods=['POST'])
def predict():
    N = request.form['N']
    P = request.form['P']
    K = request.form['K']
    Temp = request.form['Temp']
    Humidity = request.form['Humidity']
    pH = request.form['pH']
    Rainfall = request.form['Rainfall']
    params = np.array([[N, P, K, Temp, Humidity, pH, Rainfall]])  
    pred = model.predict(params)
    return render_template('main.html',crop=pred[0])
    

if __name__ =="__main__":
    test.run(debug = True)