from flask import Flask, current_app, request, redirect, url_for, send_from_directory, render_template
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, world!'

events = [
        {'date':'2017-10-25', 'tags':['day care', 'medical care'], 'data':'Fell ill after eating .'},
        {'date':'2017-10-16', 'tags':['day care'], 'data':'Got scared by a car yesterday, had trouble calming down. '
                                 'Take it extra slowly when passing the road.'},
        {'date':'2017-10-08', 'tags':['family', 'day care'], 'data':'Teeth are much better now. Should be able to eat '
                                 'normally by now.'},
        {'date':'2017-10-06', 'tags':['family', 'day care'], 'data':'Kalle has had trouble with his teeth during the night.'
                                 ' He has not eaten properly, and is very tired. '
                                 'Grandmother is available today if he needs to be '
                                 'picked up extra early.'},
        {'date':'2017-10-05', 'tags':['day care'], 'data':'Kalle has been visiting the dentist. He is extra tired '
                                 'today. He should eat an extra banana after lunch. '
                                 'May be angry in the afternoon.'}
]

contact_list = [
    {'name':'Annika Gunhild', 'role':'Mother', 'phone':'070-456 23 XX', 'email':'annika.gunhild@careflow.com', 'labels': ['family']},
    {'name':'Lars Haberg', 'role':'Father', 'phone':'070-456 35 XX', 'email':'lars.haberg@careflow.com', 'labels': ['family']},
    {'name':'Linda Rohult', 'role':'Teacher', 'phone':'070-234 95 XX', 'email':'linda_rohult@teaching.com', 'labels': ['school']},
    {'name':'Rin Lyholm', 'role':'Football trainer', 'phone':'070-132 78 XX', 'email':'rin_lyholm_87@football.com', 'labels': ['daycare']},
]

@app.route('/current_events/')
def current_events():
    return json.dumps(events)


@app.route('/add_event/', methods=['POST'])
def add_event():

    if request.method == 'POST':
        json = request.get_json()
        labels = json['labels']
        data = json['data']
        date = time.strftime("%Y-%m-%d")

        events.insert(0, {'date':date, 'data':data})
        return '', 204


@app.route('/updated_events/')
def updated_events():
    events = [
        {'date':'2017-10-07', 'data':'Updated event added!'},
        {'date':'2017-10-25', 'data':'Fell ill after eating .'},
        {'date':'2017-10-16', 'data':'Got scared by a car yesterday, had trouble calming down. '
                                     'Take it extra slowly when passing the road.'},
        {'date':'2017-10-08', 'data':'Teeth are much better now. Should be able to eat '
                                     'normally by now.'},
        {'date':'2017-10-06', 'data':'Kalle has had trouble with his teeth during the night.'
                                     ' He has not eaten properly, and is very tired. '
                                     'Grandmother is available today if he needs to be '
                                     'picked up extra early.'},
        {'date':'2017-10-05', 'data':'Kalle has been visiting the dentist. He is extra tired '
                                     'today. He should eat an extra banana after lunch. '
                                     'May be angry in the afternoon.'}
    ]
    return json.dumps(events)

@app.route('/medicins/')
def medicins():
    meds = [
        {'name':'Paracetamol', 'data':'250mg 3 ggr om dagen. (8:00, 13:00, 17:00)'},
        {'name':'Sumatriptan', 'data':'50mg vid tecken av migrananfall.'}
    ]
    return json.dumps(meds)

@app.route('/checklists/')
def checklists():
    checklists = [
        {'name':'Bedtime', 'data':'Time for bed',
            'items':[
                {'item_text':'Brush teeth'},
                {'item_text':'Read bedtime story'},
                {'item_text':'Leave light on'}
            ]
        },
        {'name':'Morning routine', 'data':'This is how we get started in the morning',
            'items':[
                {'item_text':'Brush teeth'},
                {'item_text':'Make squared pancakes'},
                {'item_text':'Dont forget lunch box'}
            ]}
    ]
    return json.dumps(checklists)


@app.route('/contacts/')
def contacts():
    return json.dumps(contact_list)

@app.route('/add_contact/', methods=['POST'])
def add_contact():

    if request.method == 'POST':
        json = request.get_json()
        name = json['name']
        role = json['role']
        phone = json['phone']
        email = json['email']
        labels = json['labels']

        contact_list.insert(0, {'name':name, 'role':role, 'phone':phone, 'email':email, 'labels':labels })
        return '', 204
