

product = int(input("please enter the product"))
n = int(input("please enter the root you would like to find of the product"))
guess = int(input("please enter your guess of the derivative given your previous root answer"))
actualanswer = product ** (1/n)
#doing this allows us to found the value of any root hence n
#therefore if we want to find the second,third,fourth root, we have the user specify that
abstol = .001
#this is an aribtary value that we can set as the max difference there is for
#the guess and an absolute tolerance, abstol = absolute tolerance in this case
editedguess = guess
#we seperated guess into 2 variables
#the reason why seperating the initial user input & the modified input is good is because we can compare
#the diffference between their guess to how far they were from the actual value
while editedguess <= actualanswer:
    #this is a while loop & continues until the condition of edited guess being less than or equal to actual answer is false
    print (editedguess)
    #this has the terminal print the value of the guess being modified to approach the actualansqwer variable
    editedguess += abstol
#this constantly compares the value of the guess with the actual derivative & once it reaches a value where the edited guess
# is greater than the actual answer, the program stops
print ("the product is " +str(product))
print("your guess was " +str(guess))
print("the actual answer is " +str(actualanswer))

diff = editedguess - guess
#this compares the how far the guess was when compared to the guess that slowly approached the actual answer
print("your guess was "+str (diff) + " off")
#another thing to note is that we are taking the value from the 16th decimal place so the results is more accurate
# regarding how much the user is off; if there is to much strain running it,
# then reduce it yourself by setting a limit on the number or something
#this uses the same amount of ram as google for me: 1.4 gb.
