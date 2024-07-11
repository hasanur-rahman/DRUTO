import os, sys
import filecmp

inpFilePath = str(sys.argv[1])
fiCount = int(sys.argv[2])

# Get input list
fileOpen = open(inpFilePath, 'r')
rawInpList = fileOpen.read().split('\n')
if(rawInpList[-1] == ''):
    rawInpList = rawInpList[:-1]
fileOpen.close()
inpList = []
for item in rawInpList:
    inpList.append(item.replace(' ', '-'))


# Mesuare SDC probability
for item in inpList:
    os.chdir(item)
    
    print("CURRENT INPUT: " + item)
    
    # set directory variables
    curdir = "."
    prog_output = curdir + "/bamboo_fi/prog_output"
    baseline = curdir + "/bamboo_fi/baseline"
    errdir = curdir + "/bamboo_fi/err_output"

    # read golden output from ./baseline/golden_std_output
    file_gld_out = baseline + "/output.txt"

    # read filenames from ./std_output
    fiInfoLogPath = curdir + "/bamboo_fi/bamboo.fi.log.txt" 
    run_count = 0
    with open(fiInfoLogPath, 'r') as f:
        run_count = len(f.readlines())

    if run_count > fiCount:
        run_count = fiCount
    #run_count = int(os.popen("ls " + prog_output + " | wc -l").read())

    # check for SDCs
    sdc_count = 0
    benign_count = 0
    crash_count = 0
    for f in range(1, run_count+1):
        file_out = prog_output + "/output.txt-" + str(f)
        try:
            file_err = open(errdir + "/err_output-" + str(f))
            error_msg = file_err.read()
            file_err.close()
        except IOError:   # no error output
            error_msg = ""
        if (error_msg != ""):
            crash_count += 1
        elif filecmp.cmp(file_out, file_gld_out):
            benign_count += 1
        else:
            sdc_count += 1

    # print results

    print ("SDC count     = " + str(sdc_count))
    print ("Crash count   = " + str(crash_count))
    print ("Benign count  = " + str(benign_count))
    print ("Total Fi runs = " + str(run_count))
    print ("SDC rate = " + "{:.8f}".format((100.0 * sdc_count) / (1.0 * run_count)))
    print ("\n")
    
    os.chdir("../")
