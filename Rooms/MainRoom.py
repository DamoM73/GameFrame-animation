from GameFrame import Level, Globals
from Objects.Asteroid import Asteroid
from Objects.Character import Character
from Objects.Explosion import Explosion
from Objects.Button import Button

class MainRoom(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.add_room_object(Asteroid(self, 100, 100))
        self.add_room_object(Character(self, Globals.SCREEN_WIDTH/2, Globals.SCREEN_HEIGHT/2))
        self.add_room_object(Explosion(self, Globals.SCREEN_WIDTH - 100, Globals.SCREEN_HEIGHT - 100))
        self.add_room_object(Button(self, Globals.SCREEN_WIDTH/2, 100))