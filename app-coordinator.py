from UI.Console import *
from Repository.GenericFileRepository import *
# from Domain. import *


def main():
    repoProdus = GenericFileRepository("A.txt")
    repoRecenzie = GenericFileRepository("B.txt")
    v1 = ProducatorValidator()
    serviceProducator = ServiceProducator(repoProdus, repoRecenzie, v1)
    v2 = Dupl(serviceProducator)
    serviceRecenzie = ServiceRecenzie(repoRecenzie, v2)
    dr = Console(serviceRecenzie, serviceProducator, "C.txt")
    dr.run_console()


main()
