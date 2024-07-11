import os, sys

curInputArgs = str(sys.argv[1])

profileOpen = open("header.cuh", 'r')
profileCont = profileOpen.read()
profileOpen.close()
profileOpen = open("mvt.cuh", 'w')
profileOpen.write(profileCont.replace("YYYYYY", curInputArgs))
profileOpen.close()

