from Ikastetxea.Pertsona import Pertsona

class Irakaslea(Pertsona):

    def __init__(self,i,n,s,M,ad,departamenduZkia):
     super().__init__(i,n,s,M,ad)
     self.departamenduZkia= departamenduZkia

    def setGroup(self,group):
        self.group=group

    def getGroup(self):
       return self.group

    def print(self):
        print(self.Id, self.name, self.surname, self.movile, self.adina,self.departamenduZkia)



