def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    if b==0:
        print("Can't divide by zero. Try again")
        return 0
    else:
        return a/b
def Calculator(choice):
    a = int(input('Enter your 1st number: '))
    b = int(input('Enter your 2nd number: '))

    if (choice == 1):
        print('Sum is '+ str(Add(a,b)))
    elif choice == 2:
        print('Difference is '+ str(Subtract(a,b)))
    elif choice == 3:
        print('Product is '+ str(Multiply(a,b)))
    elif choice == 4:
        print('Quotient is '+ str(Divide(a,b)))
    else:
        print('No operation specified/exist')
def Menu():
    choice = (input('Enter your choice (digit) : 1-> Add 2-> Subtract 3-> Multiply 4-> Divide '))
    Calculator(int(choice))

def main():
    Menu()

main()
    