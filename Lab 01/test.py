def calculator(a,b,sel):

    print(str((a + b) if (sel == 1) else ((a - b) if (sel == 2) else((a * b) if (sel == 3) else ((a / b) if (sel==4) else 0)))))

sel = int(input('Enter your choice '))
a = int(input('Enter your 1st number '))
b = int(input('Enter your 2nd number '))


calculator(a,b,sel)