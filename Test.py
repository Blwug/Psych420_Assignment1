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




#Comments
#using an eval function, however, that is bad coding practice
    #using a def f(x): return (x**3) - this works && yields the same results as
    #using f = lambda x: x**3 i still don't know the instance why you would use one
    #over the other
    #this time we'll try using the import numpy as np so we have to redo the entire code
    #newtons method helps apporx 0 that's close to the actual 0 & use iterations
    #each time you do it, it gets closer
    #next method we try doing the point slope form which is similar to how the prof
    #showed how he did it
    #either way we decided to just do it with what  we are comfortable with
    #the video that we tried using which explained newtons, organic chemistry does not fit for this instance
    #the methods I tried consited of Newton Raphson method & bisection model, however, I
    #could not get the result I was looking for

#first we'll make a descriptor towards making the program & setting the parameters
#we'll try using bisection hybrid model we'll see if it works
#bi section tries to set a range that contains a root  f(a) <0 & f(b) > 0
#f(a) & f(b) have different signs (+/-)
#we only know the value - the midpoint c = a+b/2
#if f(c)>0 then no roots but a-c have different signs than there's a root within that sign
#d = a+c/2 f(d)<0 therefore it contains at least 1 root - we keep doing this to reach the
#actual root of the problem for f(x) to approach 0 - bisection method
#inequality of f(a) *f(b) < 0
#f(c) given c = a+b/2 - midpoint
#if f(c) is close to 0, then we accept c - if f(c) = 0 then there's a solution 10**-20 then done
#else if f(a) * f(c)> then a= c else if f(b)* f(c) >0 then b = c && just keep repeaitng to have it get to a closer solution
#we'll use the fibonacci series equation of x^2 - x - 1 = 0
# golden ratio = 1+ square root 5/2
#f(x) = 0
