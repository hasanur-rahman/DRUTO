import os, sys
from datetime import datetime

curInputArgs = str(sys.argv[1])
timeLogPath = str(sys.argv[2])

timeLogFile = open(timeLogPath, 'a')

# Get input list
prev_time = datetime.now()
os.system("python profile.py")
cur_time = datetime.now()
timeLogFile.write("Input: " + curInputArgs + ", Profiling time: " + str((cur_time - prev_time).total_seconds()) + "\n")

prev_time = datetime.now()
os.system("python inject.py")
cur_time = datetime.now()
timeLogFile.write("Input: " + curInputArgs + ", Fault Injection time: " + str((cur_time - prev_time).total_seconds()) + "\n")

timeLogFile.close() 
