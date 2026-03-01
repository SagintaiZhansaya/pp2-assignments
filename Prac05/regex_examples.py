#1 findall
import re

txt = "Jkdho5603_i"
x = re.findall(r"\d", txt)

print(x)

#2 search
import re

txt = "hello 1!"
x = re.search(r"\w", txt)

print(x)

#3 split
import re

txt = "The rain in Spain"
x = re.split(r"\s", txt)
print(x)

#4 sub
import re

txt = "The rain in Spain"
x = re.sub(r"[^The]", "10", txt)

print(x)