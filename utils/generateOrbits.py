import numpy as np

import sys   
sys.setrecursionlimit(10**6) 

def last_value_orbit(func, x0, n):

    if n == 0: return x0
    
    next_x0 = func(x0)
    return last_value_orbit(func, next_x0, n-1)
    
def generate_orbit(func, x0, n, lst):

    if n == 0:
        lst.append(x0)
        return lst
        
    lst.append(x0)
    next_x0 = func(x0)
    return generate_orbit(func, next_x0, n-1, lst)

def generate_orbit_iter(func, x0, steps):
    val = x0
    orbit_results = [val]
    for _ in range(steps):
        next_val = func(val)
        orbit_results.append(next_val)
        val = next_val
        
    return orbit_results