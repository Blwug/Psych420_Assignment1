import math

def functionOriginal(x):
    return (x ** 4)


def functionDerived(x):
    return (4 * x ** 3)

const_tol = .001


# used the power rule
# You need both a goal and an initial guess
# Use variable (and function) names that make sense and communicate something
def originalvalue(goal, guess):


    iteration = 1

    while True:
        f = functionOriginal(guess)
        f_d = functionDerived(guess)

        error = (goal - f) / f_d
        print("x_{} = {}".format(iteration, guess))
        guess = error + guess
        iteration = iteration +1
        #this helps the program remember the number of instance the function occured
        if guess/- error < const_tol:
            #this function stops a repeating out
                #ie: x_5 = 2, x_6 = 2 will not occur
            break
        elif iteration == 30:
            break
       # after 30 instance of the program, the program stops

#goal = float(input("goal "))
#guess = float(input("guess "))

#originalvalue(goal,guess)
originalvalue(800,55)




#goal is 16 and the guess is  5000000
#takes 57 iteration to get the answer of the fourth root of the goal: 2.

