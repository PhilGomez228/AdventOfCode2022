import re
with open("Day7/Day7Inputs.txt", 'r') as f:
    inputs = [line.strip() for line in f.readlines()]

def addDirectoryFileSize(currentPath, directoriesList, directoryFileSize):
    for i in directoriesList[''.join(currentPath)]:
        if 'dir' in i:
            currentPath.append('/'+i[4:])
            addDirectoryFileSize(currentPath, directoriesList, directoryFileSize)
            directoryFileSize[''.join(currentPath[:-1])] += directoryFileSize[''.join(currentPath)]
            currentPath.pop()

fileSize = 0
directories = {}
directoryFileSize = {}
currentDir = '/'
currentPath = ['/']
files = []
smallDirectories = []
for i in inputs:
    if i == inputs[-1]:
        files.append(i)
        directories[''.join(currentPath)] = files[0:]
        fileSize += int(re.match(r"\d+", i).group())
        directoryFileSize[''.join(currentPath)] = fileSize 
    if "$ cd" in i:
        directories[''.join(currentPath)] = files[0:]
        directoryFileSize[''.join(currentPath)] = fileSize
        files.clear()
        if "$ cd .." == i:
            currentPath.pop()
            files = directories[''.join(currentPath)][0:]
            fileSize = directoryFileSize[''.join(currentPath)]
            continue
        currentDir = i[5:]
        if currentPath[-1] != currentDir or currentPath[0] != currentDir:
            currentPath.append('/' + currentDir)
        fileSize = 0
    if i == "$ ls":
        continue
    if "$" not in i:
        files.append(i)
        if i[:3] != 'dir':
            fileSize += int(re.match(r"\d+", i).group())

addDirectoryFileSize(list('/'), directories, directoryFileSize)

#Part 1
for i in directoryFileSize.values():
    if i <= 100000:
        smallDirectories.append(i)
print(sum(smallDirectories))

#Part 2
emptySpace = 70000000 - directoryFileSize['/']
spaceNeeded = 30000000 - emptySpace
qualifyingDirectries = []
for i in directoryFileSize.values():
    if i > spaceNeeded:
        qualifyingDirectries.append(i)
print(min(qualifyingDirectries))