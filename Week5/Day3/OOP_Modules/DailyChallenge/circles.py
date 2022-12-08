import turtle
class Circle():
    '''A class initialized with radius or diameter of a circle'''
    def __init__(self, radius = 0, diameter = 0,) -> None:
        self.radius = radius
        self.diameter = radius*2
    @classmethod
    def from_diameter(cls,diameter):
        new_circle = Circle(diameter/2)
        return new_circle

    def circle_area(self) -> float:
        '''calculates the area of the circle'''
        return  3.14 * self.radius**2

    def print_circle(self): #what is the output?
        '''prints the circle with given area using module turtle'''
        output = turtle.circle(self.circle_area())
        return output

    def __add__(self,other)->object:
        '''adds two circles together'''
        return Circle(self.radius + other.radius)

    def __le__(self, other)->str:
        '''compare two circles radius'''
        return self.circle_area() <= other.circle_area()
    
    def __l__(self):
        return self.circle_area()

    def __eq__(self, other):
        return self.circle_area() == other.circle_area()

    def __repr__(self):
        return str
    def sort_circles(self, list)->list:
        '''sort 3 circles in a list'''
        to_sort =[self]
        to_sort.append(list)
        sorted_circles = to_sort.sort()
        return sorted_circles

circleA = Circle(2)
circleB = Circle(4)
circleC = Circle(3,6)
print(f'circleA radius:{circleA.radius} | diameter: {circleA.diameter}')
print(f'circleB radius:{circleB.radius} | diameter: {circleA.diameter}')
circleA.print_circle()
circleA.circle_area()
print(circleA + circleB)
circles_to_sort = [circleB, circleC]
circleA.sort_circles(circles_to_sort)
print(circleA = circleB)