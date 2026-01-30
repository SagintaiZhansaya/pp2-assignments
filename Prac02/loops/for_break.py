#1
for i in range(10):
    if i == 5:
        break
    print(i)

#2
numbers = [4, 7, 2, -1, 9, 3]

for num in numbers:
    if num < 0:
        break
    print(num)

#3
numbers = [10, 23, 45, 70, 11]
target = 45

for num in numbers:
    if num == target:
        print("Found it!")
        break

#4
text = "Hello World"

for s in text:
    if s == " ":
        break
    print(s)

#5
word = "strength"

for letter in word:
    if letter in "aeiou":
        print("First vowel:", letter)
        break

