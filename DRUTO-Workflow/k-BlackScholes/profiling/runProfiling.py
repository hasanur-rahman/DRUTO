import os, sys

####
bmName = "blackscholes"
####

curInputArgs = str(sys.argv[1])

os.system("mkdir Result")
os.system("cp -r base/* .")

profileOpen = open("profile.py", 'r')
profileCont = profileOpen.read()
profileOpen.close()

profileOpen = open("profile.py", 'w')
profileOpen.write(profileCont.replace("XXXXXXX", str(curInputArgs)))
profileOpen.close()

os.system("python profile.py")
os.system("mv Result/exec_count.txt Result/exec_count_" + str(curInputArgs.replace(" ", "_")) + ".txt")

#profileOpen = open("profile.py", 'r')
#profileCont = profileOpen.read()
#profileOpen.close()
#
#profileOpen = open("profile.py", 'w')
#profileOpen.write(profileCont.replace("\"" + str(curInputArgs) + "\"", "XXXXXXX"))
#profileOpen.close()

os.system("rm -r profile.py header src " + bmName + "*")

os.system("rm *.cu *.cuh *.cpp")
