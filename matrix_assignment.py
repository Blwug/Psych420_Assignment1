import numpy as np
a = 0
b = 1
c = 2
d = 3

m = 4
n = 5
o = 6
p = 7

matrix_1 = [a, b, c, d]
matrix_2 = [m, n, o, p]

#using a square matrix to prove a*b != b*a


am =np.dot(matrix_1[0],matrix_2[0])

cn = np.dot(matrix_1[2], matrix_2 [1])
ao = np.dot(matrix_1[0], matrix_2[2])
cp = np.dot(matrix_1[2], matrix_2[3])
bm = np.dot(matrix_1[1], matrix_2[0])
dn = np.dot(matrix_1[3], matrix_2[1])
bo = np.dot(matrix_1[1], matrix_2[2])
dp = np.dot(matrix_1 [3], matrix_2[3])

#below is b*a but have not done that yet
#ma = np.dot(matrix_1[0] *matrix_2[0])
#ob = np.dot(matrix_1[2] * matrix_2 [1])
#mc = np.dot(matrix_1[0] * matrix_2[2])
#od = np.dot(matrix_1[2] * matrix_2[3])
#na = np.dot(matrix_1[1] * matrix_2[0])
#pb = np.dot(matrix_1[3] * matrix_2[1])
#nc = np.dot(matrix_1[1] * matrix_2[2])
#pd = np.dot(matrix_1 [3] * matrix_2[3])
product_am_cn = am + cn
product_bm_dn = bm +dn
product_ao_cp = ao + cp
product_bo_dp = bo + dp
row_one_product_matrix_a_b = ([product_am_cn], [product_bm_dn])
row_two_product_matrix_a_b = ([product_ao_cp], [product_bo_dp])

print("This is the product of matrix_1 * matrix_2 " + str(row_one_product_matrix_a_b) + str(row_two_product_matrix_a_b))




















