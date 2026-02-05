#1
class Person:
    population = 0  

    def __init__(self, name):
        self.name = name  
        Person.population += 1

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.population) 

#2
class Dog:
    species = "dog" 

    def __init__(self, name):
        self.name = name  

d1 = Dog("Buddy")
d2 = Dog("Max")

print(d1.species)  
print(d2.species)  

#3
class Car:
    wheels = 4  

    def __init__(self, brand):
        self.brand = brand

c1 = Car("Toyota")
c2 = Car("BMW")

print(c1.wheels)  
print(c2.wheels)  

#4
class Student:
    all_names = []  

    def __init__(self, name):
        self.name = name
        Student.all_names.append(name)

s1 = Student("Alice")
s2 = Student("Bob")

print(Student.all_names)  

#5
class Button:
    click_count = 0  

    def click(self):
        Button.click_count += 1
        print("Button clicked!")

b1 = Button()
b2 = Button()

b1.click()  
b2.click() 

print(Button.click_count)  