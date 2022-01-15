#our y is 128
#figure out the square root of y in comparasino to the user

import math
number = int(input("please enter your guess"))
#user input of the guess
Actualnumber = math.sqrt(128)
#we have the computer store the value
Guess = Actualnumber - number
#we are comparing how close the guess is in comparasion to the actual guess

print ("the square of 128 is " +str (Actualnumber))
if Guess <= 10:
    print ("your guess was close to result")
else:
    print ("try again, you were not as close to the guess")


