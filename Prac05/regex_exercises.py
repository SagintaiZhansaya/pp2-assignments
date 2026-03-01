#1
import re

text = "abbb a ab aaaa"
pattern = "ab*"

m = re.search(pattern, text)
print(m.group())

#2
import re

text = "abbb abb a ab"
pattern = "ab{2,3}"

m = re.search(pattern, text)
print(m.group())

#3
import re

text = "hello_world Hello_WORLD"
pattern = "[a-z]+_[a-z]+"

m = re.findall(pattern, text)
print(m)

#4
import re

text = "Hello world Anna john"
pattern = "[A-Z][a-z]+"

m = re.findall(pattern, text)
print(m)

#5
import re 

text = "ahfkb ab ajjjb aabb"
pattern = "a.*b"

m = re.search(pattern, text)
print(m.group())

#6
import re

text = "Hello, world. Python is fun"
print(re.sub(r"[ ,\.]", ":", text))

#7
import re

def snake_to_camel(text):
    x = re.split("_", text)
    return x[0] + "".join(word.capitalize() for word in x[1:])

text = "apple_banana_mango"
print(snake_to_camel(text))

#8
import re

text = "AppleBananaMango"
print(re.findall("[A-Z][a-z]*", text))

#9
import re

text = "HelloWorldPython"
print(re.sub("([A-Z])", r" \1", text).strip())

#10
import re

def camel_to_snake(text):
    return re.sub("([A-Z])", r"_\1", text).lower()

text = "helloWorldBye"
print(camel_to_snake(text))