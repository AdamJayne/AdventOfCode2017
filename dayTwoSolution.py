twoFile = open("./resources/day2Resource")
resource = twoFile.read()

# Part 1
total = 0
for row in resource.split("\n"):
    thisRow = list(map(int, row.split()))
    total = total + (max(thisRow) - min(thisRow))
print(total)

# Part 2
