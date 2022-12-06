from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Wash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer, unique=True, nullable=False)
    stop = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Wash %r>' % self.id


@app.route('/api/status', methods=['POST'])
def create_bd():
    if request.method == 'POST':
        curStatus = int(request.form.get('status'))
        while True: 
            if(curStatus == 1) :
                time.sleep(2)
            elif(curStatus == 2) :
                time.sleep(2)
            elif(curStatus == 3) :
                time.sleep(2)
            elif(curStatus == 4) :
                time.sleep(2)

            #добавить в бд запись
            return jsonify(
                status = curStatus + 1
            )



#маршрут получения журнала

if __name__ == '__main__':
    app.run(threaded=True)