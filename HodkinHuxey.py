import matplotlib.pyplot as plt
import math

voltage = 1
init_t = 0
start_time = 0
end_time = 16
time_step = .1
cap = 1
res = 2
volt_t = 3
max_volt = 8
injection_current = ()
tau = cap * res
ena = 115
gna = 120
ek = -12
gk = 36
el = 10.6
gl = 0.3

new_t = [init_t]
voltages = [voltage]


init_injection = 1
new_injection = [init_injection]



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

def m_dot(volt, m):
    return (alpha_m(volt) * (1 - m)) - (beta_m(volt) * m)

def n_dot(volt, n):
    return (alpha_n(volt) * (1 - n)) - (beta_n(volt) * n)

def h_dot(volt, h):
    return (alpha_h(volt) * (1 - h)) - (beta_h(volt) * h)

def m_infinity(volt):
    return alpha_m(volt) / (alpha_m(volt) + beta_m(volt))

def n_infinity(volt):
    return alpha_n(volt) / (alpha_n(volt) + beta_n(volt))

def h_infinity(volt):
    return alpha_h(volt) / (alpha_h(volt) + beta_h(volt))

def times (init_t, new_t):
    new_t.append(init_t)

def vt (voltage, time_step):
    return (voltage + dvdt) * time_step

current_voltage = vt

def injection_time(init_injection, new_injection):
    new_injection.append (init_injection)


def dvdt (current_voltage, current_injection, m, n, h):   #values that we need to allow the argument to pass

    ina = gna * pow(m, 3.0) * h * (current_voltage - ena)
    ik = gk * pow(n, 4.0) * (current_voltage - ek)
    il = gl * (current_voltage - el)

    return current_injection - (ina + ik + il)

def between (x, new_injection):

    if (x >= new_injection[0]) and (x <= new_injection[1]):
        return injection_current
    else:
        return 0


while init_t < end_time:
    init_t += time_step
    times(init_t, new_t)


    #h_sim = h_dot(voltage, h_sim)
    #n_sim = n_dot(voltage, n_sim)
    #m_sim = m_sim(voltage, m_sim)

    #m_sim = m_infinity(voltage)
    #n_sim = n_infinity(voltage)
    #h_sim = h_infinity(voltage)

    #voltages.append(h_sim)

print (new_t)

def plot_graph():
  plt.plot(new_t, voltages)
  plt.xlabel('Time')
  plt.ylabel('Voltage')
  plt.title('Voltage-Time Graph')
  plt.show()












