import math

def functionOriginal(x):
    f = 3*x**2 - 16
    return f

def functionDerived(x):
    f_d = 6*x
    return f_d

def runMethod (x_0):
    iteration = 1
    while True:
        f = functionOriginal(x_0)
        f_d = functionDerived(x_0)
        x_next = x_0 - (f/f_d)

        print ("x_{} = {}".format(iteration, x_next))
        if iteration == 5:
            break
        x_0 = x_next
        iteration = iteration +1

runMethod(10)

