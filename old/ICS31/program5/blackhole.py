# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        
    def update(self, speed):
        pass
                
    
    def display(self, canvas):
        canvas.create_oval(self._x-Black_Hole.radius      , self._y-Black_Hole.radius,
                                self._x+Black_Hole.radius, self._y+Black_Hole.radius,
                                fill='black')
    
    def contains(self,xy):
        return (self._x - self._width/2) - xy[0]  <= Black_Hole.radius <= (self._x + self._width/2) - xy[0] and\
               (self._y - self._height/2) - xy[1] <= Black_Hole.radius <= (self._y + self._height/2) - xy[1]