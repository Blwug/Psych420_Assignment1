import math

def functionOriginal(x):
    f = x**1/4
    return f

def functionDerived(x):
    f_d = 4*x**3
    return f_d
#used the power rule
def originalvalue (x_0):
    iteration = 1
    while True:
        f = functionOriginal(x_0)
        f_d = functionDerived(x_0)
        #defining the function allows x to be x_0 within the equation

        x_next = x_0 - (f/f_d)
        print ("x_{} = {}".format(iteration, x_next))
        x_0 = x_next
        # this is the update method, the initial value of x0 gets updated to be x_next
        # x_next uses newton formula of xn+1 = xn -f(xn)/f`(xn)

        iteration = iteration +1

        if iteration == 10:
            #breaks after n number of the loop running
            break

originalvalue(3)