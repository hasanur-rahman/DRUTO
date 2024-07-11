import os, sys

totalFiNum = sys.argv[1]

# Get input list
fileOpen = open("inputs.txt", 'r')
rawInpList = fileOpen.read().split('\n')
if(rawInpList[-1] == ''):
    rawInpList = rawInpList[:-1]
fileOpen.close()
inpList = []
for item in rawInpList:
    tempList = []
    tempList.append(item)
    tempList.append(item.replace(' ', '-'))
    inpList.append(tempList)

# Generate FI base for each input
for item in inpList:
    os.system("cp -r fi-base " + item[1])
    os.chdir(item[1])
    # Update profile.py
    profileOpen = open("profile.py", 'r')
    profileCont = profileOpen.read()
    profileOpen.close()
    profileOpen = open("profile.py", 'w')
    profileOpen.write(profileCont.replace("XXXXXXX", item[0]))
    profileOpen.close()
    # Update inject.py
    injectOpen = open("inject.py", 'r')
    injectCont = injectOpen.read()
    injectOpen.close()
    injectOpen = open("inject.py", 'w')
    injectOpen.write(injectCont.replace("XXXXXXX", item[0]).replace("FOO", totalFiNum))
    injectOpen.close()
    os.chdir("../")