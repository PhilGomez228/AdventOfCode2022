with open("Day4/Day4Inputs.txt", 'r') as f:
    inputs = [line.strip().split(',') for line in f.readlines()]

count = 0
part2Count = 0
for i in inputs:
    pairs = []
    pairSections = []
    for j in i:
        
        x,y = j.split('-')
        x = int(x)
        y = int(y)
        pairs.append([x,y])
        pairSections.append(list(range(x,y+1)))
#Part 1
    if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1] or pairs[1][0] <= pairs[0][0] and pairs[1][1] >= pairs[0][1]:
        count += 1


#Part 2
    if any(x in pairSections[1] for x in pairSections[0]) or any(x in pairSections[0] for x in pairSections[1]):
        part2Count += 1

print(count)
print(part2Count)