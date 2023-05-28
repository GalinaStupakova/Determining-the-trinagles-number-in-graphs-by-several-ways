import timeit 
code_to_test = '''
import snap
G2 = snap.GenRndGnm(snap.TUNGraph, 3000, 3000)
count = 0
for i in range(3000):
	for j in range(i+1, 3001):
		for k in range(j+1, 3001):
			if G2.IsEdge(i, j) == True and G2.IsEdge(j, k) == True and G2.IsEdge(k, i) == True:
				count +=1 
print(count)	'''		
elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)