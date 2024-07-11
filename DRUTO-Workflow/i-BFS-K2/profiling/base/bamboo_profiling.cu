#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cuda.h>

#include <cuda_runtime.h>
#include <cuda.h>
#include <device_launch_parameters.h>

const long long MAX_THREAD_NUMBER = 1000000;
extern "C" __device__ unsigned long long counterArray[MAX_THREAD_NUMBER], counterArraySecond[MAX_THREAD_NUMBER];

long long dynamicKernelIndex = 0;
int targetStaticKernelIndex = 1;

void bambooLogKernelBegin(int staticKernelIndex) {
	
}

void bambooLogKernelEnd(int staticKernelIndex) {

#ifdef KERNELTRACE
	cudaDeviceSynchronize();
#endif

	
	unsigned long long resultArray[MAX_THREAD_NUMBER] = {0};
	if (dynamicKernelIndex > 0) {
		exit(0);
	}

	if ((staticKernelIndex != targetStaticKernelIndex)){
		cudaMemcpyToSymbol(counterArray, &resultArray, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyHostToDevice);
		cudaMemcpyToSymbol(counterArraySecond, &resultArray, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyHostToDevice);
		return;
	}

	//unsigned long long secResultArray[MAX_THREAD_NUMBER] = {0};
	cudaMemcpyFromSymbol(&resultArray, counterArray, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyDeviceToHost);
	//cudaMemcpyFromSymbol(&resultArraySec, counterArraySecond, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyDeviceToHost);	

	FILE *profileFile = fopen("Result/exec_count.txt", "a");
	fclose(profileFile);
	profileFile = fopen("Result/exec_count.txt", "a");
	for(long long i=0; i<MAX_THREAD_NUMBER-1LL; i++){
		if(resultArray[i] > 0){
			//printf(" -- index %lld -- counter %lld --\n", i, resultArray[i]);
			//FILE *profileFile = fopen("Result/exec_count.txt", "a");
			fprintf(profileFile, "%lld: %llu\n", i, resultArray[i]);
			//if (resultArraySec[i] > 0) 
			//	fprintf(profileFile, "%lld: %llu\n", i+MAX_THREAD_NUMBER, resultArraySec[i]);
			//fclose(profileFile);
		}
		
	}
	fclose(profileFile);

	
	if (resultArray[MAX_THREAD_NUMBER-1LL] > MAX_THREAD_NUMBER-2LL){
		profileFile = fopen("Result/exec_count.txt", "a");
		memset(resultArray, 0, sizeof(resultArray));
		cudaMemcpyFromSymbol(&resultArray, counterArraySecond, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyDeviceToHost);
		for(long long i=0; i<MAX_THREAD_NUMBER; i++){
			if(resultArray[i] > 0){
				//printf(" -- index %lld -- counter %lld --\n", i, resultArray[i]);
				//FILE *profileFile = fopen("Result/exec_count.txt", "a");
				fprintf(profileFile, "%lld: %llu\n", i + MAX_THREAD_NUMBER - 1LL, resultArray[i]);
				//if (resultArraySec[i] > 0) 
				//	fprintf(profileFile, "%lld: %llu\n", i+MAX_THREAD_NUMBER, resultArraySec[i]);
				//fclose(profileFile);
			}
			
		}
		fclose(profileFile);
	}

	
//	cudaMemcpyToSymbol(counterArray, &resultArray, MAX_THREAD_NUMBER * sizeof(unsigned long long), 0, cudaMemcpyHostToDevice);
	dynamicKernelIndex++;
	
}
