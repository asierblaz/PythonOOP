
class Zuzendaria():

    def __init__(self, izena, abizena, JaiotzeData, SariKopurua):
        self.izena = izena
        self.abizena = abizena
        self.JaiotzeData = JaiotzeData
        self.SariKopurua = SariKopurua

    def __str__(self):
        s = "ZUZENDARIA: "+ self.izena + " Formatua: "+ self.abizena + " Jaiotze Data: "+ self.JaiotzeData +  " Sari Kopurua: "+ str( self.SariKopurua)
        return s
