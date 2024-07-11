import math
import random
import os
from datetime import datetime


memY = {}

class Chromosome:
    def __init__(self, bounds):
        self.noOfArgs = len(bounds)
        self.x = []
        self.inputString = ""
        for i in range(0, self.noOfArgs):
                #self.x.append(random.randint(bounds[i][0], bounds[i][1]))
                if i == 0:
                        self.x.append(random.randint(bounds[i][0], bounds[i][1]) * 16)
                        self.inputString = self.inputString + str(self.x[i])
                else:
                        self.x.append(random.randint(bounds[i][0], bounds[i][1]))
                        self.inputString = self.inputString + " " + str(self.x[i])

        self.y = 0
        self.cc = 0

    def func(self):
        global memY

        # Update values
        self.inputString = ""
        for i in range(0, self.noOfArgs):
                if i == 0:
                        self.inputString = self.inputString + str(self.x[i])
                else:
                        self.inputString = self.inputString + " " + str(self.x[i])

        if self.inputString in memY:
                self.y = memY[self.inputString]

        else:
                os.chdir("./fitness-function/")
                print(" -- Evaluating input: " + self.inputString)
                os.system("python getSDCScore.py \"" + self.inputString + "\"")
                if os.path.exists("Result/fitnessScore.txt") == True:
                     rf = open("Result/fitnessScore.txt", 'r')
                     fs = float(rf.read().strip())
                     self.y = fs
                     memY[self.inputString] = self.y
                     rf.close()
                os.chdir("../")

        logF = open("ga-output.log", 'a')
        logF.write("Evaluating input: " + self.inputString + "; fitness score: " + str(self.y) + "\n")
     
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        logF.write("**** [TIME] **** : " + str(dt_string) + "\n" )
        logF.close()
        logF.close()



