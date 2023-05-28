import snap
import numpy as np
G2 = snap.GenRndGnm(snap.TNGraph, 6, 6)
num_nodes = G2.GetNodes()
matrix = [[0]*num_nodes for _ in range(num_nodes)]    # создаем квадратную матрицу размером 10 на 10
for EI in G2.Edges():
	matrix[EI.GetSrcNId()][EI.GetDstNId()] = 1
	matrix[EI.GetDstNId()][EI.GetSrcNId()]= 1
for EI in G2.Edges():
    print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))
b = np.triu(matrix)
d = np.linalg.matrix_power(b, 2)
c=np.bitwise_and(d, b)
print(np.sum(c))
