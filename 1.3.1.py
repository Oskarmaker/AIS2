from numpy import array,zeros
matrix=zeros((8,8))
for line in range(len(matrix)):
    for row in range(len(matrix[line])):
        matrix[line][row]=(line+row)%2
print(matrix)