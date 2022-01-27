import math
import matplotlib.pyplot as plt

def update_accelerations(positions, accelerations, constant_spring):
    a1 = float(input(spring_constant * positions))
    a1 = accelerations.append(a1)


def update_velocity(speeds, accelerations , delta_t ):
    v1 = float(input(speeds + accelerations * delta_t))
    speeds.append(v1)

def update_positions(positions, speeds, delta_t):

    p1 = float(((-1) * positions) * speeds * delta_t)
    speeds.append(p1)

def update_times(times, current_time):

    times.append(current_time)

delta_t = 0.1
spring_constant = 3
#[] makes it a list, despite delta_t being a static number, it gives us an error for the previous def f(x) if [] is left out

measurement_time = [0]
positions = [-10]
speeds = [0]

#measurement_time = 0
#positions = -10
#speeds = 0



accelerations = []
run_time = 20 #seconds

update_accelerations(positions, accelerations, spring_constant)
#updates the update_accelerations method given the previously formula, def, previously used

current_time = 0
for current_time in range (run_time):
    current_time += run_time
    #current_time = sum(run_time)
   # current_time += delta_t


    update_times(measurement_time, current_time)
    #adding new values to the given list for def (update_times)

    update_accelerations(positions, accelerations, spring_constant)

    update_velocity(speeds, accelerations, delta_t)

    update_positions(positions, speeds, delta_t)

print (measurement_time)
print (positions)
print(speeds)
print(accelerations)












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