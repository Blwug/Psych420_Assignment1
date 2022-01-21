import math

def func(x):
    return (x ** n)
    #nth root formula

def dfunc(x):
    return (n * x ** (n-1))
    #power rule


const_tol = .001
#tolerence

def originalvalue(goal, x0, n):
#x0 = initial guess from the user
#goal  = the number we are trying to find the root for
#n = nth root of the goal
    #goal^1/n
    iteration = 1

    while True:
        f = func(x0)
        f_d = dfunc(x0)

        x1 = (goal - f) / f_d

        #the formula xn+1 based on the Newton's Raphson method.

        print("x_{} = {}".format(iteration, x0))
        x0 = x1 + x0

        #the updated value of the initial guess

        iteration = iteration +1
        #this helps the program remember the number of instance the function occured

        if ((x0* x1)**2)/ abs(x0 - x1) < const_tol:

            #this function stops a repeating output &
                #ie: x_5 = 2, x_6 = 2 will not occur
            break
        elif iteration == 30:
            break
       # after 30 instance of the program, the program stops

goal = float(input("please enter the goal "))
x0 = float(input("please enter your guess "))

n = float(input("please enter the root you are trying to find "))

originalvalue(goal, x0, n)

#if goal =16, guess= 5, n = 4, then x_6 = ~~2.0033

