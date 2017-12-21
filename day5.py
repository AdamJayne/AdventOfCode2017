resource = open('./resources/day5Resource').read()

# Part 1

m = list(map(int, resource.split('\n')))


def execute(x):
    pos = 0
    instructions = 0
    while pos < len(x):
        move = x[pos]
        x[pos] += 1
        pos += move
        instructions += 1
    return instructions


print(execute(m))

# Part 2

z = list(map(int, resource.split('\n')))


def execute2(x):
    pos = 0
    instructions = 0
    while pos < len(x):
        move = x[pos]
        if move >= 3:
            x[pos] -= 1
        else:
            x[pos] += 1
        pos += move
        instructions += 1
    return instructions


print(execute2(z))
