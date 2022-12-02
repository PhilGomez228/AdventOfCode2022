with open("Day1/Day1Inputs.txt") as f:
    inputs = [line.strip() for line in f.read().split("\n")]

calorieCount = []
countPerElf = 0

for i in inputs:
    if i == inputs[-1]:
        calorieCount.append(countPerElf + int(i))
    elif i == "":
        calorieCount.append(countPerElf)
        countPerElf = 0
        
    else:
        countPerElf += int(i)


#Part 1
print("The most calories one elf carries is:", max(calorieCount), " Which is held by Elf #", calorieCount.index(max(calorieCount)) + 1, "\n")

#Part 2
top3ElvesCount = []
for i in range(0,3):
    top3ElvesCount.append(max(calorieCount))
    calorieCount.remove(max(calorieCount))
print("The top 3 Elves hold", sum(top3ElvesCount), "calories.")