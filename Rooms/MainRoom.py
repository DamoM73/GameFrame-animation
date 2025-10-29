from GameFrame import Level, Globals
from Objects.Asteroid import Asteroid
from Objects.Chracter import Character

class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.add_room_object(Asteroid(self, 100, 100))
        self.add_room_object(Character(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2))