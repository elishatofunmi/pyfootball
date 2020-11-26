import time
import os
import sys
from Scripts.PlayersProperties import *
from Scripts.footballProperties import *
from Scripts.net import network
import numpy as np

import pygame
import sys
from pygame.locals import *
pygame.init()


class Environment:
    def __init__(self, scoreA, scoreB):

        self.FPS = 20
        self.fpsClock = pygame.time.Clock()

        # initialize the network
        self.net = network()
        self.net.TeamAScore = scoreA
        self.net.TeamBScore = scoreB

        # set up the window
        self.DISPLAYSURF = pygame.display.set_mode((1200, 780), 0, 32)
        pygame.display.set_caption(
            'REINFORCEMENT LEARNING (Discrete Mathematics) - Football Analytics (footRein)')
        # set up the colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.col = (0, 50, 150)

        # set game status
        self.myFontA = pygame.font.SysFont("Times New Roman", 35)
        self.myFontB = pygame.font.SysFont("Times New Roman", 20)

        # load Team and their positions
        MapTeam = {
            'ball': 'others/ball.jpeg',
            'PlayerAKeeper': 'players/TeamAk.png',
            'PlayerA1': 'players/teamA1.png',
            'PlayerA2': 'players/teamA2.png',
            'PlayerA3': 'players/teamA3.png',
            'PlayerA4': 'players/teamA4.png',
            'PlayerA5': 'players/teamA5.png',
            'PlayerA6': 'players/teamA6.png',
            'PlayerA7': 'players/teamA7.png',
            'PlayerA8': 'players/teamA8.png',
            'PlayerA9': 'players/teamA9.png',
            'PlayerA10': 'players/teamA10.png',
            'PlayerBKeeper': 'players/TeamBk.png',
            'PlayerB1': 'players/teamB1.png',
            'PlayerB2': 'players/teamB2.png',
            'PlayerB3': 'players/teamB3.png',
            'PlayerB4': 'players/teamB4.png',
            'PlayerB5': 'players/teamB5.png',
            'PlayerB6': 'players/teamB6.png',
            'PlayerB7': 'players/teamB7.png',
            'PlayerB8': 'players/teamB8.png',
            'PlayerB9': 'players/teamB9.png',
            'PlayerB10': 'players/teamB10.png'
        }
        self.LoadTeamPositions = {}
        for m in MapTeam.keys():
            image_path = 'images/'+str(MapTeam[m])
            self.LoadTeamPositions[m] = pygame.image.load(image_path)
            self.LoadTeamPositions[m] = pygame.transform.scale(
                self.LoadTeamPositions[m], (20, 20))

        self.nextTeam = 'Team A'

        # randomly decide start team
        self.Team = np.random.choice(['A', 'B'])

        if self.Team == 'A':
            # Randomly decide start strikers
            self.startingChoicePlayer = np.random.choice(
                ['PlayerA9', 'PlayerA10'])
            self.nextPlayer = np.random.choice(['PlayerA9', 'PlayerA10'])

        else:
            self.startingChoicePlayer = np.random.choice(
                ['PlayerB9', 'PlayerB10'])
            self.nextPlayer = np.random.choice(['PlayerA9', 'PlayerA10'])

        self.excludedPlayer = self.startingChoicePlayer
        return

    # draw on the surface object

    def boarddisplay(self, count, nextplayer):

        self.DISPLAYSURF.fill(self.WHITE)
        pygame.draw.rect(self.DISPLAYSURF, self.GREEN, (20, 20, 1160, 660))
        # box 18
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (20, 200, 200, 300))
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (1000, 200, 200, 300))
        # insert the goal posts
        pygame.draw.rect(self.DISPLAYSURF, self.BLUE, (20, 250, 20, 200))
        pygame.draw.rect(self.DISPLAYSURF, self.BLUE, (1160, 250, 20, 200))

        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (598, 0, 4, 700))
        pygame.draw.ellipse(self.DISPLAYSURF, self.WHITE, (500, 200, 200, 300))
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (20, 20, 20, 20))
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (1160, 20, 20, 20))
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (20, 660, 20, 20))
        pygame.draw.rect(self.DISPLAYSURF, self.WHITE, (1160, 660, 20, 20))

        # Object Detection
        pygame.draw.rect(self.DISPLAYSURF, self.RED,
                         (self.net.superDict['ball'].listX[count]-3, self.net.superDict['ball'].listY[count]-3, 25, 25))

        # Boundary Box around nextPlayer
        pygame.draw.rect(self.DISPLAYSURF, self.RED,
                         (self.net.superDict['ball'].listX[-1]-3, self.net.superDict['ball'].listY[-1]-3, 25, 25))

        return

    def displayBall(self, count):
        # display ball
        self.DISPLAYSURF.blit(
            self.LoadTeamPositions['ball'], (self.net.superDict['ball'].listX[count], self.net.superDict['ball'].listY[count]))
        return

    def displayDefaultA(self, count=0):

        for k in self.net.playersListA:
            self.DISPLAYSURF.blit(self.LoadTeamPositions[str(k)], (self.net.superDict[str(
                k)].listX[count], self.net.superDict[str(k)].listY[count]))

        return

    def displayDefaultB(self, count=0):
        # randomly display players A within enclosed position x, y, xwidth, ywidth
        for k in self.net.playersListB:
            self.DISPLAYSURF.blit(self.LoadTeamPositions[str(k)], (self.net.superDict[str(
                k)].listX[count], self.net.superDict[str(k)].listY[count]))

        return

    def updateLastPosition(self, count):

        for k in self.net.playersListA:
            self.net.superDict[str(
                k)].positionx = self.net.superDict[str(k)].listX[count]
            self.net.superDict[str(
                k)].positiony = self.net.superDict[str(k)].listY[count]

        for k in self.net.playersListB:
            self.net.superDict[str(
                k)].positionx = self.net.superDict[str(k)].listX[count]
            self.net.superDict[str(
                k)].positiony = self.net.superDict[str(k)].listY[count]

        # ball
        self.net.superDict['ball'].positionx = self.net.superDict['ball'].listX[count]
        self.net.superDict['ball'].positiony = self.net.superDict['ball'].listY[count]

        return

    # Always get sourced

    def sourcedTargetDict(self):
        player = self.startingChoicePlayer

        sourceTeam = {}
        OtherTeam = {}
        AList = ['PlayerAKeeper', 'PlayerA1', 'PlayerA2', 'PlayerA3', 'PlayerA4', 'PlayerA5', 'PlayerA6',
                 'PlayerA7', 'PlayerA8', 'PlayerA9', 'PlayerA10']

        BList = ['PlayerBKeeper', 'PlayerB1', 'PlayerB2', 'PlayerB3', 'PlayerB4', 'PlayerB5', 'PlayerB6',
                 'PlayerB7', 'PlayerB8', 'PlayerB9', 'PlayerB10']

        # Create Source Data of Source players
        for m in AList:
            sourceTeam[m] = self.net.GetplayersLocation(defaultPlayer=m)

        # Create Target Data of Target players
        for m in BList:
            OtherTeam[m] = self.net.GetplayersLocation(defaultPlayer=m)

        if player in AList:

            output = sourceTeam, OtherTeam

        else:

            output = OtherTeam, sourceTeam

        return output

    def FindLongDistance(self, x1, x2, y1, y2):
        x = np.abs(x1 - x2)
        y = np.abs(y1 - y2)

        return int(np.sqrt(pow(x, 2) + pow(y, 2)))

    def evaluateTeam(self, xTeam, yTeam):
        # get ball coordinate
        ballcoordinate = self.net.GetplayersLocation(defaultPlayer='ball')
        minimumDistance = {}

        for keys in list(xTeam.keys()):
            a, b = xTeam[keys]
            dist = self.FindLongDistance(
                ballcoordinate[0], a, ballcoordinate[1], b)
            minimumDistance[keys] = dist

        for keys in list(yTeam.keys()):
            a, b = yTeam[keys]
            dist = self.FindLongDistance(
                ballcoordinate[0], a, ballcoordinate[1], b)
            minimumDistance[keys] = dist

        self.nextplayer = self.net.sortdata(minimumDistance)[0]
        if self.nextplayer in list(xTeam.keys()):
            Team = 'A'
        else:
            Team = 'B'
        return self.nextplayer, Team

    # overwrite current player by making opposing players to attack thereby changing next player and Team

    def runProgram(self, startGame=True, FreeKick=(False, 'PlayerAKeeper')):
        count = 0
        Status = False
        StatusCheck = True
        outVal = False
        subsequentCount = True
        nextPlayer = self.nextPlayer
        freeKick = False

        if FreeKick[0] == True:
            self.net.game_status = 'This is a Free Kick!!!'
            self.startingChoicePlayer = FreeKick[1]
            xcor, ycor = self.net.GetplayersLocation(FreeKick[1])
            self.net.superDict['ball'].positionx = xcor
            self.net.superDict['ball'].positiony = ycor

            if FreeKick[1] in self.net.playersListA:
                nextPlayer = np.random.choice(self.net.playersListA[1:])
            else:
                nextPlayer = np.random.choice(self.net.playersListB[1:])
        else:
            pass

        # display board
        self.boarddisplay(count, nextPlayer)

        # display ball
        self.displayBall(count)

        # display player A
        self.displayDefaultA(count)

        # display player B
        self.displayDefaultB(count)

        while True:
            # show game status
            self.randNumLabelA = self.myFontA.render(
                'Team A: '+str(self.net.TeamAScore) + ', Team B: '+str(self.net.TeamBScore), 1, self.BLACK)
            self.randNumLabelB = self.myFontB.render(
                'Game Status: ' + str(self.net.game_status), 1, self.BLACK)

            # make choice of player
            ChoicePlayerCoordinate = self.net.GetplayersLocation(
                defaultPlayer=self.startingChoicePlayer)

            XDict, YDict = self.sourcedTargetDict()
            # set Count in network to be current count
            self.net.count = count

            if count == 0:
                YDictZero = YDict
                if subsequentCount == True:
                    playersChoice = 'B'
                else:
                    playersChoice = np.random.choice(['A', 'B'], p=[0.3, 0.7])

                if playersChoice == 'A':
                    self.net.AttemptGoal(self.startingChoicePlayer,  sourcePlayerCoordinate=ChoicePlayerCoordinate,
                                         SourcedictDataX=XDict, SourcedictDataY=YDict)

                else:
                    # keep deciding the next player
                    self.startingChoicePlayer, self.excludedPlayer = self.net.updateposition(self.startingChoicePlayer,  sourcePlayerCoordinate=ChoicePlayerCoordinate,
                                                                                             SourcedictDataX=XDict, SourcedictDataY=YDict)

                    self.nextPlayer = self.startingChoicePlayer
                    self.net.game_status = "Next Player: " + \
                        str(self.startingChoicePlayer)

            # Let the opposing team Attack
            if StatusCheck:
                OpposingPlayee, Status = self.net.Attack(YDict)
            else:
                pass

            pygame.display.update()
            self.fpsClock.tick(self.FPS)

            # display board
            self.boarddisplay(count, nextPlayer)

            # display ball
            self.displayBall(count)

            # display player A
            self.displayDefaultA(count)

            # display player B
            self.displayDefaultB(count)

            self.DISPLAYSURF.blit(self.randNumLabelA, (450, 700))
            self.DISPLAYSURF.blit(self.randNumLabelB, (450, 740))

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            if Status == True:
                self.startingChoicePlayer = OpposingPlayee
                # update count
                self.updateLastPosition(count=count)

            # increment count
            count += 1

            if count == 50:
                self.updateLastPosition(count=49)

                count = 0
                goal, goalStatus = self.net.ComputeGoal()

                if goal == False:
                    if goalStatus in ['PlayerAKeeper', 'PlayerBKeeper']:
                        freeKick = np.random.choice(
                            [True, False], p=[0.3, 0.7])
                        outVal = True
                        if freeKick == True:
                            break
                        else:
                            pass
                    else:
                        outVal = False
                else:
                    self.net.game_status = 'Goal!!!!'
                    outVal = True
                    break
            else:
                pass

            if startGame == True:
                time.sleep(2)
                startGame = False

            subsequentCount = False

        return outVal, freeKick, goalStatus


# Score of the match
ScoreA, ScoreB = 0, 0
freeKick = False


def main(ScoreA, ScoreB, freeKick=freeKick):
    env = Environment(ScoreA, ScoreB)

    outVal, FreeKick, goalStatus = env.runProgram(
        startGame=True, FreeKick=freeKick)
    if outVal == True:
        # get the score of the match
        ScoreA, ScoreB = env.net.TeamAScore, env.net.TeamBScore
        main(ScoreA, ScoreB, freeKick=(FreeKick, goalStatus))
    return


if __name__ == "__main__":
    main(ScoreA, ScoreB, freeKick=(False, "PlayerAKeeper"))
