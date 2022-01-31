import mysql.connector
from classi.fun import over_write,stampa
import json
import os


class persistenza:

    def save(self,obj,table_name):
        print('save data from ' + str(type(self)))


class file(persistenza):
    __name = 'farmacia.json'
    try:
        __size_far = os.path.getsize(__name)
    except:
        over_write(__name,[])
        __size_far = os.path.getsize(__name)

    def save(self,obj):
        if self.__size_far == 0:
            far = [obj.model_to_dict()]
            over_write(self.__name,far)
        else:
            far = json.loads(stampa(self.__name))
            far.append(obj.model_to_dict())
            over_write(self.__name,far)
        print('salva sul file ' + self.__name)


class ram(persistenza):
    
    def save(self):
        print('salva sulla ram')


class db(persistenza):
    
    def __init__(self):
        self.db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "farmacia"
        )
        self.cursor = self.db.cursor()


    def save(self, obj, table_name):
        if table_name == "address":
            value = db.value_in_tuple(obj)
            sql = "INSERT INTO address (via, number, city, postcode, province, country, other_details) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql, value)
            self.db.commit()
        print('Salvo sul database')
    
    @staticmethod
    def value_in_tuple(obj):
        value = []
        for i in obj.model_to_dict():
            if i != "id":
                value.append(obj.model_to_dict()[i])
        value = tuple(value)
        return value

    @staticmethod
    def key_in_tuple(obj):
        key = []
        for i in obj.model_to_dict():
            key.append(i)
        key = tuple(key)
        return key


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

