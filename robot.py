
from weapon import Weapon 
# from dinosaur import Dinosaur

class Robot:
    def __init__(self, name) :
        self.name = name
        self.health = 500
        self.weapon = Weapon('Weapon',100)
        
    def attack_dinosaur(self, dinosaur):
           pass


