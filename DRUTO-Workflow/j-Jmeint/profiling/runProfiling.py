import os, sys

####
bmName = "jmeint"
####

curInputArgs = str(sys.argv[1])

os.system("mkdir Result")
os.system("cp -r base/* .")

os.chdir("inputGen")
os.system("python data_generator.py " + curInputArgs)
os.system("mv locations_" + curInputArgs + ".data " + "../")
os.chdir("../")

profileOpen = open("profile.py", 'r')
profileCont = profileOpen.read()
profileOpen.close()

profileOpen = open("profile.py", 'w')
profileOpen.write(profileCont.replace("XXXXXXX", "\"" + "locations_" + curInputArgs + ".data " + "\""))
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

os.system("rm -r profile.py header src " + bmName + ".*")
os.system("rm locations_" +  curInputArgs + ".data")
## Get input list
#fileOpen = open("inputs.txt", 'r')
#rawInpList = fileOpen.read().split('\n')
#if(rawInpList[-1] == ''):
#    rawInpList = rawInpList[:-1]
#fileOpen.close()
#inpList = []
#for item in rawInpList:
#    tempList = []
#    tempList.append(item)
#    tempList.append(item.replace(' ', '-'))
#    inpList.append(tempList)
## Test Case: inpList = [["1000 10 20", "1000-10-20"]]
#
## Generate FI base for each input
#for item in inpList:
#    os.system("cp -r fi-base " + item[1])
#    os.chdir(item[1])
#    # Update profile.py
#    profileOpen = open("profile.py", 'r')
#    profileCont = profileOpen.read()
#    profileOpen.close()
#    profileOpen = open("profile.py", 'w')
#    profileOpen.write(profileCont.replace("XXXXXXX", item[0]))
#    profileOpen.close()
#    # Update inject.py
#    injectOpen = open("inject.py", 'r')
#    injectCont = injectOpen.read()
#    injectOpen.close()
#    injectOpen = open("inject.py", 'w')
#    injectOpen.write(injectCont.replace("XXXXXXX", item[0]).replace("YAFAN", totalFiNum))
#    injectOpen.close()
#    os.chdir("../")
