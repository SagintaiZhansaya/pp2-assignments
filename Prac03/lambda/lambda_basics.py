#1
x = lambda a : a + 10
print(x(5))

#2
x = lambda a, b : a * b
print(x(6, 5))

#3
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

#4
def my_func(n):
    return lambda a : a * n

double = my_func(2)

print(double(17))

#5
def my_func(n):
    return lambda a : a * n

triple = my_func(3)

print(triple(17))
