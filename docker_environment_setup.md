The steps to setup the experiment environment are as follows:

- docker pull ubuntu:14.04
- docker run --name DRUTO_EXEC_14_04 --gpus all -dti ubuntu:14.04 /bin/bash
- docker exec -ti DRUTO_EXEC_14_04 /bin/bash
- cd root
- sudo apt-get update
- sudo apt-get install build-essential
- sudo apt-get install wget
- wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1204/x86_64/cuda-repo-ubuntu1204_6.0-37_amd64.deb
- sudo apt-get install cuda-6-0
- export PATH=$PATH:/usr/local/cuda/bin
- source ~/.bashrc
- nvcc --version
- gcc --version
- mkdir llvm3.0
- cd llvm3.0/
- wget https://releases.llvm.org/3.0/llvm-3.0.tar.gz
- tar -xvf llvm-3.0.tar.gz
- wget https://releases.llvm.org/3.0/clang-3.0.tar.gz
- tar -xvf clang-3.0.tar.gz
- mv clang-3.0.src llvm-3.0.src/tools/clang
- mv llvm-3.0.src llvm-3.0
- ./configure --enable-optimized --disable-assertions --enable-targets=host --with-python="/usr/bin/python2"
make -j8
- export PATH=$PATH:/root/llvm3.0/llvm-3.0/Release/bin

