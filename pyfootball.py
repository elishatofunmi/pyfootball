import time
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

        # define the ball
        self.foot_ball = pygame.image.load('images/others/ball.jpeg')
        self.foot_ball = pygame.transform.scale(self.foot_ball, (20, 20))

        # Define team A
        self.TEAMA_goalkeeper = pygame.image.load('images/players/TeamAk.png')
        self.TEAMA_goalkeeper = pygame.transform.scale(
            self.TEAMA_goalkeeper, (20, 20))

        self.TEAMA_one = pygame.image.load('images/players/teamA1.png')
        self.TEAMA_one = pygame.transform.scale(self.TEAMA_one, (20, 20))

        self.TEAMA_two = pygame.image.load('images/players/teamA2.png')
        self.TEAMA_two = pygame.transform.scale(self.TEAMA_two, (20, 20))

        self.TEAMA_three = pygame.image.load('images/players/teamA3.png')
        self.TEAMA_three = pygame.transform.scale(self.TEAMA_three, (20, 20))

        self.TEAMA_four = pygame.image.load('images/players/teamA4.png')
        self.TEAMA_four = pygame.transform.scale(self.TEAMA_four, (20, 20))

        self.TEAMA_five = pygame.image.load('images/players/teamA5.png')
        self.TEAMA_five = pygame.transform.scale(self.TEAMA_five, (20, 20))

        self.TEAMA_six = pygame.image.load('images/players/teamA6.png')
        self.TEAMA_six = pygame.transform.scale(self.TEAMA_six, (20, 20))

        self.TEAMA_seven = pygame.image.load('images/players/teamA7.png')
        self.TEAMA_seven = pygame.transform.scale(self.TEAMA_seven, (20, 20))

        self.TEAMA_eight = pygame.image.load('images/players/teamA8.png')
        self.TEAMA_eight = pygame.transform.scale(self.TEAMA_eight, (20, 20))

        self.TEAMA_nine = pygame.image.load('images/players/teamA9.png')
        self.TEAMA_nine = pygame.transform.scale(self.TEAMA_nine, (20, 20))

        self.TEAMA_ten = pygame.image.load('images/players/teamA10.png')
        self.TEAMA_ten = pygame.transform.scale(self.TEAMA_ten, (20, 20))

        # define team B
        self.TEAMB_goalkeeper = pygame.image.load('images/players/TeamBk.png')
        self.TEAMB_goalkeeper = pygame.transform.scale(
            self.TEAMB_goalkeeper, (20, 20))

        self.TEAMB_one = pygame.image.load('images/players/teamB1.png')
        self.TEAMB_one = pygame.transform.scale(self.TEAMB_one, (20, 20))

        self.TEAMB_two = pygame.image.load('images/players/teamB2.png')
        self.TEAMB_two = pygame.transform.scale(self.TEAMB_two, (20, 20))

        self.TEAMB_three = pygame.image.load('images/players/teamB3.png')
        self.TEAMB_three = pygame.transform.scale(self.TEAMB_three, (20, 20))

        self.TEAMB_four = pygame.image.load('images/players/teamB4.png')
        self.TEAMB_four = pygame.transform.scale(self.TEAMB_four, (20, 20))

        self.TEAMB_five = pygame.image.load('images/players/teamB5.png')
        self.TEAMB_five = pygame.transform.scale(self.TEAMB_five, (20, 20))

        self.TEAMB_six = pygame.image.load('images/players/teamB6.png')
        self.TEAMB_six = pygame.transform.scale(self.TEAMB_six, (20, 20))

        self.TEAMB_seven = pygame.image.load('images/players/teamB7.png')
        self.TEAMB_seven = pygame.transform.scale(self.TEAMB_seven, (20, 20))

        self.TEAMB_eight = pygame.image.load('images/players/teamB8.png')
        self.TEAMB_eight = pygame.transform.scale(self.TEAMB_eight, (20, 20))

        self.TEAMB_nine = pygame.image.load('images/players/teamB9.png')
        self.TEAMB_nine = pygame.transform.scale(self.TEAMB_nine, (20, 20))

        self.TEAMB_ten = pygame.image.load('images/players/teamB10.png')
        self.TEAMB_ten = pygame.transform.scale(self.TEAMB_ten, (20, 20))

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
                         (self.net.bal.listX[count]-3, self.net.bal.listY[count]-3, 25, 25))

        # Boundary Box around nextPlayer
        pygame.draw.rect(self.DISPLAYSURF, self.RED,
                         (self.net.bal.listX[-1]-3, self.net.bal.listY[-1]-3, 25, 25))

        return

    def displayBall(self, count):
        # display ball
        self.DISPLAYSURF.blit(
            self.foot_ball, (self.net.bal.listX[count], self.net.bal.listY[count]))
        return

    def displayDefaultA(self, count=0):
        self.DISPLAYSURF.blit(self.TEAMA_goalkeeper,
                              (self.net.keeperA.listX[count], self.net.keeperA.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_one, (self.net.A1.listX[count], self.net.A1.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_two, (self.net.A2.listX[count], self.net.A2.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_three, (self.net.A3.listX[count], self.net.A3.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_four, (self.net.A4.listX[count], self.net.A4.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_five, (self.net.A5.listX[count], self.net.A5.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_six, (self.net.A6.listX[count], self.net.A6.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_seven, (self.net.A7.listX[count], self.net.A7.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_eight, (self.net.A8.listX[count], self.net.A8.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_nine, (self.net.A9.listX[count], self.net.A9.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMA_ten, (self.net.A10.listX[count], self.net.A10.listY[count]))

        return

    def displayDefaultB(self, count=0):
        # randomly display players A within enclosed position x, y, xwidth, ywidth
        self.DISPLAYSURF.blit(self.TEAMB_goalkeeper,
                              (self.net.keeperB.listX[count], self.net.keeperB.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_one, (self.net.B1.listX[count], self.net.B1.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_two, (self.net.B2.listX[count], self.net.B2.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_three, (self.net.B3.listX[count], self.net.B3.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_four, (self.net.B4.listX[count], self.net.B4.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_five, (self.net.B5.listX[count], self.net.B5.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_six, (self.net.B6.listX[count], self.net.B6.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_seven, (self.net.B7.listX[count], self.net.B7.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_eight, (self.net.B8.listX[count], self.net.B8.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_nine, (self.net.B9.listX[count], self.net.B9.listY[count]))
        self.DISPLAYSURF.blit(
            self.TEAMB_ten, (self.net.B10.listX[count], self.net.B10.listY[count]))
        return

    def updateLastPosition(self, count):
        # ball
        self.net.bal.positionx = self.net.bal.listX[count]
        self.net.bal.positiony = self.net.bal.listY[count]

        # playersA
        self.net.keeperA.positionx = self.net.keeperA.listX[count]
        self.net.keeperA.positiony = self.net.keeperA.listY[count]

        self.net.A1.positionx = self.net.A1.listX[count]
        self.net.A1.positiony = self.net.A1.listY[count]

        self.net.A2.positionx = self.net.A2.listX[count]
        self.net.A2.positiony = self.net.A2.listY[count]

        self.net.A3.positionx = self.net.A3.listX[count]
        self.net.A3.positiony = self.net.A3.listY[count]

        self.net.A4.positionx = self.net.A4.listX[count]
        self.net.A4.positiony = self.net.A4.listY[count]

        self.net.A5.positionx = self.net.A5.listX[count]
        self.net.A5.positiony = self.net.A5.listY[count]

        self.net.A6.positionx = self.net.A6.listX[count]
        self.net.A6.positiony = self.net.A6.listY[count]

        self.net.A7.positionx = self.net.A7.listX[count]
        self.net.A7.positiony = self.net.A7.listY[count]

        self.net.A8.positionx = self.net.A8.listX[count]
        self.net.A8.positiony = self.net.A8.listY[count]

        self.net.A9.positionx = self.net.A9.listX[count]
        self.net.A9.positiony = self.net.A9.listY[count]

        self.net.A10.positionx = self.net.A10.listX[count]
        self.net.A10.positiony = self.net.A10.listY[count]

        # PlayerB

        self.net.keeperB.positionx = self.net.keeperB.listX[count]
        self.net.keeperB.positiony = self.net.keeperB.listY[count]

        self.net.B1.positionx = self.net.B1.listX[count]
        self.net.B1.positiony = self.net.B1.listY[count]

        self.net.B2.positionx = self.net.B2.listX[count]
        self.net.B2.positiony = self.net.B2.listY[count]

        self.net.B3.positionx = self.net.B3.listX[count]
        self.net.B3.positiony = self.net.B3.listY[count]

        self.net.B4.positionx = self.net.B4.listX[count]
        self.net.B4.positiony = self.net.B4.listY[count]

        self.net.B5.positionx = self.net.B5.listX[count]
        self.net.B5.positiony = self.net.B5.listY[count]

        self.net.B6.positionx = self.net.B6.listX[count]
        self.net.B6.positiony = self.net.B6.listY[count]

        self.net.B7.positionx = self.net.B7.listX[count]
        self.net.B7.positiony = self.net.B7.listY[count]

        self.net.B8.positionx = self.net.B8.listX[count]
        self.net.B8.positiony = self.net.B8.listY[count]

        self.net.B9.positionx = self.net.B9.listX[count]
        self.net.B9.positiony = self.net.B9.listY[count]

        self.net.B10.positionx = self.net.B10.listX[count]
        self.net.B10.positiony = self.net.B10.listY[count]
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
            self.net.bal.positionx = xcor
            self.net.bal.positiony = ycor

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
