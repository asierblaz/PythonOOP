from Ibilgailuak.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas,tipo):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo



    def __str__(self):
        s = "Bicicleta Color " + self.color + " ," + str(self.ruedas) + " ruedas ,"+ self.tipo
        return s;