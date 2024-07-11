import os, sys

inputFirstArgs = str(sys.argv[1])
inputSecondArgs = str(sys.argv[2])
inputThirdArgs = str(sys.argv[3])

profileOpen = open("header.cuh", 'r')
profileCont = profileOpen.read()
profileOpen.close()
profileOpen = open("gemm.cuh", 'w')
profileOpen.write(profileCont.replace("XXXXXX", inputFirstArgs).replace("YYYYYY", inputSecondArgs).replace("ZZZZZZ", inputThirdArgs))
profileOpen.close()

