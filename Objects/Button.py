from GameFrame import RoomObject
import pygame

class Button(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image("button.png")
        self.set_image(image, 176, 64)

        self.handle_mouse_events = True


    def clicked(self, button_number):
        if button_number == 1:  # left mouse button
            print("Left")
        elif button_number == 3:  # right mouse button
            print("Right")
        elif button_number == 2:  # middle mouse button
            print("Middle")