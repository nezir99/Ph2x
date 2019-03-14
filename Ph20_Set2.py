import numpy as np
from os import sys
import matplotlib.pyplot as plt 
from scipy import integrate
from scipy.special import erf

expression = (sys.argv[1])
a = float(sys.argv[2])
b = float(sys.argv[3])  
N = int(sys.argv[4])
accuracy = float(sys.argv[5])



def integrateTR(func, a, b, N):
    hN = (b - a) / N
    xN = np.linspace(a, b, N + 1)    
    _sum = func(xN[0])/2 + func(xN[1:-1]).sum() + func(xN[-1])/2
    return _sum * hN
    
if expression == "e^x":
    func = np.exp
def integrateSEF(func, a, b, N): 
    ar = np.arange(0, N + 1)
    ar2 = ar % 2 == 1
    ar3 = (ar2 + 1) * 2    
    hN = (b - a) / N
    xN = np.linspace(a, b, N + 1)
    _sum = func(xN[0]) + func(xN[-1]) + (ar3[1:-1] \
                                         * func(xN[1:-1])).sum()
    return np.sum(_sum * (hN / 3))


def rel_accuracy(func, a, b, accuracy):
    n = 2
    while abs((integrateSEF(func, a, b, n * N) - (integrateSEF(func, a, b, \
        (2 * n) * N))/integrateSEF(func, a, b, n * N))) > accuracy:
        n = 2*n
    return integrateSEF(func, a, b, N)
     
        
print(rel_accuracy(func, a, b, accuracy))
#print(integrateSEF(func, a, b, N))

errorSEF = [integrateSEF(func, a, b, N) - (np.e - 1) for N in range(2,10000,2)]
lst_N = [N for N in range(2, 10000, 2)]

errorTR = [integrateTR(func, a, b, N) - (np.e - 1) for N in range(2,10000,2)]

#gaussian = lambda x: 1/np.sqrt(np.pi) * np.exp(np.e ** x)
#result = integrate.romberg(gaussian, 0, 1, show=True)
#errorROM = [integrateTR(func, a, b, N) - (np.e - 1) for N in range(2,10000,2)]

#plt.loglog(lst_N, errorROM, label = "error")
#plt.xlabel("N")
#plt.ylabel("Error")
#plt.savefig("Plot.png")
#plt.legend()
#plt.show()

plt.loglog(lst_N, errorSEF, label = "Simpson's")
plt.loglog(lst_N, errorTR, label = "Trapezoidal")
plt.xlabel("N")
plt.ylabel("Error")
plt.savefig("Ph20_Set2_Plot.png")
plt.legend()
#plt.show()

