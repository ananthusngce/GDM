
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
import joblib
import traceback
from flask_restful import reqparse
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "hey"

@app.route('/predict', methods=['POST'])
def predict():
	lr = joblib.load("GDM_model.pkl")
	if lr:
		try:
			json = request.get_json()	 
			temp=list(json[0].values())
			vals=np.asarray(temp)
			input_data_reshaped = vals.reshape(1,-1)
			prediction = lr.predict(input_data_reshaped)
			print("here:",prediction)        
			return jsonify({'prediction': str(prediction[0])})

		except:        
			return jsonify({'trace': traceback.format_exc()})
	else:
		return ('No model here to use')
    


if __name__ == '__main__':
    app.run(debug=True)
    
