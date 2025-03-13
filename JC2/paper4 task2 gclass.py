player = [None for i in range(10)]
scores = [None for i in range(10)]

filename = "HighScore.txt"

def ReadHighScores(file):
    playerIndex = 0
    scoreIndex = 0
    file = open(file, 'r')
    for i in range(20):
        line = file.readline()
        if i % 2 != 0 :
            player[playerIndex] = line.strip()
            playerIndex = playerIndex + 1
        else:
            scores[scoreIndex] = line.strip()
            scoreIndex = scoreIndex + 1

def OutputHighScores():
    for i in range(3):
        print(player[i], scores[i])
    
ReadHighScores(filename)     
print(player)
print(scores)

name = input("enter new player name: ")
score = int(input("enter new player's score: "))