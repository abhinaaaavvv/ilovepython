import math

a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of c: "))

d = pow(b, 2) - (4 * a * c)
if d >= 0:
    d = math.sqrt(d)
else:
    d = 0.0

x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)
print(f"the values are {x1} and {x2}")
