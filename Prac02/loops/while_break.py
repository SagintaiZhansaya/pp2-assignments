#1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#2
i = 0
txt = "Hello, World!"

while i < len(txt):
    print(txt[i], end='')

    if txt[i] == "o":
        break
    i += 1

#3
numbers = [3, 7, 2, 9, 5]
i = 0

while i < len(numbers):
    if numbers[i] == 9:
        print("number 9 in position", i)
        break
    i += 1

#4
i = 0
txt = "apple, banana, orange"

while i < len(txt):
    print(txt[i], end='')

    if txt[i] == "e":
       break
    i += 1

#5
i = 0
summa = 0

while i < 100:
    summa += i
    if summa > 50:
        break
    i += 1

print("The sum became more than 50 on the number", i)
