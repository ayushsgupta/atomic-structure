import re
import matplotlib.pyplot as plt
import Constants
from Orbital import Orbital
from Nucleus import Nucleus

# 9-27-17

class Atom:

    def __init__(self, symbol):
        # if len(configuration) < 3:
        self.symbol = symbol
        self.configuration = Constants.CONFIGURATION[symbol] # Need to add error handling

        '''
        else:
            self.configuration = configuration # Need to add reverse of element-->configuration
        '''

        self.orbitals = list()
        self.fillOrbitals()

        self.nucleus = Nucleus(self.symbol)

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
        if which in range(0, len(self.orbitals)):
            return self.orbitals[which]
        else:
            return self.orbitals[-1]

    def getNumElectrons(self):
        n = 0
        for o in self.orbitals:
            n += o.getNumElectrons()
        return n

    def getAtomicNumber(self):
        return self.nucleus.getNumProtons()

    def getAtomicMass(self):
        return self.nucleus.getMassNumber()

    def getCharge(self):
        charge = 0
        for o in self.orbitals:
            charge += o.getOrbitalCharge()
        charge += self.nucleus.getNuclearCharge()
        return charge

    def ionize(self, n = 1):
        i = -1
        for t in range(0, n):
            while i >= (-1 * len(self.orbitals)):
                if not self.orbitals[i].isEmpty():
                    self.orbitals[i].ionize()
                    break
                else:
                    i -= 1

    def getSymbol(self):
        if self.getCharge() is 0:
            return self.symbol
        elif self.getCharge > 0:
            return "%s%d+" % (self.symbol, self.getCharge())
        else:
            return "%s%d-" % (self.symbol, -self.getCharge())
