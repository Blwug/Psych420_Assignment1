#gK = n^4 *gK max
#gNa = m^3hgNamax
    #m  represents channel required to be open
    #h represents not opened chanenl
#Leak is not voltage dependent; constant to what the voltage is
#gK n = 1
#



def alpha_n (new_voltage, e): #potassium activation|if alpha>beta than increased liklihood for it to open
    function_alpham = -0.01 * ((new_voltage [-1] +60) / e**(new_voltage[-1] +60/-10))-1
    new_alpha_k.append(function_alpham)

def beta_n (new_voltage, e): #potassium activation | if beta is high then more likely for it to close
    function_beta_m = 0.125*e**((new_voltage[-1] +70)/80)
    new_beta_k.append(function_beta_m)

def alpha_m (new_voltage, e):
    function_alpha_na = -0.1*(new_voltage[-1] +45)/e**((new_voltage[-1]+45)/-10) -1
    new_alpha_na.append(function_alpha_na)

def beta_m (new_voltage, e):
    function_beta_na = 4*e**((new_voltage[-1]+70)/-18)
    new_beta_na.append(function_beta_na)

def alpha_h (new_voltage, e):
    function_alpha_h = 0.07*e**(new_voltage[-1]+40)/20
    new_alpha_h.append(function_alpha_h)

def beta_h (new_voltage, e):
    function_beta_h = 1/1+e**(new_voltage[-1]+40)/-10
    new_beta_h.append(function_beta_h)


#dv/dt = rate of change - voltage = 0 ii stim = 0, i ionic = 0
#the dv/dt formula = -(I subscript stim +I subscript ionic)/Cm
#I subscript ionic is equal to the sum of Na, K and leakage currents
#those formula are derived from g(E subscript m - E subscript eq)
    #equilibrium potentional is net ion flex being 0

#we need to define m dot, n dot and h. first
# q is charge and u is voltage
#neruon potentional = membrane potentional = effective potentional of sodium
#effective potentional * conductivaity

#g = gmax *f(V,t)
#	f = fraction of channels open which is based on votlage & time
#	if al sodium channels open then f = 1 then max conductance

#I total = C* dv/dt = (Vk-V)gk (V,t) +(Vna - V) gna(V,T) + (Vl-V) gl - membrane potentional
	#more voltage dependent and dependent on fraction channel

#f is open channel
#1-f is closed channels

#beta is when open channel closes

#potassium activation is gk = gkn^4 (v,t)
#g bar = max conductivty when all gates open

#n%4 is due to the activation gate being required to be max opened & all 4 needs to be opened
#for ion to pass

#f is called n for potassium
#alpha and beta are voltage dependent so that the potassium gate activate from ~0 and deactive when  below
#-20

#gna written down like m^3 3 activation gate

#h is the inactivation

#dm= open gate of am (v) * (1-m) - beta (voltage) m

#activates at -50 and deactivates below -30


#inactivatino is h = 0 given that gna = 0
#h is to the first power

#dh/dt = alphah (voltage) 1-h) - Bh(voltage) h
#slowly inactivate at -20 and deinactivate below -40

#adding the effective potentional and thje condcutive potentional

#conductive current is voltage dependent so that the potassium can bne said as a maxium
#condutance
#4 gates in each channel

#sodium  3 gates in each channel
#h is the inactivatino
#each of these gating varaibles represents the open to close states
#beta is open to close alpha is closed to open

#gL = gL (same conductance not voltage dependent

