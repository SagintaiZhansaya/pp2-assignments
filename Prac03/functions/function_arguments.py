#1
def my_func(name):
    print("Hello,", name)

my_func("Bob")

#2
def my_func(name = "friend"):
    print("Hello,", name)

my_func("Alex")
my_func()

#3
def my_func(name, age):
    print("Hello, my name is", name, ", I am", age)

my_func("Steven", 17)

#4
def my_func(cities):
    for city in cities:
        print(city)

cities = ['Almaty', 'Astana', 'Shymkent']
my_func(cities)

#5
def addition(x, y):
    return x + y

result = addition(4, 6)
print(result)