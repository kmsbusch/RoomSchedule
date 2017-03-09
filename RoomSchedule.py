from tinydb import TinyDB, Query
from flask import Flask, jsonify, render_template, request
#from flask.ext.pymongo import PyMongo

# client = MongoClient('localhost:27017')

# db = client.RoomSchedule


# http://webdesignfromscratch.com/html-css/datasheet/

app = Flask(__name__)

# mongo = PyMongo(app)
#
# rooms = mongo.db.rooms

db = TinyDB('data/room_data.json')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

default_room_data = {
    'number':'414',
    'quarter':'1701',
    'times':{
        '9:00':['']*6,
        '10:00':['']*6,
        '11:00':['']*6,
        '12:00':['']*6,
        '1:00':['']*6,
        '2:00':['']*6,
        '2:30':['']*6,
        '3:00':['']*6,
        '4:00':['']*6,
        '5:30':['']*6,
        '6:00':['']*6,
        '7:00':['']*6,
        '7:30':['']*6,
        '8:00':['']*6,
        '9:01':['']*6,
        '10:01':['']*6
    }
}

@app.route('/')
def index():
    return render_template('choose_room.html')

@app.route('/get_schedule', methods=['POST'])
def get_schedule():
    Room = Query()
    room = request.form.get('rooms')
    quarters = request.form.get('quarters')
    data = db.search(Room.number == room and Room.quarter == quarters)
    return render_template('room_table.html', data=data)

@app.route('/update_schedule', methods=['POST'])
def update_schedule():
    Room = Query()
    form = request.form.to_dict()
    schedule = db.search(Room.number == form['room'] and Room.quarter == form['quarter'])
    if len(schedule) == 0:  #construct a new one
        schedule = default_room_data
        schedule['number'] = form['room']
        schedule['quarter'] = form['quarter']
        del(form['room'])
        del(form['quarter'])
        for key, value in form.items():
            classtime = key[0:len(key)-1]
            day = int(key[-1])
            schedule['times'][classtime][day] = value
        db.insert(schedule)
    else:
        pass
    return render_template('choose_room.html')

@app.route('/rooms', methods=['GET'])
def get_rooms():
    data = db.all()
    # list_data = [d for d in data]
    return render_template('template.html', data=data)


if __name__ == '__main__':
    app.run()
