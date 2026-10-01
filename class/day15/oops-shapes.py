import math
class Shape:
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def volume(self):
        return self.length*self.breadth*self.height

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
    def volume(self):
        return self.side*self.side*self.side

class Rectangle(Shape):
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def volume(self):
        return self.length*self.breadth*self.height

class Triangle(Shape):
    def __init__(self,base,height,a,b,c):
        self.base=base
        self.height=height
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.a+self.b+self.c
    def volume(self):
        return 0

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius
    def volume(self):
        return 0

s=Square(5)
r=Rectangle(4,6,3)
t=Triangle(3,4,3,4,5)
c=Circle(7)

print("Square:",s.area(),s.perimeter(),s.volume())
print("Rectangle:",r.area(),r.perimeter(),r.volume())
print("Triangle:",t.area(),t.perimeter(),t.volume())
print("Circle:",c.area(),c.perimeter(),c.volume())