import re
import matplotlib.pyplot as plt
import Constants
from Orbital import Orbital

# 9-27-17

class Atom:

    def __init__(self, configuration):
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
