# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random, uniform


class Floater(Prey):
    def __init__(self,x,y):
        self._image = PhotoImage(file='ufo.gif')
        Prey.__init__(self,x,y,self._image.width(),self._image.height(),0,5)
        Prey.randomize_angle(self)
        
    def update(self, speed):
        Prey.move(self)
        Prey.wall_bounce(self)
        if random() <= .3:
            speed_mult,rad_mult = uniform(-.5,.5),uniform(-.5,.5)
            while self._speed + speed_mult > 3 and self._speed + speed_mult < 7:
                self._speed += speed_mult
            self._angle += rad_mult
            
            
            
    def display(self, canvas):
       canvas.create_image(*self.get_location(),image=self._image)