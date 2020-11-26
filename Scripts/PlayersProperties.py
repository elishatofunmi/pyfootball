# General player properties
class defaultProperties:
    def __init__(self):
        self.positionx = 0
        self.positiony = 0
        self.listX = []
        self.listY = []

        return

    def setCoordinates(self, x, y):
        self.positionx = x
        self.positiony = y
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return

    def getCoordinates(self):
        return self.positionx, self.positiony

    def update(self, count):
        self.positionx = self.listX[count]
        self.positiony = self.listY[count]
        return

    def GetlastLocation(self):

        return self.positionx, self.positiony
