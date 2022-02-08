#import matplotlib.pyplot as plt

start_time = 1
run_time = 6
inc = .5
updated_time = [0]

dt = .05 #the amount the value increases over the increment

stop_time = 6
cap = 1
res = 2
threshold = 3
spike_display = 8
initial_voltage = 0
one = 1
current = 3 #current is i which is not voltage | we need to make an update method with amp
dv = 1
aT = 1


new_voltage = [1]

voltages = initial_voltage
injection_current = 4.3
injection_time = start_time *stop_time
tau = res*cap  #this is the vesocity of the firing rate


def update_resistor_current (voltage, res,cap, dv, dt):
    RI = voltage + (res*cap(dv/dt))

def update_dv_over_dt (one, tau, current, voltage, res):
    dv_dt = (one/tau) * (res*current - voltage) # tau is res*cap



def update_voltage (voltages, current_voltages): # we want to calcuate voltage in respect to time
    voltage = current * res
    voltages.append(voltage)

def update_times (times, current_time):
    times.append(current_time)

while start_time < run_time:
    start_time += inc

    update_times(updated_time, start_time)
    update_voltage(new_voltage, voltages)



print (updated_time) #this gives us our updated time
print(new_voltage) #this gives us our voltage value










