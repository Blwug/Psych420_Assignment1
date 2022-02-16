import matplotlib.pyplot as plt

voltage = 0
initial_time = 0
stop_time = 20
time_step = .1
cap = 1
res = 1
voltage_tol = 3
max_voltage = 8
resting_potential = 0
current = 4

injectionCurrent = 0
injectionStartTime = 0
injectionEndTime = 6
function_injection_value = []
new_dv_dt_value = []
new_time = [0]
new_voltage = [voltage]
new_current = [injectionCurrent]
new_injectiontime = [injectionCurrent] #inital value is the static injectionCurrent value

#put in the constants
#put in the value of alpha (channels opening; requires all of them to be open)
#put in the value of beta (channels closing; if one closed then rest follows -> expotentional decay)
#don't forget the euler is constant!!

def times(initial_time, new_time):  # updates the time value
    new_time.append(initial_time)

def current_injection (injectionStartTime, new_injectiontime):
        new_injectiontime.append(injectionStartTime)

def dv_dt(cap, res, current, new_voltage):
    function_dv_dt = (1 / (cap * res)) * (res * current - new_voltage[-1])
    new_dv_dt_value.append(function_dv_dt)


def function_voltage(voltage, new_dv_dt_value, time_step, new_injectiontime):
    function_voltage = (voltage + new_dv_dt_value[-1] * time_step) * new_injectiontime[-1] #if the last element of new_injectiontime is 0 then that means there is no voltage
    new_voltage.append(function_voltage)


while initial_time < stop_time:

    initial_time += time_step #updates the time value
    dv_dt(cap, res, current, new_voltage)
    times(initial_time, new_time)


    if new_time [-1] < 2 or new_time[-1] >12: #if the last element of new_time is less than 2, or greater than 12 than there is no current
        injectionStartTime = 0
    elif new_time[-1] > 2:
        injectionStartTime = 1

    current_injection(injectionStartTime, new_injectiontime) #updates the current_injection value given the while condition is true


    if new_voltage[-1] >=max_voltage:
        new_voltage[-1] = resting_potential
    elif new_voltage[-1] > voltage_tol:
        new_voltage[-1] = max_voltage
    elif new_time[-1] <2:
      new_voltage[-1] = 0

    function_voltage(new_voltage[-1], new_dv_dt_value, time_step, new_injectiontime) #calls





print(new_dv_dt_value)
print(new_time)
print(new_voltage)
print(new_injectiontime)

plt.plot(new_time, new_voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()
plt.savefig('Graph.png')
