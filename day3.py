resource = int(open('./resources/day3Resource').read())

# Part 1

n = int(resource)

i = 1
while i*i < n:
    i += 2
pivots = [i*i - k*(i-1) for k in range(5)]
for p in pivots:
    dist = abs(p - n)
    if dist <= (i-1)//2:
        print(i-1-dist)
        break

# Part 2
# This was found on Reddit, I couldn't do it

values = [(0, 0, 1)]

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

level = 1
x, y = 0, 0

terminate = False

while not terminate:

    for direction in range(4):

        if terminate:
            break

        dirX, dirY = directions[direction]

        if direction == 0:
            moveN = level - 2
        elif direction in [1, 2]:
            moveN = level - 1
        else:
             moveN = level

        for _ in range(moveN):

            x += dirX
            y += dirY

            new = sum([k[2] for k in values if abs(x-k[0]) <= 1 and abs(y-k[1]) <= 1])
            values.append((x, y, new))

            if new >= n:
                print(new)

                terminate = True
                break

    level += 2