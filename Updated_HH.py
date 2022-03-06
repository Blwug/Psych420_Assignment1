from math import exp
import matplotlib

start_t = 0.0
time_step = 0.4
end_t = 10.0
init_v = 0.0

new_times = []
voltages = []

ena = 115.0
gna = 120.0
ek = -12.0
gk = 36.0
el = 10.6
gl = 0.3

injection_time  = 0.0
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

def dvdt (cur_voltage, cur_injection, hh_m, hh_n, hh_h):
    ina = gna * pow(hh_m, 3.0) * hh_h * (cur_voltage - ena)
    ik = gk * pow(hh_n, 4.0) * (cur_voltage - ek)
    il = gl * (cur_voltage - el)

    return cur_injection - (ina + ik + il)

def update_values(old_value, rate_of_change, time_step): #updates the value of the previous value
    return ((rate_of_change &time_step) + old_value)

def between(x, injection_start_time, injection_stop_time, injection_current):
    if (x >= injection_start_time and x<= injection_stop_time):
        return injection_current
    else:
        return 0

def run_sim():

    m_sim = m_infinity(init_v)
    n_sim = n_infinity(init_v)
    h_sim = h_infinity(init_v)

    while start_t <= end_t:
        start_t += time_step
        new_times.append(start_t)
        m_sim = update_values (m_sim, m_dot(init_v, m_sim), time_step)
        n_sim = update_values(n_sim, n_dot(init_v, n_sim), time_step)
        h_sim = update_values(h_sim, h_dot(init_v, h_sim), time_step)
        init_v = update_values(init_v, dvdt(init_v, cur_injection, hh_m, hh_n, hh_h), time_step)

        voltages.append(init_v)

    def graph():
        plt.plot(new_times, voltages)
        plt.xlabel ('times')
        plt.ylabel ('voltage')
        plt.show()


between(0.02, 450.0, 50.0, 300.0, 7.0)
plot_graph()
