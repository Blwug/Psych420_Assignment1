res = 2
cap = 1
voltage = 3
current = 2
new_dv_dt = []
initial_time = 0
end_time = 2
time_step =.5
updated_time = []
def dv_dt (res, cap, voltage): #derivative of voltage in relation to time
    updated_dv_dt = (1/res*cap) * (res * current - voltage)
    new_dv_dt.append(updated_dv_dt)

def new_time (initial_time, updated_time):
    updated_time.append(initial_time)

while initial_time < end_time:
    initial_time += time_step

    new_time(initial_time, updated_time)
    dv_dt(res, cap, voltage)

print ("this is the the time value", updated_time)
print ("this is the derivative of voltage in relation to time", new_dv_dt)










