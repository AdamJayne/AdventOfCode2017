myFile = open("./resources/day1Resource")
theKey = myFile.read()

# Part1


def duplicate(numbers):
    total = 0
    for i, n in enumerate(numbers):
        if n == numbers[(i + 1) % len(numbers)]:
            total = total + int(n)
    return total


print(duplicate(theKey))

