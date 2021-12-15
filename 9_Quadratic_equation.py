import cmath

a = int(input())
b = int(input())
c = int(input())

delta = b*b + 4*a*c

x1 = (-b + cmath.sqrt(delta))/(2*a)
x2 = (-b - cmath.sqrt(delta))/(2*a)

print(x1)
print(x2)
