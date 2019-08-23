#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def main(busCoordFn, linesFile, loadsFile):
    mpl.rcParams.update({'font.size': 20})


    #Process the buscoorinates data.
    with open(busCoordFn, 'r') as f:
        busCoords = f.read().splitlines()
    busData = [i.split() for i in busCoords]
    coordDict = dict({})
    for i in busData:
        coordDict[i[0]] = (float(i[1]), float(i[2]))
         
    with open(linesFile, 'r') as f:
        lines = f.read().splitlines()     
    lines = [i.split() for i in lines]

    with open(loadsFile, 'r') as f:
        loads = f.read().splitlines()
    loads = [i.split() for i in loads]
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.subplots()
    
    plt.scatter(coordDict['1'][0], coordDict['1'][1], s=80, c='r', 
                marker='h')

    #plotLines 
    for i in lines:
        x,y = zip(*[coordDict[i[0]], coordDict[i[1]]])
        plt.plot(x,y, 'k')
    
    
    color = {'1': '#FF7D0F', '2': '#6049B3', '3': '#0DB813'}
    # Plot Loads
    for i in loads:
        busName = i[1]
        phaseNum = i[2]
        customerNum = i[0].lstrip('LOAD')
        rndm = lambda : 1 #lambda : np.random.randint(0, 10)
        plt.scatter(coordDict[busName][0], coordDict[busName][1], s=40,
                c=color[phaseNum], marker='o', edgecolors=None)     
        plt.text(coordDict[busName][0]-rndm(), coordDict[busName][1]+rndm(), 
                    customerNum, fontsize=12)

    legend_elements = [Line2D([0], [0], marker='h', color='w', 
                    label='Substation', markerfacecolor='r', 
                    markersize=10),
                    Line2D([0], [0], marker='o', color='w', 
                    label='Phase a', markerfacecolor=color['1'], 
                    markersize=10),
                    Line2D([0], [0], marker='o', color='w', 
                    label='Phase b', markerfacecolor=color['2'], 
                    markersize=10),
                    Line2D([0], [0], marker='o', color='w', 
                    label='Phase c', markerfacecolor=color['3'], 
                    markersize=10)]
    ax.legend(handles=legend_elements)
    ax.axis('off')

    fig.savefig('gridDiagram.pdf')
 
 

if __name__ == "__main__":

    main(*sys.argv[1:])


