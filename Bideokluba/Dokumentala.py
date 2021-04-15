from Bideokluba.Bideoa import Bideoa

class Dokumentala(Bideoa):

    def __init__(self, izena, formatua, prezioa, urtea, produktora,herrialdea):
        self.izena = izena
        self.formatua = formatua
        self.prezioa = prezioa
        self.urtea = urtea
        self.produktora = produktora
        self.herrialdea = herrialdea

    def __str__(self):
        s = "DOKUMENTALA: "+ self.izena + " Formatua: "+ self.formatua + " Prezioa: "+ str(self.prezioa) + " Urtea: " + str(self.urtea) + " Produktora: "+ self.produktora + " Herrialdea: "+ self.kapituloak
        return s
