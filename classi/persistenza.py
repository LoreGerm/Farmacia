class persistenza:
    _id = 0

    def __init__(self, id):
        self._id = id

    def set_id(self,id):
        self._id = id
    def get_id(self):
        return self._id

    def save(self):
        pass


class file(persistenza):
    _name = "farmacia.txt"
    _size_far = 0

    def __init__(self, name="farmacia.txt"):
        self._name = name
    

    def set_name(self, name):
        self._name = name
    def get_name(self):
        return self._name

    def save(self, obj):
        pass


class ram(persistenza):
    pass


class db(persistenza):
    pass


class persistence_factory:

    def get_persistance(self, persistence_type):
        pass

