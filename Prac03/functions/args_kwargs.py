#1
def my_func(*names):
    for name in names:
        print('Hello, ' + name)

my_func('Alex', 'Jhon', 'Sam')

#2
def total_sum(*numbers):
    total = 0
    for x in numbers:
        total += x
    print(total)

total_sum(1, 2, 3, 4, 5)

#3
def max_num(*numbers):
    mnum = numbers[0]
    for x in numbers:
        if x > mnum:
            mnum = x
    print(mnum)

max_num(4, 2, 6, 7, 8)

#4
def min_num(*numbers):
    mnum = numbers[0]
    for x in numbers:
        if x < mnum:
            mnum = x
    print(mnum)

min_num(4, 2, 6, 7, 8)

#5
def one_word(*words):
    one = ''
    for word in words:
        one += word
    print(one)

one_word('cat', 'dog', 'hamster')

