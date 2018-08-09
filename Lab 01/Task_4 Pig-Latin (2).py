def PigLatin(a):
    if a[0] in ['a','e','i','o','u','A','E','I','O','U']:
    #if a[0] == 'a' or a[0] == 'i' or a[0] == 'e' or a[0] == 'o' or a[0] == 'u' or a[0] == 'A' or a[0] == 'I' or a[0] == 'E' or a[0] == 'O' or a[0] == 'U':

        return a + 'ay' 
    else:
        return a[1:] + a[0] + 'ay'

def main():
    a = input('Enter your text: ')
    n = a.split(' ')
    b = []
    for i in range(len(n)):
        b.append(PigLatin(n[i]))

    c = str('')
    for i in range(len(b)):
        c = c + b[i] + ' '
    print(c)
    

main()
#print(PigLatin('hello'))