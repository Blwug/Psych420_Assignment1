#1. I am running on Windows 10
#2. I will be using Python
#3. PyCharm IDE

#4. We will be square rooting a valid number
import math

number = int(input("Please enter a number to square root & round down to a whole number"))
number = math.sqrt(number)
#we are squaring the value we got from the user
number = (math.floor(number))
#we are rounding the number down to whole number

print("the square root of the number is " + str(number))








