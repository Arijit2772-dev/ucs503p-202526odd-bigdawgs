import requests
import json

# The URL where your Flask app is running
url = 'http://127.0.0.1:5000/predict'

# Sample data for a laptop you want to predict the price of
laptop_data = {
    'Company': 'Apple',
    'TypeName': 'Ultrabook',
    'Inches': 13.3,
    'Ram': 8,
    'Weight': 1.37,
    'Touchscreen': 0,
    'Ips': 1,
    'ppi': 226.983005,
    'Cpu brand': 'Intel Core i5',
    'OpSys': 'macOS'
}

# Send the data as a POST request to the API
response = requests.post(url, json=laptop_data)

# Print the prediction returned by the API
print(response.json())