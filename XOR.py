import matplotlib.pyplot as plt
a = (0,1), (1,0)
b = (1,1),( 0,0)

plt.scatter(a,b)
plt.scatter(b,a)

plt.show()

'''
(x1,x2)
OR gate requires either of X1 or X2 to be 1 to return a 1
(0,0) returns 0 
(0,1) returns 1
(1,0) returns 1 
(1,1) returns 1 
NAND gate requires X1 and X2 to not be the same value to return 1
(0,0) returns 1
(0,1) returns 1 
(1,0) returns 1
(1,1) returns 0 
AND gate requires X1 and X2 to be both the same value to return 1
 (0,0) returns 0
(0,1) returns 0
(1,0) returns 0
(1,1) returns 1 
XOR gate requires X1 and X2 to be mutually exclusive to return 1
 (0,0) returns 0
(0,1) returns 1
(1,0) returns 1
(1,1) returns 0 

Determining the value of the output requires the inner layer
values to be multiplied with that of the hidden layer, the perceptron.
Every perceptron is the product of the summation of the inner_layer
multiplied by their weights  and the bias, a constant value, is added 
afterwards. After the perceptron gets their value, the value of the 
perceptron is either a 1 if the product is greater than the threshold else
the threshold value is returned a 0. Next, the value of the perceptrons 
are multiplied with the other perceptron products to determine the 
final value, the output. 

'''







