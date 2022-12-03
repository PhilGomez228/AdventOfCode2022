from string import ascii_lowercase, ascii_uppercase
with open("Day3/Day3Inputs.txt") as f:
    inputs = [line.strip() for line in f.readlines()]
count = 1
itemValues = {}
for i in ascii_lowercase:
    itemValues[i] = count
    count += 1
for i in ascii_uppercase:
    itemValues[i] = count
    count += 1
#Part 1
commonItemsValues = []
for i in inputs:
    firstHalf = slice(0, len(i)//2)
    secondHalf = slice(len(i)//2, len(i))
    common = ''.join(set(i[firstHalf]).intersection(i[secondHalf]))
    commonItemsValues.append(itemValues[common])
print(sum(commonItemsValues))

#Part 2
i = 0
badgeValues = []
while i < len(inputs):
    common = ''.join(set(inputs[i]).intersection(inputs[i+1]).intersection(inputs[i+2]))
    badgeValues.append(itemValues[common])
    i += 3
print(sum(badgeValues))