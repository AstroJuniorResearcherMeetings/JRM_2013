import math
from abc import abstractproperty

#####################
class Shape (object):
    
    @abstractproperty
    def area (self):
        pass

#####################
class Circle (Shape):

    def __init__ (self,radius):
        self.radius = radius

    @property
    def area (self):
        return math.pi*self.radius**2

#####################
class Rectangle (Shape):
    
    def __init__ (self,width,heigth):
        self.heigth = abs(heigth)
        self.width = abs(width)

    def area (self):
        return self.heigth*self.width

    def scale_height (self,scale):
        self.heigth *= scale

#####################
class Square (Rectangle):
    
    def __init__ (self,length):

        super(Square,self).__init__(length,length)







class Data (object):
    
    def __init__ (self,input):
        self.input = input








