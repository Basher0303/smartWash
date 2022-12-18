import time
import asyncio
import threading
import subprocess
from datetime import datetime
import json

class Wash: 
    def __init__(self) :
        self.status = 0
        self.changedStatus = False
        self.isWashActive = False
        self.statusNames = ["Мойка свододна", "Нанесение эмульсии", "Нанесение пены", "Мойка", "Нанесение воска", "Сушка"]


    def getChangedStatus(self) :
        return self.changedStatus

    def setChangedStatus(self, newStatus):
        self.changedStatus = newStatus

    def getIsWashActive(self) :
        return self.isWashActive

    def getStatus(self):
        return self.status

    def getStatusName(self):
        return self.statusNames[self.status]

    #Нанесение эмульсии
    async def addEmulsion(self):
        self.status = 1
        self.changedStatus = True
        await asyncio.sleep(5)

    #Нанесение пены
    async def addFoam(self):
        self.status = 2
        self.changedStatus = True
        await asyncio.sleep(5)

    #Мойка
    async def washAway(self):
        self.status = 3
        self.changedStatus = True
        await asyncio.sleep(5)

    #нанесение воска
    async def addWax(self):
        self.status = 4
        self.changedStatus = True
        await asyncio.sleep(5)

    #Сушка
    async def drying(self):
        self.status = 5
        self.changedStatus = True
        await asyncio.sleep(5)

    #Конец мойки
    async def endWash(self):
        self.status = 0
        self.changedStatus = True
        self.isWashActive = False



    async def start(self) :
        self.isWashActive = True
        await self.addEmulsion()
        await self.addFoam()
        await self.washAway()
        await self.addWax()
        await self.drying()
        await self.endWash()

