import os, sys

####
bmName = "gemm"
####

curInputArgs = str(sys.argv[1])

os.system("mkdir Result")
os.system("cp -r base/* .")

os.chdir("inputGen")
os.system("python inputsizeGenerator.py " + str(curInputArgs.split(" ")[0]) + " " + str(curInputArgs.split(" ")[1]) + " " + str(curInputArgs.split(" ")[2]))
os.system("mv gemm.cuh " + "../")
os.chdir("../")

profileOpen = open("profile.py", 'r')
profileCont = profileOpen.read()
profileOpen.close()

profileOpen = open("profile.py", 'w')
profileOpen.write(profileCont.replace("XXXXXXX", curInputArgs))
profileOpen.close()


os.system("python profile.py")
os.system("mv Result/exec_count.txt Result/exec_count_" + str(curInputArgs.replace(" ", "_")) + ".txt")


os.system("rm -r profile.py header output.txt src " + bmName + "*")
os.system("rm *.cu *.cuh polybench*")

