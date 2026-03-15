with open("nums.txt", "a") as f:
    f.write("\nseven eight nine")
    f.write("\nten eleven twelve")

with open("nums.txt") as f:
    print(f.read())