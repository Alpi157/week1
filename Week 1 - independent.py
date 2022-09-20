name = input('Your last name, first name? ')
age = input('How old are you? ')
num = input('Your phone number? ')
print ("Your full name is ", name)
print ("Your age is ", age)
print ("Your phone number is ", num)



a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))
d = float((a + b + c) / 2)
print ("area of square is ", a * b)
print ("area of triangle is ", (d * (d - a) * (d - b) * (d - c)) ** 0.5)



print ("a) multiply the planned number by 5;")
print ("b) add 8;")
print ("c) multiply the sum by 2.")
a = float(input('Enter the result: '))
print(((a / 2) - 8) / 5)



a = float(input('First number: '))
o = str(input('Operation: '))
b = float(input('Second number: '))
if o == '+':
    print(a + b)
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/':
    print(a / b)


number = 14
if number > 10 and number != 12 and number <= 15 or number == 18:
    print("True")



i = 34
while i <= 67:
    if i % 2 == 0:
        print(i)
    i = i + 1




i = 1
while i <= 100:
    if i != 50 and i != 99:
        print(i)
    i = i + 1 



def printing(letter, number):
    print(letter * number)
word = str(input("Enter the word "))
number = int(input("Enter the number "))
word = tuple(word)
for letters in word:
    printing(letters, number)   












    
