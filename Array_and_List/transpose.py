A = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3],
     [4,4,4,4]]

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j])
    print(row)
