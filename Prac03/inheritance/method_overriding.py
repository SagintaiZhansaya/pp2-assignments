#1
class ONE:
    def sequence(self):
        print("first")

class TWO(ONE):
    def sequence(self):  
        print("second")

o = ONE()
o.sequence()

t = TWO()
t.sequence()

#2
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):  
        print("Car is driving")

v = Vehicle()
c = Car()

v.move() 
c.move()  

#3
class Employee:
    def get_salary(self):
        return 3000

class Manager(Employee):
    def get_salary(self): 
        return 5000

e = Employee()
m = Manager()

print(e.get_salary())  
print(m.get_salary())  

#4
class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def login(self):  
        super().login()
        print("Admin privileges granted")

a = Admin()
a.login()

#5
class Shape:
    def area(self):
        print("Area formula not defined")

class Circle(Shape):
    def area(self):   
        print("Area = π * r²")

s = Shape()
c = Circle()

s.area() 
c.area()  
