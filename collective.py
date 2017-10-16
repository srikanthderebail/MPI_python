#!/usr/bin/env python
import numpy as np
from mpi4py import MPI


def main():
    # This is to create default communicator and get the rank
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    #Let us try to broadcast a numpy array to all processes
    if rank == 1:
        array = np.ones((5,5))
    else:
        array = None
    array = comm.bcast(array,root=1)

    comm.Barrier()

    # Similarly we can scatter an array or gather pieces of arrays
    if rank == 1:
        arraytoscatter =np.array([0,1,2,3])
    else:
        arraytoscatter = None
    chunkrec = comm.scatter(arraytoscatter,root=1)
    print('Processor ',rank,' received ',chunkrec)

    comm.Barrier()

    #Now let us try to gather all the chunks back in proc 0
    arraytoscatter = comm.gather(chunkrec,root=0)
    if rank == 0:
        print('Processor ',rank,' received: ',arraytoscatter)

    # Let us try all to all which in a sense transposes your matrix
    A = rank*np.ones((4,1))
    B  = np.zeros((4,1))
    comm.Alltoall(A,B)
    print('Processor ',rank,' sent ',A)
    print('Processor ',rank,' received ',B)



if __name__ == "__main__" :
    main()

