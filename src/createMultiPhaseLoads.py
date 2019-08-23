#!/usr/bin/env python3

import sys
import numpy as np
from itertools import chain
class Load:                                                                    
    def __init__(self, name, numphases, bus, phase, loadShape, volts, 
        power, pf=0.95, vminPu=0.9, vmaxPu=1.1):
        self.name = name                                                       
        self.numphases = numphases                                             
        self.bus = bus                                                         
        self.phase = phase  
        self.loadShape = loadShape                                             
        self.volts = volts                                                     
        self.power = power                                                     
        self.pf = pf                                                           
        self.vminPu = vminPu                                                   
        self.vmaxPu = vmaxPu                                                   
                                                                               
    def toOpenDss(self):                                                       
        return(f"New Load.{self.name} Phases={self.numphases} "+               
            f"Bus1={self.bus}.{self.phase} kV={self.volts} "+            
            f"PF={self.pf} kW={self.power} Yearly={self.loadShape} " + 
            f"Vminpu={self.vminPu} Vmaxpu={self.vmaxPu} ")                     
                                                                               
    def divideToTwoPhases(self):                                               
        secondPhase = self.phase % 3 + 1 # shift one Phase up.
        newPower = self.power/2                                                
        load1 = Load(self.name + f"_{self.phase}", 1, self.bus, 
                    self.phase, self.loadShape, self.volts, newPower, 
                    self.pf, self.vminPu, self.vmaxPu)                                  
                                                                               
        load2 = Load(self.name + f"_{secondPhase}", 1, self.bus,               
                    secondPhase, self.loadShape, self.volts, newPower,         
                    self.pf, self.vminPu, self.vmaxPu)                         
        return((load1,load2)) 

def main(fn):

    with open(fn, 'r') as f:
        fileData = f.readlines()
    fileData = [i.split() for i in fileData]
    
    loads = [Load(name=i[1].split('.')[1], 
                numphases=1, 
                bus=int(i[3].split('=')[1].split('.')[0]),
                phase=int(i[3].split('=')[1].split('.')[1]),
                loadShape=i[6].split('=')[1],
                volts=0.23,
                power=float(i[9].split('=')[1]))
            for i in fileData]
    loadsDivided = [i.divideToTwoPhases() for i in loads] 
    loadString = [[i[0].toOpenDss(), i[1].toOpenDss()] 
                    for i in loadsDivided]
    flattenedList = list(chain.from_iterable(loadString))

    with open('newLoad.txt', 'w') as f:
        for line in flattenedList:
            f.write(f"{line} \n")    


if __name__ == "__main__":
    main(*sys.argv[1:])
