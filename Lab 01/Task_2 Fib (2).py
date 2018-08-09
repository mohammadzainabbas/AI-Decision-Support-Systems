def Fib(n):
    if n==0 or n==1:
       return 1    
    else:
        return Fib(n-1)+Fib(n-2)
def main():
    a = int(input('Enter your number '))
    print(str(Fib(a)))
#main()
a = int(input('Enter number '))
for i in range(0,a):
    print(str(Fib(i)))