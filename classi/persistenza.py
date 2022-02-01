import mysql.connector
from classi.fun import over_write,stampa
import json
import os


class persistenza:

    def save(self,obj,table_name):
        print('save data from ' + str(type(self)))


class file(persistenza):
    
    def save(self,obj,file):
        try:
            self.__size_far = os.path.getsize(file)
        except:
            over_write(file,[])
            self.__size_far = os.path.getsize(file)
        if isinstance(obj,list):
            if self.__size_far == 0:
                far = [obj[0].model_to_dict()]
                for i in range(1,obj):          ############# ERROR #############
                    far.append(obj[i].model_to_dict())
                over_write(file,far)
            else:
                far = json.loads(stampa(file))
                for i in range(obj):
                    far.append(obj[i].model_to_dict())
                over_write(file,far)
        else:
            if self.__size_far == 0:
                far = [obj.model_to_dict()]
                over_write(file,far)
            else:
                far = json.loads(stampa(file))
                far.append(obj.model_to_dict())
                over_write(file,far)
        print('salva sul file ' + file)


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

