myfile = open("./resources/day1Resource.txt")
theKey = myfile.read()

def duplicateTracker(numberString):
    total = 0
    for i, n in enumerate(numberString):
        if n == numberString[(i+1)%len(numberString)]:
            total = total + int(n)
    return total


print(duplicateTracker(theKey))