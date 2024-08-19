f = open("input.txt", "r")
i = f.readline()

floor = 0

for c in i:
    if c == '(':
        floor += 1

    else:
        floor -= 1

print(floor)
