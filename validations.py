def optiune():
    """

    desc.:verifica daca optiunea introdusa este valida
    """
    lit = []
    i = 0
    while True:
        try:
            c = str(input("Adaugati optiune:"))
            c = c.split(",")
            for i in c:
                if not (i in ["1",
                              "2",
                              "3",
                              "4",
                              "5",
                              "a1",
                              "a2",
                              "x",
                              "",
                              "",
                              "Undo",
                              "Redo"]):
                    raise ValueError
                else:
                    lit.append(i)
            return lit
        except ValueError:
            print("Comanda ", i, " este invalida")


def cauta(lista, x):
    for p in lista:
        if p.getId() == x:
            return 1
    return 0
