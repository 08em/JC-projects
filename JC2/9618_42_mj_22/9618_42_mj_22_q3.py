# 3a) 
class Card :
    def __init__(self, PNumber, PColour):
        self.__Number = PNumber # of type integer
        self.__Colour = PColour # of type string

# b)
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

# c)

CardArray = [Card(0, "") for i in range(30)]
file = open("JC2/CardValues.txt", 'r')
for i in range(30):
        num = file.readline().strip()
        colour = file.readline().strip()
        CardArray[i] = Card(num, colour)

# d)
chosenCards = [0 for _ in range(30)]

chosenCards = [0 for _ in range(30)]

def ChooseCard():
    selected = False
    while selected == False:
        cardNum = int(input("enter card number between 1 and 30 inclusive: "))
        if cardNum < 1 or cardNum > 30 :
            print("number must be between 1 and 30")
            cardNum = int(input("enter card number between 1 and 30 inclusive: "))
        elif chosenCards[cardNum-1] == 1:
            print("card already chosen, please choose another card")
        else:
            print(f"card {cardNum} is available")
            chosenCards[cardNum-1] = 1
            selected = True

    return cardNum-1 #returns INDEX of the card if available

print(chosenCards)

# e) i.

player1 = [Card(0, "") for i in range(4)]  # of Card

for i in range(4):
    num = ChooseCard()
    player1[i] = CardArray[num]

for i in range(4):
    print(player1[i].GetNumber())
    print(player1[i].GetColour())

# ii. screenshot
# test 1 : 1, 5, 9, 10
# test 2 : 2, 2, 3, 4, 4, 5