#I = I_R + I_C
#diff_I = I_R + C/(d_v*d_t)
#(V/R) + C(d_v*d_t)
#RI = RC/(d_v/d_t)
#(1/tau) * (RI - V)
#(d_v/d_t)
#1* (1/tau)* (RI-V)
#d_v/d_t

#LandF equation

dt = .05
#represents the amount of time increments increase of every iteration
max_t = 10
#
start_time = 1
stop_time = 6

cap = 1
#capacitor
res = 2
#resistor
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

#constant values

voltage = init_v

injection_time = start_time * stop_time
#injection_time represents

tau = res*cap

#def resting_potential()
#the resting potential is when voltage = 0
#resting means that there's no change
#might not need to write a function for this


def updatetime (initial_time, rate_of_change, time_step):

    t1 =((rate_of_change *time_step) + initial_time)
    #t1 is the updated time method, t0 is the initial time value

def updateacceleration (localres, locali, localv, tau):
    #we need to add our own variables for this but we did not define I yet
    #borrowing the varable the prof used as the name to act as a placeholder

    aT = (negative_one *localv +(localres *locali))*(one/tau)
    # aT = dv/dt
    #the formula represents dv/dt = [-v(t) + R*I(t)](1/t)]
        #local values means their initial value

while start_time >= stop_time:
    start_time +=  dt
    #this updates the initial value of time by the amount of delta time (0.5)
    #for every iteration of the new time value, we need to know the
    #resistence and the voltage value to get the new aT(dv/dt)
    #we can set a def updatevoltage(_,_,_), and def updatetime(_,_,_)
    #to get the new updated value


#def run_integrate_fire

#notes| things to work on still
#create a function that helps the voltage amount decrease exponentially until
#it reaches the resting potential, 0
#create a method that increases the spike of the voltage from 3 to 8
#create a method that decreases the voltage when it hits 8 to 0
#set an if statement and a check statement to have the voltage increase from 0 to 3
    #the check statement will be that when time == stop_time: break
#create a graph that shows the voltage increase from every cycle


