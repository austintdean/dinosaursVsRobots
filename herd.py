from dinosaur import Dinosaur



class Herd:
    def __init__(self) -> None:
        self.herd = [Dinosaur("T Rex"),Dinosaur("Brachiosaurus"),Dinosaur("Triceratops")]

    def create_herd(self, dino_object):
        self.herd.append(dino_object)
        print(f'Added {dino_object.name} the held!')

