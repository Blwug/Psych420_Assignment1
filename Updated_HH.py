from math import exp
import matplotlib as plt

start_t = 0.0
time_step = 0.4
end_t = 10.0
init_v = 0.0

new_times = [start_t]
voltages = [init_v]

ena = 115.0
gna = 120.0
ek = -12.0
gk = 36.0
el = 10.6
gl = 0.3

injection_current  = 0.0
injection_start_time = 0.0
injection_end_time = 6.0

delta_time = 0.0

times = []


def alpha_n(volts):
    return (0.1 - (0.01 * volts)) / (exp(1 - (0.1 * volts)) - 1)

def alpha_m(volts):
    return (2.5 - (0.1 * volts)) / (exp(2.5 - (0.1 * volts)) - 1)

def alpha_h(volts):
    return 0.07 * exp((-1.0 * volts) / 20.0)

def beta_n(volts):
    return 0.125 * exp((-1.0 * volts) / 80.0)

def beta_m(volts):
    return 4.0 * exp((-1.0 * volts) / 18.0)

def beta_h(volts):
    return 1.0 / (exp(3.0 - (0.1 * volts)) + 1.0)

#derivative function

def m_dot(volts, m):
    return (alpha_m(volts) * (1 - m)) - (beta_m(volts) * m)

def n_dot(volts, n):
    return (alpha_n(volts) * (1 - n)) - (beta_n(volts) * n)

def h_dot(volts, h):
    return (alpha_h(volts) * (1 - h)) - (beta_h(volts) * h)

def m_infinity(volts):
    return alpha_m(volts) / (alpha_m(volts) + beta_m(volts))

def n_infinity(volts):
    return alpha_n(volts) / (alpha_n(volts) + beta_n(volts))

def h_infinity(volts):
    return alpha_h(volts) / (alpha_h(volts) + beta_h(volts))

def dvdt (cur_voltage, injection_current, hh_m, hh_n, hh_h):
    ina = gna * pow(hh_m, 3.0) * hh_h * (cur_voltage - ena)
    ik = gk * pow(hh_n, 4.0) * (cur_voltage - ek)
    il = gl * (injection_current - el)

    return injection_current - (ina + ik + il)

def update_values(old_value, rate_of_change, time_step): #updates the value of the previous value
    return ((rate_of_change &time_step) + old_value)

def between(injection_current, injection_start_time, injection_stop_time):
    if (injection_current >= injection_start_time and injection_current<= injection_stop_time):
        return  injection_current
    else:
        return 0

def run_sim():

    m = m_infinity(init_v)
    h = n_infinity(init_v)
    h = h_infinity(init_v)

    while start_t <= end_t:
        start_t += time_step
        new_times.append(start_t)
        between(injection_current, injection_start_time, injection_end_time)

        m = update_values (m, m_dot(init_v, m_sim), time_step)
        n = update_values(n, n_dot(init_v, n_sim), time_step)
        h = update_values(h, h_dot(init_v, h_sim), time_step)
        init_v = update_values(init_v, dvdt(init_v, injection_current, hh_m, hh_n, hh_h), time_step)


        voltages.append(init_v)
        new_times.append(start_t)

def graph():
    plt.plot(new_times, voltages)
    plt.xlabel ('times')
    plt.ylabel ('voltage')
    plt.show()



print(voltages)
print(new_times)

#graph()