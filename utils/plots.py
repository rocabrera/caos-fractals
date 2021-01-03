import numpy as np
import matplotlib.pyplot as plt

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