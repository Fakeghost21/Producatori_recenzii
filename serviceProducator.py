from Domain.producator import *
from Domain.recenzie import *


class ServiceProducator:
    def __init__(self, repository, repository2, validator):
        self.__repo = repository
        self.__repoRecenzie = repository2
        self.__validator = validator

    def create1(self, obj):
        self.__validator.validate(obj)
        self.__repo.create(obj)

    def update1(self, obj):
        c = self.__repo.read(obj.getId())
        self.__repo.update(obj)

    def delete1(self, id_obj):
        clients = self.__repo.read()
        for client in clients:
            if client.getId() == id_obj:
                self.__repo.delete(id_obj)
                return

    def read1(self, obj_id=None):
        return self.__repo.read(obj_id)

    def __mediaRecenzilor(self):
        s = 0
        nr = 0
        for elem in self.__repoRecenzie.read():
            s = s + elem.getNota()
            nr += 1
        return s // nr

    def __producatoriFormulaDictionar(self):
        producatori = self.__repo.read()
        dict = {}
        media = self.__mediaRecenzilor()
        for p in producatori:
            dict[p.getId()] = (p.getCifraAfaceri() / p.getVanzari()) * media
        return dict

    def sortareDupaFormula(self):
        producatori = self.__repo.read()
        formula = self.__producatoriFormulaDictionar()
        return sorted(producatori, key=lambda prod: formula[prod.getId()])

    def __notaMinima(self):
        recenzii = self.__repoRecenzie.read()
        min = 11
        for r in recenzii:
            if r.getNota() < min:
                min = r.getNota()
        return min

    def producatorNotaMinima(self):
        producatori = self.__repo.read()
        recenzii = self.__repoRecenzie.read()
        minima = self.__notaMinima()
        max = 0
        producatorul = None
        for p in producatori:
            number = 0
            for r in recenzii:
                if r.get_id_producator() == p.getId() and r.getNota() == minima:
                    number += 1
            if number > max:
                max = number
                producatorul = self.__repo.read(p.getId())
        return producatorul





