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
        return

    def getCoordinates(self):
        return self.positionx, self.positiony


# Ball property
class ball(defaultProperties):
    def __init__(self):
        super().__init__()
        self.x1bound = 0
        self.x2bound = 1200
        self.y1bound = 0
        self.y2bound = 700
        self.positionx = 600
        self.positiony = 350
        self.listX = [self.positionx]
        self.listY = [self.positiony]

        return

    def update(self, count):
        self.positionx = self.listX[count]
        self.positiony = self.listY[count]
        return

    def GetlastLocation(self):

        return self.positionx, self.positiony


# defenders properties
class defenders(defaultProperties):
    def __init__(self):
        super().__init__()
        # setting bounds for defenders
        self.x1bound = 0
        self.x2bound = 400
        self.y1bound = 0
        self.y2bound = 700
        return

# mid-fielders properties


class midfielders(defaultProperties):
    def __init__(self):
        super().__init__()
        # setting bounds for mid-fielders
        self.x1bound = 400
        self.x2bound = 800
        self.y1bound = 0
        self.y2bound = 700

        return


# Strikers properties
class stricker(defaultProperties):
    def __init__(self):
        super().__init__()
        # setting bounds for strikers
        self.x1bound = 800
        self.x2bound = 1200
        self.y1bound = 0
        self.y2bound = 700
        return


# Class players A
class playerAKeeper(defaultProperties):
    def __init__(self):
        super().__init__()
        self.positionx = 40
        self.positiony = 330
        self.listX = [self.positionx]
        self.listY = [self.positiony]

        return


class playerA1(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 140
        self.positiony = 100
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA2(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 140
        self.positiony = 250
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA3(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 140
        self.positiony = 400
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA4(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 140
        self.positiony = 550
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA5(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 340
        self.positiony = 150
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA6(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 340
        self.positiony = 300
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA7(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 340
        self.positiony = 450
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA8(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 500
        self.positiony = 350
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA9(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 550
        self.positiony = 300
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerA10(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 550
        self.positiony = 400
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


# Class players B
class playerBKeeper(defaultProperties):
    def __init__(self):
        super().__init__()
        self.positionx = 1130
        self.positiony = 330
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB1(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 1030
        self.positiony = 100
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB2(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 1030
        self.positiony = 250
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB3(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 1030
        self.positiony = 400
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB4(defenders):
    """
    defenders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 1030
        self.positiony = 550
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB5(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 830
        self.positiony = 150
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB6(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 830
        self.positiony = 300
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB7(midfielders):
    """
    midfielders
    """

    def __init__(self):
        super().__init__()
        self.positionx = 830
        self.positiony = 450
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB8(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 750
        self.positiony = 350
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB9(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 650
        self.positiony = 300
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return


class playerB10(stricker):
    """
    stricker
    """

    def __init__(self):
        super().__init__()
        self.positionx = 650
        self.positiony = 400
        self.listX = [self.positionx]
        self.listY = [self.positiony]
        return
