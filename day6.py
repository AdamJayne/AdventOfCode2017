resource = open('./resources/day6Resource').read()

# Part 1

memory1 = list(map(int, resource.split()))
workingMemory = list(map(int, resource.split()))
history = []
history.append(memory1[:])
actions = 1


def mancala(m):
    global actions
    start = m.index(max(m))
    account = m[start]
    m[start] = 0
    increment = 1
    while account > 0:
        if (start + increment) > (len(m) - 1):
            start = -1
        start += increment
        m[start] += 1
        account -= 1
    while m != memory1:
        pos = m.index(max(m))
        count = m[pos]
        m[pos] = 0
        while count > 0:
            if (pos + increment) > (len(m) - 1):
                pos = -1
            pos += increment
            m[pos] += 1
            count -= 1
        actions += 1
        for i in history:
            if i == m:
                print(actions)
                history.append(m[:])
                return actions
        history.append(m[:])


duplicate = history[mancala(workingMemory)-1]
# Part 2


def mancala2(m):
    global actions
    start = m.index(max(m))
    account = m[start]
    m[start] = 0
    increment = 1
    while account > 0:
        if (start + increment) > (len(m) - 1):
            start = -1
        start += increment
        m[start] += 1
        account -= 1
    history.append(m[:])
    actions += 1
    while m != duplicate:
        pos = m.index(max(m))
        count = m[pos]
        m[pos] = 0
        while count > 0:
            if (pos + increment) > (len(m) - 1):
                pos = -1
            pos += increment
            m[pos] += 1
            count -= 1
        actions += 1
        history.append(m[:])
    print(actions)
    return actions


end = mancala2(duplicate[:])
print(6128 - 5042)
