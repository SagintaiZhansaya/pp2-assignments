import shutil
import os

shutil.copy("nums.txt", "nums_copy.txt")

with open("nums_copy.txt") as f:
    print(f.read())

if os.path.exists("nums_copy.txt"):
    os.remove("nums_copy.txt")
    print("succesfully deleted")
else:
    print("The file does not exist")