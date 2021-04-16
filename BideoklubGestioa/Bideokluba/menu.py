from Bideokluba.Bideoa import Bideoa
from Bideokluba.Pelikula import Pelikula
from Bideokluba.Seriea import Seriea
from Bideokluba.Zuzendaria import Zuzendaria
from Bideokluba.Dokumentala import Dokumentala
from Bideokluba.Functions import Functions

b1= Bideoa("Breaking Bad","AVI",20,2010);
b2= Bideoa("The Walking Dead","MP4",32,2008);
b3= Bideoa("El Rey Leon","VHS",6,2001);
b4= Bideoa("El Hobbit","DVD",16,2016);
b5= Bideoa ("Los Animales de Africa" ,"MOV",5,2012)
b6= Bideoa ("Creacion de la Raza Humana" ,"VHS",5,2003)

bideoak =[b1,b2,b3,b4,b5,b6]

z1=Zuzendaria("Pedro","Rodriguez","10-10-1962",10)
z2=Zuzendaria("Eva","Garcia","19-03-1980",23)

zuzendariak=[z1,z2]

s1= Seriea(b1.izena,b1.formatua,b1.prezioa,b1.urtea,5,250)
s2= Seriea(b2.izena,b2.formatua,b2.prezioa,b2.urtea,15,322)

serieak= [s1,s2]
p1= Pelikula(b3.izena,b3.formatua,b3.prezioa,b3.urtea,230,z1.abizena)
p2= Pelikula(b4.izena,b4.formatua,b4.prezioa,b4.urtea,530,z2.abizena)

pelikulak = [p1,p2]


d1 = Dokumentala(b5.izena,b5.formatua,b5.prezioa,b5.urtea,"HappyFIlms","Francia")
d2 = Dokumentala(b6.izena,b6.formatua,b6.prezioa,b6.urtea,"National Geographic","EEUU")

dokumentalak = [d1,d2]


def bideoakInprimatu():
    print("-------------Bideoak------------")
    Functions.listaImprimatu(bideoak)
    print("-----------------------------------")

def zuzendariakInprimatu():
    print("-------------Zuzendariak------------")
    Functions.listaImprimatu(zuzendariak)
    print("-----------------------------------")


def serieakInprimatu():
    print("-------------Serieak------------")
    Functions.listaImprimatu(serieak)
    print("-----------------------------------")

def dokumentalakInprimatu():
    print("-------------Dokumentalak------------")
    Functions.listaImprimatu(dokumentalak)
    print("-----------------------------------")

def pelikulakInprimatu():
    print("-------------Pelikulak------------")
    Functions.listaImprimatu(pelikulak)
    print("-----------------------------------")



def bideoaGehitu():
    print("-------------Bideoa Gehitu ------------")
    izena= input("Sartu Bideoaren Izena:")
    formatua = input("Sartu Bideoaren Formatua:")
    prezioa = int(input("Sartu Bideoaren Prezioa :"))
    urtea = int(input("Sartu Bideoaren Urtea:"))
    respuesta=  int(input("Sartutako Bideoa Pelikula (1), Seriea(2) , Dokumentala(3) edo ez Dauka Mota(4)?"))
    bn = Bideoa(izena, formatua, prezioa, urtea)
    bideoak.append(bn)

    if (respuesta==1):
        print("----------PELIKULA SORTU---------")
        print("Hauek dira eskuragarri dauden Zuzendariak.\n")

        zuzendariakInprimatu()
        baiez = int(input("Sortu nahi duzun zuzendaria listan dago | BAI(1) | EZ(0) ?"))
        if(baiez==1):

            zein = int(input("Zein da filmaren zuzendaria?"))
            luzera = int(input("Zein da filmaren luzera(min)?"))
            pn = Pelikula(bn.izena, bn.formatua, bn.prezioa, bn.urtea, luzera,str(zuzendariak[zein-1].izena))
            pelikulak.append(pn)
            print("Pelikula Sortu da\n")
            pelikulakInprimatu()
        else:
            zuzendariaSortu()
            zuzendariakInprimatu()
            zein = int(input("Zein da filmaren zuzendaria?"))
            luzera = int(input("Zein da filmaren luzera(min)?"))
            pn = Pelikula(bn.izena, bn.formatua, bn.prezioa, bn.urtea, luzera, str(zuzendariak[zein - 1].izena))
            pelikulak.append(pn)
            print("Pelikula Sortu da\n")
            pelikulakInprimatu()

    if (respuesta == 2):
        print("----------SERIEA SORTU---------")
        tenporadak = int(input("Zenbat tenporada ditu filmak?"))
        kapituloak = int(input("Zenbat kapitulo ditu serieak?"))

        sn = Seriea(bn.izena, bn.formatua, bn.prezioa, bn.urtea, tenporadak, kapituloak)
        serieak.append(sn)


        print("Seriea sortu da\n")
        serieakInprimatu()

    if (respuesta == 3):
        print("----------DOKUMENTALA SORTU---------")
        produktora = input("Zein da dokumentalaren produktora?")
        herrialdea = input("zein da dokumentalaren herrialdea?")

        dn = Dokumentala(bn.izena, bn.formatua, bn.prezioa, bn.urtea, produktora, herrialdea)
        dokumentalak.append(dn)


        print("Dokumentala sortu da\n")
        serieakInprimatu()

    if  (respuesta ==4):
        print("Bideoa sortu da")
        bideoakInprimatu()


def zuzendariaSortu():
    print("-------------Zuzendaria sortu------------")
    izena = input("Sartu Zuzendariaren izena:")
    abizena = input("Sartu Zuzendariaren abizena:")
    jaio = input("Sartu Zuzendariaren JaiotzeData:")
    sariak= int(input("Sartu Zuzendariaren sari kopurua"))

    zn = Zuzendaria(izena, abizena, jaio, sariak)
    zuzendariak.append(zn)
    print("Taldea sortu da")

def bideoaEzabatu():
    print("-------------Bideoa Ezabatu------------")
    bideoakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun bideoaren zenbakia:"))
    Functions.listatikNezabatu(bideoak,zein-1)
    print("Bideoa ezabatu da")
    bideoakInprimatu()

def pelikulaEzabatu():
    print("-------------Pelikula Ezabatu------------")
    pelikulakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun pelikularen zenbakia:"))
    Functions.listatikNezabatu(pelikulak,zein-1)

    print("Pelikula ezabatu da")
    pelikulakInprimatu()


def serieaEzabatu():
    print("-------------Seriea Ezabatu------------")
    serieakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun seriearen zenbakia:"))
    Functions.listatikNezabatu(serieak,zein-1)
    print("Seriea ezabatu da")
    serieakInprimatu()


def dokumentalaEzabatu():
    print("-------------Dokumentala Ezabatu------------")
    dokumentalakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun dokumentalaren zenbakia:"))
    Functions.listatikNezabatu(dokumentalak,zein-1)

    print("Dokumentala ezabatu da")
    dokumentalakInprimatu()


def zuzendariaEzabatu():
    print("-------------Zuzendaria Ezabatu------------")
    zuzendariakInprimatu()
    zein = int(input("Sartu ezabatu nahi duzun zuzendariaren zenbakia:"))
    Functions.listatikNezabatu(zuzendariak,zein-1)

    print("zuzendaria ezabatu da")
    zuzendariakInprimatu()

def bideoaAldatu():
    print("-------------Bideoa Aldatu------------")
    bideoakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun bideoaren posizioa:"))
    izena = input("Sartu Bideoaren Izena:")
    formatua = input("Sartu Bideoaren Formatua:")
    prezioa = int(input("Sartu Bideoaren Prezioa :"))
    urtea = int(input("Sartu Bideoaren Urtea:"))
    bideoak[zein-1].izena=izena
    bideoak[zein-1].formatua=formatua
    bideoak[zein-1].prezioa=prezioa
    bideoak[zein-1].urtea=urtea
    print("Bideoa aldatu da")
    bideoakInprimatu()

def pelikulaAldatu():
    print("-------------Pelikula Aldatu------------")
    pelikulakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun pelikularen posizioa:"))

    izena = input("Sartu Pelikularen Izena:")
    formatua = input("Sartu Pelikularen Formatua:")
    prezioa = int(input("Sartu Pelikularen Prezioa :"))
    urtea = int(input("Sartu Pelikularen Urtea:"))
    luzera = int(input("Zein da filmaren luzera(min)?"))

    pelikulak[zein-1].izena=izena
    pelikulak[zein-1].formatua=formatua
    pelikulak[zein-1].prezioa=prezioa
    pelikulak[zein-1].urtea=urtea
    pelikulak[zein-1].luzera=luzera
    print("Hauek dira eskuragarri dauden Zuzendariak.\n")
    zuzendariakInprimatu()
    baiez = int(input("Aldatu nahi duzun zuzendaria listan dago | BAI(1) | EZ(0) ?"))
    if (baiez == 1):

        zuzen = int(input("Zein da filmaren zuzendaria?"))
        pelikulak[zein-1].zuzendaria= str(zuzendariak[zuzen - 1].izena)
    else:
        zuzendariaSortu()
        zuzendariakInprimatu()
        zuzen = int(input("Zein da filmaren zuzendaria?"))
        pelikulak[zein-1].zuzendaria= str(zuzendariak[zuzen - 1].izena)

    print("Pelikula aldatu da\n")
    pelikulakInprimatu()


def serieaAldatu():
    print("-------------Seriea Aldatu------------")
    serieakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun seriearen posizioa:"))
    izena = input("Sartu seriearen Izena:")
    formatua = input("Sartu seriearen Formatua:")
    prezioa = int(input("Sartu seriearen Prezioa :"))
    urtea = int(input("Sartu seriearen Urtea:"))
    tenporadak = int(input("Zenbat tenporada ditu serieak?"))
    kapituloak = int(input("Zenbat kapitulo ditu serieak?"))

    serieak[zein-1].izena=izena
    serieak[zein-1].formatua=formatua
    serieak[zein-1].prezioa=prezioa
    serieak[zein-1].urtea=urtea
    serieak[zein-1].tenporadak=tenporadak
    serieak[zein-1].kapituloak=kapituloak
    print("Seriea aldatu da")
    serieakInprimatu()

def dokumentalaAldatu():
    print("-------------Dokumentala Aldatu------------")
    dokumentalakInprimatu()
    zein = int(input("Sartu aldatu nahi duzun dokumentalaren posizioa:"))
    izena = input("Sartu dokumentalaren Izena:")
    formatua = input("Sartu dokumentalaren Formatua:")
    prezioa = int(input("Sartu dokumentalaren Prezioa :"))
    urtea = int(input("Sartu dokumentalaren Urtea:"))
    produktora = input("Zein da dokumentalaren produktora?")
    herrialdea = input("zein da dokumentalaren herrialdea?")
    dokumentalak[zein-1].izena=izena
    dokumentalak[zein-1].formatua=formatua
    dokumentalak[zein-1].prezioa=prezioa
    dokumentalak[zein-1].urtea=urtea
    dokumentalak[zein-1].produktora=produktora
    dokumentalak[zein-1].herrialdea=herrialdea
    print("Dokumentala aldatu da")
    dokumentalakInprimatu()

def zuzendariaAldatu():
    print("-------------Zuzendaria Aldatu------------")
    zuzendariakInprimatu()
    izena = input("Sartu Zuzendariaren izena:")
    abizena = input("Sartu Zuzendariaren abizena:")
    jaio = input("Sartu Zuzendariaren JaiotzeData:")
    sariak = int(input("Sartu Zuzendariaren sari kopurua"))
    zuzendariak[zein-1].izena=izena
    zuzendariak[zein-1].abizena=abizena
    zuzendariak[zein-1].jaio=jaio
    zuzendariak[zein-1].sariak=sariak
    print("Zuzendaria aldatu da")
    zuzendariakInprimatu()


def bilatuSariak(sariak=0):
    cont=0;
    saridunak=[]
    for i in zuzendariak:
        if(i.SariKopurua>=sariak):
            cont=cont+1;
            saridunak.append(i)
    print("\n",cont, " Zuzendari aurkitu dira  ", sariak, " sari baino gehiagorekin: ")
    Functions.listaImprimatu(saridunak)

def prezioMerkea(prezioa=0):
    cont=0;
    preziomerkedunak=[]
    for i in bideoak:
        if(i.prezioa<=prezioa):
            cont=cont+1;
            preziomerkedunak.append(i)
    print("\n",cont, " Bideo aurkitu dira  ", prezioa, "  baino gutxiago balio dutenak: ")
    Functions.listaImprimatu(preziomerkedunak)

def formatuaBilatu(formatua=""):
    cont=0;
    formatuak=[]
    for i in bideoak:
        if(i.formatua==formatua):
            cont=cont+1;
            formatuak.append(i)
    print("\n",cont, " Bideo aurkitu dira  ", formatua, "  formatua dutenak: ")
    Functions.listaImprimatu(formatuak)



print("----------BideoKlub----------")
print("1- Sortu\n"
      "2- Inprimatu\n"
      "3- Ezabatu\n"
      "4- Aldatu \n"
      "5- Datuen Bilaketa \n"
      "6- Irten"
)
aukera = int(input("Aukeratu bat: "))




while (aukera!=6):

    if(aukera== 1):
        print("Zer sortu nahi duzu?")
        print("1- Bideoa\n"
          "2- Zuzendaria\n")
        zein= int(input("Aukeratu bat: "))
        if(zein ==1):
            bideoaGehitu()
        if(zein==2):
            zuzendariaSortu()


    if(aukera== 2):
        print("Zer Inprimatu nahi duzu?")
        print("1- Bideoa\n"
          "2- Pelikula\n"
          "3- Seriea\n"
          "4- Dokumentala\n"
          "5- Zuzendariak\n")
        zein= int(input("Aukeratu bat: "))
        if(zein ==1):
            bideoakInprimatu()
        if(zein==2):
            pelikulakInprimatu()
        if(zein== 3):
            serieakInprimatu()
        if (zein == 4):
            dokumentalakInprimatu()
        if (zein == 5):
            zuzendariakInprimatu()

    if (aukera == 3):
        print("Zer borratu nahi duzu?")
        print("1- Bideoa\n"
              "2- Pelikula\n"
              "3- Seriea\n"
              "4- Dokumentala\n"
              "5- Zuzendaria\n")
        zein = int(input("Aukeratu bat: "))
        if (zein == 1):
            bideoaEzabatu()
        if (zein == 2):
            pelikulaEzabatu()
        if (zein == 3):
            serieaEzabatu()
        if (zein == 4):
            dokumentalaEzabatu()
        if (zein == 5):
            zuzendariaEzabatu()

    if (aukera == 4):
        print("Zer Aldatu nahi duzu?")
        print("1- Bideoa\n"
              "2- Pelikula\n"
              "3- Seriea\n"
              "4- Dokumentala\n"
              "5- Zuzendaria\n")
        zein = int(input("Aukeratu bat: "))
        if (zein == 1):
            bideoaAldatu()
        if (zein == 2):
            pelikulaAldatu()
        if (zein == 3):
            serieaAldatu()
        if (zein == 4):
            dokumentalaAldatu()
        if (zein == 5):
            zuzendariaAldatu()

    if (aukera == 5):
        print("Zer Bilatu nahi duzu?")
        print("1- n sari baino gehiago dituzten zuzendariak\n"
              "2- n € baino gutxiago balio duten bideoak \n"
              "3- Formatu mota bateko bideoak")

        zein = int(input("Aukeratu bat: "))
        if(zein ==1):
            sariak=int(input("Sartu sari kopurua: "))
            bilatuSariak(sariak)
        if(zein ==2):
            kopurua=int(input("Sartu prezioa : "))
            prezioMerkea(kopurua)

        if(zein ==3):
            formatua=input("Sartu formatua: ")
            formatuaBilatu(formatua)











    print("\n\n1- Sortu\n"
          "2- Inprimatu\n"
          "3- Ezabatu\n"
          "4- Aldatu \n"
          "5- Datuen Bilaketa \n"
          "5- Irten"
          )

    aukera = int(input("Aukeratu bat: "))

