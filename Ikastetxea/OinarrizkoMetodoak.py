from Ikastetxea.Departamentuak import Departamentuak

d1= Departamentuak("Teknikoa",1)
d2= Departamentuak("Bulegoa",2)
d3= Departamentuak("Idazkaritza",3)

lista = [d1, d2, d3]
class OinarrizkoMetodoak:
    @staticmethod
    def BildumanGehitu(Departamentua):
        lista.append(Departamentua)

    @staticmethod
    def DepartamentuBildumaIkusi():
        for i in lista:
            i.print()

