import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle

# Initialize the flask app
app = Flask(__name__)

# Load the trained pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Define a route for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Convert the incoming JSON data to a pandas DataFrame
    # The keys in your JSON ('Company', 'TypeName', etc.) must match these columns
    input_data = pd.DataFrame([data])
    
    # Make a prediction
    prediction_log = pipe.predict(input_data)[0]
    
    # Since you trained on the log of the price, convert it back
    prediction = np.exp(prediction_log)

    # Return the result as JSON
    return jsonify({'predicted_price': prediction})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5000)