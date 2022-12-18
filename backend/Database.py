import mysql.connector
import time

class Database : 
    def __init__(self, host, user, passwd, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
        )
        self.cursor = self.db.cursor()

    def addStatus(self, status):
        self.cursor.execute(f"INSERT INTO `logs` (`id`, `date`, `status`) VALUES (NULL, {int(time.time())}, {status});")
        self.db.commit()

    
    def getAllStatus(self):
        self.cursor.execute("SELECT * FROM `logs`")
        res = []
        for log in self.cursor :
            res.append({
                "id": log[0],
                "date": log[1],
                "status": log[2]
            })
        return res