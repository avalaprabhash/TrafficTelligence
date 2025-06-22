import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('D:/SmartBridge-Project/model.pkl', 'rb'))
scale = pickle.load(open('C:/Users/SmartbridgePC/Desktop/AIML/Guided projects/scale.pkl', 'rb'))

@app.route('/')  # route to display the home page
def home():
    return render_template('index.html')  # rendering the home page

@app.route('/predict', methods=["POST", "GET"])  # route to show the predictions in a web UI
def predict():
    # reading the inputs given by the user
    input_feature = [float(x) for x in request.form.values()]
    features_values = [np.array(input_feature)]
    # Update the column names to match your model's expected input order
    names = ['temp', 'rain', 'snow', 'holiday', 'weather', 'year', 'month', 'day', 'hours', 'minutes', 'seconds']
    data = pd.DataFrame(features_values, columns=names)
    data = scale.transform(data)
    data = pd.DataFrame(data, columns=names)
    # predictions using the loaded model file
    prediction = model.predict(data)
    text = "Estimated Traffic Volume is : "
    return render_template("index.html", prediction_text=text + str(prediction[0]))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)