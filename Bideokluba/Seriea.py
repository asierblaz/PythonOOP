from Bideokluba.Bideoa import Bideoa

class Seriea(Bideoa):

    def __init__(self, izena, formatua, prezioa, urtea, tenporadak,kapituloak):
        self.izena = izena
        self.formatua = formatua
        self.prezioa = prezioa
        self.urtea = urtea
        self.tenporadak = tenporadak
        self.kapituloak = kapituloak

    def __str__(self):
        s = "SERIEA: "+ self.izena + " Formatua: "+ self.formatua + " Prezioa: "+ str(self.prezioa) + " Urtea: " + str(self.urtea) + " Tenporadak: "+ str(self.tenporadak) + " Kapituloak: "+ str(self.kapituloak)
        return s
