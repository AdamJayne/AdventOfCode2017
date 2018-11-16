data = open("./resources/day9Resource").read()
for i in enumerate(data):
    if i[1] == "{":
        print("HERE")
