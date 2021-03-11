

class Departamentuak:

    def __init__(self,izena,zenbakia):
        self.izena=izena
        self.zenbakia= zenbakia

    def getIzena(self):
            return self.izena

    def setIzena(self, izena):
            self.izena = izena

    def getZenbakia(self):
            return self.zenbakia

    def setZenbakia(self, zenbakia):
            self.zenbakia = zenbakia

    def print(self):
            print(self.izena, self.zenbakia)