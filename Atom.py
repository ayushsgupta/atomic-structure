import re
import matplotlib.pyplot as plt
import Constants
from Orbital import Orbital

# 9-27-17

class Atom:

    def __init__(self, configuration):
        if len(configuration) < 3:
            self.configuration = Constants.CONFIGURATION(configuration) # Need to add error handling
        else:
            self.configuration = configuration
        self.orbitals = list()
        self.fillOrbitals()

    def fillOrbitals(self):
        filled = re.findall(r'\d[spdf]\d{1,2}', self.configuration)
        for o in filled:
            self.orbitals.append(Orbital(int(o[0]), Constants.AZDICT1[o[1]]))
            if len(o) is 4:
                num_electrons = int(o[2:4])
            elif len(o) is 3:
                num_electrons = int(o[2])
            for x in range(0, num_electrons):
                self.orbitals[-1].addElectron()
    
    def getConfiguration(self):
        return self.configuration
    
    def getOrbitals(self):
        return self.orbitals
    
    def getOrbital(self, which):
        if which in [0:len(orbitals)]:
            return self.orbitals[which]
        else:
            return self.orbitals[-1]
