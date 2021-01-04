import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from utils.generateOrbits import generate_orbit_iter

def plot_style(ax, title, xlabel, ylabel):
    if ax:
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    else:
        ax.xlabel(xlabel)
        ax.ylabel(ylabel)
        ax.title(title)
    

#########
def plot_many_orbits(ys,ax):
    lines = []
    for i, y in enumerate(ys):
        lines.append(ax.plot(y, marker="o",label=f"{i}"))
        
def plot_one_orbits(y,ax):
    return ax.plot(y, marker="o", label="0")

def plot_orbit(val, title, xlabel, ylabel, ax=None):
    ax = ax or plt.gca()
    plot_style(ax, title, xlabel, ylabel)
    if isinstance(val[0], list): 
        lines = plot_many_orbits(val,ax)
        ax.legend()
        return lines
    else: 
        lines = plot_one_orbits(val,ax)
        ax.legend()
        return lines
#########
    
def plot_func(func, lims, title, xlabel, ylabel, ax=None):
    ax = ax or plt.gca()
    plot_style(ax, title, xlabel, ylabel)
    initial, final = lims
    x = np.linspace(initial, final, 1000)
    y = list(map(func,x))
    
    line1 = ax.plot(x,y,label=f"{func.__name__}")
    line2 = ax.plot(x,x,label="y=x")
    
    ax.legend()
    
    return line1, line2

#########

def plot_bifurcation_diagram(func,x0, steps, r_step, round_param, rrange, labels, ax=None):
    
    
    title, xlabel, ylabel = labels
    ax = ax or plt.gca()
    plot_style(ax, title, xlabel, ylabel)
        
    initial_r, final_r = rrange
    rs = np.arange(initial_r, final_r+r_step, r_step)
    transition_r = []
    aux = 1
    
    lines = []
    for r in rs:
        func_r = partial(func, r)

        y = generate_orbit_iter(func_r, x0, steps)
        final_states = set(map(lambda x: round(x,round_param), y[-100:]))
        
        n_periods = len(final_states)
        for final_state in final_states:            
            if aux < n_periods :
                aux = n_periods
                transition_r.append(r)
            
            lines.append(ax.scatter(r, final_state, c = "r", s = 5))
            
    ax.legend()
    
    return transition_r,lines 