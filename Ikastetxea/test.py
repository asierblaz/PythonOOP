from Ikastetxea.Pertsona import Pertsona
from Ikastetxea.Ikaslea import Ikaslea
from Ikastetxea.Irakaslea import Irakaslea
from Ikastetxea.Departamentuak import Departamentuak
from Ikastetxea.Taldea import Taldea
from Ikastetxea.OinarrizkoMetodoak import OinarrizkoMetodoak

p1=Pertsona(11,"Asier","Blazquez",6491245,20)

p1.print()
print("Adina orain 80 urte jarriko dugu")
p1.setadina(80)
print(p1.getname(),"ren adina = ", p1.getadina())
p1.print()
print("__________________________________________")
i1=Ikaslea(11,"Asier","Blazquez",6491245,20,"dam")
i1.print()


print(p1.adina)
p1.adina=50
p1.print()


irak1=Irakaslea(11,"Pedro","Lopez",6491245,20,10)
irak1.print()


depart1= Departamentuak("Ikasleak",212)
depart1.print()

tal1= Taldea(12,"DAM")
tal1.print()


print("---------Metodo Estatikoak--------------")

OinarrizkoMetodoak.BildumanGehitu(depart1)

OinarrizkoMetodoak.DepartamentuBildumaIkusi()