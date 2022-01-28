import math
import matplotlib.pyplot as plt

def update_accelerations(positions, accelerations, constant_spring):
    a1 = -1 * positions[-1] * spring_constant
    accelerations.append(a1)
# [-1] gets the last element of the list
#we need to do this becasue if we only put (-1), then the code can not run
#because

def update_velocity(speeds, accelerations , delta_t ):
    v1 = speeds[-1] + accelerations[-1] * delta_t
    speeds.append(v1)

def update_positions(positions, speeds, delta_t):

    p1 = positions[-1] + speeds[-1]*delta_t
    positions.append(p1)
#by having the positions and speed getting the last element, if the values trying to find
#p3 then it'll look at the previous element, p2 to calcuate the new value of p3

def update_times(times, current_time):

    times.append(current_time)

delta_t = 0.1
spring_constant = 3
#[] makes it a list, despite delta_t being a static number, it gives us an error for the previous def f(x) if [] is left out

measurement_times = [0]
positions = [-10]
speeds = [0]
accelerations = []
#measurement_time = 0
#positions = -10
#speeds = 0


run_time = 10.0 #seconds
#originally run_time =10 as that worked for line 46

update_accelerations(positions, accelerations, spring_constant)
#updates the update_accelerations method given the previously formula, def, previously used

current_time = 0
while current_time < run_time:
#for current_time in range (run_time):
    #I wanted to run the above operation, line 46, however, it gave me
    # a type error of float object =/= interperted as an int and
    #because of that I had to change the value of run_time from 10.0
    #to 10

    current_time += delta_t
    #another method is to write current_time = current_time + delta_t
    #both mean the same thing since we are updating the current_time value
    #with a new value, +delta_t during the new iterations

    update_times(measurement_times, current_time)
    #adding new values to the given list for def (update_times)

    update_accelerations(positions, accelerations, spring_constant)
    #finds the new value of acceleration and adds it to the list
    update_velocity(speeds, accelerations, delta_t)

    update_positions(positions, speeds, delta_t)


print (measurement_times)
print (positions)
print(speeds)
print(accelerations)
#this is just a check to see whether we got the correct values


fig, axs = plt.subplots(3, 1, figsize=(15, 12))  # 3 rows, 1 column
axs[0].plot(measurement_times, positions, '-o')
axs[0].set_title("Position")

axs[1].plot(measurement_times, speeds)
axs[1].set_title("Velocity")

axs[2].plot(measurement_times, accelerations)
axs[2].set_title("Acceleration")

fig.suptitle('Oscillator Without Dampening')
#using the "'/'' helps label the graph used since we are setting the
#titles with set_title
plt.show()




#initial notes towards handling the issue

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
#this calls back to the last element of the function
#p - spring

