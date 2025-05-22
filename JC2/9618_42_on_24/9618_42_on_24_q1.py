# 1a) i.
class EventItem :
    def __init__(self, EventName, Type, Difficulty) :
        self.__EventName = EventName # OF TYPE STRING
        self.__Type = Type # OF TYPE STRING
        self.__Difficulty = Difficulty # OF TYPE INTEGER

# ii.
    def GetName(self):
        return self.__EventName

    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__Type
    
# b) i.
Group = [None for _ in range(5)] #array of EventItem, 5 spaces

# ii.
Group[0] = EventItem("Bridge", "jump", 3) 
Group[1] = EventItem("Water wade", "swim", 4) 
Group[2] = EventItem("100 mile run", "run", 5) 
Group[3] = EventItem("Gridlock", "drive", 2) 
Group[4] = EventItem("Wall on wall", "jump", 4) 

# c)
class Character :
    def __init__(self, pCharacterName, pJump, pSwim, pRun, pDrive):
        self.__CharacterName = pCharacterName # STRING
        self.__Jump = pJump # INTEGER
        self.__Swim = pSwim # INTEGER
        self.__Run = pRun # INTEGER
        self.__Drive = pDrive # INTEGER

    def GetName(self):
        return self.__CharacterName # STRING
    
# d)
    def CalculateScore(self, eventType, eventDifficulty):
        charLevel = 0
        chance = 0
        if eventType == "jump" :
            charLevel = self.__Jump
        elif eventType == "swim" :
            charLevel = self.__Swim
        elif eventType == "run" :
            charLevel = self.__Run
        else :
            charLevel = self.__Drive

        if charLevel >= eventDifficulty :
            chance = 100
        elif (eventDifficulty-charLevel == 1) :
            chance = 80
        elif (eventDifficulty-charLevel == 2) :
            chance = 60
        elif (eventDifficulty-charLevel == 3) :
            chance = 40
        else:
            chance = 20
            
        return chance
    
# e) i.
Character1 = Character("Tarz", 5, 3, 5, 1)
Character2 = Character("Geni", 2, 2, 3, 4)
    
# ii.
point1 = 0
point2 = 0
for i in range(5):
    event = Group[i].GetEventType()
    difficulty = Group[i].GetDifficulty()
    chance1 = Character1.CalculateScore(event, difficulty)
    chance2 = Character2.CalculateScore(event, difficulty)

    if chance1 == chance2 :
        print("event is a draw")
    elif chance1 > chance2 :
        point1 += 1
        print(Character1.GetName(), "has won the", Group[i].GetName(), "event")
    else:
        point2 += 1
        print(Character2.GetName(),"has won the", Group[i].GetName(), "event")

if point1 > point2 :
    print(Character1.GetName(),"has won the most points")
elif point2 > point1 :
    print(Character2.GetName(), "has won the most points")
else :
    print("it is a draw")

# iii. screenshot