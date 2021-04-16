class Functions:
    @staticmethod
    def listanGehitu(lista,objetua):
        lista.append(objetua)

    @staticmethod
    def listaImprimatu(lista):
        for cont, i in enumerate(lista):
            print(cont+1," ", end=""), print(i)

    @staticmethod
    def listatikNezabatu(lista, n):
        del (lista[n])



