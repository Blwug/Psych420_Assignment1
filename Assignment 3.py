def current (c, t): #current is equal to i and we are finding delta charge/ delta time
    I = c/t

def ohm_law (i, r): #inverse relationship of increasding the resistence decreases the current
    v = i*r

def electric_power (i, r): #power is rate of energy that can be transferred
    p = (i**2) *r


def dv_dt (negative_one, tau, r, i , v, t): #dv_dt = dv/dt which is acceleration

    aT = negative_one *(v *t) + r * (i *t)


dt = .05 #represents the amount of time increments increase of e

max_t = 10 #max time until the program stops recording


stop_time = 6 #program stops running the iterative function


c = 1 #charge

r = 2 #resistor

t = 1 #time

v = 0 #voltage

negative_one = -1

one = 1

threshold = 3 #when it reaches the threshold, the voltage, v, spikes to 8 which is the max

spike_display = 8 #max value of the neuron

tau = r*c #represents time constant

while t >= stop_time: #until the start time is greater or equal to the stop time, the program keeps looping
    t += dt #this updates the value of time by dt, .05 so first run is 1+ .05








