with open("Day6/Day6Inputs.txt",'r') as f:
    inputs = f.read().strip()
#Part 1 change all values for 14 to 4
    
#Part 2 showing
for i in range(0,len(inputs)):
    if len(set(inputs[i:i+14])) == 14:
        print(i+14)
        break