import os, sys

####
bmName = "mvt"
####

curInputArgs = str(sys.argv[1])

os.system("mkdir Result")
os.system("cp -r base/* .")

os.chdir("inputGen")
os.system("python inputsizeGenerator.py " + curInputArgs)
os.system("mv mvt.cuh " + "../")
os.chdir("../")



profileOpen = open("profile.py", 'r')
profileCont = profileOpen.read()
profileOpen.close()

profileOpen = open("profile.py", 'w')
profileOpen.write(profileCont.replace("XXXXXXX", "\"" + str(curInputArgs) + "\""))
profileOpen.close()

os.system("python profile.py")
os.system("mv Result/exec_count.txt Result/exec_count_" + str(curInputArgs.replace(" ", "_")) + ".txt")


os.system("rm -r profile.py header src " + bmName + "*")

