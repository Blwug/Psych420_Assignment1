from math import exp
hh_m = [2.0]
a = 1.4
stop = 2.0
time_step = 0.2
_hh_m = 2
gna = 4.0
volts = 3.0
new_ina = [1.0]
ena = 4.0
xx1 = [1]


#def fx_ina(gna, hh_m, volts, ena, hh_h, current_time):
 #   ina = (gna * pow(hh_m, 3.0) * hh_h & (volts - ena) * current_time)
  #  new_ina.append(ina)
new_alpha_n  = []

def alpha_n(volts):  #general formula, we'll specify the value within the update function
    function_alpha_n = (2.5 - (0.1 * volts)) / (exp(2.5 - (0.1 * volts)) - 1)
    new_alpha_n.append(function_alpha_n)

def _hh_m(x):
    temp = x * 2
    hh_m.append(temp)

def fx_ina(hh_m):
    ina = pow(hh_m, 3.0)
    new_ina.append(ina)

def temp_alpha_n(x):
    x = x + 3
    xx1.append(x)

while a < stop:
    a += 0.2

_hh_m(hh_m[-1])
fx_ina(hh_m[-1])
temp_alpha_n(hh_m[-1])


print("ina " +str(new_ina))
print("hh_m " +str(hh_m))
print(xx1)


