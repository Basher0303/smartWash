from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import time
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Wash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bdstatus = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Wash %r>' % self.id


@app.route('/api/status', methods=['POST'])
def create_bd():
    if request.method == 'POST':
        curStatus = int(request.form.get('status'))
        wash = Wash(bdstatus=curStatus)
        db.session.add(wash)
        db.session.commit()

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
@app.route('/api/bdres', methods = ['POST'])
def output_bd():
    wash = Wash.query.order_by(Wash.date.desc()).all()
    return jsonify(wash)

if __name__ == '__main__':
    app.run(threaded=True)