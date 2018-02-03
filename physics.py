#Stokes' Law
# Force = 6π * eta * R * V

# eta = viscosity. R = radius. V = velocity


import math

def calc_friction(viscosity, radius, velocity):
    return 6 * math.pi * viscosity * radius * velocity
