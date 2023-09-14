import numpy as np

psi = np.zeros(10)
psi[0] = 1
psi[1] = 1
n = len(l) 

def V(x,a):
    if -a < x < a:
        return 0
    else:
        return 1000

for i in range(n-1):
    psi[i+1] = 2*psi[i] - psi[i-1] - 2*(E-V())* dx**2 * psi[i] 
print(l)
