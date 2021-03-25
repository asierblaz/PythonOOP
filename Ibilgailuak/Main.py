from Ibilgailuak.Coche import Coche
from Ibilgailuak.Bicicleta import Bicicleta
from Ibilgailuak.Camioneta import Camioneta
from Ibilgailuak.Motocicleta import Motocicleta

coche = Coche("azul", 4, 150, 1200)
camioneta = Camioneta ("blanco",4,100,1300,1500)
bici= Bicicleta ("verde", 2, "urbana")
moto = Motocicleta("negro",2,"deportiva",180,900)

ibilgailuak= [coche,camioneta,bici,moto]

def listaImprimatu(lista):
    for i in lista:
        print(i)


def katalogo(lista,gurpilKupurua=0):
    cont=0;
    vehiculos=[]
    listaImprimatu(lista)
    for i in lista:
        if(i.ruedas==gurpilKupurua): #edo i.getRuedas()
            cont=cont+1;
            vehiculos.append(i)
    print("\nSe han encontrado",cont, "vehiculos con ", gurpilKupurua, "ruedas: ")
    listaImprimatu(vehiculos)

katalogo(ibilgailuak)
print("\n")
katalogo(ibilgailuak,2)
print("\n")
katalogo(ibilgailuak,4)
