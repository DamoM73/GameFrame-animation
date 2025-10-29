from GameFrame import RoomObject, Globals
import random


class Asteroid(RoomObject):

    def __init__(self, room, x, y):

        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)

        # set animation values
        self.frame_rate = 4                         # frames change every 4 game frames
        self.current_frame = random.randint(0, 7)   # start at a random frame
        self.num_frames = 8                         # total number of frames

        # set image
        self.image_frames = []                      # list to hold image frames
        for index in range(self.num_frames):        # load each image frame from the Asteroid_frames folder
            self.image_frames.append(
                self.load_image(f"Asteroid_frames\Asteroid_{index}.png")
            )
        self.update_image()                         # start the animation by calling update_image()

    def update_image(self):
        """
        Animates the asteroid by changing the image as per frame rate
        """
        self.current_frame = (self.current_frame + 1) % self.num_frames     # increment the frame number
        self.set_image(self.image_frames[self.current_frame], 50, 49)       # set the new image
        self.set_timer(self.frame_rate, self.update_image)                  # reset the timer to call this method again after frame_rate game frames
