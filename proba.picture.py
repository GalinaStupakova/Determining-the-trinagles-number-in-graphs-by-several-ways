import snap
import numpy as np
z = []
count = 0
G1 = snap.TNGraph.New()
G1.AddNode(1)
G1.AddNode(2)
G1.AddNode(3)
G1.AddNode(4)
G1.AddNode(5)
rows, cols = 5, 5           # rows - количество строк, cols - количество столбцов
matrix = [[0]*5 for _ in range(5)]    # создаем квадратную матрицу размером 5 на 5
G1.AddEdge(1,2)
matrix[0][1] = 1
matrix[1][0] = 1
G1.AddEdge(2,3)
matrix[1][2] = 1
matrix[2][1] = 1
G1.AddEdge(3,4)
matrix[2][3] = 1
matrix[3][2] = 1
G1.AddEdge(4,5)
matrix[3][4] = 1
matrix[4][3] = 1
G1.AddEdge(1,5)
matrix[4][0] = 1
matrix[0][4] = 1
G1.AddEdge(1,3)
matrix[0][2] = 1
matrix[2][0] = 1
G1.AddEdge(1,4)
matrix[0][3] = 1
matrix[3][0] = 1
