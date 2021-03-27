class ServiceRecenzie:
    def __init__(self, repositoryR, validator):
        self.__repo = repositoryR
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

    def creareHistograma(self):
        recenzii = self.__repo.read()
        histo = []
        for nota in range(1, 11):
            nr = 0
            for r in recenzii:
                if r.getNota() == nota:
                    nr += 1
            histo.append(nr)
        return histo
