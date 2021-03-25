from Ibilgailuak.Vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def getVelocidad(self):
        return self.velocidad

    def setVelocidad(self, velocidad):
        self.velocidad = velocidad

    def getCilindrada(self):
        return self.cilindrada

    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada

    def __str__(self):
        s = "Coche Color " + self.color + " ," + str(self.ruedas) + " ruedas ,"+ str(self.velocidad) +" km/h , "+str(self.cilindrada)+" cc"
        return s