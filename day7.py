data = open("./resources/day7Test").read()

data1 = [
    "tknk (41) -> ugml, padx, fwft",
    "padx (45) -> pbga, havc, qoyq"
]

for i in data1:
    name, weight, carried = ""
    splitted = i.split(" -> ")
    for (dx, x) in enumerate(splitted):
        if dx == 0:
            res = x.split()
            name = res[0]
            weight = res[1]
        if dx == 1:
            carried = carried.split(", ")

