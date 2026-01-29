#1
i = 1
while i < 6:
    print(i)
    i += 1

#2
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#3
i = 1
while i < 10:
    print(f"{i} * {i} = {i * i}")
    i += 1

#4
i = 1
print("even numbers:", end=' ')
while i < 20:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1

#5
i = 0
count = 0
txt = "cucumber"

while i < len(txt):
    if txt[i] == "c":
        count += 1
    i += 1

print(count)