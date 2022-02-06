
voltage = 1
initial_voltage = voltage
initial_time = 1
stop_time = 10
time_step = .5
cap = 2
res = 1
one = 1
tau = cap * res
new_acc_value = []
updated_time = []
new_voltage = []

def times (initial_time, updated_time): #this stores the new value of time
    updated_time.append(initial_time)

def acc (tau, one, voltage): # this stores the new value of acceleration, dv/dt
    updated_acc = (one/tau) * (tau - voltage)
    new_acc_value.append(updated_acc)

def voltages (voltage, new_acc_value, updated_time):
    updated_voltage = voltage + new_acc_value * updated_time
    new_voltage.append(updated_voltage)





while initial_time <= stop_time:
    initial_time += time_step

    acc(tau,one,voltage)
    times(initial_time, updated_time)
   # voltages(voltage, new_acc_value, updated_time)

    #def voltages (voltage, new_acc_value, updated_time): #this should get the new value of voltage
       # updated_voltage = voltage + new_acc_value *updated_time
        #new_voltage.append(updated_voltage)


print (new_acc_value)
print (updated_time)
print(voltages)





#def update_voltage (voltage, ):




#set the value of voltage
#update the value of voltage using dv/dt
#then update the value of voltage using old voltage + dv/dt*time_step

#break down the questions to make it tolerable to do

