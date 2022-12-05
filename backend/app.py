from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Wash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Integer, unique=True, nullable=False)
    stop = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Wash %r>' % self.id



@app.route('/status', methods=['POST'])
def create_bd():
    if request.method == 'POST':
        print(request)

@app.route('/api/res', methods =['GET'])
def task():
    
    if request.method == 'GET':
        bd = Wash.query.first()
        return jsonify(request)
if __name__ == '__main__':
    app.run()