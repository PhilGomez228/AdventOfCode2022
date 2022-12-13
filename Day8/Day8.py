import numpy as np
with open("Day8/Day8Inputs.txt",'r') as f:
    trees = [line.strip() for line in f.readlines()]
visibleTrees = len(trees) * 2 + len(trees[0]) * 2 - 4
newTrees = np.zeros((len(trees),len(trees[0])), dtype=int)
for i in range(0,len(trees)):
    newTrees[i] = [int(tree) for tree in trees[i]]
treesFromHouse = []
for i in range(1,len(trees) - 1):
    for j in range(1,len(trees[0]) - 1):
        visibleFromLeft = True
        visibleFromRight = True
        visibleFromBottom = True
        visibleFromTop = True
        leftTrees = [int(tree) for tree in newTrees[i, :j]]
        leftTrees.reverse()
        upTrees = [int(tree) for tree in newTrees[:i, j]]
        upTrees.reverse()
        rightTrees = [int(tree) for tree in newTrees[i, j+1:]]
        downTrees = [int(tree) for tree in newTrees[i+1:,j]]
        #Part1
        if newTrees[i,j] <= max(leftTrees):
            visibleFromLeft = False
        if newTrees[i,j] <= max(rightTrees):
            visibleFromRight = False
        if newTrees[i,j] <= max(upTrees):
            visibleFromTop = False
        if newTrees[i,j] <= max(downTrees):
            visibleFromBottom = False
        if visibleFromBottom or visibleFromLeft or visibleFromRight or visibleFromTop:
            visibleTrees+=1

        #Part 2            
        leftTreeVisible = 1
        rightTreeVisible = 1
        upTreeVisible = 1
        downTreeVisible = 1
        for x in range(0,len(leftTrees)):
            if leftTrees[x] < newTrees[i,j]:
                if x == 0:
                    continue
                leftTreeVisible+=1
            elif leftTrees[x] >= newTrees[i,j]:
                if x == 0:
                    break
                leftTreeVisible+=1
                break
            else:
                 break
        for x in range(0,len(rightTrees)):
            if rightTrees[x] < newTrees[i,j]:
                if x == 0:
                    continue
                rightTreeVisible+=1
            elif rightTrees[x] >= newTrees[i,j]:
                if x == 0:
                    break
                rightTreeVisible+=1
                break
            else:
                break
        for x in range(0,len(upTrees)):
            if upTrees[x] < newTrees[i,j]:
                if  x == 0:
                    continue
                upTreeVisible+=1
            elif upTrees[x] >= newTrees[i,j]:
                if x == 0:
                    break
                upTreeVisible+=1
                break
            else:
                 break
        for x in range(0,len(downTrees)):
            if downTrees[x] <  newTrees[i,j]:
                if x == 0: 
                    continue
                downTreeVisible+=1
            elif downTrees[x] >= newTrees[i,j]:
                if x == 0:
                    break
                downTreeVisible+=1
                break
            else:
                 break
        treesFromHouse.append(leftTreeVisible*rightTreeVisible*upTreeVisible*downTreeVisible)
print("Part 1:",visibleTrees)
print("Part 2:",max(treesFromHouse))