#1
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#2
i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

#3
word = "education"
i = 0

while i < len(word):
    letter = word[i]
    i += 1
    if letter in "aeiou":
        continue
    print(letter)

#4
numbers = [3, -1, 5, -7, 2, -4]
i = 0

while i < len(numbers):
    num = numbers[i]
    i += 1
    if num < 0:
        continue
    print(num)

#5
i = 0

while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)
