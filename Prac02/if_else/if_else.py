#1
is_checked = False

if is_checked:
    print("no new messages")
else:
    print("there are new messages")

#2
a = 4
b = 3

if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")
else:
    print("b is greater than a")

#3
number = 9

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#4
username = "Bob"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Username cannot be empty")

#5
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")
