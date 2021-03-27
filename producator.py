from Domain.entity import *


class Producator(Entity):

    def __init__(self, theId, nume, nr_vanzari, cif_afaceri):
        super().__init__(theId)
        self.__a = nume
        self.__b = nr_vanzari
        self.__c = cif_afaceri

    def get_nume(self):
        return self.__a

    def getVanzari(self):
        return self.__b

    def getCifraAfaceri(self):
        return self.__c

    def __str__(self):
        return "{}:{},{},{}".format(
            self.getId(),
            self.__a,
            self.__b,
            self.__c,
        )
