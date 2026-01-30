#1
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

#2
words = ["apple", "", "banana", "", "cherry"]

for word in words:
    if word == "":
        continue
    print(word)

#3
text = "Hello"

for c in text:
    if c.islower():
        continue
    print(c)

#4
i = 0

while i < 10:
    i += 1
    if i < 5:
        continue
    print(i)

#5
scores = [78, 45, 89, 32, 91]

for score in scores:
    if score < 50:
        continue
    print("Passed:", score)

