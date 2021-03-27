class RecenzieException(Exception):
    pass


class Dupl:
    def __init__(self, service):
        self.__v = service

    def validate(self, r):
        if self.__v.read1(r.get_id_producator()) is None:
            raise RecenzieException("Nu exista acest producator")
        if r.getNota() > 10 or r.getNota() < 1:
            raise RecenzieException("Nota trebuie sa fie intre 1 si 10")
