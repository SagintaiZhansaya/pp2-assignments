#1
print(True)
print(type(True))

print(False)
print(type(False))

#2
print(bool("Hello"))
print(bool(15))

#3
print(bool("Jenny"))
print(bool(9087))
print(bool(["one", "two", "three"]))

#4
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#5
its_raining = True

if its_raining:
    print("take the umbrella")
else:
    print("have a good day")