import sys, os
import subprocess
import argparse
import csv
import re
import os, sys

SCALE = 1000000.0

inputArgs = str(sys.argv[1])
execCountFilePath = str(sys.argv[2])



sdcScore = 0.0
totalDICount = 0
threadExecMap = dict()

topDiCount = 0
topThreadIndex = -1

with open(execCountFilePath, 'r') as f:
	lines = f.readlines()
	
	

	for line in lines:
		line = line.strip()
	
		threadIndex = int(line.split(":")[0])
		execCount = int(line.split(":")[1])

		curExecCount =  threadExecMap.get(threadIndex, 0)
		threadExecMap[threadIndex] = curExecCount + execCount

		if topDiCount < threadExecMap[threadIndex]:
			topDiCount = threadExecMap[threadIndex]
			topThreadIndex = threadIndex 		

		totalDICount = totalDICount + execCount
		


	print("Total Dynamic Execution Count: " + str(totalDICount))

if topThreadIndex == -1:
	sys.exit("there has to be a top thread!")


for threadIndex in threadExecMap.keys():
	diCount = threadExecMap[threadIndex]
	beginThreshold = topDiCount - int(0.20 * topDiCount)
	endThreshold = topDiCount + int(0.20 * topDiCount)

	if (diCount < beginThreshold) or (diCount > endThreshold):
		continue

	sdcScore += ((1.0 * diCount) / (1.0 * totalDICount))



SCALE = totalDICount
							
	

print("SDC Score: " + str(sdcScore * SCALE))		


os.system("mkdir Result")
outputFilePath = "Result/SDC_score_" + inputArgs.replace(" ", "_") + ".txt"
os.system("rm " + outputFilePath)

outputFile = open(outputFilePath, "w")
outputFile.write("%s:%.6f"%( inputArgs, sdcScore * SCALE))
outputFile.close()

outputFilePath = "Result/dynamic_footprint_" + inputArgs.replace(" ", "_") + ".txt"
outputFile = open(outputFilePath, "w")
outputFile.write(str(totalDICount))
outputFile.close()
