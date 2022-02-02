 #import math
#import matplotlib.pyplot as plt

def update_current (c, t):  #current is equal to i and we are finding delta charge/ delta time

    i = c/t
    i.append(i)


def update_ohm_law (i, r):  #inverse relationship of increasing the resistance decreases the current

    v = i*r
    v.append(v)

def update_electric_power (i, r):  #power is rate of energy that can be transferred

    p = (i**2) *r
    p.append(p)


def update_dv_dt (negative_one, one, tau, r, i , v, t):  #dv_dt = dv/dt which is acceleration

    #aT = (one/r*cap) * (r*c - v)
    aT = (negative_one *(v *t) + r * (i *t))/(one/tau)
    aT.append(aT)

dt = .05  #represents the amount of time increments increase of e

max_t = 10  #max time until the program stops recording


stop_time = 6  #program stops running the iterative function

c = 1  #charge/current

r = 2  #resistor

t = [1]  #time

cap = [1] #capacitor

v = [0]  #voltage

negative_one = -1

one = 1

threshold = 3  #when it reaches the threshold, the voltage, v, spikes to 8 which is the max

spike_display = 8  #max value of the neuron

tau = r*c  #represents the different firing rate (you can think of it like different viscosity rates)


while t >= stop_time:  #until the start time is greater or equal to the stop time, the program keeps looping
    t += dt  #this updates the value of time by dt, .05 so first run is 1+ .05













