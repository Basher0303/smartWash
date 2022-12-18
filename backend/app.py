from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import time
import asyncio
import threading
import subprocess
from datetime import datetime
import mysql.connector
import json

from Wash import Wash
from Database import Database


wash = Wash()
db = Database(host="localhost",user="alex",passwd="03032002",database="wash")

loop = asyncio.get_event_loop()
app = Flask(__name__)
CORS(app)




@app.route('/api/start', methods=['GET'])
async def starting():
    if request.method == 'GET':
        if wash.getIsWashActive() == False:
            th2 = threading.Thread(target=asyncio.run, args=(wash.start(), ))
            th2.start()

        while True: 
            print(wash.getStatus())
            if(wash.getChangedStatus() == True):
                db.addStatus(wash.getStatus())
                wash.setChangedStatus(False)
                return jsonify(
                    status = wash.getStatus(),
                    statusName = wash.getStatusName()
                )
            time.sleep(0.5)            



#маршрут получения журнала
@app.route('/api/getList', methods = ['GET'])
def output_bd():
    return db.getAllStatus()




th1 = threading.Thread(target=app.run)
th1.start()
