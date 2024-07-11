DRUTO: Upper-Bounding Silent Data Corruption Vulnerability in GPU Applications
=====

* Published in the 38th IEEE International Parallel & Distributed Processing Symposium (IPDPS), 2024. 
* Authors: Md Hasanur Rahman, Sheng Di, Shengjian Guo, Xiaoyi Lu, Guanpeng Li and Franck Cappello. 
* This project was done with the collaboration of Argonne National Laboratory, Amazon Web Services and UC Merced.
 
## Goal
The goal of the paper is to efficiently approximating the upper bound of SDC probability of GPU kernels. Please check our [paper](https://doi.org/10.1109/IPDPS57955.2024.00058) for more details.

## Experimental Setup

We use the same system setup as used in [LLFI-GPU](https://github.com/DependableSystemsLab/LLFI-GPU) for a fair evaluation. Specifically, we use LLVM3.0 and NVCC6.0 on a docker contained-based ubuntu machine. The steps to setup the environment are mentioned details in `docker_environment_setup.md` file. 


## Thanks
* We use open-source tools LLFI-GPU (https://github.com/DependableSystemsLab/LLFI-GPU) and GPU-Trident (https://github.com/DependableSystemsLab/GPU-Trident) for our experiments such as fault injection and case study. 
* We are grateful for open-source releases of PTX backends by [NVIDIA](https://llvm.org/docs/NVPTXUsage.html), which is well documented here: https://github.com/apc-llc/nvcc-llvm-ir.
* We also adopt some parts of these open-source codes to the benefits of our workflow design, especially to profile the cuda runtime information. 


## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)
