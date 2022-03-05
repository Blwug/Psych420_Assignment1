import numpy as np
#a = np.ones((3,2))
x1 = [5]
x2 = [4]
x3 = [7]
weight_1 = [-0.3]
weight_2 = [0.6]
bias = 5.0

inner_layer = np.array([x1,x2,x3])

hidden_layer_weight = np.array([weight_1, weight_2]) #print(hidden_layer_bias)
hidden_layer_weight = np.reshape(hidden_layer_weight, 2) #print(hidden_layer_bias)


inner_hidden_dot_product_1 = np.zeros((1,2))

#for i in range (len(inner_layer)):
   #for j in range (len(hidden_layer_weight)):
        #inner_hidden_dot_product_1 = inner_layer[i][j] * hidden_layer_weight[j][i]

inner_hidden_dot_product_1 = inner_layer * hidden_layer_weight + bias


print(inner_hidden_dot_product_1)



#counts number of instance the code occurs

#for i in range(len(inner_layer)):
    #for j in range(len(hidden_layer_bias)):



#print(inner_hidden_dot_product_1)
#print(inner_hidden_dot_product_2)
#print(inner_layer)
#print (hidden_layer_bias)
