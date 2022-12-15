from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import time
import asyncio
import threading
import subprocess
from datetime import datetime
import mysql.connector
import json

loop = asyncio.get_event_loop()
app = Flask(__name__)
CORS(app)


mydb = mysql.connector.connect(
    host="localhost",
    user="alex",
    passwd="03032002",
    database="wash"
)

my_cursor = mydb.cursor()


statusNames = ["Мойка свододна", "Нанесение эмульсии", "Нанесение пены", "Мойка", "Нанесение воска", "Сушка"]
statusWash = 0
isWashActive = False
statusChanged = False



@app.route('/api/start', methods=['GET'])
async def starting():
    if request.method == 'GET':
        global isWashActive, statusChanged
        if isWashActive == False:
            th2 = threading.Thread(target=asyncio.run, args=(startWash(), ))
            th2.start()
            isWashActive = True

        while True: 
            print(statusWash)
            if(statusChanged == True):
                statusChanged = False
                return jsonify(
                    status = statusWash,
                    statusName = statusNames[statusWash]
                )
            time.sleep(0.5)            



#Старт мойки
async def startWash():
    await addEmulsion()
    await addFoam()
    await washAway()
    await addWax()
    await drying()
    await endWash()

#Нанесение эмульсии
async def addEmulsion():
    global statusWash, statusChanged
    statusWash = 1
    addStatusInDb()
    statusChanged = True
    await asyncio.sleep(5)

#Нанесение пены
async def addFoam():
    global statusWash, statusChanged
    statusWash = 2
    addStatusInDb()
    statusChanged = True
    await asyncio.sleep(5)

#Мойка
async def washAway():
    global statusWash, statusChanged
    statusWash = 3
    addStatusInDb()
    statusChanged = True
    await asyncio.sleep(5)

#нанесение воска
async def addWax():
    global statusWash, statusChanged
    statusWash = 4
    addStatusInDb()
    statusChanged = True
    await asyncio.sleep(5)

#Сушка
async def drying():
    global statusWash, statusChanged
    statusWash = 5
    addStatusInDb()
    statusChanged = True
    await asyncio.sleep(5)

#Конец мойки
async def endWash():
    global statusWash, statusChanged, isWashActive
    statusWash = 0
    addStatusInDb()
    statusChanged = True
    isWashActive = False



#Добавить статус в базу данных
def addStatusInDb():
    my_cursor.execute(f"INSERT INTO `logs` (`id`, `date`, `status`) VALUES (NULL, {int(time.time())}, {statusWash});")
    mydb.commit()

#маршрут получения журнала
@app.route('/api/dbres', methods = ['GET'])
def output_bd():
    my_cursor.execute("SELECT * FROM `logs`")
    res = []
    for log in my_cursor :
        res.append({
            "id": log[0],
            "date": log[1],
            "status": log[2]
        })
    return res




th1 = threading.Thread(target=app.run)
th1.start()
