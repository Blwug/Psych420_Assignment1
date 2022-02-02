def current (c, t):
    I = c/t
        #Amp is rate of change of charge/rate of change of time
def ohm_law (i, r):
    v = i*r
        #increasing voltage increases the current
        #increase the rresistence current decrease
        #more resistence harder for the current to flow

def electric_power (i, r):
    p = (i**2) *r
        #or I = V/R = V**2/R
        #power is the rate of the energy that can be transfer

def dv_dt (negative_one, tau, r, i , v, t):

    aT = negative_one *(v *t) + r * (i *t)

        #aT represents acceleration
        # aT = dv/dt
        #T represents time

dt = .05
        #represents the amount of time increments increase of e
        # very iteration
max_t = 10
start_time = 1
stop_time = 6
        #start and stop time represents the duration for the
        # program to run

c = 1
        #charge
r = 2
        #resistor
t = 0
        #time is equal to 0
init_v = 0
        #initial voltage

negative_one = -1

one = 1

threshold = 3
        #if it reaches the threshold then the voltage
        # spikes to the max, 8

spike_display = 8
        #this is the max value of the neuron
        # before the electrical signal decays


    #I = res + cap
    #constant values

tau = r*c

    #def resting_potential()
    #the resting potential is when voltage = 0
    #resting means that there's no change
    #might not need to write a function for this


while start_time >= stop_time:
    t += dt
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






