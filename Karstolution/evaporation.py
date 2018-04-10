import numpy as np
try:
    from numba import jit
except ImportError:
    # do-nothing decorator
    jit = lambda x:x

@jit
def evaporation(TC, h, V):
    T = 273.15 + TC  #absolute temperature (K)
    E = np.exp(-6094.4642/T + 21.1249952 - 2.724552e-2*T + 1.6853396e-5*T**2 + 2.4575506*np.log(T))
    E = E/1.3332e2
    A = np.pi*0.017841241**2

    eva = A * (0.002198 + 0.0398*V**0.5756) * E * (1-h)*1000/3600/18

    return eva
