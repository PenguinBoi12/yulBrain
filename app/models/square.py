class Square:
    def __init__(self, value, image):
        self._value = value
        self._image =  image


    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, new_value):
        self._value = new_value


    @property
    def image(self):
        return self._image


    @image.setter
    def image(self, new_image):
        self._image = new_image


    @staticmethod
    def parse(json_object):
        return Square(json_object['value'], json_object['image'])
