from abc import abstractproperty


# define superclass
class Shape (object):
    
    # an abstract property is a required property of the class.
    # so all shape objects will have something called area
    @abstractproperty
    def area (self):
        pass


# create a subclass of shape which is a Rectangle
class Rectangle (Shape):
    
    
    def __init__ (self,width,heigth):
        self.width = abs(width)
        self.heigth = abs(heigth)

    # this allows you to access this method without parentheses
    @property
    def ratio (self):
        return self.width/self.heigth

    # area is a property. If you didn't have it then the code would give
    # an error, try it. 
    def area (self):
        return self.width*self.heigth
    

# create a subclass of Rectangle which is a Square
class Square (Rectangle):
    
    
    def __init__ (self,side_length):

        # access the superclass Rectangle
        super(Square,self).__init__(side_length,side_length)




square = Square(10)
square.area() # returns the area of the square by using the method Square inhereted from Rectangle
square.ratio # Inhereted ratio for Rectangle


        
        

