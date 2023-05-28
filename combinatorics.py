import snap
G2 = snap.GenRndGnm(snap.TUNGraph, 10, 10)
count = 0
for i in range(10):
    for j in range(i+1, 11):
        for k in range(j+1, 11):
            if G2.IsEdge(i, j) == True and G2.IsEdge(j, k) == True and G2.IsEdge(k, i) == True:
                count +=1 
print(count)