Preliminary Fault Injection Study
=====

* This directory contains automated scripts to perform fault injection into each GPU application kernel with LLFI-GPU. Please refer to LLFI-GPU [repo](https://github.com/DependableSystemsLab/LLFI-GPU) for more details.
* Also, the fault injection scripts in the folder can be used to evaluate our baseline *Random*.

## How To Conduct Fault Injection
1. Install LLFI-GPU.
2. Copy specified application cuda (`.cu`) and header files into `fi-base` folder. Also, copy `inputs.txt` file and input generation scripts (if any) to conduct fault injection under your chosen inputs.
3. You still need to modify `fi-base` folder files according to the specific application.
4. Populate `inputs.txt` according to the application input arguments. Note that some applications such as BFS takes text-based inputs instead of numerical inputs. You can find the scripts to generate text-based inputs in the corresponding application folder.
5. Run `0-genBase.py` with desired number of fault injection trials. For example, `python 0-genBase.py 1000` .
6. Run `1-runFi-multiple.py` to inject faults for the specified inputs. For example, `python 1-runFi-multiple.py` .
7. To measure the rate of different failure outcomes (sdc, crash/hang, benign), run `2-measure.py <inputs.txt path> <number of injected faults>`. For example, `python 2-measure.py inputs.txt 1000`


## Note
* Please follow the guidelines of each application benchmark suites for input generation.
* The fault injection code is directly adopted from LLFI-GPU: https://github.com/DependableSystemsLab/LLFI-GPU .
