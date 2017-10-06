class Adder:
    a = 0
    b = 0
    def add(self):
        return self.a + self.b
    def __init__(self,a,b):
        self.a = a;
        self.b = b;
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

x = Adder(a,b)
print(x.add())