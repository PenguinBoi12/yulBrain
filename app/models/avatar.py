class Avatar:
    def __init__(self, id, name, type, image, waiting, main, x, y):
        self._id = id
        self._name = name
        self._type = type
        self._image = image
        self._waiting = waiting
        self._main = main
        self._x = x
        self._y = y


    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name


    @name.setter
    def image(self, new_name):
        self._name = new_name


    @property
    def type(self):
        return self._type


    @type.setter
    def type(self, new_type):
        self._type = new_type


    @property
    def image(self):
        return self._image


    @image.setter
    def image(self, new_image):
        self._image = new_image


    @property
    def waiting(self):
        return self._waiting


    @waiting.setter
    def waiting(self, new_waitin):
        self._waiting = waiting


    @property
    def main(self):
        return self._main


    @main.setter
    def main(self, new_main):
        self._main = main


    @property
    def x(self):
        return self._x


    @x.setter
    def x(self, new_x):
        self._x = new_x


    @property
    def y(self):
        return self._y


    @y.setter
    def y(self, new_y):
        self._y = new_y


    def to_json(self):
        return { 'id':self.id, 'name':self.name, 'type':self.type, 'image':self.image, 'waiting':self.waiting, 'main':self.main, 'x':self.x, 'y':self.y }

    @staticmethod
    def parse(json_object):
        return Avatar(json_object['id'], json_object['name'], json_object['type'], json_object['image'],  json_object['waiting'], json_object['main'], json_object['x'], json_object['y'])
