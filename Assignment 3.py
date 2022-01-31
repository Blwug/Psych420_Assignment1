
#equation goes here

dt = .05
max_t = 10
init_t = 0
start_time = 1
stop_time = 6
cap = 1
res = 2
threshold = 3
spike_display = 8
init_v = 0
voltage = init_v
injection_current = 4.3
#def injection_time = (start_time, stop_time):
tau = res*cap
#these are the paramaters necessarily
neg_one = -1
one = 1

#we need to write def dv/dt = [-v(t) + R*I(t)](1/t)
def dv_dt (voltage, res, tau):
    vel_change_time = (((neg_one*(voltage))*tau) +(res * init_t)*(one/tau))

print (vel_change_time)