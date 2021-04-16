

class Bideoa():

    def __init__(self, izena, formatua, prezioa, urtea):
        self.izena = izena
        self.formatua = formatua
        self.prezioa = prezioa
        self.urtea = urtea

    def __str__(self):
        s = "BIDEOA : "+ self.izena + " Formatua: "+ self.formatua + " Prezioa: "+ str(self.prezioa) + " Urtea: " + str(self.urtea)
        return s
