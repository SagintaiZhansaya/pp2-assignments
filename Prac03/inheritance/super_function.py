#1
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

c = Car("Toyota", 4)
print(c.brand, c.doors)   


#2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, major):
        super().__init__(name)
        self.major = major

s = Student("Alice", "Math")
print(s.name, s.major)     

#3
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Alice", "A")
print(s.name, s.grade)     

#4
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

d = Dog("Alpha", "Husky")
print(d.name, d.breed)    

#5
class Products:
    def __init__(self, name):
        self.name = name

class Prices(Products):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

food = Prices("pizza", 12)
print(food.name, food.price)