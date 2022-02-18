#Provide a program in the language of your choice that implements matrix multiplication
# and demonstrates the non-commutativity of matrix multiplication. Probably useful to also
# know how to multiply a vector and a matrix to each other.

#chain of left most bracket stop when it reaches the one dimension
#2 dimension collection of 1D and is encased by 2 left bracket
import numpy as np

a1= [[1, 3,3], [2,2,4]]
a2= [[1, 2,3], [3,4,5]]

a1_a2 = np.zeros([2,3])
a2_a1 = np.zeros([2,3])
for i in range(len(a1)):
    for j in range (len(a2)):
        a1_a2[i][j] += a1[i][j] * a2[j][i]

for x in range(len(a2)):
    for y in range(len(a1)):
        a2_a1[x][y] += a2[x][y] * a1[y][x]

print (a1_a2)
print (a2_a1)
print("a1*a2 != a2 * a1")

