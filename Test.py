import matplotlib.pyplot as plt


def update_acceleration(positions, accelerations, spring_constant):
    """ Update the acceleration"""
    a1 = -1 * positions[-1] * spring_constant
    accelerations.append(a1)  # Adding the acceleration to the list.


def update_velocity(speeds, accelerations, delta_t):
    """ Update the speed"""
    v1 = speeds[-1] + accelerations[-1] * delta_t
    speeds.append(v1)


def update_position(positions, speeds, delta_t):
    """ Update the position"""
    p1 = positions[-1] + speeds[-1] * delta_t
    positions.append(p1)


def update_times(times, current_time):
    times.append(current_time)


# Square brackets means this is a list.
delta_t = 0.1  # deltaT never changes.
spring_constant = 3.0  # never changes
measurement_times = [0]  # An array that stores each time that a measurement is made.
positions = [-10]
speeds = [0]
accelerations = []
run_time = 10.0  # seconds

# Update the acceleration
update_acceleration(positions, accelerations, spring_constant)

current_time = 0
while current_time < run_time:
    current_time = current_time + delta_t
    update_times(measurement_times, current_time)

    # Our pathway is:
    # 1. Find Acceleration
    update_acceleration(positions, accelerations, spring_constant)

    # 2. Find Velocity/Speed
    update_velocity(speeds, accelerations, delta_t)

    # 3. Find Position
    update_position(positions, speeds, delta_t)

print(measurement_times)
print(positions)
print(speeds)