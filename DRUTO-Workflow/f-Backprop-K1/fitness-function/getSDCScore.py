import os, sys, subprocess

inputArgs = str(sys.argv[1])
os.system("mkdir ../sdc-score-calc/Input/")
os.system("mkdir Input")


## Profling ##
os.chdir("../profiling/")
os.system("mkdir Result")
os.system("rm Result/*")

proc = subprocess.Popen(["python", "runProfiling.py", inputArgs ], stdout=subprocess.PIPE, shell=False)
proc.communicate()

print("###### Profiling done #####")
# Now move Results to calc SDC score
tempBuffer = "exec_count_" + inputArgs.replace(" ", "_") + ".txt"
os.system("rm ../sdc-score-calc/Input/exec_count_* ")


os.system("mv " + "Result/" + tempBuffer + " ../sdc-score-calc/Input/")



## SDC Score Calculation ##
os.chdir("../sdc-score-calc/")
os.system("rm Result/*")
tempBuffer = "exec_count_" + inputArgs.replace(" ", "_") + ".txt"
tempBuffer = "python calcSdcScore.py \"" + inputArgs + "\" " + "Input/" + tempBuffer
os.system(tempBuffer)
os.system("rm Input/exec_count_*")

## Now move Result to run GA
tempBuffer = "Result/SDC_score_" + inputArgs.replace(" ", "_") + ".txt"
os.system("rm ../fitness-function/Input/* ")
os.system("mv " + tempBuffer + " ../fitness-function/Input/")
tempBuffer = "Result/dynamic_footprint_" + inputArgs.replace(" ", "_") + ".txt"
os.system("mv " + tempBuffer + " ../fitness-function/dynamic_footprint.txt")

## Genetic Algorithm ##
os.chdir("../fitness-function/")

os.system("mkdir Result")
os.system("rm Result/*")
tempBuffer = "Input/SDC_score_" + inputArgs.replace(" ", "_") + ".txt"
outputFile = open("Result/fitnessScore.txt", 'w')
with open(tempBuffer, 'r') as f:
	fitnessScore = float(f.readline().strip().split(":")[1])
	outputFile.write("%.8f\n"%(fitnessScore))
outputFile.close()

os.system("rm Input/SDC_score_*")
os.system("mv dynamic_footprint.txt Result/")	
