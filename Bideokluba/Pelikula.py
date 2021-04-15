from Bideokluba.Bideoa import Bideoa

class Pelikula(Bideoa):

    def __init__(self, izena, formatua, prezioa, urtea, luzera,generoa):
        self.izena = izena
        self.formatua = formatua
        self.prezioa = prezioa
        self.urtea = urtea
        self.luzera = luzera
        self.generoa = generoa

    def __str__(self):
        s = "PELIKULA: "+ self.izena + " Formatua: "+ self.formatua + " Prezioa: "+ str(self.prezioa) + " Urtea: " + str(self.urtea) + " Luzera(min): "+ str(self.luzera) + " Generoa: "+ self.generoa
        return s
