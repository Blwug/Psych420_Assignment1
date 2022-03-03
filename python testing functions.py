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
e = 2.71828 #could replace with import math and then use exp.. eh


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


value = []
new_not_dv_dt_value = [1]


n = 1
h = 1
m = h


hh_m = 3
hh_n = 4
hh_h = 4

def times(initial_time, new_time):  # updates the time value
    new_time.append(initial_time)

def current_injection (injectionStartTime, new_injectiontime):
        new_injectiontime.append(injectionStartTime)


def function_voltage(voltage, new_dv_dt_value, time_step, new_injectiontime):
    function_voltage = (voltage + new_dv_dt_value[-1] * time_step) * new_injectiontime[-1] #if the last element of new_injectiontime is 0 then that means there is no voltage
    new_voltage.append(function_voltage)

#voltage dependent values
def alpha_n (new_voltage, e): #potassium activation|if alpha>beta than increased liklihood for it to open
    function_alpha_n = (0.1 - (0.01 * new_voltage[-1]/ e ** (1 - (0.1 * new_voltage[-1])) - 1))
    new_alpha_n.append(function_alpha_n)

def beta_n (new_voltage, e): #potassium activation | if beta is high then more likely for it to close
    function_beta_n = (0.125 - e ** (-1 * new_voltage[-1] /80))
    new_beta_n.append(function_beta_n)

def alpha_m (new_voltage, e):
    function_alpha_na = (2.5-  (0.1 * new_voltage[-1]))/ (e**(2.5 - (0.1 * new_voltage[-1])) -1)
    new_alpha_m.append(function_alpha_na)

def beta_m (new_voltage, e):
    function_beta_na = 4*e**((-1 * new_voltage[-1])/18)
    new_beta_m.append(function_beta_na)

def alpha_h (new_voltage, e):
    function_alpha_h = 0.07*e**(0.1 * new_voltage[-1])/20
    new_alpha_h.append(function_alpha_h)

def beta_h (new_voltage, e):
    function_beta_h = 1/e**(3.0 - (new_voltage[-1] * 0.1)+1)
    new_beta_h.append(function_beta_h)

def m_dot (new_alpha_m, new_beta_m, m):
    function_m_dot = (new_alpha_m[-1] * (1- m)) - (new_beta_m[-1] * m)
    new_function_m_dot.append(function_m_dot[-1])

def n_dot (new_alpha_n, new_beta_n, n):
    function_n_dot = (new_alpha_n[-1] * (1-n)) - (new_beta_n[-1] * n)
    new_function_n_dot.append(function_n_dot)

def h_dot (new_alpha_h, new_beta_h, h):
    function_h_dot = (new_alpha_h[-1] * (1-h)) - (new_beta_h[-1] * h)
    new_function_h_dot.append(function_h_dot)

def m_infinity(new_alpha_m, new_beta_m):
    function_m_infinity = new_alpha_m[-1]/(new_alpha_m[-1] + new_beta_m[-1])
    new_function_m_infinity.append(function_m_infinity)

def n_infinity(new_alpha_n, new_beta_n):
    function_n_infinity = new_alpha_n[-1] / (new_alpha_n[-1] +new_beta_n[-1])
    new_function_n_infinity.append(function_n_infinity)

def h_infinity (new_alpha_h, new_beta_h):
    function_h_infinity = new_alpha_h[-1] /(new_alpha_h[-1] + new_beta_h[-1])
    new_function_h_infinity.append(function_h_infinity)


def dv_dt(cap, res, current, new_voltage):
    function_dv_dt = (1 / (cap * res)) * (res * current - new_voltage[-1])
    new_dv_dt_value.append(function_dv_dt)

def not_dv_dt(new_voltage, new_injectiontime, hh_m, hh_n, hh_h, gna, gk,gl): #hh_m,n,h can be sub in for anything its just an arg
    ina = gna * pow(hh_m, 3.0) * hh_h & (new_voltage[-1] - ena)
    ik = gk * pow(hh_n, 4) *(new_voltage[-1] - ek)
    il = gl * (new_voltage - el)

    function_not_dv_dt = new_injectiontime - (ina + ik + il)
    new_not_dv_dt_value.append(function_not_dv_dt)

def change(new_dv_dt_value, not_dv_dt):
    return ((new_dv_dt_value * not_dv_dt))


while initial_time < stop_time:

    initial_time += time_step #updates the time value
    dv_dt(cap, res, current, new_voltage)
    times(initial_time, new_time)


    if new_time [-1] < 2 or new_time[-1] >12: #if the last element of new_time is less than 2, or greater than 12 than there is no current
        injectionStartTime = 0
    elif new_time[-1] > 2:
        injectionStartTime = 1
    current_injection(injectionStartTime, new_injectiontime) #updates the current_injection value given the while condition is true
    value = change (new_dv_dt_value[-1], new_not_dv_dt_value[-1])


    if new_voltage[-1] >=max_voltage or new_time[-1] <2:
        new_voltage[-1] = resting_potential

    elif new_voltage[-1] > voltage_tol:
        new_voltage[-1] = max_voltage

    function_voltage(new_voltage[-1], new_dv_dt_value, time_step, new_injectiontime) #calls



#print(new_dv_dt_value)
#print(new_time)
#print(new_voltage)
#print(new_injectiontime)
print (value)
print(new_not_dv_dt_value)

plt.plot(new_time, new_voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()
plt.savefig('Graph.png')