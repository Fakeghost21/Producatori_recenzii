from Domain.entity import *


class Recenzie(Entity):

    def __init__(self, theId, id_producator, nota):
        super().__init__(theId)
        self.__a = id_producator
        self.__b = nota

    def get_id_producator(self):
        return self.__a

    def getNota(self):
        return self.__b

    def __str__(self):
        return "{}:{},{}".format(
            self.getId(),
            self.__a,
            self.__b,
        )
