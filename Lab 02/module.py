#Define a variable: 
Age = 78 
# Define a method 
def Print(): 
    print ("hello")    
# Define a class 
class Piano: 
    def __init__(self): 
        self.Type = input("What type of piano? ") 
        self.Height = input("What height (in feet)? ") 
        self.Price = input("How much did it cost? ") 
        self.Age = input("How old is it (in years)? ")
    def PrintDetails(self): 
        print ("This piano is a/an " + self.Height + " foot",) 
        print (self.Type, "piano, " + self.Age, "years old and costing " + self.Price + " dollars.") 
