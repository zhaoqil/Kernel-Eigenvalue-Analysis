import numpy as np
from helper_fun import eigen_n_sphere
from kernels import k1, k2, k3, k4
import matplotlib.pyplot as plt

# eigenvalues for dim = 3
    
N = 500
rho = 0.3
kappa = 0.2
d1 = eigen_n_sphere(N, 3, k1, 1)
d2 = eigen_n_sphere(N, 3, k2, 1)
d3 = eigen_n_sphere(N, 3, k3, rho)
d4 = eigen_n_sphere(N, 3, k4, kappa)
w1 = d1['eig_val']
w2 = d2['eig_val']
w3 = d3['eig_val']
#print("w3 experiment: ", w3)
w4 = d4['eig_val']

ind = np.linspace(1,N, num = N)
w1_anal = 1/(ind * (ind+1) * (2*ind+1))
#w1_anal2 = 1/(ind ** 1.25)
#w1_anal3 = 1/(ind ** 2)
w2_anal = 1/((2*ind-1) * (2*ind+1) * (2*ind+3))
w3_anal = 4*np.pi/(2*ind+1)*rho**ind * N
#print("w3 analytic: ", w3_anal)
w4_anal = kappa**ind

fig, ax = plt.subplots()
cols = ['red', 'blue', 'purple', 'orange']
ax.plot(w1, c=cols[0], label='k1')
#ax.plot(w1_anal, c = 'green', label = 'k1_anal')
#ax.plot(w1 / w1_anal, c = cols[0], label = 'error_1')
#ax.plot(w1 / w1_anal2, c = cols[1], label = 'error_2')
#ax.plot(w1 / w1_anal3, c = cols[2], label = 'error_3')
ax.plot(w2, c=cols[1], label='k2')
#ax.plot(w2 / w2_anal, c = cols[1], label = 'error_2')
#print(w3[0:50] / w3_anal[0:50])
#ax.plot(w3[0:50] / w3_anal[0:50], c = cols[2], label = 'error_3')
#ax.plot(w4 / w4_anal, c = cols[3], label = 'error_4')
ax.plot(w3, c=cols[2], label='k3')
ax.plot(w4, c=cols[3], label='k4')
ax.set_yscale('log')
plt.legend(loc='lower left')
plt.xlabel("Index")
plt.ylabel("w")
plt.show()

# Problems with k1 and k2 are similar