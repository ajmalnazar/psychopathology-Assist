from flask import Flask
from dash import Dash
import dash_bootstrap_components as dbc
import pyrebase


# Connect to Firebase:
config={"apiKey":"AIzaSyCisrYSWTYnrGgsLu8z3caDbJ6xWksDVlM",
    "authDomain": "psychopathology-assist.firebaseapp.com",
    "projectId": "psychopathology-assist",
    "databaseURL": "https://psychopathology-assist-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "psychopathology-assist.appspot.com",
    "messagingSenderId": "356297272973",
    "appId": "1:356297272973:web:d6810ced1a97035dae7cc4",
    "measurementId": "G-TZ952BZC1D"}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Create a Flask server:
server = Flask(__name__)
server.config.from_pyfile('config.py')

# Create a Dash app:
app = Dash(__name__,
            server=server,
            routes_pathname_prefix='/dashboard/',
            external_stylesheets=[dbc.themes.LUX])


if __name__ == '__main__':
    from views import *
    app.run_server(debug=True)
