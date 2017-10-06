class Shape:
    def __init__(self,x,y):
        #run-time initialization
        self.x = x
        self.y = y
    #Compile-time initialization
    description = "This shape has not been described yet"
    author = "Nobody has claimed this shape yet"

    def area(self):
        return self.x*self.y
    def perimeter(self):
        return 2*self.x*self.y
    def describe(self,text):
        self.description = text
    def authorName(self,text):
        self.author = text
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale

#Inhertiant class
class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x
class DoubleSquare(Square):
    def __init__(self,y):
        self.x = 2*y
        self.y = y
    #Overwriting perimeter function
    def perimeter(self):
        return 2*self.x + 3*self.y
    

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

x = Shape(a,b)
y = DoubleSquare(a)

print(x.area())
print(y.perimeter())