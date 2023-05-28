import snap
import numpy as np
from scipy.sparse import lil_matrix, triu
 
G = snap.LoadEdgeList(snap.PUNGraph, "Amazon0302.txt", 0, 1)
 
num_nodes = G.GetNodes()
 
# разреженная матрица с размерами, равными количеству вершин в графе
matrix = lil_matrix((num_nodes, num_nodes))
 
for EI in G.Edges():
    matrix[EI.GetSrcNId(), EI.GetDstNId()] = 1
    matrix[EI.GetDstNId(), EI.GetSrcNId()] = 1
 
# Возведите матрицу в куб, чтобы получить количество путей длиной 3 между каждой парой вершин
# Поскольку это требует много вычислений, используем `.tocsc()` для преобразования матрицы в другой формат, который более эффективен для этой операции
matrix = matrix.tocsc()
cubed_matrix = matrix**3
 
trace = cubed_matrix.diagonal().sum()
 
num_triangles = trace / 6
 
print(num_triangles)