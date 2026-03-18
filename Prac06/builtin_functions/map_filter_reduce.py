#1
nums = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, nums))
print(square)

#2
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

#3
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(result)

#4
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)