from uuid import uuid4


class Teacher(object):
    def __init__(self, imie :str = None, nazwisko: str = None):
        self.id = uuid4()
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)