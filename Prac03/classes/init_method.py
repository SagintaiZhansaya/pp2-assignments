#1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

#2
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

#3
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

#4
class products:
    def __init__(self, product, price):
        self.product = product
        self.price = price

food1 = products('apple', 10)
food2 = products('pizza', 15)
food3 = products('bread', 5)

print(food1.product, food1.price)
print(food2.product, food2.price)
print(food3.product, food3.price)

#5
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.name)  
print(dog1.age)   

print(dog2.name)  
print(dog2.age)   