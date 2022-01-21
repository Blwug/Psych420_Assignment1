import math
import matplotlib.pyplot as plt

def s_t(d_t, v, s):
    return v +d_t*speed

#s_of_t

def v_t(d_t,a,v):
    return v + a*d_t

#print v_t(3,2,2)

def a_t(p,s):
    return -1*p*s
#print a_t(3,1)

v = 0
s = 10
p = 2
d_t = .5
t = 0
i = 0




#def release_spring(s_t,v_t,a_t):
    #while i <10:


        #a = a_t(p*s)
        #v = v_t(d_t + a*d_t)
        #s = s_t(d_t + v_t*s_t)
print (a_list)












#plot create list empty and hold it and after the function return the list for a and t (accerlation and time)
#keeps track of velocity & accerlation
#before the loop do s_list = [0]*iteration+1 - you're creating a list of 0, iteration + 1
#update first value s_list[0] = s - wants to reassign the value of s


#you have to update it seperatly - last most recent updates towards providing the update of the varaible
#one for loop & one while loop, each update is done sequential before we start doing it again

#velocity of time, K is a constant - we can pick that for damped oscillator
#make the plot figure then we need to change one code towards making the damped oscillator of friction & weight on the spring
#easy to experiment within the lines of the code
#change the P value changes the oscilation value

#a = [1,3]
#a.append(3)
#this increases the list
#a[-1]
#p - spring

#they made 2 seperate list && had it update by using the append functino or the iteration +1
#a_list + 1 which is going to be the new value