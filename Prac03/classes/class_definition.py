#1
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#2
class MyClass:
  x = 8

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

#3
class MyClass:
    name = 'Anna'
    age = 21

p1 = MyClass()
print(p1.name, p1.age)

#4
class student:
    major = 'Tourism'
    gpa = 3.85

Jenny = student()

if Jenny.gpa == 4.00:
    print('You are A+ student!')
else:
    print('Great gpa.')

#5
class products:
    product = 'apple'
    price = 10

food = products()

print(food.product, 'costs', food.price, 'dollars')
