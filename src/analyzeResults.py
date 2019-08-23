#!/usr/bin/env python3

import os
import sys
import json
from json import encoder
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



def analyzeVoltage(voltageArray, axis=0):
    """ Analyzes the voltages
    
    parameters
    ----------
    voltageArray: numpy.array(n, 3)
    
    returns
    -------
    
    """
    results = dict({'uQuant': np.quantile(voltageArray, 0.95, 
                                axis).tolist()})
    results['lQuant'] = np.quantile(voltageArray, 0.05, 
                                axis).tolist() 
    results['max'] = np.max(voltageArray, axis).tolist()
    results['min'] = np.min(voltageArray, axis).tolist()
    return(results) 



def main(caseName, meterFn, directory, writeDirectory):
    mpl.rcParams['font.size'] = 18
   
    gridMeterResults = pd.read_csv(directory + meterFn, 
                        delimiter=',\s', engine='python') 
    gridMeterResultsDict = {'Max kW': float(gridMeterResults['"Max kW"'][0]),
                        'Max kVA': float(gridMeterResults['"Max kVA"'][0]),
                        'Zone Losses kWh': float(gridMeterResults[
                                '"Zone Losses kWh"'][0]),
                        'Zone Losses kvarh': float(gridMeterResults[
                                '"Zone Losses kvarh"'][0])}
    files = [directory + fl for fl in os.listdir(directory) if 
                fl.startswith(caseName)]
    voltage = dict({}) 
    for fl in files:
        busNumber = fl.lstrip(directory + caseName).rstrip('.csv')
        resultsMatrix = np.genfromtxt(fl, delimiter=', ', names=True)
        voltage[busNumber] = np.stack((resultsMatrix['V1'], 
                                        resultsMatrix['V2'], 
                                        resultsMatrix['V3'])
                                    ).transpose()/230 

    voltages = np.concatenate([i for i in voltage.values()], axis=0)
    gridSummary = analyzeVoltage(voltages, axis=None) 
    summary = dict({})
    #Analyze the results of each bus 
    for key, value in voltage.items():
           summary[key] = analyzeVoltage(value)
    
    fullResults = dict({'Grid Energy Summary': gridMeterResultsDict,
                    'Grid Summary': gridSummary, 
                    'Bus Summary': summary}) 
    
    resultsFileName = writeDirectory + caseName.split('_')[0] + \
                        '.json'
    with open(resultsFileName, 'w') as f:
         json.dump(fullResults, f, indent=2)
    

    # Plot histogram of the voltages
    fig, axs = plt.subplots(1, 3, sharey=True, tight_layout=True,
                        figsize=(8,8*9/16))
    axs[0].hist(voltages[:,0], 100, density=True) 
    axs[0].set_title(r'Phase $a$')
    axs[0].set_xlabel('Volt (pu)')
    axs[0].set_ylabel('Probability')
    axs[0].set_xlim(0.90, 1.1)
    axs[1].hist(voltages[:,1], 100, density=True) 
    axs[1].set_xlim(0.90, 1.1)
    axs[1].set_title(r'Phase $b$')
    axs[1].set_xlabel('Volt (pu)')
    axs[2].hist(voltages[:,2], 100, density=True) 
    axs[2].set_xlim(0.90, 1.1)
    axs[2].set_title(r'Phase $c$')
    axs[2].set_xlabel('Volt (pu)')
    #plt.show()
    fig.savefig(writeDirectory + caseName.split('_')[0]+'.pdf')



    mpl.rcParams['font.size'] = 21
    fig, axs = plt.subplots(1,1, figsize=(6,6), 
                subplot_kw={'position': [0.2, 0.2, 0.75, 0.75]})
    axs.violinplot(voltages, [1,2,3], showmedians=True, showextrema=True)
    axs.set_xticks([1,2,3])
    axs.set_xticklabels([r'Phase $a$', r'Phase $b$', 'Phase $c$'])
    axs.set_yticks([0.90, 0.95, 1.00, 1.05, 1.10])
    axs.set_ylim(0.88, 1.12)
    axs.set_ylabel('Voltage (pu)')
    fig.savefig(writeDirectory + caseName.split('_')[0]+'violin.pdf')


if __name__ == "__main__":
    main(*sys.argv[1:])
