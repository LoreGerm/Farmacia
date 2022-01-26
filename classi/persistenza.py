import mysql.connector


class persistenza:

    def save(self,obj,table_name):
        print('save data from ' + str(type(self)))


class file(persistenza):
    _name = 'farmacia.txt'

    def save(self):
        print('salva sul file ' + self._name)


class ram(persistenza):
    
    def save(self):
        print('salva sulla ram')


class db(persistenza):
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "farmacia"
    )
    cursor = db.cursor()

    def save(self, obj, table_name):
        if table_name == "address":
            value = db.key_in_tuple(obj) + db.value_in_tuple(obj)
            sql = "INSERT INTO address (%s,%s,%s,%s,%s,%s,%s) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(sql, value)
            self.db.commit()
        print('Salvo sul database')
    
    @staticmethod
    def value_in_tuple(obj):
        value = []
        for i in obj.model_to_dict():
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

