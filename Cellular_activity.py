a = 1.4
time_step = .2
stop = 2.0
new_ina = [1.0]
new_ik = [1.0]
new_il = [1.0]

gna = 2.0
hh_m = 2.0
hh_h = 2.0
hh_n = 2.0
gk = 2.0
ek = 2.0


new_not_dv_dt_value = [1]

def fx_ina (gna, hh_m, new_voltage, ena, hh_h):
    ina = gna * pow(hh_m, 3.0) * hh_h & (new_voltage[-1] - ena)
    new_ina.append(ina)

def fx_ik (gk, hh_n, new_voltage, ek):
    ik = gk * pow(hh_n, 4) *(new_voltage[-1] - ek)
    new_ik.append(ik)

def fx_il (gl, new_voltage, el):
    il = gl * (new_voltage[-1] - el)
    new_il.append(il)

def not_dv_dt (new_ina, new_ik, new_il):
    function_not_dv_dt = (new_ina + new_ik + new_il)
    new_not_dv_dt_value.append(function_not_dv_dt)


while a <= 1.999:
    a += time_step
    not_dv_dt(new_ina[-1], new_ik[-1], new_il[-1])

print(new_not_dv_dt_value)
print(a)
