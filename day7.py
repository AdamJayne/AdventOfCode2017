data = open("./resources/day7Resource").read()

formatted = data.split("\n")
shrinked = []
topLevel = []
names = []
bottom = ""
for i in formatted:
    x = i.split(" -> ")
    if len(x) == 2:
        shrinked.append(x)
for i in shrinked:
    name = i[0].split()
    names.append(name[0])
    top = i[1].split(", ")
    for v in top:
        topLevel.append(v)
for i in names:
    if i in topLevel:
        pass
    else:
        bottom = i
print(bottom)

