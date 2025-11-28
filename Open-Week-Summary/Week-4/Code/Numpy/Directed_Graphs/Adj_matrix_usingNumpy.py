#Adjacency Matrix Using Numpy Implementation
V = [0,1,2,3,4]
E = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 3), (3, 4)] # each of the tuples represent a edge from v1 to v2 for example 0-->1,0-->2

size=len(V)
import numpy as np
AMat = np.zeros(shape=(size,size))
for(i,j) in E:
    AMat[i,j] = 1 # mark 1 if edge is found or present in graph from i to j, else 0 for example 0 --> 1 = 1, 0 --> 5 = 0
print(AMat)
# this print a matrix with allocation as vertices as x axis and also vertices as y axis