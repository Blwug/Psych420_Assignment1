voltage = 0
init_t = 0
stop_time = 14
time_step = .1
cap = 1
res = 2
voltage_tol = 4
max_voltage = 8
resting_potential = 0
current = 1

new_t = []

def times (init_t, new_t):
    new_t.append (init_t)

while init_t <stop_time:
    init_t += time_step
    times (init_t, new_t)

print(new_t)
