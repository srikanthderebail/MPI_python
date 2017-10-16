#!/usr/bin/env python
import numpy as np
from mpi4py import MPI

# This is to create default communicator and get the rank
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Let us just tell each processor to print its rank
print('Hello there, I am processor ',rank)












