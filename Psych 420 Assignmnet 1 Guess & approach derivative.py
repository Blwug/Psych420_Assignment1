import math

def functionOriginal(x):
    return (x ** n)
   # return (x ** 4)

def functionDerived(x):
    return (n * x ** (n-1))
     #return (4 * x ** (4-1))

const_tol = .001

def originalvalue(goal, guess, n):

    iteration = 1

    while True:
        f = functionOriginal(guess)
        f_d = functionDerived(guess)

        error = (goal - f) / f_d
        print("x_{} = {}".format(iteration, guess))
        guess = error + guess
        iteration = iteration +1
        #this helps the program remember the number of instance the function occured
        if ((guess* error)**2)/ abs(guess - error) < const_tol:
            #this function stops a repeating output &
                #ie: x_5 = 2, x_6 = 2 will not occur
            break
        elif iteration == 30:
            break
       # after 30 instance of the program, the program stops

goal = float(input("please enter the goal "))
guess = float(input("please enter your guess "))

n = float(input("please enter the root you are trying to find "))

originalvalue(goal, guess, n)

#originalvalue (16, 5, 4)
#commenting lines 4,8, 34,35,37,39 and uncommenting lines 5,9,41
#gives the output x_6 = 2.0033728398582538

#inputting 16,5,4 gives x_6 = 2.0033728398582538