#1
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(name, age)

#2
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)

#3
names = ["Sara", "John", "Finn"]
gpas = [3.8, 3.5, 2.6]

for i, (name, gpa) in enumerate(zip(names, gpas), start=1):
    print(i, name, gpa)

#4
x = "123"
print(isinstance(x, str))  

num = int(x)
print(isinstance(num, int))  

y = 4.5
print(isinstance(y, float))