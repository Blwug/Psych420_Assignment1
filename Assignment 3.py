
#import matplotlib.pyplot as plt

def update_current (v, r):  #current is equal to i and we are finding delta charge/ delta time

    i = v/r #voltage is potential difference & is divided by resistence


#def update_ohm_law (i, r):  #inverse relationship of increasing the resistance decreases the current

    #v = i*r
    #v.append(v)

#def update_electric_power (i, v):  #power is rate of energy that can be transferred

    #p = v * i
    #p.append(p)

#def update_voltage (v, t, one, d_t, i, c): #finding change of voltage is finding the next value of voltage
   # v_1 = v(t) + d_t *(i/c)


def update_dv_dt ( one, r, i , v, cap):  #dv_dt = dv/dt which is acceleration

    aT = (one/(r*cap)) *(r*i - v)



dt = .05  #represents the amount of time increments increase of e

max_t = 10  #max time until the program stops recording


stop_time = [6]  #program stops running the iterative function

c = [1]  #charge/current

r = 2  #resistor

t = [1]  #time

cap = 1 #capacitor

v = [0]  #voltage

        #for every value that we can get from a list, we append it [-1]
        #to get the last element of those values

negative_one = -1

one = 1

threshold = 3  #when it reaches the threshold, the voltage, v, spikes to 8 which is the max

spike_display = 8  #max value of the neuron

tau = r*c  #represents the different firing rate (you can think of it like different viscosity rates)




while t >= stop_time:  #until the start time is greater or equal to the stop time, the program keeps looping
    t += dt  #this updates the value of time by dt, .05 so first run is 1+ .05

    #update_dv_dt(aT, )





    #update_ohm_.law value













