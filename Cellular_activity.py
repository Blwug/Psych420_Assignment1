import numpy as np
#a = np.ones((3,2))
x1 = [5]
x2 = [4]
x3 = [7]
bias_1 = [-0.3]
bias_2 = [0.6]

inner_layer = np.array([x1,x2,x3])

hidden_layer_bias = np.array([bias_1, bias_2]) #print(hidden_layer_bias)
hidden_layer_bias = np.reshape(hidden_layer_bias, 2) #print(hidden_layer_bias)


inner_hidden_dot_product_1 = np.zeros((1,2))

for i in range (len(inner_layer)):
   for j in range (len(hidden_layer_bias)):
        inner_hidden_dot_product_1 = inner_layer[i][j] * hidden_layer_bias[j][i]

#inner_hidden_dot_product_1 = inner_layer * hidden_layer_bias


print(inner_hidden_dot_product_1)



#counts number of instance the code occurs

#for i in range(len(inner_layer)):
    #for j in range(len(hidden_layer_bias)):



#print(inner_hidden_dot_product_1)
#print(inner_hidden_dot_product_2)
#print(inner_layer)
#print (hidden_layer_bias)
