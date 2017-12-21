resource = open("./resources/day2Resource").read()

# Part 1
total = 0
for row in resource.split("\n"):
    thisRow = list(map(int, row.split()))
    total = total + (max(thisRow) - min(thisRow))
print(total)

# Part 2
total2 = 0
for row in resource.split("\n"):
    thisRow = list(map(int, row.split()))
    for pos1 in range(0, len(thisRow)):
        for pos2 in range(0, len(thisRow)):
            if (thisRow[pos1] != thisRow[pos2]) & (thisRow[pos1] % thisRow[pos2] == 0):
                total2 = total2 + int(thisRow[pos1] / thisRow[pos2])
print(total2)
