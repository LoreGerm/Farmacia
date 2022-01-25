import mysql.connector

class persistenza:

    def save(self):
        print('save data from ' + str(type(self)))


class file(persistenza):
    _name = 'farmacia.txt'

    def save(self):
        print('salva sul file ' + self._name)


class ram(persistenza):
    
    def save(self):
        print('salva sulla ram')


class db(persistenza):
    db = mysql.connector.connet(
        host = "localhost",
        user = "root",
        password = "",
        database = "database"
    )
    cursor = db.cursor()

    def __init__(self):
        self.cursor.execute("IF NOT EXISTS(SELECT * FROM sys.databases WHERE name = 'DataBase') BEGIN CREATE DATABASE [database]")
    
    def save(self):
        print('Salvo sul database')


class persistence_factory:

    def get_persistance(self, persistence_type):
        pers_obj = None
        if persistence_type == "db":
            pers_obj = db()
        elif persistence_type == "file":
            pers_obj = file()
        elif persistence_type == "ram":
            pers_obj = ram()

        return pers_obj

