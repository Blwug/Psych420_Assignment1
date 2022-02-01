def inertia (I_R, I_C):
    I = I_R + I_C
    #I represents current
def xx (I_R, C, d_v, d_t):
    diff_I = I_R + C/(d_v*d_t)

def resistence (voltage, I):
    R = voltage/I

#def voltage (I, R):
  #voltage = I *R
    #Finding the value of voltage, I, or R can be done through
    # algebra manipulation


def resistor_inductor_circuit (V, R_C, d_v, d_t):
    R1 = V + R_C*(d_v/d_t)

def dv_dt (one, tau, RI, V):
    a1 = (one/tau) * (RI - V)

    # a1 = dv/dt
    #the formula represents dv/dt = [-v(t) + R*I(t)](1/t)]
    #local values means their initial value

aT = a1
    #dv is difference in vel
    #dt i sdifference in time
    #aT represents acceleration being impacted by the time value



dt = .05
#represents the amount of time increments increase of every iteration
max_t = 10
start_time = 1
stop_time = 6
#start and stop time represents the duration for the program to run

cap = 1
#capacitor
res = 2
#resistor
    #R = Resistence
threshold = 3
#if it reaches the threshold then the voltage spikes to the max, 8
spike_display = 8

#this is the max value of the neuron before the electrical signal decays
init_t = 0
#initial time
init_v = 0
#initial voltage

injection_current = 4.3
negative_one = -1
one = 1

#I = res + cap
#constant values

tau = res*cap

#def resting_potential()
#the resting potential is when voltage = 0
#resting means that there's no change
#might not need to write a function for this


while start_time >= stop_time:
    init_t += dt
    #this updates the initial value of time by the amount of delta time (0.5)
    #for every iteration of the new time value, we need to know the
    #resistence and the voltage value to get the new aT(dv/dt)
    #we can set a def updatevoltage(_,_,_), and def updatetime(_,_,_)
    #to get the new updated value

    #to do that we need to call on our def functions && append it
    #so that we can get that value again
    # if we are appending, then we need to use [] to make the variables a list
        #however, we do not do this for the constant variables

    #we can do that by having an update method within this while loop
    #so that every iteration helps us get this new value





#def run_integrate_fire

#notes| things to work on still
#create a function that helps the voltage amount decrease exponentially until
#it reaches the resting potential, 0
#create a method that increases the spike of the voltage from 3 to 8
#create a method that decreases the voltage when it hits 8 to 0
#set an if statement and a check statement to have the voltage increase from 0 to 3
    #the check statement will be that when time == stop_time: break
#create a graph that shows the voltage increase from every cycle


