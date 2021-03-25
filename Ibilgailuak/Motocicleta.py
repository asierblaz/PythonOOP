from Ibilgailuak.Bicicleta import Bicicleta

class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas,tipo, velocidad , cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
        self.velocidad= velocidad
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
        s = "Motocicleta Color " + self.color + " ," + str(self.ruedas) + " ruedas ,"+ self.tipo + ", "+ str(self.velocidad)+" km/h"+ ", "+ str(self.cilindrada)+ " cc"
        return s