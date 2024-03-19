from numpy import arange,zeros
matrix=zeros((5,5))
# print(arange(0,5))
for line in range(len(matrix)):
    matrix[line]=arange(0,5)
print(matrix)