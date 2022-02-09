import matplotlib.pyplot as plt

voltage = 0
initial_time = 0
stop_time = 14
time_step = .1
cap = 2
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
new_injectiontime = [injectionCurrent]
#if the current injection time is true, then have the voltage run else have it fail the next interval of the threshold

def times(initial_time, new_time):  # this stores the new value of time
    new_time.append(initial_time)

def current_injection (injectionStartTime, new_injectiontime):
        new_injectiontime.append(injectionStartTime)


def dv_dt(cap, res, current, new_voltage):
    function_dv_dt = (1 / (cap * res)) * (res * current - new_voltage[-1])
    new_dv_dt_value.append(function_dv_dt)


def function_voltage(voltage, new_dv_dt_value, time_step, new_injectiontime):
    function_voltage = (voltage + new_dv_dt_value[-1] * time_step) * new_injectiontime[-1]
    new_voltage.append(function_voltage)


while initial_time < stop_time: #and injectionStartTime < injectionEndTime:

    initial_time += time_step
    dv_dt(cap, res, current, new_voltage)
    times(initial_time, new_time)

    if new_time [-1] < 2:
        injectionStartTime = 0
    elif new_time[-1] >12:
        injectionStartTime = 0
    elif new_time[-1] > 2:
            injectionStartTime = 1

    current_injection(injectionStartTime, new_injectiontime)


    if new_voltage[-1] >=max_voltage:
        new_voltage[-1] = resting_potential
    elif new_voltage[-1] > voltage_tol:
        new_voltage[-1] = max_voltage
    elif new_time[-1] <2:
      new_voltage[-1] = 0

    function_voltage(new_voltage[-1], new_dv_dt_value, time_step, new_injectiontime)





print(new_dv_dt_value)
print(new_time)
print(new_voltage)
print(new_injectiontime)

plt.plot(new_time, new_voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()
plt.savefig('I_and_F_graph.png')
# def update_voltage (voltage, ):