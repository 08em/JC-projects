# use ctrl + to enlarge the screen when screenshotting and then use windows snipping tool to crop
# 2
# a)
class Picture:
    def __init__(self, Description, Width, Height, FrameColour) :
        self.__Description = Description # of type string
        self.__Width = Width # of type integer
        self.__Height = Height # of type integer
        self.__FrameColour = FrameColour # of type string

# b)
    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height
    
    def GetWidth(self):
        return self.__Width
    
    def GetColour(self):
        return self.__FrameColour

# c)
    def SetDescription(self, newDesc):
        self.__Description = newDesc

# d) 
pictureArr = [Picture("", 0,0) for i in range(100)]

# e)

def ReadData(file):
    try:
        file = open("Pictures.txt", 'r')
        for num in range(100):
                line1 = file.readline().strip()
                line2 = file.readline().strip()
                line3 = file.readline().strip()
                line4 = file.readline().strip()
                pictureArr[num] = Picture(line1, line2, line3, line4)
        
    
    except FileNotFoundError:
        print("file cannot be found")
