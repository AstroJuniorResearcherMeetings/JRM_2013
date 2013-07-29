# This gives a simple example of a class

# quick notes:
#     instance == object
#     method is a function within an object

# define using 'class', 
# this inherits traits from the class 'object' (inheritance discussed later)
class Rectangle (object):
    """
    A document giving information about the class Rectangle
    """
    
    # when an instance of this class is created this method is called
    def __init__ (self,width,heigth):

        # self is a variable which holds variables the class knows about
        self.width = abs(width)
        self.heigth = abs(heigth)

    # you can define methods for common things about a Rectangle
    def area (self):
        # this method knows about the class variables
        return self.width*self.heigth


# create a rectangle object 2.3 by 5.0
rectangle = Rectangle(2.3,5.0)

# create a rectangle object 1.3 by 10.2
rectangle2 = Rectangle(1.3,10.2)


print("The areas of the rectangles:")
print(rectangle.area())
print(rectangle2.area())



