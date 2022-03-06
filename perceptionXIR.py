import numpy as np

#alright, let's break down what we have to do

#make an array for x1,x2
x1 = [2,1]
x2 = [3,2]
bias = 0.3
x1.append(bias)
x2.append(bias)
hidden_layer = np.zeros([2,2])
# this is hidden layer [[0. 0.] [0. 0.]]

#have 2 bias, one value, and have that multiply with x1 and x2
#after that add those values up to get a total
for i in range(len(x1)):
    for j in range(len(x2)):
        hidden_layer = x1[i][j] * x2[j][i]

print (hidden_layer)


#set a threshold and if the value passes the threshold, then we change that value
#to 1 else if it does not then we assign that value 0


#have a threshold


#for i in range(len(a1)):
 #  for j in range (len(a2)):
  #      a1_a2[i][j] += a1[i][j] * a2[j][i]

#for x in range(len(a2)):
 #   for y in range(len(a1)):
  #      a2_a1[x][y] += a2[x][y] * a1[y][x]
#XOR where if only one is true then 1 else if TT or FF then 0
#multi layered perception has an output layer, input and a perception (hidden layer)
#hidden and output is a 2 layer network
#hidden uses a weighted sum since each input connects to hidden which then connects to output
#each connection has a weight
#if 3 inputs and 2 hidden then 6 weights
#matrix just gathers the connection made with the input vector and the hidden
#h1 (x1,x2,x3) h2 (x1,x2,x3)
#hidden is weighted sum of summation (input * weight)
#weight1_1 *x1 + w1_2 * x2 +w1_3 * x3 | this is the matrix product (weighted sum)
#weight2_1 *x1 + w2_2 + w2 + w2_3 + w3
#row * column

#sigmold = f(x) = 1/1+ e**-x

#i = column vector
# = hidden i = Wij * Ii + biasi
# positive number = 1, negative = -1
#bias is the threshold but

#sigmoid takes any value uses a range of 0,1 & the bias pushes it to 1 or -1
#iterating over i because i multiples each row of x,
#inputs goes in add the bias pass it to activation function and goes to the output
#output does the same process but uses the hidden layer product & + bias (!= bias for the input)

#add two matrix (element) and then perform matrix product and then we use the sigmoid function after
#adding the bias we can do that by appending b1 and b2 into the dot product of input and hidden
#we use the vector x1,x2,x3, if add bias, then append 1 so that when we do the summation, we add the bias within the product of input & hidden layer



#h1 h2 is the product of weighted sum


#weight  matrix is between input and hidden layer
#weight matrix is between hidden and output layer



