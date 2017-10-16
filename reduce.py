#!/usr/bin/env python
import numpy as np
from mpi4py import MPI


def main():
    # This is to create default communicator and get the rank
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    
    
    
    # Let us compute the maximum of an array in parallel using reduce
    A = np.random.randn(10,1)
    #if rank == 0:
    maxallreduce = np.zeros((1,1))
    max = np.amax(A, axis =0)
    print('Reduce version: Process',rank,' has',max)

    comm.Reduce(max,maxallreduce,op=MPI.MAX,root=0)
    if rank ==0:
        print('Reduce version: Maximum of all arrays is ',maxallreduce)



    # Let us compute the maximum of an array in parallel using all reduce
    A = np.random.randn(10,1)
    max = np.amax(A, axis =0)
    print('AllReduce version: Process',rank,' has',max)

    maxall = np.zeros((1,1))
    comm.Allreduce(max,maxall,op=MPI.MAX)
    print('AllReduce version: Maximum of all arrays is ',maxall)



if __name__ == "__main__" :
    main()

