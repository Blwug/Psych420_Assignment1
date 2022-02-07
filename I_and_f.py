voltage = 1.0
initial_voltage = voltage
initial_time = 1.0
stop_time = 10.0
#this was too big
time_step = .05
# Careful with your numbers. Python
# treats integers differently from floats at times.
cap = 2.0
res = 1.0
#Don't do things like this.
#Just clutters the code and does
#not help understanding
#### one = 1 #####
tau = cap * res
new_acc_value = []
updated_time = []
new_voltage = []

# Initial implies first, but you are not using this to add the first
# time every time. Give it a more descriptive and accurate name.
# And probably don't need a function for this at all. Small functions
# doing one thing are good, but not if the can be replaced with a one liner -
# that takes no more room than the function call: time.append(time[-1] + time_step)
def times (initial_time, updated_time): #this stores the new value of time
    updated_time.append(initial_time)

# What were you trying to achieve with "one"?
# def acc (tau, one, voltage): # this stores the new value of acceleration, dv/dt
#     updated_acc = (one/tau) * (tau - voltage)
#     new_acc_value.append(updated_acc)

#The integrate and fire model does not have an acceleration. What is this supposed to be?
def acc (tau, voltage): # this stores the new value of acceleration, dv/dt
    #I don't know where this formula came from. It is not like anything in the notes.
    updated_acc = (1/tau) * (tau - voltage)
    new_acc_value.append(updated_acc)

#This is my start time
time = [0.0]
#while initial_time <= stop_time:
while time[-1] <= stop_time:
    #you are not using your times function so delete it above
    time.append(time[-1] + time_step)
    acc(tau,voltage)
    # Next line serves no purpose.
    times(initial_time, updated_time)
   # voltages(voltage, new_acc_value, updated_time)

   #You have not defined a local function that you never use
   #I have no idea why this is here.
    def voltages (voltage, new_acc_value, updated_time): #this should get the new value of voltage
        updated_voltage = voltage + new_acc_value *updated_time
        new_voltage.append(updated_voltage)


print (new_acc_value)
print (updated_time)
print(new_voltage)


# There is nothing here to suggest you followed my last advice. You don't understand the algorithm so
# You cannot code it. No surprise. Write out BY HAND the different stages of the algorithm, their
# equations and how they connect. Then, maybe, you will be able to start coding the pieces.


#def update_voltage (voltage, ):




#set the value of voltage
#update the value of voltage using dv/dt
#then update the value of voltage using old voltage + dv/dt*time_step

#break down the questions to make it tolerable to do

