
class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas


    def getColor(self):
            return self.color

    def setColor(self, color):
            self.color = color

    def getRuedas(self):
            return self.ruedas

    def setRuedas(self, ruedas):
            self.ruedas = ruedas

    def __str__(self):
        s = "Vehiculo Color " + self.color + " ," + str(self.ruedas) + " ruedas"
        return s
