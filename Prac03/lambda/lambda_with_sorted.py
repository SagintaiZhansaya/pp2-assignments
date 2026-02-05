#1
students = [('Bob', 21), ('Jeremy', 25), ('Anabell', 23)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#2
words = ['cat', 'apple', 'dog', 'table', 'weather']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#3
nums = [34, 12, 25, 47, 19]
result = sorted(nums, key=lambda x: x % 10)
print(result)

#4
nums = [1, 2, 3, 4, 5]
result = sorted(nums, key=lambda x: -x)
print(result)

#5
products = [('apple', 10), ('milk', 20), ('bread', 7)]
prices = sorted(products, key=lambda x: x[1])
print(prices)