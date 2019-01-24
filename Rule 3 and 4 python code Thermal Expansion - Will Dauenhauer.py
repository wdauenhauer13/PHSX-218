
# coding: utf-8

# In[2]:


import numpy as np

def rule3(dA,dB): 
    dQ = np.sqrt(dA**2 + dB**2)
    return dQ

dT_i = 0.3 #C
dT_f = 0.1 #C

d_Delta_T = rule3(dT_i, dT_f)

print (d_Delta_T)



def rule4 (A,B,C,D,dB,dC,dD):
    d_alpha = A*np.sqrt((dB/B)**2+(dC/C)**2+(dD/D)**2)
    return d_alpha

alpha = .000017228 #m
Delta_L = .00125 #m
L = 1.05 #m
Delta_T = 69.1 #C
d_Delta_L =.00001 #m
d_L = .00125 #m
d_Delta_T = .3162 #C

err_alpha = rule4(alpha,Delta_L,L,Delta_T,d_Delta_L,d_L,d_Delta_T)

print (err_alpha)
1.6009697557183024e-07



def expansion (A,B,C):
    alpha = (A*B**-1*C**-1)
    return alpha

delta_L = .00125 #m
L = 1.05 #m
delta_T = 69.1 #C

alpha = expansion(delta_L,L,delta_T)

print(alpha)

