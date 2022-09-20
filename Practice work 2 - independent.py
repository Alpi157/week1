import math
def ctg(x):
    return math.cos(x) / math.sin(x)


a = int(input('Enter a: '))
b = int(input('Enter b: '))
h = int(input('Enter h: '))
s = ((math.pow(a, 2) + b) * h) / (2 * (a - b) + 4)
print("s={0:2f}".format(s))
print("\n")



x = int(input('Enter x: '))
y = int(input('Enter y: '))
h = (math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(pow(math.e, x) + (pow(math.e, -1*x)))))/(pow((pow(math.e, x) + (pow(math.e, -1*x))), 3) * pow((math.sin(4 * y) + math.cos(2 * y) - 2), 2))
print("h={0:2f}".format(h))
print("\n")



x = int(2)
y = int(1)
a = pow(pow(x, y), x) + pow(pow(x, x), y) - pow(x, 4)
print("Ans = {0:2f}".format(a))
print("\n")



x = int(3)
y = float(0.2)
a = (5 * x * y) / (pow(x, 3) - 4) + math.exp(pow(x, 2)) + math.sqrt((math.cos(y) ** 2) - pow(y, 2))
print("Ans = {0:2f}".format(a))
print("\n")


x = int(3)
y = int(5)
a = math.sqrt(abs(y)) + (math.atan(math.log(x)) ** 3) / (pow(x, y) - y + 1)
print("Ans = {0:2f}".format(a))
print("\n")



x = int(3)
y = int(1)
z = int(2)
a = pow(4, x*y) - pow(x, y*z) + pow((x * y), z)
print("Ans = {0:2f}".format(a))
print("\n")



x = int(2)
y = int(2)
z = int(1)
a = (4 * abs(x) - x * y * pow(z, 2)) / (x + math.exp(y*x) - 2 * y * z)
print("Ans = {0:2f}".format(a))
print("\n")



x = int(3)
y = int(1)
z = int(3)
a = (2 * 3 * 4) / ((math.sin(x) ** 3) + math.tan(y) ** 3) - math.sqrt(pow(z, x-y))
print("Ans = {0:2f}".format(a))
print("\n")



x = int(4)
a = (math.log(pow((x - 3), 4)) + pow(2, x) * math.sin(3 * x) ** 2) / (4 * x - 5.2)
print("Ans = {0:2f}".format(a))
print("\n")



x = int(2)
y = int(2)
z = int(1)
a = math.sqrt(0.6 * x * y * z) + pow(pow(y, x), 2) - math.exp(math.sin(pow(2 * x, 2)))
print("Ans = {0:2f}".format(a))
print("\n")



x = float(0.5)
y = int(2)
a = (math.asin(pow(x, 3)) - 6) / (8 * (math.cos(4 * 8) - math.sin(4 * x)))
print("Ans = {0:2f}".format(a))
print("\n")



x = int(2)
y = int(1)
z = int(3)
a = (abs(math.log(pow(x, 3))) + math.exp(2 * x)) / (x + 3.4) - ctg(3 / x*y*z) ** 3
print("Ans = {0:2f}".format(a))
print("\n")














