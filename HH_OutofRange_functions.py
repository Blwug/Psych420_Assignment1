import matplotlib.pyplot as plt
from math import exp

voltage = 0.0
initial_time = 0.0
stop_time = 16
time_step = .4
voltage_tol = 3
max_voltage = 8
resting_potential = 0.0

ena = 115.0
gna = 120.0
ek = -12.0
gk = 36.0
el = 10.6
gl = 0.3

injectionCurrent = 0.0
injectionStartTime = 0.0
injectionEndTime = 6.0
function_injection_value = []

new_time = [0.0]
new_voltage = [voltage]
new_current = [injectionCurrent]
new_injectiontime = [injectionCurrent]  # inital value is the static injectionCurrent value

new_alpha_n = [1.2]
new_beta_n = [1.3]
new_alpha_m = [1.4]
new_beta_m = [1.6]
new_alpha_h = [1.7]  # Na inactivation
new_beta_h = [1.4]
new_function_m_dot = [1.2]
new_function_n_dot = [1.4]
new_function_h_dot = [1.4]
new_function_m_infinity = [1.2]
new_function_n_infinity = [1.4]
new_function_h_infinity = [1.4]

new_ina = [2.0]
new_ik = [5.0]
new_il = [3.0]

dv_dt_value = [0.0]

hh_m = [0.4]

hh_n = [1.0]

hh_h = [1.0]


def function_voltage(rate_of_change, time_step,new_injectiontime):  # injectiontime
    function_voltage = ((rate_of_change * time_step) *new_injectiontime)
    new_voltage.append(function_voltage)

def rate_of_change(new_ina, new_ik, new_il, new_injectiontime):
    function_dv_dt = new_injectiontime - (new_ina + new_ik + new_il)
    dv_dt_value.append(function_dv_dt)

def alpha_n(volts):  # general formula, we'll specify the value within the update function
    function_alpha_n = (0.1 - (0.01 * volts / (exp(1 - (0.1 * volts)) - 1)))
    new_alpha_n.append(function_alpha_n)

def beta_n(volts):
    function_beta_n = 0.125 * exp((-1.0 * volts) / 80.0)
    new_beta_n.append(function_beta_n)


def alpha_m(volts):
    function_alpha_na = (2.5 - (0.1 * volts)) / (exp(2.5 - (0.1 * volts)) - 1)
    new_alpha_m.append(function_alpha_na)


def beta_m(volts):
    function_beta_na = 4 * exp((-1 * volts) / 18)
    new_beta_m.append(function_beta_na)


def alpha_h(volts):
    function_alpha_h = 0.07 * exp((0.1 * volts) / 20)
    new_alpha_h.append(function_alpha_h)


def beta_h(volts):
    function_beta_h = 1 / (exp(3.0 - (volts * 0.1)) + 1)
    new_beta_h.append(function_beta_h)


def m_dot(hh_alpha_m, hh_beta_m, m): # m = hh_m
    function_m_dot = (hh_alpha_m * (1 - m)) - (hh_beta_m * m)
    new_function_m_dot.append(function_m_dot)


def n_dot(hh_alpha_n, hh_beta_n, n):
    function_n_dot = (hh_alpha_n * (1 - n)) - (hh_beta_n * n)
    new_function_n_dot.append(function_n_dot)


def h_dot(hh_alpha_h, hh_beta_h, h):
    function_h_dot = (hh_alpha_h * (1 - h)) - (hh_beta_h * h)
    new_function_h_dot.append(function_h_dot)


def m_infinity(hh_alpha_m, hh_beta_m):
    function_m_infinity = hh_alpha_m / (hh_alpha_m + hh_beta_m)
    new_function_m_infinity.append(function_m_infinity)


def n_infinity(hh_alpha_n, hh_beta_n):
    function_n_infinity = hh_alpha_n / (hh_alpha_n + hh_beta_n)
    new_function_n_infinity.append(function_n_infinity)


def h_infinity(hh_alpha_h, hh_beta_h):
    function_h_infinity = hh_alpha_h / (hh_alpha_h + hh_beta_h)
    new_function_h_infinity.append(function_h_infinity)


def _hh_m(new_function_m_dot, new_function_m_infinity):
    function_hh_m = ((new_function_m_dot * new_function_m_infinity))
    hh_m.append(function_hh_m)


def _hh_n(new_function_n_dot, new_function_n_infinity):
    function_hh_n = ((new_function_n_dot - new_function_n_infinity))
    hh_n.append(function_hh_n)


def _hh_h(new_function_h_dot, new_function_h_infinity):
    function_hh_h = ((new_function_h_dot * new_function_h_infinity ))
    hh_h.append(function_hh_h)

def fx_ina(gna, hh_m, hh_h, new_voltage, ena):
    ina = gna * pow(hh_m, 3.0) * hh_h *(new_voltage - ena)
    new_ina.append(ina)


def fx_ik(gk, hh_n, new_voltage, ek):
    ik = (gk * pow(hh_n, 4) * (new_voltage - ek))
    new_ik.append(ik)


def fx_il(gl, new_voltage, el):
    il = ((gl * (new_voltage - el)))
    new_il.append(il)

def times(initial_time, new_time):  # updates the time value
    new_time.append(initial_time)


def current_injection(injectionStartTime, new_injectiontime): #update line 154

    new_injectiontime.append(injectionStartTime)


#while new_time[-1] >= injectionStartTime and new_time[-1] <= injectionEndTime:
 #   initial_time += time_step
#else:
 #   initial_time = 0


while initial_time <= stop_time:

    initial_time += time_step  # updates the time value
    times(initial_time, new_time)
  #  injectionStartTime = 1
    current_injection(injectionStartTime,
                   new_injectiontime)


    alpha_n(new_voltage[-1])  # volts = new_voltage[-1] because we are redefining that within this statement
    alpha_m(new_voltage[-1])
    alpha_h(new_voltage[-1])
    beta_n(new_voltage[-1])
    beta_m(new_voltage[-1])
    beta_h(new_voltage[-1])
    h_dot(new_alpha_h[-1], new_beta_h[-1], hh_h[-1])
    m_dot(new_alpha_m[-1], new_beta_m[-1], hh_m[-1])
    n_dot(new_alpha_n[-1], new_beta_n[-1], hh_n[-1])
    m_infinity(new_alpha_m[-1], new_beta_m[-1])
    n_infinity(new_alpha_n[-1], new_beta_n[-1])
    h_infinity(new_alpha_h[-1], new_beta_h[-1])

    fx_ina(gna, hh_m[-1], hh_h[-1], new_voltage[-1], ena)
    fx_ik(gk, hh_n[-1], new_voltage[-1], ek)
    fx_il(gl, new_voltage[-1], el)


    _hh_m(new_function_m_dot[-1], new_function_m_infinity[-1])
    _hh_n(new_function_n_dot[-1], new_function_n_infinity[-1])
    _hh_h(new_function_h_dot[-1], new_function_h_infinity[-1])


    function_voltage(dv_dt_value[-1], time_step, new_injectiontime[-1])  # calls

    rate_of_change(new_ina[-1], new_ik[-1], new_il[-1], new_injectiontime[-1])  # new_injectiontime


#print("new rate of change  " + str(dv_dt_value))
#print("injection " +str(new_injectiontime))
#print("hh_m " +str(hh_m))
#print("ina  " +str(new_ina))
#print ("ss" + str( new_function_n_dot))
#print ("bb" + str(new_function_m_dot))
#print ("zz" + str(new_function_h_dot))
#print("voltage" + str(new_voltage))
#print ("wah" + str(new_function_m_infinity))
print ("times" + str(new_time))
print("injection " +str(new_injectiontime))


plt.plot(new_time, dv_dt_value)
plt.xlabel('time')
plt.ylabel('voltage')

# plt.plot(new_time, new_voltage)
# plt.xlabel('time')
# plt.ylabel('voltage')
plt.show()
plt.savefig('Graph.png')