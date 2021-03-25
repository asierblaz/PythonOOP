from Ibilgailuak.Coche import Coche

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada , carga):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga = carga

    def getCarga(self):
        return self.carga

    def setCarga(self, carga):
        self.carga = carga

    def __str__(self):
        s = "Camioneta Color " + self.color + " ," + str(self.ruedas) + " ruedas ,"+ str(self.velocidad) +" km/h , "+str(self.cilindrada)+" cc, "+ str(self.carga)+" kg de carga"
        return s