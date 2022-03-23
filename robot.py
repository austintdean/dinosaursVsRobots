from weapon import Weapon 




class Robot:
    def __init__(self, name, weapon_passed_in):
        self.name = name
        self.health = 500
        self.weapon = weapon_passed_in 
        # weapon_passed_in is an object 
    
    def attack_dinosaur(self, dinosaur):
        dinosaur_damage = dinosaur.health - self.weapon.attack_power 
        dinosaur.health = dinosaur_damage
        return dinosaur.health
        