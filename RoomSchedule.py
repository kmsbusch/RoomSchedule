from tinydb import TinyDB, Query
from flask import Flask, jsonify, render_template
#from flask.ext.pymongo import PyMongo

# client = MongoClient('localhost:27017')

# db = client.RoomSchedule


# http://webdesignfromscratch.com/html-css/datasheet/

app = Flask(__name__)

# mongo = PyMongo(app)
#
# rooms = mongo.db.rooms

db = TinyDB('C:\\Users\\busmic1206\\RoomSchedule\\data\\room_data.json ')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def index():
    return render_template('room_table.html')

@app.route('/rooms', methods=['GET'])
def get_rooms():
    data = db.all()
    # list_data = [d for d in data]
    return render_template('template.html', data=data)


if __name__ == '__main__':
    app.run()
