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
pictureArr = [Picture("", 0,0, "") for i in range(100)]

# e)
pictureCount = 0

def ReadData():
    global pictureCount
    try:
        file = open("JC2/Pictures.txt", 'r')
        for num in range(25):
                line1 = file.readline().strip()
                line2 = file.readline().strip()
                line3 = file.readline().strip()
                line4 = file.readline().strip()
                pictureArr[num] = Picture(line1, line2, line3, line4)
                pictureCount = pictureCount + 1
        
    
    except FileNotFoundError:
        print("file cannot be found")

# f)

ReadData()

# g)

frameColour = input("enter frame colour: ").lower()
maxWidth = int(input("enter maximum picture width: "))
maxHeight = int(input("enter maximum picture height: "))

for i in range(len(pictureArr)):
    tempPicture = pictureArr[i]
    if tempPicture.GetColour() == frameColour :
        if int(tempPicture.GetWidth()) <= maxWidth and int(tempPicture.GetHeight()) <= maxHeight :
            print(tempPicture.GetDescription(), tempPicture.GetWidth(), tempPicture.GetHeight())


# 3a)

ArrayNode = [[-1, i+1, -1] for i in range(20)] # of type integer
ArrayNode[19][1] = -1
RootPointer = -1 # of type integer
FreeNode = 0 # of type integer

# b)

def AddNode(array):
    global RootPointer, FreeNode
    newItempointer = 0
    num = input("enter node to be added to the tree: ")''
    if FreeNode == -1 :
        print("tree is full")
    else: 
        newItemPointer = freePointer
        freePointer = array[newItemPointer][1]

        if rootPointer == -1:
            rootPointer = newItemPointer
            array[newItemPointer][1] = num
        else: 
            tempPointer = rootPointer
            if num > array[tempPointer][1] :
                while array[tempPointer][2] != -1:
                    tempPointer = array[tempPointer][2]
                if num > array[tempPointer][1] :
                    array[tempPointer][2] = newItemPointer
                else: 
                    array[tempPointer][0] = newItemPointer

            else: 
                while array[tempPointer][0] != -1:
                    tempPointer = array[tempPointer][0] 
                array[tempPointer][0] = newItemPointer
                if num > array[tempPointer][1] :
                    array[tempPointer][2] = newItemPointer
                else: 
                    array[tempPointer][0] = newItemPointer

            array[newItemPointer][1] = num

        

    


