from pertsona import pertsona
class ikaslea(pertsona):


    def __init__(self,i,n,s,M,ad,group):
     super().__init__(i,n,s,M,ad)
     self.group= group

    def setGroup(self,group):
        self.group=group
    def getGroup(self):
       return self.group

    def print(self):
        print(self.Id, self.name, self.surname, self.movile, self.adina,self.group)



