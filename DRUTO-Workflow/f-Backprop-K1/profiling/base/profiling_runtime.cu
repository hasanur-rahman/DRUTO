#include <stdio.h>
#include <cuda.h>

const long long MAX_THREAD_NUMBER = 1000000;
__device__ unsigned long long counterArray[MAX_THREAD_NUMBER] = {0};
__device__ unsigned long long counterArraySecond[MAX_THREAD_NUMBER] = {0};


extern "C" __device__ void bambooProfile(long bambooIndex)
{
	int blockId = blockIdx.x 
		+ blockIdx.y * gridDim.x 
		+ gridDim.x * gridDim.y * blockIdx.z; 
	long long index = blockId * (blockDim.x * blockDim.y * blockDim.z)
		+ (threadIdx.z * (blockDim.x * blockDim.y))
		+ (threadIdx.y * blockDim.x)
		+ threadIdx.x;

	//printf("profiling: %lld\n", index);

	if (counterArray[MAX_THREAD_NUMBER - 1] < index) {
		counterArray[MAX_THREAD_NUMBER - 1] = index;
	}
	if (index < MAX_THREAD_NUMBER - 1LL)
		counterArray[index]++;
	else {
		if  (index < MAX_THREAD_NUMBER * 2 - 1LL)
			counterArraySecond[index - MAX_THREAD_NUMBER - 1LL]++;

	}
	//atomicAdd(&counterArray[index], 1ULL);
}
