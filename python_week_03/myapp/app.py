import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def get_data():
    #return requests.get('http://localhost:5000/hello').content
    return render_template("home.html")
