marks =[[1 for i in range(5)], 
        [2 for i in range(5)],
        [3 for i in range(5)],
        [4 for i in range(5)],
        [5 for i in range(5)]]

for row in range(5):
    for col in range(5):
        print(marks[row][col], end = " ")
    print()

testScores = [[67, 78],
              [88, 79],
              [94, 55],
              [99, 82],
              [74, 62]]

studentNames = ["Alex", "John", "Ian", "Irin", "Aileen"]

print(studentNames[0], testScores[0][0], testScores[0][1])
print(studentNames[1], testScores[1][0], testScores[1][1])
print(studentNames[2], testScores[2][0], testScores[2][1])
print(studentNames[3], testScores[3][0], testScores[3][1]) 
print(studentNames[4], testScores[4][0], testScores[4][1])

for row in range(len(studentNames)):
    print(studentNames[row], testScores[row][0], testScores[row][1])

