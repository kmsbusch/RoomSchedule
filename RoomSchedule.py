from flask import Flask, jsonify, render_template
from flask.ext.pymongo import PyMongo

# client = MongoClient('localhost:27017')

# db = client.RoomSchedule




app = Flask(__name__)

mongo = PyMongo(app)

# rooms = mongo.db.rooms


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/rooms', methods=['GET'])
def get_rooms():
    data = mongo.db.rooms.find_one()
    # list_data = [d for d in data]
    return render_template('template.html', data=data)


if __name__ == '__main__':
    app.run()
