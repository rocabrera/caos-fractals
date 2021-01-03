import numpy as np

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