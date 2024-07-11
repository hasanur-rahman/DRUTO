import sys, os, subprocess

inputArgs = str(sys.argv[1])
inpFilePath = str(sys.argv[2])

execMap = dict()

# EXEC_INFO staticIndex: 94, threadIndex: 132
with open(inpFilePath, 'r') as f:
	lines = f.readlines()

	for line in lines:
		filtered_line = str(line.strip())
		if "EXEC_INFO" in filtered_line:
			print(filtered_line)
			staticInst = int(filtered_line.split(",")[0].split(":")[1])
			threadInst = long(filtered_line.split(",")[1].split(":")[1])
			if execMap.has_key(threadInst):
				insideMap = execMap[threadInst]
				
				curCount = insideMap.get(staticInst, 0)
				execMap[threadInst][staticInst] = curCount + 1
			else:
				execMap[threadInst] = dict()
				execMap[threadInst][staticInst] = 1



os.system("mkdir Result")
tempBuffer = "Result/exec_count_" + str(inputArgs.replace(" ", "_")) + ".txt"
os.system("rm " + tempBuffer)
outFilePath = open(tempBuffer, "a")
for threadIndex in execMap.keys():
	insideMap = execMap[threadIndex]
	for staticInst, execCount in insideMap.items():
		buf = str(threadIndex) + ":" + str(staticInst) + ":" + str(execCount) + "\n"
		outFilePath.write(buf)


outFilePath.close()
