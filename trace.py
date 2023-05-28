import snap
import numpy as np
G2 = snap.GenRndGnm(snap.TUNGraph, 10, 10)
matrix = [[0]*10 for _ in range(10)]    # создаем квадратную матрицу размером 10 на 10
for EI in G2.Edges():
	matrix[EI.GetSrcNId()][EI.GetDstNId()] = 1
	matrix[EI.GetDstNId()][EI.GetSrcNId()]= 1
a = np.linalg.matrix_power(matrix, 3)
b = np.trace(a)
print(b*(1/6))