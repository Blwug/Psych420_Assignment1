def m_dot (new_alpha_m, new_beta_m, m):
    function_m_dot = (new_alpha_m[-1] * (1- m)) - (new_beta_m[-1] * m)
    new_function_m_dot.append(function_m_dot[-1])

def m_infinity(new_alpha_m, new_beta_m):
    function_m_infinity = new_alpha_m[-1]/(new_alpha_m[-1] + new_beta_m[-1])
    new_function_m_infinity.append(function_m_infinity)






def update(old_value, rate_of_change, time_step):
  return ((rate_of_change * time_step) + old_value)

