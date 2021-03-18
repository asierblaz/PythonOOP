
class Funtzioak:
    @staticmethod
    def listanGehitu(lista,objetua):
        lista.append(objetua)

    @staticmethod
    def listaImprimatu(lista):
        for i in lista:
            i.print()

    def listatikNezabatu(lista, n):
        del (lista[n])