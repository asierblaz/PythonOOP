from Ikastetxea.Pertsona import Pertsona
from Ikastetxea.Ikaslea import Ikaslea
from Ikastetxea.Irakaslea import Irakaslea
from Ikastetxea.Departamentuak import Departamentuak
from Ikastetxea.Taldea import Taldea
from Ikastetxea.funtzioak import Funtzioak


p1= Pertsona(1,"Asier","B",6491245,25)
p2= Pertsona(2,"Hodei","M",6478415448,20)
p3= Pertsona (3,"Profesor","P",78787878,45)
id=4;
pertsonak=[p1,p2,p3]

d1= Departamentuak("Teknikoa",1)

d2= Departamentuak("Bulegoa",2)

d3= Departamentuak("Idazkaritza",3)

departs=[d1,d2,d3]

t1=Taldea("DAM",1)
t2=Taldea("SMR",2)
t3=Taldea("DW",3)
taldeak=[t1,t2,t3]

ik1 = Ikaslea(p1.Id,p1.name,p1.surname,p1.movile,p1.adina,t1.kodea)
ik2 = Ikaslea(p2.Id,p2.name,p2.surname,p2.movile,p2.adina,t2.kodea)
ikasleak=[ik1, ik2]

ir1= Irakaslea(p3.Id,p3.name,p3.surname,p3.movile,p3.adina,d1.izena)
irakasleak=[ir1]


def pertsonakInprimatu():
    print("-------------Pertsonak------------")
    Funtzioak.listaImprimatu(pertsonak)
    print("-----------------------------------")

def ikasleakInprimatu():
    print("-------------Ikasleak------------")
    Funtzioak.listaImprimatu(ikasleak)
    print("-----------------------------------")

def irakasleakInprimatu():
    print("-------------Irakasleak------------")
    Funtzioak.listaImprimatu(irakasleak)
    print("-----------------------------------")


def kideaGehitu():
    print("-------------Kidea Gehitu------------")
    izena= input("Sartu Pertsonaren Izena:")
    abizena = input("Sartu Pertsonaren Abizena:")
    mugikorra = input("Sartu Pertsonaren Telefonoa:")
    adina = input("Sartu Pertsonaren adina:")
    respuesta=  int(input("Sartutako pertsona Ikaslea (1), Irakaslea(2) edo Ez dauka lana(3)?"))
    pn = Pertsona(id, izena, abizena, mugikorra, adina)

    if (respuesta==1):
        print("Hauek dira eskuragarri dauden taldeak.")

        taldeakInprimatu()

        zein = input("¿Zein taldean egongo da ikaslea?")

        ikn = Ikaslea(pn.Id, pn.name, pn.surname, pn.movile, pn.adina, zein)

        print("Ikaslea sortu da")
        ikasleakInprimatu()

    if (respuesta== 2):
        print("Hauek dira eskuragarri dauden taldeak.")
        departamentuakInprimatu()
        zein = input("¿Zein departamentuan egongo da irakaslea?")

        irn = Irakaslea(pn.Id, pn.name, pn.surname, pn.movile, pn.adina, zein)

        print("Ikaslea sortu da")
        irakasleakInprimatu()

    if  (respuesta ==3):
        print("Pertsona sortu da")
        pertsonakInprimatu()



def departamentuakInprimatu():
        print("-------------Departamentuak------------")
        Funtzioak.listaImprimatu(departs)
        print("--------------------------------------")


def taldeakInprimatu():
    print("-------------Taldeak------------")
    Funtzioak.listaImprimatu(taldeak)
    print("--------------------------------------")


def departamentuaSortu():
    print("-------------Departamentua sortu------------")
    izena = input("Sartu Departamentuaren Izena:")
    id = input("Sartu Departamentuaren kodea:")

    dn = Departamentuak(izena, id)

    print("Departamentua sortu da")
    departamentuakInprimatu()

def taldeaSortu():
    print("-------------Taldea sortu------------")
    kodea = input("Sartu Taldearen kodea:")
    zenbakia = input("Sartu Taldearen zenbakia:")

    tn = Taldea(kodea, zenbakia)

    print("Taldea sortu da")
    taldeakInprimatu()

def pertsonakEzabatu():
    print("-------------Pertsonak ezabatu------------")
    pertsonakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun pertsonaren posizioa:"))
    Funtzioak.listatikNezabatu(pertsonak,zein-1)
    print("pertsona ezabatu da")
    pertsonakInprimatu()

def ikasleakEzabatu():
    print("-------------Ikasleak ezabatu------------")
    ikasleakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun ikasleareN posizioa:"))
    Funtzioak.listatikNezabatu(ikasleak,zein-1)
    print("Ikaslea ezabatu da")
    ikasleakInprimatu()

def irakasleakEzabatu():
    print("-------------irakaslea ezabatu------------")
    irakasleakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun irakaslearen posizioa:"))
    Funtzioak.listatikNezabatu(irakasleak,zein-1)

    print("irakaslea ezabatu da")
    irakasleakInprimatu()

def taldeakEzabatu():
    print("-------------Taldea sortu------------")
    taldeakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun taldearen posizioa:"))
    Funtzioak.listatikNezabatu(taldeak,zein-1)
    print("taldea ezabatu da")
    taldeakInprimatu()

def departamentuakEzabatu():
    print("-------------Taldea sortu------------")
    departamentuakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun departamentuaren posizioa:"))
    Funtzioak.listatikNezabatu(departs,zein-1)
    print("departamentua ezabatu da")
    departamentuakInprimatu()


def pertsonaAldatu():
    print("-------------Pertsona Aldatu------------")
    pertsonakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun pertsonaren posizioa:"))
    izena = input("Sartu Pertsonaren Izena:")
    abizena = input("Sartu Pertsonaren Abizena:")
    mugikorra = input("Sartu Pertsonaren Telefonoa:")
    adina = input("Sartu Pertsonaren adina:")
    pertsonak[zein-1].name=izena
    pertsonak[zein-1].surname=abizena
    pertsonak[zein-1].movile=mugikorra
    pertsonak[zein-1].adina=adina
    print("Pertsona aldatu da")
    pertsonakInprimatu()

def ikasleaAldatu():
    print("-------------Ikaslea Aldatu------------")
    ikasleakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun ikaslearen posizioa:"))
    izena = input("Sartu ikaslearen Izena:")
    abizena = input("Sartu ikaslearen Abizena:")
    mugikorra = input("Sartu ikaslearen Telefonoa:")
    adina = input("Sartu ikaslearen adina:")
    ikasleak[zein-1].name=izena
    ikasleak[zein-1].surname=abizena
    ikasleak[zein-1].movile=mugikorra
    ikasleak[zein-1].adina=adina
    print("Ikaslea aldatu da")
    ikasleakInprimatu()

def irakasleaAldatu():
    print("-------------Ikaslea Aldatu------------")
    irakasleakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun irakaslearen posizioa:"))
    izena = input("Sartu irakaslearen Izena:")
    abizena = input("Sartu irakaslearen Abizena:")
    mugikorra = input("Sartu irakaslearen Telefonoa:")
    adina = input("Sartu irakaslearen adina:")
    irakasleak[zein-1].name=izena
    irakasleak[zein-1].surname=abizena
    irakasleak[zein-1].movile=mugikorra
    irakasleak[zein-1].adina=adina
    print("Irakaslea aldatu da")
    irakasleakInprimatu()

def taldeaAldatu():
    print("-------------Taldea Aldatu------------")
    taldeakInprimatu()
    kodea = input("Sartu Taldearen kodea:")
    zenbakia = input("Sartu Taldearen zenbakia:")
    taldeak[zein-1].kodea=kodea
    taldeak[zein-1].zenbakia=zenbakia

    print("taldea aldatu da")
    taldeakInprimatu()

def departamentuaAldatu():
    print("-------------Departamentua Aldatu------------")
    departamentuakInprimatu()
    izena = input("Sartu Departamentuaren Izena:")
    id = input("Sartu Departamentuaren kodea:")
    departs[zein-1].kodea=izena
    departs[zein-1].zenbakia=id
    print("Departamentua aldatu da")
    departamentuakInprimatu()




print("----------Ikastetxea----------")
print("1- Sortu\n"
      "2- Inprimatu\n"
      "3- Ezabatu\n"
      "4- Aldatu \n"
      "5- Irten"
)
aukera = int(input("Aukeratu bat: "))




while (aukera!=5):

    if(aukera== 1):
        print("Zer sortu nahi duzu?")
        print("1- Pertsona\n"
          "2- Taldea\n"
          "3- Departamentua\n")
        zein= int(input("Aukeratu bat: "))
        if(zein ==1):
            kideaGehitu()
        if(zein==2):
            taldeaSortu()
        if(zein== 3):
            departamentuakInprimatu()

    if(aukera== 2):
        print("Zer Inprimatu nahi duzu?")
        print("1- Pertsona\n"
          "2- Ikaslea\n"
          "3- Irakaslea\n"
          "4- Taldea\n"
          "5- Departamentua\n")
        zein= int(input("Aukeratu bat: "))
        if(zein ==1):
            pertsonakInprimatu()
        if(zein==2):
            ikasleakInprimatu()
        if(zein== 3):
            irakasleakInprimatu()
        if (zein == 4):
            taldeakInprimatu()
        if (zein == 5):
            departamentuakInprimatu()

    if (aukera == 3):
        print("Zer borratu nahi duzu?")
        print("1- Pertsona\n"
              "2- Ikaslea\n"
              "3- Irakaslea\n"
              "4- Taldea\n"
              "5- Departamentua\n")
        zein = int(input("Aukeratu bat: "))
        if (zein == 1):
            pertsonakEzabatu()
        if (zein == 2):
            ikasleakInprimatu()
        if (zein == 3):
            irakasleakInprimatu()
        if (zein == 4):
            taldeakInprimatu()
        if (zein == 5):
            departamentuakInprimatu()

    if (aukera == 4):
        print("Zer Aldatu nahi duzu?")
        print("1- Pertsona\n"
              "2- Ikaslea\n"
              "3- Irakaslea\n"
              "4- Taldea\n"
              "5- Departamentua\n")
        zein = int(input("Aukeratu bat: "))
        if (zein == 1):
            pertsonaAldatu()
        if (zein == 2):
            ikasleaAldatu()
        if (zein == 3):
            irakasleaAldatu()
        if (zein == 4):
            taldeaAldatu()
        if (zein == 5):
            departamentuaAldatu()












    print("1- Sortu\n"
          "2- Inprimatu\n"
          "3- Ezabatu\n"
          "4- Aldatu \n"
          "5- Irten"
          )

    aukera = int(input("Aukeratu bat: "))
