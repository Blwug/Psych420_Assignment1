import math

def functionOriginal(x):
    return (x ** 4)


def functionDerived(x):
    return (4 * x ** 3)


# used the power rule
# You need both a goal and an initial guess
# Use variable (and function) names that make sense and communicate something
def originalvalue(goal, guess):
    iteration = 1
    while True:
        # Computing values at current guess
        f = functionOriginal(guess)
        f_d = functionDerived(guess)
        # Misplace parentheses; details matter
        error = (goal - f) / f_d
        print("x_{} = {}".format(iteration, guess))
        guess = error + guess
        # this is the update method, the initial value of x0 gets updated to be x_next
        # x_next uses newton formula of xn+1 = xn -f(xn)/f`(xn)

        iteration = iteration + 1

        if iteration == 10:
            # breaks after n number of the loop running
            break


originalvalue(16, 2.3)
