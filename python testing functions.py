import matplotlib.pyplot as plt

voltage = 0
initial_time = 0
stop_time = 14
time_step = .1
cap = 1
res = 2
voltage_tol = 3
max_voltage = 8
resting_potential = 0
current = 4

ena = 115
gna = 120
ek = -12
gk = 36
el = 10.6
gl = 0.3
e = 2.71828


injectionCurrent = 0
injectionStartTime = 0
injectionEndTime = 6
function_injection_value = []
new_dv_dt_value = []
new_time = [0]
new_voltage = [voltage]
new_current = [injectionCurrent]
new_injectiontime = [injectionCurrent] #inital value is the static injectionCurrent value

new_alpha_n = []
new_beta_n = []
new_alpha_m = [1]
new_beta_m = [1]
new_alpha_h = [] #Na inactivation
new_beta_h = []

new_I_k =[]
new_I_na = []
new_I_leak = []
n = 1
h = 1
m = h

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

#voltage dependent values
def alpha_n (new_voltage, e): #potassium activation|if alpha>beta than increased liklihood for it to open
    function_alpha_m = -0.01 * ((new_voltage [-1] +60) / e**(new_voltage[-1] +60/-10))-1
    new_alpha_n.append(function_alpham)

def beta_n (new_voltage, e): #potassium activation | if beta is high then more likely for it to close
    function_beta_m = 0.125*e**((new_voltage[-1] +70)/80)
    new_beta_n.append(function_beta_m)

def alpha_m (new_voltage, e):
    function_alpha_na = -0.1*(new_voltage[-1] +45)/e**((new_voltage[-1]+45)/-10) -1
    new_alpha_m.append(function_alpha_na)

def beta_m (new_voltage, e):
    function_beta_na = 4*e**((new_voltage[-1]+70)/-18)
    new_beta_m.append(function_beta_na)

def alpha_h (new_voltage, e):
    function_alpha_h = 0.07*e**(new_voltage[-1]+40)/20
    new_alpha_h.append(function_alpha_h)

def beta_h (new_voltage, e):
    function_beta_h = 1/1+e**(new_voltage[-1]+40)/-10
    new_beta_h.append(function_beta_h)

def dn_dt (new_alpha_n, new_voltage, n, new_beta_n): #change in number of open potassium channel = alpha - beta (rate of open channel - rate of closed channel)
    function_dn_dt = new_alpha_n[-1] * new_voltage[-1] *(1-n) - new_beta_n[-1] * new_voltage[-1] * n
    new_function_dn_dt.append(function_dn_dt)

def dm_dt (new_alpha_m, new_voltage, m, new_beta_m):
    function_dm_dt = new_alpha_m [-1] * new_voltage[-1] *(1-m) - new_beta_m *new_voltage[-1] *m
    new_function_dm_dt.append(function_dm_dt)



while initial_time < stop_time:

    initial_time += time_step #updates the time value
    dv_dt(cap, res, current, new_voltage)
    times(initial_time, new_time)


    if new_time [-1] < 2 or new_time[-1] >12: #if the last element of new_time is less than 2, or greater than 12 than there is no current
        injectionStartTime = 0
    elif new_time[-1] > 2:
        injectionStartTime = 1
    current_injection(injectionStartTime, new_injectiontime) #updates the current_injection value given the while condition is true


    if new_voltage[-1] >=max_voltage or new_time[-1] <2:
        new_voltage[-1] = resting_potential

    elif new_voltage[-1] > voltage_tol:
        new_voltage[-1] = max_voltage

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