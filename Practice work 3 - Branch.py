a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

if a == b == c:
    print('Numbers are equal')
else:
    print(min(a,(min(b, c))))
    

    
    
