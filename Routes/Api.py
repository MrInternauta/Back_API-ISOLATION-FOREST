# -*- coding: utf-8 -*-
import sys, os
from flask import request, jsonify, Flask
from IsolationForest import calculateAnomaly
import json 

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

#--------------
# calculateAnomaly
@app.route('/calculateAnomaly', methods=['GET'])
def getcalculateAnomaly():
    return (( calculateAnomaly() ))