


from robot import Robot
from weapon import Weapon


class Fleet :
    def __init__(self) -> None:
        self.fleet = [Robot("Megazord", Weapon("sword", 100 )),Robot('Iron Giant', Weapon("spear", 100)),Robot('biltzcrank', Weapon("extendo fist", 100)),]
        

    def create_fleet(self, robot_object):
        self.fleet.append(robot_object)
        print(f'Added {robot_object.name} the fleet!')



 