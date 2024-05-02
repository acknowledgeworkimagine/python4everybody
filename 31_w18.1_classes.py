class PartyAnimal:
    def __init__(self):
        self.x=0 #It helps to read it as x within self (the instance - when created)
        
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

print("Type: \n", type(an))
print("Dir: \n", dir(an))
print("Type: \n", type(an.x))
print("Type: \n", type(an.party))