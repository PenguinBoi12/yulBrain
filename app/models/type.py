class Type:
    def __init__(self, id, name):
        self._id = id
        self._name =  name


    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_name):
        self._name = new_name


    def to_json(self):
        return { 'id':self.id, 'name':self.name}    