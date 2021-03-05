class pertsona:
  skin="white"

  def __init__(self, i,n, s,M, ad):

       self.Id= i
       self.name = n
       self.surname = s
       self.movile = M
       self.adina= ad

  def getid(self):
      return self.Id

  def getname(self):
      return self.name

  def getsurname(self):
      return self.surname

  def getmovile(self):
     return self.movile

  def getadina(self):
     return self.adina

  def setid(self,id):
    self.id=id

  def setname(self,name):
    self.name=name

  def setsurname(self,surname):
   self.surname=surname

  def setmovile(self,movile):
    self.movile=movile

  def setadina(self,adina):
    self.adina = adina

  def print(self):
    print(self.Id, self.name,self.surname,self.movile,self.adina)

