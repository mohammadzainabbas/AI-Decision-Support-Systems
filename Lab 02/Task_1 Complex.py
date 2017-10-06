import math
class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    def Magnitude(self):
        return math.sqrt(math.pow(self.real,2) + math.pow(self.imaginary,2))
    def Orientation(self):
        return math.atan(self.real/self.imaginary)
    def info(self):
        print('Your number is: ' + str(self.real) + ' + ' + str(self.imaginary) + 'i')
        return 

a = int(input('Enter real part: '))
b = int(input('Enter imaginary part: '))
x = Complex(a,b)
print(x.info())

print(x.Magnitude())
print(x.Orientation())