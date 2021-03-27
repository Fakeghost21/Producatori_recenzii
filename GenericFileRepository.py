from Domain.producator import *
from Domain.recenzie import *
import pickle


class GenericFileRepository:

    def __init__(self, filename):
        self.__storage = []
        self.__filename = filename

    def __load_from_file(self):
        try:
            with open(self.__filename, 'rb') as f_read:
                self.__storage = pickle.load(f_read)
        except FileNotFoundError:
            self.__storage.clear()
        except Exception:
            self.__storage.clear()

    def __save_to_file(self):

        with open(self.__filename, 'wb') as f_write:
            pickle.dump(self.__storage, f_write)

    def create(self, entity):
        """
        Adds a new entity.
        :param entity: the given entity
        :return: -
        :raises: RepositoryError if the id already exists
        """
        self.__load_from_file()
        id_entity = entity.getId()
        for obj in self.__storage:
            if obj.getId() == id_entity:
                raise ValueError("id invalid")
        self.__storage.append(entity)
        self.__save_to_file()

    def read(self, id_entity=None):
        """
        Gets a vote by id or all the votes
        :param id_entity: optional, the entity id
        :return: the list of entities or the entity with the given id
        """
        self.__load_from_file()
        if id_entity is None:
            return self.__storage[:]
        for obj in self.__storage:
            if obj.getId() == id_entity:
                return obj
        return None

    def update(self, entity):
        """
        Updates an entity.
        :param entity: the entity to update
        :return: -
        :raises: RepositoryError if the id does not exist
        """
        self.__load_from_file()
        id_entity = entity.getId()
        for i in range(len(self.__storage)):
            if id_entity == self.__storage[i].getId():
                self.__storage[i] = entity
                self.__save_to_file()
                break
        return

    def delete(self, id_entity):
        """
        Deletes a entity.
        :param id_entity: the entity id to delete.
        :return: -
        :raises RepositoryError: if no entity with id_entity
        """
        for i in range(len(self.__storage)):
            id2 = self.__storage[i].getId()
            if id_entity == id2:
                del self.__storage[i]
                self.__save_to_file()
                break


def test1():
    r = GenericFileRepository("teste.txt")
    assert r.read() == []
    g = Producator(112, "Ernest", 120000, 30000)
    g2 = Producator(1127, "Ernest2", 1200, 30000)
    g3 = Producator(1123, "Ernest3", 12, 30000)
    g4 = Producator(424,"", 12, 345)
    r.create(g)
    r.create(g2)
    r.create(g3)
    assert len(r.read()) == 3


#test1()
