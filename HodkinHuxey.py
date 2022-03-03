#import matplotlib.pyplot plt
import math

voltage = 0
init_t = 0
start_time = 0
end_time = 16
time_step = .1
cap = 1
res = 2
volt_t = 3
max_volt = 8
tau = cap * res

ena = 115
gna = 120
ek = -12
gk = 36
el = 10.6
gl = 0.3

new_t = [init_t]

def times (init_t, new_t):
    new_t.append(init_t)

def dvdt (tau, new_voltage):
    return (1/tau) * (tau - new_voltage[-1])

def vt (voltage, time_step):
    return (voltage + dvdt) * time_step

def alpha_n (volt):
    return -0.01 * ((volt + 60) / math.exp(1 - (0.1 * volt)) -1)

def alpha_m(volt):
    return (2.5 - (0.1 * volt)) / (math.exp(2.5 - (0.1 * volt)) - 1)

def alpha_h(volt):
    return 0.07 * math.exp((-1.0 * volt) / 20.0)

def beta_n(volt):
    return 0.125 * math.exp((-1.0 * volt) / 80.0)

def beta_m(volt):
    return 4.0 * math.exp((-1.0 * volt) / 18.0)

def beta_h(volt):
    return 1.0 / (math.exp(3.0 - (0.1 * volt)) + 1.0)

