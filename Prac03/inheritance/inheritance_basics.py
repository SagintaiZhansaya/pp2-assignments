#1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    pass

d = Dog("Buddy")
d.speak()  

#2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print("This vehicle is a", self.brand)

class Car(Vehicle):
    pass

c = Car("Toyota")
c.info()  

#3
class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        print("Color of the shape is", self.color)

class Circle(Shape):
    pass

circle = Circle("Red")
circle.display_color()  

#4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, "is", self.age, "years old")

class Student(Person):
    pass

s = Student("Alice", 20)
s.info()  

#5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print(self.name, "earns", self.salary)

class Manager(Employee):
    pass

m = Manager("Bob", 5000)
m.show_salary()  
