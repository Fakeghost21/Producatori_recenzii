from Domain.entity import *


class Object1(Entity):

    def __init__(self, theId, a, b, c, d):
        super().__init__(theId)
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    def get1(self):
        return self.__a

    def get2(self):
        return self.__b

    def get3(self):
        return self.__c

    def get4(self):
        return self.__d

    def __str__(self):
        return "{}:{},{},{},{}".format(
            self.getId(),
            self.__a,
            self.__b,
            self.__c,
            self.__d
        )
