#Assignment 1 Bonus | Taking the value of number & square value of number & dividing them again

import math
number = int(input("Please enter the product "))
n = int(input("Please enter the base "))
number = number ** (1/n)
#we are multiplying it by 1/n to get the exponent and this works for any root
print("the exponent is  " + str(number))


