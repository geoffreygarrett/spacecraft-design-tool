# -*- coding: utf-8 -*-
"""
Created on Sun Apr 01 23:19:32 2018

@author: Vladimir
"""

import numpy as np

#Total power

P_pavg = 74 #Average payload power
P_pp = 124.6 #Peak payload power

P_tp = 332.93*np.log(P_pp) - 1047

print('Peak power:')
print(P_tp)


#Solar array calculations

R = 69911.  #Radius
h = 5500.   #Orbital height
mu_j = 126.687*10**6
lambda_j = 30.   #Degrees in eclipse


#Orbital, eclipse and day period in minutes
#Assumption: circular orbit

T_t_sec = 2*np.pi*np.sqrt((R+h)**3/(mu_j))
T_t = T_t_sec/60

T_e_sec = (2*lambda_j)*T_t_sec/(360)
T_e = T_e_sec/60

T_d = T_t - T_e

print('Periods:')
print(T_t)
print(T_e)
print(T_d)

#Power required 

X_e = 0.6
X_d = 0.8
P_e = P_tp #Power required during eclipse
P_d = P_tp #Power required during daylight

P_sa = ((T_e*P_e/X_e)+(T_d*P_d/X_d))/(T_d)

print('P_sa:')
print(P_sa)

#Power at EOL classic way

J_j = 50.26  #Solar irradiance
c_eff = 26.8 #Solar cell efficiency
c_deg = 1.5  #Solar cell degradation
I_d = 0.77   #Inherent degradation due to shadowing & other design inefficiencies
theta = 10   #Panel inclination
sat_life = 4  #Satellite mission duration + transfer orbit


P_o = J_j*c_eff/100  #Efficiency of cell given solar irradiance

P_BOL = P_o*I_d*np.cos(theta*np.pi/180)

L_d = (1-1.5/100)**sat_life #Degradation of solar cell

P_EOL = P_BOL*L_d

#Solar array area

A_sa = P_sa/P_EOL

print('A_sa:')
print((A_sa))



#Power at EOL Geoffrey way

P_BOLG = P_sa/L_d

dej = 5  #Ratio of solar distance of Jupiter to Earth's solar distance 
ppa = 3.12*10**3 #Power per area
n = 0.1 #??


A_saG = P_BOLG*(5)**2/(ppa*n)

print('A_sa the Geoffrey way')
print(A_saG)

