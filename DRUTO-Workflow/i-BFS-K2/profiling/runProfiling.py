import os, sys

####
bmName = "bfs"
####

curInputArgs = str(sys.argv[1])

os.system("mkdir Result")
os.system("cp -r base/* .")

os.chdir("inputGen")
os.system("./gen_dataset.sh " + curInputArgs)
os.system("mv graph" + curInputArgs + ".txt " + "../")
os.chdir("../")

profileOpen = open("profile.py", 'r')
profileCont = profileOpen.read()
profileOpen.close()

profileOpen = open("profile.py", 'w')
profileOpen.write(profileCont.replace("XXXXXXX", "\"" + "graph" + curInputArgs + ".txt " + "\""))
profileOpen.close()

os.system("python profile.py")
os.system("mv Result/exec_count.txt Result/exec_count_" + str(curInputArgs.replace(" ", "_")) + ".txt")
os.system("rm graph" + curInputArgs + ".txt")


os.system("rm -r profile.py header src kernel.cu kernel2.cu " + bmName + "*")

