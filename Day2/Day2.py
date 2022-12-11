with open("Day2/Day2Inputs.txt", 'r') as f:
    inputs = [lines.strip() for lines in f.readlines()]
    inputs = [line.split() for line in inputs]
RPSDictionary = {'A' : "rock", 'B' : "paper", 'C' : "scissors", 'X' : "rock", 'Y' : "paper", 'Z' : "scissors", "rock" : 1, "paper" : 2, "scissors" : 3}
score = 0

#Part 1
for i in range(0, len(inputs)):
    score += RPSDictionary[RPSDictionary[inputs[i][1]]]
    if RPSDictionary[inputs[i][0]] == RPSDictionary[inputs[i][1]]:
        score += 3
    elif inputs == ["A","Y"] or inputs == ["B","Z"] or inputs == ["C", "X"]:
        score += 6

print("Answer for part 1 is", score)

#Part 2
part2Score = 0
for i in range(0, len(inputs)):
    if inputs[i][1] == 'X':
        if inputs[i][0] == 'A':
            part2Score += RPSDictionary["scissors"]
        elif inputs[i][0] == 'B':
            part2Score += RPSDictionary["rock"]
        else:
            part2Score += RPSDictionary["paper"]
    elif inputs[i][1] == "Y":
        part2Score += RPSDictionary[RPSDictionary[inputs[i][0]]] + 3
    else:
        part2Score += 6
        if inputs[i][0] == 'A':
            part2Score += RPSDictionary["paper"]
        elif inputs[i][0] == 'B':
            part2Score += RPSDictionary["scissors"]
        else:
            part2Score += RPSDictionary["rock"]

print("The answer for Part 2 is", part2Score)