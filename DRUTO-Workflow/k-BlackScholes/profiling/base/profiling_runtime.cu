#include <stdio.h>
#include <cuda.h>

const long long MAX_THREAD_NUMBER = 1000000;
__device__ unsigned long long counterArray[MAX_THREAD_NUMBER] = {0}; // this contains the execution count of a thread that is less than 10^6
__device__ unsigned long long counterArraySecond[MAX_THREAD_NUMBER] = {0}; // this contains the execution count of a thread that is greater than 10^6


extern "C" __device__ void bambooProfile(long bambooIndex) // is called when an instruction (bambooIndex) is executed
{
	int blockId = blockIdx.x 
		+ blockIdx.y * gridDim.x 
		+ gridDim.x * gridDim.y * blockIdx.z; 
	long long index = blockId * (blockDim.x * blockDim.y * blockDim.z)
		+ (threadIdx.z * (blockDim.x * blockDim.y))
		+ (threadIdx.y * blockDim.x)
		+ threadIdx.x; // index means threadIdx

	//printf("profiling: %lld\n", index);

	if (counterArray[MAX_THREAD_NUMBER - 1] < index) {
		counterArray[MAX_THREAD_NUMBER - 1] = index;
	}
	if (index < MAX_THREAD_NUMBER - 1LL)
		counterArray[index]++; // saving the current execution count of current thread
	else {
		if  (index < MAX_THREAD_NUMBER * 2 - 1LL)
			counterArraySecond[index - MAX_THREAD_NUMBER - 1LL]++; // saving the current execution count of current thread

	}
	//atomicAdd(&counterArray[index], 1ULL);
}
