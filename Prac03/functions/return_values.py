#1
def multiplication(x, y):
    return x * y

result = multiplication(8, 9)
print(result)

#2
def is_even(x):
    if x % 2 == 0:
        return "is even"
    else:
        return "is not even"

num1 = is_even(6)
num2 = is_even(3)

print(6, num1)
print(3, num2)

#3
def check(logged_in):
    if logged_in:
        return "successfully logged in"
    else:
        return "error"

logged_in = True
is_ckecked = check(logged_in)
print(is_ckecked)

#4
def float_to_int(x):
    return int(x)

num = float_to_int(9.8)
print(num)

#5
def one_string(a, b):
    return a + b 

string = one_string("sweat", 'heart')
print(string)