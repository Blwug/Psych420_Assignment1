import math

def functionOriginal(x):
    return (x ** 4)


def functionDerived(x):
    return (4 * x ** 3)

const_tol = .01


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

        iteration = iteration + 1
        if guess - error/error < const_tol:
            break



originalvalue(16, 2.3)
