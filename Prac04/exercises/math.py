#1
x = float(input())
import math

p = math.pi
print(round(x * p / 180, 6))

#2
h = float(input())
b1 = float(input())
b2 = float(input())

print((b1 + b2) * h / 2)

#3
n = int(input())
l = float(input())
import math

perimeter = n * l
apothem = l / (2 * math.tan(math.pi / n))

print(round(perimeter * apothem / 2))

#4
b = float(input())
h = float(input())

print(round(b * h, 1))