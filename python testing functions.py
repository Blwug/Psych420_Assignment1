import matplotlib.pyplot as plt
import numpy as np
voltage = 1
initial_time = 0
stop_time = 10
time_step = .5
cap = 2
res = 1
tol = 3
max = 8
resting_potential = 0
current = 4

injectionCurrent = 4.3
injectionStartTime = 1
injectionEndTime = 6
updated_injection_value = []
injectionTimes = injectionStartTime, injectionEndTime
new_acc_value = []
updated_time = []
new_voltage = []

def times (initial_time, updated_time): #this stores the new value of time
    updated_time.append(initial_time)

def acc (cap,res,current, new_voltage): # this stores the new value of acceleratioThe rn, dv/dt
    updated_acc = (1/(cap*res)) * (res*current - new_voltage) #tau is equal to cap/res
    new_acc_value.append(updated_acc)

def voltages (voltage, new_acc_value, updated_time):
    updated_voltage = voltage + new_acc_value [-1] * updated_time [-1]
    new_voltage.append(updated_voltage)





while initial_time < stop_time:
    initial_time += time_step
    acc(cap,res,current, voltage)
    times(initial_time, updated_time)

    voltages(voltage, new_acc_value, updated_time)
    new_voltage [0] = resting_potential
    if new_voltage[-1] == tol:
        new_voltage[-1] = max
    elif new_voltage[-1] <tol:
        new_voltage[-1] = tol
    else: new_voltage [-1] = resting_potential





print (new_acc_value)
print (updated_time)
print(new_voltage)

plt.plot (new_voltage,updated_time,)
plt.ylabel('voltage')
plt.xlabel('time')
plt.show()



#def update_voltage (voltage, ):




#set the value of voltage
#update the value of voltage using dv/dt
#then update the value of voltage using old voltage + dv/dt*time_step

#break down the questions to make it tolerable to do