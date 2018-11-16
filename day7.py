data = open("./resources/day7Resource").read()

formatted = data.split("\n")
shrinked = []
topLevel = []
programs = []
names = []
bottom = ""
for i in formatted:
    x = i.split(" -> ")
    programs.append(x[0])
    if len(x) == 2:
        shrinked.append(x)
for i in shrinked:
    name = i[0].split()
    names.append(name[0])
    top = i[1].split(", ")
    for v in top:
        topLevel.append(v)
for i in names:
    if i not in topLevel:
        bottom = i
print(bottom) #part 1



# class Program:
#     name = ""
#     weight = 0
#     holding = []
#
#     def __init__(self, program):
#         s = program.split(" -> ")
#         for i in enumerate(s):
#             if i[0] == 0:
#                 nw = i[1].split()
#                 self.name = nw[0]
#                 self.weight = int(nw[1].replace("(", "").replace(")", ""))
#             if i[0] == 1:
#                 holding = i[1].split(", ")
#                 self.holding = holding
#
#
#     def hasStack(self):
#         if len(self.holding) > 0:
#             return True
#
#
#     def viewContents(self):
#         print(self.name, self.weight, self.holding)
#
#
# pgrams = []
# for i in formatted:
    #p = Program(i)
    #pgrams.append(p)


#for i in pgrams:
    #tw = 0
    #if i.hasStack():
     #   for z in