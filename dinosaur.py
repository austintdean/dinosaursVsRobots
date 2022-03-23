


class Dinosaur:
    def __init__(self, name) :
        self.name = name 
        self.health = 500
        self.attack_power = 100

    def attack_robot(self, robot):
        robot_damage = robot.health - self.attack_power 
        robot.health = robot_damage
        return robot.health
        