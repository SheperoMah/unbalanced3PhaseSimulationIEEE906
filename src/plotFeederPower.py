#!/usr/bin/env python3

import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def main(flName,writeName):
    mpl.rcParams['font.size'] = 18

    results = np.genfromtxt(flName, names=True, delimiter=', ')
    powerA = results['S1_kVA']
    powerB = results['S2_kVA']
    powerC = results['S3_kVA']
    
    powerA[::-1].sort()
    powerB[::-1].sort() 
    powerC[::-1].sort()

    fig, ax = plt.subplots(1,1, figsize=(6,6))
    ax.plot(powerA)
    ax.plot(powerB)
    ax.plot(powerC)  
    ax.set_xlim(0)
    ax.set_xticks([2*8760*i for i in range(0,4)])
    ax.legend([r'$s_a$', r'$s_b$', r'$s_c$'])
    ax.set_xlabel('Number of time-steps (30-min)')
    ax.set_ylabel('Apparent power (kVA)')
    ax.grid(True)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    fig.savefig(writeName)

if __name__ == "__main__":
    main(*sys.argv[1:])
