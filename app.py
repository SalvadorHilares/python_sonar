from email.message import Message
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/software2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Publisher(db.Model):
    __tablename__ = 'publisher'
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(100), nullable = False)
    topic = db.Column(db.String(100), nullable = False)

class Subscriber(db.Model):
    __tablename__ = "subscriber"
    id = db.Column(db.Integer, primary_key=True)

db.create_all()

@app.route("/agregar/message", methods = ['POST'])
def message_post():
    error = False
    response = {}
    try:
        mess = request.get_json()["message"]
        topic = request.get_json()["control"]
        publisher = Publisher(mensaje=mess, topic=topic)
        db.session.add(publisher)
        db.session.commit()
        response["mensaje"] = mess
        response["topic"] = topic
    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "Mensaje no ingresado"
    response['error'] = error
    return jsonify(response)

@app.route("/ver/message", methods = ['POST'])
def message_get():
    error = False
    response = {}
    try:
        topic = request.get_json()["control"]
        messages = db.session.query(Publisher).filter(Publisher.topic == topic).all()
        response["messages"] = messages
    except FileNotFoundError:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    if error:
        response['error_message'] = "Mensaje no ingresado"
    response['error'] = error
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html', data=Publisher.query.all())

if __name__ == '__main__':
    app.run(port=5003, debug=True)
else:
    print('using global variables from FLASK')