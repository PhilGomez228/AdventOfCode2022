import re
import copy
with open("Day5/Day5Inputs.txt", 'r') as f:
    stacks, commands = f.read().strip("\n").split("\n\n")
stacks = [list(''.join(x).strip()) for x in list(zip(*stacks.split("\n")[:-1]))[1::4]]
commands = re.findall(r"(?P<crates>\d+)......(?P<fromStack>\d)....(?P<toStack>\d)", commands)

#Part 1
for i in range(0,len(stacks)):
    stacks[i].reverse()
part2Stacks = copy.deepcopy(stacks)
for i in commands:
    for j in range(0, int(i[0])):
        stacks[int(i[2]) - 1].append(stacks[int(i[1]) - 1][-1])
        stacks[int(i[1]) - 1].pop()
topStack = []
for i in stacks:
    topStack.append(i[-1])
print(topStack)

#Part 2

for i in commands:
    part2Stacks[int(i[2]) - 1] += part2Stacks[int(i[1]) - 1][-int(i[0]):]
    del part2Stacks[int(i[1]) - 1][-int(i[0]):]
part2TopStack = []
for i in part2Stacks:
    part2TopStack.append(i[-1])
print(part2TopStack)