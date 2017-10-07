from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/current_events/')
def current_events():
    events = [
        {'date':'2017-10-06', 'data':'Kalle har haft ont i tån'},
        {'date':'2017-10-05', 'data':'Kalle har varit hos tandläkaren och ar trott.'}
    ]
    return json.dumps(events)

@app.route('/medicins/')
def medicins():
    meds = [
        {'name':'Paracetamol', 'data':'250mg 3 ggr om dagen.'},
        {'name':'Sumatriptan', 'data':'50mg vid tecken av migrananfall.'}
    ]
    return json.dumps(meds)

@app.route('/checklists/')
def checklists():
    checklists = [
                
    ]
    return json.dumps(checklists)


