new = 1.2
time_step = 0.4
goal = 1.6
init_time = 0
time_end = 2
cur_time = [init_time]
stop = []

while True:
    if init_time == goal:
        stop = 1
        break
    else:
            if init_time < time_end:
                stop = 0
                init_time += time_step
                cur_time.append(init_time)




print(cur_time)
print(stop)
