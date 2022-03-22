


from robot import Robot


class Fleet :
    def __init__(self) -> None:
        self.robots = [Robot("One"),Robot("Two"),Robot("Three")]
      
    def create_fleet(self):
        make_fleet = True
        while make_fleet is True:
            for robot in self.robots:
                print(f'this is {robot.name}')
        
    

start_work = Fleet()

start_work.create_fleet 

for robot in start_work.robots:
    print(robot.name)
        