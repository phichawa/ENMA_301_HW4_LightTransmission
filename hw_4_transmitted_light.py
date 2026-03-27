# a more detailed explanation of how this program works can be found in the README file 

import math

# set the initial intensity
I0 = 10.0
I = I0

# refractive indices (including air)
n = [1.0, 1.489, 1.333, 1.460, 1.489, 1.0]

# absorption coefficients (m^-1)
alpha = [0.132, 0.097, 0.132, 0.132]

# thicknesses (m)
t = [0.002, 0.01, 0.002, 0.02]

# reflection function
def reflection(n1, n2):
    return ((n1 - n2) / (n1 + n2))**2

# loop through each of the materials
for i in range(len(alpha)):
    # reflection at interface
    R = reflection(n[i], n[i+1])
    T = 1 - R
    I = I * T

    # absorption through material
    I = I * math.exp(-alpha[i] * t[i])

# final interface
R_final = reflection(n[-2], n[-1])
I = I * (1 - R_final)

# print final light transmittion output
print("The final transmitted intensity is ", I, "W/m^2")
print("The final percent transmitted is ", (I / I0) * 100, "%")
