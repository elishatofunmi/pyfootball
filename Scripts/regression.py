import numpy as np
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
