import matplotlib.pyplot as plt
import numpy as np

voltage = 1
initial_time = 0
stop_time = 10
time_step = .5
cap = 2
res = 1
voltage_tol = 3
max_voltage = 8
resting_potential = 0
current = 4

injectionCurrent = 4.3
injectionStartTime = 1
injectionEndTime = 6
function_injection_value = []
new_dv_dt_value = []
new_time = [0]
new_voltage = [voltage]


def times(initial_time, new_time):  # this stores the new value of time
    new_time.append(initial_time)


def dv_dt(cap, res, current, new_voltage):
    function_dv_dt = (1 / (cap * res)) * (res * current - new_voltage[-1])
    new_dv_dt_value.append(function_dv_dt)


def function_voltage(voltage, new_dv_dt_value, time_step):
    function_voltage = voltage + new_dv_dt_value[-1] * time_step
    new_voltage.append(function_voltage)


while initial_time < stop_time:
    initial_time += time_step
    dv_dt(cap, res, current, new_voltage)
    times(initial_time, new_time)

    function_voltage(new_voltage[-1], new_dv_dt_value, time_step)
    new_voltage[0] = resting_potential
    if new_voltage[-1] < voltage_tol:
        new_voltage[-1] = voltage_tol
    elif new_voltage[-1] < max_voltage:
        new_voltage[-1] = max_voltage
    else:
        new_voltage[-1] == max_voltage
        new_voltage[-1] = resting_potential


print(new_dv_dt_value)
print(new_time)
print(new_voltage)

plt.plot(new_time, new_voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()

# def update_voltage (voltage, ):


# set the value of voltage
# update the value of voltage using dv/dt
# then update the value of voltage using old voltage + dv/dt*time_step

# break down the questions to make it tolerable to do
