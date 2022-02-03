#we want two formula

def update_resistor_current (voltage, res,cap, dv, dt):
    RI = voltage + (res*cap(dv/dt))

def update_dv_over_dt (one, tau, current, voltage):
    dv_dt = (one/tau) * (res*current - voltage) # tau is res*cap
    aT.append(dv_dt)




def update_voltage (voltages, current_voltages): # we want to calcuate voltage in respect to time
    voltage = current * res
    current_voltages.append(voltage)



dt = .05 #the amount the value increases over the increment
increment = .5
start_time = 1
stop_time = 6
cap = 1
res = 2
threshold = 3
spike_display = 8
initial_voltage = 0
one = 1
current = [3] #current is i which is not voltage | we need to make an update method with amp
dv = [1]
aT = []
voltage = []

voltages = initial_voltage
injection_current = 4.3
injection_time = start_time *stop_time
tau = res*cap  #this is the vesocity of the firing rate

run_time = stop_time

while start_time >= stop_time:

    start_time += .5
    #update the value of voltage and Amp in relation to time

    update_dv_over_dt(one, tau, current, voltage)

    update_dv_over_dt(one, tau, current, voltage)

print(voltage)
print(aT)
print(start_time)








