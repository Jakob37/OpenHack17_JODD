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
        {'date':'2017-10-06', 'data':'Kalle har haft ont i tan'},
        {'date':'2017-10-05', 'data':'Kalle har varit hos tandlakaren och ar trott.'}
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
        {'name':'Bedtime', 'data':'Time for bed'},
        {'name':'Morning routine', 'data':'This is how we get started in the morning'}
    ]
    return json.dumps(checklists)


@app.route('/contacts/')
def contacts():
    contacts = [
        {'name':'Annika Gunhild', 'role':'Mother', 'phone':'070-456 23 XX', 'email':'annika.gunhild@careflow.com'},
        {'name':'Lars Haberg', 'role':'Father', 'phone':'070-456 35 XX', 'email':'lars.haberg@careflow.com'},
        {'name':'Linda Rohult', 'role':'Teacher', 'phone':'070-234 95 XX', 'email':'linda_rohult@teaching.com'},
        {'name':'Rin Lyholm', 'role':'Football trainer', 'phone':'070-132 78 XX', 'email':'rin_lyholm_87@football.com'},
    ]
    return json.dumps(contacts)