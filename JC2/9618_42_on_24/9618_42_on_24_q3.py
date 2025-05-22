# 3a)
HighScores = [["" for _ in range(3)] for i in range(7)]

# b)
def ReadData():
    try :
        file = open("JC2/HighScoreTable.txt", 'r')
        for r in range(7):
            for c in range(3) :
                HighScores[r][c] = file.readline().strip()

        return HighScores
    
    except FileNotFoundError :
        print("file not found")

# c)
def OutputHighScores(array):
    for r in range(7):
        print(array[r][0], "reached level", array[r][1], "with a score of", array[r][2])

# d)
def SortScores():
    arrLength = len(HighScores)
    for j in range(arrLength-1):
        for i in range(0, arrLength-j-1):
            if int(HighScores[i][1]) < int(HighScores[i+1][1]) : #descending order
                temp = HighScores[i][1]
                HighScores[i][1] = HighScores[i+1][1]
                HighScores[i+1][1] = temp
            elif int(HighScores[i][1]) == int(HighScores[i+1][1]) :
                if int(HighScores[i][2]) < int(HighScores[i+1][2]) :  
                    temp = HighScores[i][2]
                    HighScores[i][2] = HighScores[i+1][2]
                    HighScores[i+1][2] = temp

    return HighScores

#e) i.
HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores()
print("After")
OutputHighScores(HighScores)

# ii. ss