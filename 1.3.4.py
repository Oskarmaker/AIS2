from numpy import zeros
matrix=zeros((10,10))
l1,l2=10,10
for line in range(l1):
    for row in range(l2):
        if line%(l1-1)*row%(l2-1)==0:
            matrix[line][row]=1
        # print(line%(l1-1),row%(l2-1))
print(matrix)