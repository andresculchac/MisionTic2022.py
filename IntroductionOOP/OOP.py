class Square:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def calculateArea(self): #what is this self 
        area = self.width * self.height
        return area


figure = Square(10, 12)
print(figure.calculateArea())

