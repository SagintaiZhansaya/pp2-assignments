#1
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x : x * 2, numbers))
print(doubled)

#2
names = ['Jhon', 'Bell', 'Alex']
greeting = list(map(lambda x : 'Hello, ' + x, names))
print(greeting)

#3
nums = [1, 2, 3, 4, 5]
power = list(map(lambda x : x * x, nums))
print(power)

#4
nums = [2, 4, 6, 8, 10]
division = list(map(lambda x : x // 2, nums))
print(division)

#5
nums = [10, 13, 17, 82, 94]
remainder = list(map(lambda x : x % 6, nums))
print(remainder)