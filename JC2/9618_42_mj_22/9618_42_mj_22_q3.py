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

# d) EDIT THIS CODE
chosenCards = []

def ChooseCard():
    cardNum = int(input("enter card number between 1 and 30: "))
    if cardNum < 1 or cardNum > 30 :
        print("number must be between 1 and 30")
        cardNum = int(input("enter value: "))
    else:
         chosenCards.append(cardNum)
         return cardNum - 1


# e) i.

player1 = [Card(0, "")]  # of Card

ChooseCard()
ChooseCard()
ChooseCard()
ChooseCard()

# ii. screenshot