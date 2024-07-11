import os, sys

inputFirstArgs = str(sys.argv[1])
inputSecondArgs = str(sys.argv[2])

profileOpen = open("header.cuh", 'r')
profileCont = profileOpen.read()
profileOpen.close()
profileOpen = open("2DConvolution.cuh", 'w')
profileOpen.write(profileCont.replace("XXXXXX", inputFirstArgs).replace("YYYYYY", inputSecondArgs))
profileOpen.close()

