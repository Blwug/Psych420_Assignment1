start_time = 1
stop_time = 6
inc = .5


def (start_time, updated_time):


while start_time> stop_time:
    start_time += inc


print (start_time)


















#def xx (I_R, C, d_v, d_t):
   # diff_I = I_R + C/(d_v*d_t)

#def resistence (voltage, I):
   # R = voltage/I

#def voltage (I, R):
  #voltage = I *R
    #Finding the value of voltage, I, or R can be done through
    # algebra manipulation


#def resistor_inductor_circuit (V, R_C, d_v, d_t):
  #  R1 = V + R_C*(d_v/d_t)

#def run_integrate_fire

#notes| things to work on still
#create a function that helps the voltage amount decrease exponentially until
#it reaches the resting potential, 0
#create a method that increases the spike of the voltage from 3 to 8
#create a method that decreases the voltage when it hits 8 to 0
#set an if statement and a check statement to have the voltage increase from 0 to 3
    #the check statement will be that when time == stop_time: break
#create a graph that shows the voltage increase from every cycle

# we can set a def updatevoltage(_,_,_), and def updatetime(_,_,_)
# to get the new updated value

# to do that we need to call on our def functions && append it
# so that we can get that value again
# if we are appending, then we need to use [] to make the variables a list
# however, we do not do this for the constant variables

# we can do that by having an update method within this while loop
# so that every iteration helps us get this new value