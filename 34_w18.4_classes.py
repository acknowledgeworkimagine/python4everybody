class PartyAnimal:
    def __init__(self,z):
        self.x=0 
        self.name = z
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        

class FootballFan(PartyAnimal):
    def __init__(self,z):
        super().__init__(z)
        self.points=0
    
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points", self.points)

j = FootballFan("Jim")
j.party()
j.touchdown()