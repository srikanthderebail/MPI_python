#!/usr/bin/env python
import numpy as np
from mpi4py import MPI


def main():
    # This is to create default communicator and get the rank
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Let us try a simple point to point send receive
    if rank == 0:
        data = 'This is a secret message'
        comm.send(data,dest=1,tag=11)
    elif rank == 1:
        data = comm.recv(source=0,tag=11)
        print('Received message: ',data,' from proc 0')

    comm.Barrier()

    # send recv are blocking routines. Use non-blocking versions
    if rank == 0:
        data = 'This is a secret message'
        req = comm.isend(data,dest=1,tag=11)
        # Let us say that there is some intermediate calculations
        A = np.random.randn(10,10)
        print('Norm of A is ',np.linalg.norm(A))
        req.wait()
    elif rank == 1:
        req = comm.irecv(source=0,tag=11)
        # Let us say that there is some intermediate calculations
        B = np.random.randn(10,10)
        print('Norm of B is ',np.linalg.norm(B))
        data = req.wait()
        print('Received message: ',data,' from proc 0')



if __name__ == "__main__" :
    main()

