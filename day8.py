class Register:
    name = ""
    value = 0
    held = [0]

    def __init__(self, x):
        self.name = x


    def __lt__(self, other):
        return self.value > other.value


    def inc(self, x):
        self.value += x
        self.held.append(self.value)


    def dec(self, x):
        self.value -= x
        self.held.append(self.value)


instructions = open("./resources/day8Resource").read().split("\n")
registry = []
reglist = []
numbers = []

# This for loop check all unique registry names in the instruction list
for i in instructions:
    if i.split()[0] not in reglist:
        reglist.append(i.split()[0])
        registry.append(Register(i.split()[0]))
    if i.split()[4] not in reglist:
        reglist.append(i.split()[4])
        registry.append(Register(i.split()[4]))
registry.sort()

def incDec(process, x):
    if process[1] == "inc":
        x.inc(int(process[2]))
    else:
        x.dec(int(process[2]))


def instruct(process, x, y):
    if (process[5] == "==") & (int(process[6]) == int(y.value)):
        incDec(process, x)
    if (process[5] == "!=") & (int(process[6]) != int(y.value)):
        incDec(process, x)
    if (process[5] == ">") & (y.value > int(process[6])):
        incDec(process, x)
    if (process[5] == "<") & (y.value < int(process[6])):
        incDec(process, x)
    if (process[5] == ">=") & (y.value >= int(process[6])):
        incDec(process, x)
    if (process[5] == "<=") & (y.value <= int(process[6])):
        incDec(process, x)


# This for loop pulls both the registry to process, and the registry to reference
for i in instructions:
    p = i.split();
    for r in registry:
        if p[0] == r.name:
            for r2 in registry:
                if p[4] == r2.name:
                    instruct(p, r, r2)

# This for loop gathers all held values of each registry
for n in registry:
    for i in n.held:
        numbers.append(i)

registry.sort()
print("Maximum after processing:", registry[0].value)
print("Maximum memory held:", max(numbers))

