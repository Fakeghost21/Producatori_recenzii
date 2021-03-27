from Service.serviceRecenzie import *
from Service.serviceProducator import *
from Domain.validator1 import *
from Domain.producator import *
from Domain.recenzie import *
from Domain.validatorRecenzie import *


# from Main. import *


class Console:

    def __init__(self, recenzieService, producatorService, file_name):
        self.__recenzie_service = recenzieService
        self.__producator_service = producatorService
        self.__file = file_name

    def __show_menu(self):
        print('1. Adaugare producator')
        print("a1. Afisare producator")
        print('2. Adaugare recenzie')
        print("a2. Afisare recenzie")
        print('3. Afisarea producatorilor ordonati dupa (cifra afacerilor/numar vanzari)*media recenzilor ')
        print("4. Afisarea producatorului cu cel mai mare numar de recenzii cu nota minima")
        print("5. Afisare histograma in fisier")
        print('x. Exit')

    def run_console(self):
        while True:
            self.__show_menu()
            op = input("Optiune")
            if op == "1":
                self.__handle__add_producator()
            elif op == "2":
                self.__handler_add_recenzie()
            elif op == "a1":
                self.__show_list(self.__producator_service.read1())
            elif op == "a2":
                self.__show_list2(self.__recenzie_service.read1())
            elif op == "3":
                self.__show_list(self.__producator_service.sortareDupaFormula())
            elif op == "4":
                print(self.__producator_service.producatorNotaMinima())
            elif op == "5":
                self.__writeFile()
            elif op == "x":
                break

    def __handle__add_producator(self):
        try:
            id = input('ID-ul: ')
            nume = input('Nume: ')
            vanzari = int(input('Vanzari: '))
            afaceri = float(input('Cifra afaceri: '))
            c = Producator(id, nume, vanzari, afaceri)
            self.__producator_service.create1(c)
            print('Producatorul a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)
        except ProducatorException as e:
            print(e)

    def __handler_add_recenzie(self):
        try:
            id_r = input('ID-ul: ')
            id_producator = input('X: ')
            nota = float(input('Y: '))
            r = Recenzie(id_r, id_producator, nota)
            print(r.get_id_producator())
            self.__recenzie_service.create1(r)
            print('Punctul a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)
        except RecenzieException as e:
            print(e)

    def __show_list(self, objects):
        for obj in objects:
            print(obj)

    def __show_list2(self, objects):
        for obj in objects:
            p = self.__producator_service.read1(obj.get_id_producator())
            print(p.get_nume(), obj, sep=" ")

    def __writeFile(self):
        histo = self.__recenzie_service.creareHistograma()
        f = open(self.__file, "w")
        content = " "
        for i in range(0, 10):
            line = "{}:{}\n".format(i+1, histo[i])
            content += line
        f.write(content)
        f.close()
