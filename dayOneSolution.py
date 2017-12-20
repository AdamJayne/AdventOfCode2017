myFile = open("./resources/day1Resource")
theKey = myFile.read()

# Part 1


def duplicate(numbers):
    total = 0
    for i, n in enumerate(numbers):
        if n == numbers[(i + 1) % len(numbers)]:
            total = total + int(n)
    return total


print(duplicate(theKey))


# Part 2


def mirrored(numbers):
    total = 0
    for i, n in enumerate(numbers):
        if n == numbers[(i + int(len(numbers)/2)) % int(len(numbers))]:
            total = total + int(n)
    return total


print(mirrored(theKey))