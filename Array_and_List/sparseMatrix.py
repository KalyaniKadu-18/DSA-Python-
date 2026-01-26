def displayMatrix(matrix):
    for row in matrix:
        for element in row:          
            print(element, end=" ")  
        print()

def convertToSparseMatrix(matrix):  
    sparseMatrix = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                temp = []
                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)               
    return sparseMatrix                                 

matrix = [[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,4]]

displayMatrix(matrix)

print("\nSparse Matrix : ")
result = convertToSparseMatrix(matrix)
for i in result:
    print(i)
