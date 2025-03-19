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
def ChooseCard():
    cardNum = int(input("enter value: "))
    if cardNum < 1 or cardNum > 30 :
          print("number must be between 1 and 30")
          cardNum = int(input("enter value: "))
    else: 

