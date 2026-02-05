#1
nums = [1, 2, 3, 4, 5, 6, 7]
odd = list(filter(lambda x : x % 2 != 0, nums))
print(odd)

#2
strings = ['asdf', '1234', 'tyu87', '6390']
numbers = list(filter(lambda x : x.isdigit(), strings))
print(numbers)

#2
strings = ['Hello', 'hello', 'HELLO', 'HI']
upper = list(filter(lambda x : x.isupper(), strings))
print(upper)

#3
words = ['cat', 'apple', 'dog', 'table', 'weather']
long_words = list(filter(lambda x : len(x) > 4, words))
print(long_words)

#5
nums = [1, -3, 5, -8, 9, -3]
positive = list(filter(lambda x : x > 0, nums))
print(positive)