from dinosaur import Dinosaur
from robot import Robot
from fleet import Fleet 
from herd import Herd
from random import Random




class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet().fleet
        self.herd = Herd().herd


    def run_game(self):
        self.display_welcome()
        # self.battle()
        self.display_winners()

    def display_welcome(self):
        print("**********************************************")
        print("Welcome to Robots vs Dinosaurs 3!!!")
        print("**********************************************")

    def battle(self):
       while self.fleet is True:
            self.show_dino_opponent_options
            self.dino_turn
            self.show_robo_opponent_options
            self.robo_turn
        
        # dinos attacks(sees robots to attack?"show_opponent_options"), then robot attacks(sees robots to attack("show opponent options"))
        



    def dino_turn(self):
        # attacks dinos
        if self.herd.dinosaur.health >= 0:
           Random.choice(self.herd).attack_robot(Random.choice(self.fleet))
        else:
            self.herd.remove()
      
    

    def robo_turn(self):
        if self.fleet.robot.health >= 0:
            Random.choice(self.fleet).attack_dinosaur(Random.choice(self.herd))
        else: 
            self.fleet.remove()
      
        
     

    

    def show_dino_opponent_options(self):
        # show list of robots with robot health
        for robot in self.fleet:
            print(f"{robot.name}, has {robot.health} HP")
    

    def show_robo_opponent_options(self):
        for dinosaur in self.herd:
            print(f"{dinosaur.name}, has {dinosaur.health} HP")

    def display_winners(self):
        if self.fleet == False: 
            print(f'The Dinosaurs rule!')
        if self.herd == False:
            print(f'The Robots rule!')
        
