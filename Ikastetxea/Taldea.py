

class Taldea:

    def __init__(self,kodea,zenbakia):
        self.kodea=kodea
        self.zenbakia= zenbakia

    def getKodea(self):
            return self.kodea

    def setKodea(self, kodea):
            self.kodea = kodea

    def getZenbakia(self):
            return self.zenbakia

    def setZenbakia(self, zenbakia):
            self.zenbakia = zenbakia

    def print(self):
            print(self.kodea, self.zenbakia)