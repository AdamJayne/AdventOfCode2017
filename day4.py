resource = open("./resources/day4Resource").read()
jamesResource = open("./resources/day4Resource2").read()
# part 1

v1 = 0
for r in resource.split('\n'):
    c = 0
    e = list(map(str, r.split()))
    for i1 in range(0, len(e)):
        for i2 in range(0, len(e)):
            if (e[i1] == e[i2]) and (i1 != i2):
                c += 1
    if c == 0:
        v1 += 1
print(v1)

# part 2

def chkanagram(x, y):
    l1 = list(x)
    l2 = list(y)
    l1.sort()
    l2.sort()
    return l1 == l2


v2 = 0
for r in resource.split('\n'):
    c = 0
    e = list(map(str, r.split()))
    for i1 in range(0, len(e)):
        for i2 in range(0, len(e)):
            if (i1 != i2) and (e[i1] == e[i2]):
                c += 1
            elif (i1 != i2) and chkanagram(e[i1], e[i2]):
                c += 1
    if c == 0:
        v2 += 1
print(v2)
