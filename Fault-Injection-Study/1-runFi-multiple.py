import os, sys
from datetime import datetime
import subprocess

MAX_PARALLEL = 1

# Get input list
fileOpen = open("inputs.txt", 'r')
rawInpList = fileOpen.read().split('\n')
if(rawInpList[-1] == ''):
	rawInpList = rawInpList[:-1]
fileOpen.close()
inpList = []
for item in rawInpList:
	inpList.append(item.replace(' ', '-'))

os.system("mkdir FiTimeLog")
timeLogPath = os.path.join(os.getcwd(), "FiTimeLog", "running_time.log")
#os.system("rm " + resultPath)
timeLogFile = open(timeLogPath, 'a')
timeLogFile.write("########## New Experiment #######\n")
timeLogFile.write("Time: " + str(datetime.now()) + "\n")
timeLogFile.close()

countParallel = 0
# Run FI
for item in inpList:
	print("<<<<<<<<< Now inject faults via input: " + item.replace('-', ' '))
	os.chdir(item)
	subprocess.Popen(["python", "1-runFi-unit.py", str(item.replace('-', ' '), ), timeLogPath])
	os.chdir("../")




