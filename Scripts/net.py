import numpy as np
from Scripts.PlayersProperties import *
import os
import sys
import time


class Regression:
    def __init__(self):
        return

    def network(self, xsource, ysource, Xnew, Ynew, divisor=50):
        slope = 0
        intercept = 0

        #Slope and intercept
        while True:

            try:
                slope = (ysource - Ynew)/(xsource - Xnew)
                intercept = ysource - (slope*xsource)
            except ZeroDivisionError:
                slope = 0
                pass

            if (slope != np.inf) and (intercept != np.inf):
                break
            else:
                slope = 0
                break

        # randomly select 50 new values along the slope between xsource and xnew (monotonically decreasing/increasing)
        XNewList = [xsource]
        if slope != 0 and slope != np.nan and intercept != 0 and intercept != np.nan:
            if xsource < Xnew:
                differences = Xnew - xsource
                increment = differences / divisor
                newXval = xsource
                for i in range(divisor):

                    newXval += increment
                    XNewList.append(int(newXval))
            else:
                differences = xsource - Xnew
                decrement = differences / divisor
                newXval = xsource
                for i in range(divisor-1):

                    newXval -= decrement
                    XNewList.append(int(newXval))

            # determine the values of y, from the new values of x, using y= mx + c
            yNewList = []
            for i in XNewList:
                findy = (slope * i) + intercept  # y = mx + c
                yNewList.append(int(findy))

        else:
            XNewList = [xsource]*50
            yNewList = [ysource]*50
        return XNewList[:50], yNewList[:50]


class network:

    def __init__(self):
        self.count = 0
        self.updateScore = False
        self.TeamAScore = 0
        self.TeamBScore = 0
        self.game_status = ''

        self.playersListA = [
            # players A1 - A10
            'PlayerAKeeper',
            'PlayerA1',
            'PlayerA2',
            'PlayerA3',
            'PlayerA4',
            'PlayerA5',
            'PlayerA6',
            'PlayerA7',
            'PlayerA8',
            'PlayerA9',
            'PlayerA10']
        self.playersListB = [
            # players B1 - B10
            'PlayerBKeeper',
            'PlayerB1',
            'PlayerB2',
            'PlayerB3',
            'PlayerB4',
            'PlayerB5',
            'PlayerB6',
            'PlayerB7',
            'PlayerB8',
            'PlayerB9',
            'PlayerB10',
        ]

        self.bal = defaultProperties()
        self.bal.setCoordinates(600, 350)

        self.A1 = defaultProperties()
        self.A1.setCoordinates(140, 100)

        self.A2 = defaultProperties()
        self.A2.setCoordinates(140, 250)

        self.A3 = defaultProperties()
        self.A3.setCoordinates(140, 400)

        self.A4 = defaultProperties()
        self.A4.setCoordinates(140, 550)

        self.A5 = defaultProperties()
        self.A5.setCoordinates(340, 150)

        self.A6 = defaultProperties()
        self.A6.setCoordinates(340, 300)

        self.A7 = defaultProperties()
        self.A7.setCoordinates(340, 450)

        self.A8 = defaultProperties()
        self.A8.setCoordinates(500, 350)

        self.A9 = defaultProperties()
        self.A9.setCoordinates(550, 300)

        self.A10 = defaultProperties()
        self.A10.setCoordinates(550, 400)

        self.keeperA = defaultProperties()
        self.keeperA.setCoordinates(40, 330)

        self.B1 = defaultProperties()
        self.B1.setCoordinates(1030, 100)

        self.B2 = defaultProperties()
        self.B2.setCoordinates(1030, 250)

        self.B3 = defaultProperties()
        self.B3.setCoordinates(1030, 400)

        self.B4 = defaultProperties()
        self.B4.setCoordinates(1030, 550)

        self.B5 = defaultProperties()
        self.B5.setCoordinates(830, 150)

        self.B6 = defaultProperties()
        self.B6.setCoordinates(830, 300)

        self.B7 = defaultProperties()
        self.B7.setCoordinates(830, 450)

        self.B8 = defaultProperties()
        self.B8.setCoordinates(750, 350)

        self.B9 = defaultProperties()
        self.B9.setCoordinates(650, 300)

        self.B10 = defaultProperties()
        self.B10.setCoordinates(650, 400)

        self.keeperB = defaultProperties()
        self.keeperB.setCoordinates(1130, 330)

        x, y = 0, 0
        return

    def sortdata(self, dictData):
        vals = list(dictData.values())
        keys = list(dictData.keys())
        vals.sort()
        sortedKeys = []
        for i in vals:
            for j in keys:
                if dictData[j] == i:
                    sortedKeys.append(j)

        return sortedKeys

    def StraightLineDistance(self, x1, x2, y1, y2):
        # returns the straight line distance between coordinate (x1, y1) and coordinate (x2, y2)
        x = pow(np.abs(x1 - x2), 2)
        y = pow(np.abs(y1 - y2), 2)

        return np.sqrt(x+y)

    def ComputeGoal(self):
        # get KeeperA's location
        x1, y1 = self.GetplayersLocation(defaultPlayer='PlayerAKeeper')
        x2, y2 = self.GetplayersLocation(defaultPlayer='PlayerBKeeper')
        ballx, bally = self.bal.GetlastLocation()
        GoalStatus = 'Nil'
        if ballx >= 20 and ballx <= 40:
            if (bally > y1+20 or bally < y1-20) and (bally > 250 and bally < 450):
                self.game_status = 'Goal!!!!'
                # increment team score
                self.TeamBScore += 1
                out = True
                GoalStatus = 'Nil'

            else:
                GoalStatus = 'PlayerAKeeper'
                out = False

        elif ballx >= 1130 and ballx <= 1180:
            if (bally > y2+20 or bally < y2-20) and (bally > 250 and bally < 450):
                self.game_status = 'Goal!!!!'
                # increment team score
                self.TeamAScore += 1
                out = True
            else:
                GoalStatus = 'PlayerBKeeper'
                out = False
        else:
            GoalStatus = 'Nil'
            out = False
        return out, GoalStatus

    def GetPostBoundary(self, keeper='PlayerBKeeper'):
        if keeper == 'PlayerBKeeper':
            ytarget = np.random.choice([i for i in range(250, 450)])
            xtarget = 1160

        else:
            ytarget = np.random.choice([i for i in range(250, 450)])
            xtarget = 20
        return xtarget, ytarget

    def AttemptScore(self, player, keeper, XDict, YDict):
        xtarget, ytarget = self.GetPostBoundary(keeper=keeper)
        xsource, ysource = self.GetplayersLocation(defaultPlayer=player)
        xmoves, ymoves = self.linearRegression(
            xsource, ysource, xtarget, ytarget)

        # set balls trajectory
        self.setplayersLocation(coordinates=(
            xmoves, ymoves), defaultPlayer='ball')

        # decide if the keeper should get the ball or loose it
        keeperStatus = np.random.choice([True, False], p=[0.7, 0.3])
        if keeperStatus == True:
            # set Keeper's movement to follow the ball

            if keeper in self.playersListA:
                self.keeperA.listY = [ymoves[-1]-10, ymoves[-1]-5,
                                      ymoves[-1]+10, ymoves[-1]+5, ymoves[-1]]*10
                self.keeperA.listX = [xmoves[-1]]*50
                self.game_status = "Awesome!!! Goalkeeper caught the ball."

            else:
                self.keeperB.listY = [ymoves[-1]-10, ymoves[-1]-5,
                                      ymoves[-1]+10, ymoves[-1]+5, ymoves[-1]]*10
                self.keeperB.listX = [xmoves[-1]]*50
                self.game_status = "Awesome!!! Goalkeeper caught the ball."

        else:
            currentPositionX, currentPositionY = self.GetplayersLocation(
                defaultPlayer=keeper)
            xbound, ybound = self.GetplayersBoundary(keeper)

            xmoves, ymoves = self.linearRegression(currentPositionX, currentPositionY,
                                                   xbound, ybound)
            self.setplayersLocation((xmoves, ymoves), defaultPlayer=keeper)

        if keeper in list(XDict.keys()):
            XDict.pop(keeper)
        else:
            YDict.pop(keeper)

        # Re-position other players
        for playee in XDict.keys():
            currentPositionX, currentPositionY = XDict[playee]
            xbound, ybound = self.GetplayersBoundary(playee)

            xmoves, ymoves = self.linearRegression(currentPositionX, currentPositionY,
                                                   xbound, ybound)
            self.setplayersLocation((xmoves, ymoves), defaultPlayer=playee)

        for playee in YDict.keys():
            currentPositionX, currentPositionY = YDict[playee]
            xbound, ybound = self.GetplayersBoundary(playee)
            xmoves, ymoves = self.linearRegression(currentPositionX, currentPositionY,
                                                   xbound, ybound)
            self.setplayersLocation((xmoves, ymoves), defaultPlayer=playee)

        return

    def Attack(self, OpposingPlayers):
        """
        Return the next player in the opposing team close enough to get the ball from the
        current team.
        """
        playee = 'A'
        Status = False
        # Get the current ball location
        count = self.count
        currentX, currentY = self.bal.listX[count], self.bal.listY[count]

        EstimatedDistance = {}
        for player in OpposingPlayers.keys():
            # find Euclidean Distance from ball
            playeeCoordinate = OpposingPlayers[player]
            EstimatedDistance[player] = self.StraightLineDistance(playeeCoordinate[0],
                                                                  currentX, playeeCoordinate[1], currentY)

        sortedKey = self.sortdata(EstimatedDistance)[0]
        if EstimatedDistance[sortedKey] <= 50:
            Status = True
            playee = sortedKey
        else:
            Status = False
            playee = 'A'
        return playee, Status

    def TagPlayers(self, XDict, YDict):
        """
        YDict in this case represents the source players
        XDict in this case represents the target players
        That is, YDict are tagging each XDict Player (excluding goal keepers)
        """
        SourcePlayers = list(YDict.keys())
        TargetPlayers = list(XDict.keys())

        # remove goal keepers
        # goalkeepers are always first on the list
        TargetPlayers.remove(TargetPlayers[0])
        # goalkeepers are always first on the list
        SourcePlayers.remove(SourcePlayers[0])

        # Tag players to players based on nearest neighbors
        DictTags = {}

        for k in SourcePlayers:
            EstimatedDistance = {}
            for j in TargetPlayers:
                # get source location
                xsource, ysource = self.GetplayersLocation(k)
                # get target location
                xtarget, ytarget = self.GetplayersLocation(j)

                EstimatedDistance[j] = self.StraightLineDistance(
                    xsource, xtarget, ysource, ytarget)
            FirstKey = self.sortdata(EstimatedDistance)[0]
            DictTags[k] = FirstKey
            # remove the chosen key from this data.
            TargetPlayers.remove(FirstKey)

        # reset movement of source players to target players
        for keys in DictTags.keys():
            value = DictTags[keys]
            # get source location
            xsource, ysource = self.GetplayersLocation(keys)
            xtarget, ytarget = self.GetplayersLocation(value)

            xmoves, ymoves = self.linearRegression(
                xsource, ysource, xtarget, ytarget)

            # reposition the ball in front of the player

            self.setplayersLocation(coordinates=(
                xmoves, ymoves), defaultPlayer=keys)

        return

    def LikePairsNearestNeighbor(self, playername, sourcePlayerCoordinate, SourcedictDataX, SourcedictDataY,
                                 milestone='short', conditionedValue=30):
        """
        SourcedictDataX: details of all source Players and their respective coordinate.
        SourcedictDataY: details of all target Players and their respecitve coordinate.
        playername: name of the current player
        sourcePlayerCoordinate: current coordinate of the player
        milstone: either long pass, short pass or across.
        conditionedValue: give the game to player who is free from an opponent at a distance less than 30
        """

        EstimatedDistance = {}
        for playee in SourcedictDataX.keys():
            playeeCoordinate = SourcedictDataX[playee]
            EstimatedDistance[playee] = self.StraightLineDistance(
                sourcePlayerCoordinate[0], playeeCoordinate[0], sourcePlayerCoordinate[1], playeeCoordinate[1])

        sortedKeys = self.sortdata(EstimatedDistance)
        sortedKeys.remove(playername)
        nextplayer = np.random.choice(sortedKeys)
        return nextplayer

    def repositionBall(self, xmove, ymove):
        i = 0
        x = [i+1 for i in xmove]
        y = [i+1 for j in ymove]
        return x, y

    def AttemptGoal(self, playername, sourcePlayerCoordinate, SourcedictDataX, SourcedictDataY):
        # Attempt Shot
        # get opposing keeper, target Team.
        if playername in self.playersListA:
            goalKeeper = 'PlayerBKeeper'
        else:
            goalKeeper = 'PlayerAKeeper'

        self.game_status = playername + \
            ' is Attempting to make Shot, goalkeeper is ' + goalKeeper
        self.AttemptScore(playername, goalKeeper,
                          SourcedictDataX, SourcedictDataY)
        return

    def updateposition(self, playername, sourcePlayerCoordinate, SourcedictDataX, SourcedictDataY):

        # get the next player
        outplayer = self.LikePairsNearestNeighbor(
            playername, sourcePlayerCoordinate, SourcedictDataX, SourcedictDataY)

        # update straight line movement of the ball from source to nextplayer

        xbound, ybound = SourcedictDataX[outplayer]
        xsource, ysource = self.bal.GetlastLocation()

        xmoves, ymoves = self.linearRegression(
            xsource, ysource, xbound, ybound)

        # reposition the ball in front of the player

        self.setplayersLocation(coordinates=(
            xmoves, ymoves), defaultPlayer='ball')
        self.setplayersLocation(coordinates=(
            [xbound]*50, [ybound]*50), defaultPlayer=outplayer)

        # remove playername, and update new player
        SourcedDictDataX_copy = SourcedictDataX.copy()
        SourcedDictDataX_copy.pop(outplayer)

        # update the positions of all players including playername
        """
        1. get their current position from the sourcedictDataX and SourcedDictDataY
        2. estimate a straight line move to their new position (within the specified boundary)
        """
        for playee in SourcedDictDataX_copy.keys():
            currentPositionX, currentPositionY = SourcedDictDataX_copy[playee]
            xbound, ybound = self.GetplayersBoundary(playee)

            xmoves, ymoves = self.linearRegression(currentPositionX, currentPositionY,
                                                   xbound, ybound)
            self.setplayersLocation((xmoves, ymoves), defaultPlayer=playee)

        # reset oppossing keepers position
        currentPositionX, currentPositionY = SourcedictDataY[list(
            SourcedictDataY.keys())[0]]
        xbound, ybound = self.GetplayersBoundary(
            list(SourcedictDataY.keys())[0])
        xmoves, ymoves = self.linearRegression(currentPositionX, currentPositionY,
                                               xbound, ybound)
        self.setplayersLocation(
            (xmoves, ymoves), defaultPlayer=list(SourcedictDataY.keys())[0])

        # for the opposing players, reset their positions to attack.
        self.TagPlayers(SourcedictDataX, SourcedictDataY)

        return outplayer, playername

    def linearRegression(self, x1, y1, x2, y2):
        reg = Regression()
        xmove, ymove = reg.network(x1, y1, x2, y2)

        return xmove, ymove

    def setplayersLocation(self, coordinates, defaultPlayer='ball'):
        """
        x and y are lists of 50 different positions for the specific 'player'
        updates a new location for the player passed in as defaultPlayer
        """
        x = coordinates[0]
        y = coordinates[1]
        if defaultPlayer == 'PlayerA1':
            self.A1.listX = x
            self.A1.listY = y
        elif defaultPlayer == 'PlayerA2':
            self.A2.listX = x
            self.A2.listY = y
        elif defaultPlayer == 'PlayerA3':
            self.A3.listX = x
            self.A3.listY = y
        elif defaultPlayer == 'PlayerA4':
            self.A4.listX = x
            self.A4.listY = y
        elif defaultPlayer == 'PlayerA5':
            self.A5.listX = x
            self.A5.listY = y
        elif defaultPlayer == 'PlayerA6':
            self.A6.listX = x
            self.A6.listY = y
        elif defaultPlayer == 'PlayerA7':
            self.A7.listX = x
            self.A7.listY = y
        elif defaultPlayer == 'PlayerA8':
            self.A8.listX = x
            self.A8.listY = y
        elif defaultPlayer == 'PlayerA9':
            self.A9.listX = x
            self.A9.listY = y
        elif defaultPlayer == 'PlayerA10':
            self.A10.listX = x
            self.A10.listY = y
        elif defaultPlayer == 'PlayerAKeeper':
            self.keeperA.listX = x
            self.keeperA.listY = y

        # begin for B
        elif defaultPlayer == 'PlayerB1':
            self.B1.listX = x
            self.B1.listY = y
        elif defaultPlayer == 'PlayerB2':
            self.B2.listX = x
            self.B2.listY = y
        elif defaultPlayer == 'PlayerB3':
            self.B3.listX = x
            self.B3.listY = y
        elif defaultPlayer == 'PlayerB4':
            self.B4.listX = x
            self.B4.listY = y
        elif defaultPlayer == 'PlayerB5':
            self.B5.listX = x
            self.B5.listY = y
        elif defaultPlayer == 'PlayerB6':
            self.B6.listX = x
            self.B6.listY = y
        elif defaultPlayer == 'PlayerB7':
            self.B7.listX = x
            self.B7.listY = y
        elif defaultPlayer == 'PlayerB8':
            self.B8.listX = x
            self.B8.listY = y
        elif defaultPlayer == 'PlayerB9':
            self.B9.listX = x
            self.B9.listY = y
        elif defaultPlayer == 'PlayerB10':
            self.B10.listX = x
            self.B10.listY = y
        elif defaultPlayer == 'PlayerBKeeper':
            self.keeperB.listX = x
            self.keeperB.listY = y
        elif defaultPlayer == 'ball':
            self.bal.listX = x
            self.bal.listY = y

        else:
            pass

        return

    def GetplayersLocation(self, defaultPlayer='ball'):
        """
        updates a new location for the player passed in as defaultPlayer
        """
        if defaultPlayer == 'PlayerA1':
            x, y = self.A1.positionx, self.A1.positiony
        elif defaultPlayer == 'PlayerA2':
            x, y = self.A2.positionx, self.A2.positiony
        elif defaultPlayer == 'PlayerA3':
            x, y = self.A3.positionx, self.A3.positiony
        elif defaultPlayer == 'PlayerA4':
            x, y = self.A4.positionx, self.A4.positiony
        elif defaultPlayer == 'PlayerA5':
            x, y = self.A5.positionx, self.A5.positiony
        elif defaultPlayer == 'PlayerA6':
            x, y = self.A6.positionx, self.A6.positiony
        elif defaultPlayer == 'PlayerA7':
            x, y = self.A7.positionx, self.A7.positiony
        elif defaultPlayer == 'PlayerA8':
            x, y = self.A8.positionx, self.A8.positiony
        elif defaultPlayer == 'PlayerA9':
            x, y = self.A9.positionx, self.A9.positiony
        elif defaultPlayer == 'PlayerA10':
            x, y = self.A10.positionx, self.A10.positiony
        elif defaultPlayer == 'PlayerAKeeper':
            x, y = self.keeperA.positionx, self.keeperA.positiony

        # begin for B
        elif defaultPlayer == 'PlayerB1':
            x, y = self.B1.positionx, self.B1.positiony
        elif defaultPlayer == 'PlayerB2':
            x, y = self.B2.positionx, self.B2.positiony
        elif defaultPlayer == 'PlayerB3':
            x, y = self.B3.positionx, self.B3.positiony
        elif defaultPlayer == 'PlayerB4':
            x, y = self.B4.positionx, self.B4.positiony
        elif defaultPlayer == 'PlayerB5':
            x, y = self.B5.positionx, self.B5.positiony
        elif defaultPlayer == 'PlayerB6':
            x, y = self.B6.positionx, self.B6.positiony
        elif defaultPlayer == 'PlayerB7':
            x, y = self.B7.positionx, self.B7.positiony
        elif defaultPlayer == 'PlayerB8':
            x, y = self.B8.positionx, self.B8.positiony
        elif defaultPlayer == 'PlayerB9':
            x, y = self.B9.positionx, self.B9.positiony
        elif defaultPlayer == 'PlayerB10':
            x, y = self.B10.positionx, self.B10.positiony

        elif defaultPlayer == 'ball':
            x, y = self.bal.positionx, self.bal.positiony
        elif defaultPlayer == 'PlayerBKeeper':
            x, y = self.keeperB.positionx, self.keeperB.positiony

        else:
            pass
        return x, y

    def GetplayersBoundary(self, defaultPlayer='ball'):
        """
        Get the boundary's of keepers, ball, defenders, strikers and mid-fielders
        """
        # Determine factor, range of factor is 0 - 1
        factor = 1
        factor2 = 1
        stat = False
        # get ball's coordinate
        xball, yball = self.GetplayersLocation('ball')
        if yball < 330:
            stat = False
            # within player's A post
            factor = 0.2
            factor2 = 1

        elif yball > 330 and yball < 660:
            stat = True
            factor = 1
            factor2 = 1

        else:
            stat = False
            factor = 0.7
            factor2 = 1/factor

        if defaultPlayer in ['PlayerA1', 'PlayerA2', 'PlayerB9']:
            x1, x2, y1, y2 = 150*factor, 600*factor*factor2, 330, 660

        elif defaultPlayer in ['PlayerA3', 'PlayerA4', 'PlayerB10']:
            x1, x2, y1, y2 = 150*factor, 600*factor*factor2, 20, 330

        elif defaultPlayer == 'PlayerB8':
            x1, x2, y1, y2 = 150*factor, 600*factor*factor2, 275, 345

        elif defaultPlayer in ['PlayerA5', 'PlayerB5']:
            x1, x2, y1, y2 = 400*factor, 900*factor*factor2, 330, 660

        elif defaultPlayer in ['PlayerA6', 'PlayerB6']:
            x1, x2, y1, y2 = 400*factor, 900*factor*factor2, 275, 345

        elif defaultPlayer in ['PlayerA7', 'PlayerB7']:
            x1, x2, y1, y2 = 400*factor, 900*factor*factor2, 20, 330

        elif defaultPlayer == 'PlayerA8':
            x1, x2, y1, y2 = 600*factor, 1000*factor*factor2, 275, 345

        elif defaultPlayer == 'PlayerA9':
            x1, x2, y1, y2 = 600*factor, 1000*factor*factor2, 330, 660

        elif defaultPlayer == 'PlayerA10':
            x1, x2, y1, y2 = 600*factor, 1000*factor*factor2, 20, 330

        elif defaultPlayer in ['PlayerB1', 'PlayerB2']:
            x1, x2, y1, y2 = 600*factor, 1000*factor*factor2, 330, 660

        elif defaultPlayer in ['PlayerB3', 'PlayerB4']:
            x1, x2, y1, y2 = 600*factor, 1000*factor*factor2, 20, 330

        elif defaultPlayer == 'PlayerAKeeper':
            x1, x2, y1, y2 = 20, 220, 200, 500
        elif defaultPlayer == 'PlayerBKeeper':
            x1, x2, y1, y2 = 1000, 1100, 200, 500
        else:
            x1, x2, y1, y2 = 20, 1160, 20, 660

        # Get player's location to minimize movement around the field
        xloc, yloc = self.GetplayersLocation(defaultPlayer)
        xchoice = np.random.choice([i for i in range(int(x1), int(x2))])
        ychoice = np.random.choice([i for i in range(int(y1), int(y2))])

        # ensure xsource isn't too far from Xnew
        # if stat == True:
        if xloc > xchoice:
            if np.abs(xloc-xchoice) > 100:
                xchoice = xloc - 100

        else:
            if np.abs(xloc-xchoice) > 100:
                xchoice = xloc + 100
        # else:
        #     pass

        # return a random coordinate between x1 and x2, likewise, y1 and y2.

        return xchoice, ychoice
