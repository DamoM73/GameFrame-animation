from GameFrame import RoomObject, Globals
import pygame

class Explosion(RoomObject):

    def __init__(self, room, x, y):
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set animation values
        self.frame_rate = 1                         # frames change every 4 game frames
        self.current_frame = 40                      # start at frame 0
        self.total_frames = 41                      # total number of frames
        self.running = False

        # set image
        self.image_frames = []                                  # list to hold image frames
        for index in range(self.total_frames):                  # load each image frame from the Explosion_frames folder
            self.image_frames.append(
                self.load_image(f"Explosion_frames\explosion_{index:03}.png")
            )                                           # dictionary to hold image frames by direction
        self.update_image()

        # register events
        self.handle_key_events = True

    def update_image(self):
        if self.running:
            self.current_frame = (self.current_frame + 1) % self.total_frames                 # increment the frame number
        self.set_image(self.image_frames[self.current_frame], 50, 49)   # set the new image
        self.set_timer(self.frame_rate, self.update_image)
        if self.current_frame == 40:                              # reset the timer to call this method again after frame_rate game frames
            self.running = False
            
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """

        if key[pygame.K_SPACE]:         
            self.running = True                          # character is moving
