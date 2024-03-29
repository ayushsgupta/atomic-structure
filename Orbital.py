from Electron import Electron
import Constants

# 9-27-17
# Latest update 10-1-17

class Orbital:

    '''
    Attributes:
        1. pqn - the energy level of the orbital
        2. azqn - the shape of the orbital (0:s, 1:p, 2:d, 3:f)
        3. mqn - the orientation of the orbital (NOT CURRENTLY)
        4. up to 2 electrons - 0, 1, or 2
        5. max_capacity: 2
    '''

    def __init__(self, pqn, azqn):
        self.electrons = list()
        self.pqn = pqn
        self.azqn = azqn

        if self.azqn is 0:
            self.max_capacity = 2
        elif self.azqn is 1:
            self.max_capacity = 6
        elif self.azqn is 2:
            self.max_capacity = 10
        elif self.azqn is 3:
            self.max_capacity = 14

    def __str__(self):
        return "<Orbital: n = %s, l = %s (%s), num_electrons = %s, max_capacity = %s>" % (self.pqn, self.azqn, self.getAzqn_asChar(), len(self.electrons), self.max_capacity)

    def addElectron(self):
        if len(self.electrons) < self.max_capacity:
            if self.electrons:
                set_spin = (self.electrons[0].getSqn()) * -1
            else:
                set_spin = 0.5
            self.electrons.append(Electron(self.pqn, self.azqn, set_spin))

    def getPqn(self):
        return self.pqn

    def getAzqn(self):
        return self.azqn

    def getAzqn_asChar(self):
        return Constants.AZDICT2[self.azqn]

    def getElectrons(self):
        return self.electrons

    def getElectron(self, which):
        if which in range(0, len(self.electrons)):
            return self.electrons[which]
        else:
            return self.electrons[0]

    def getMaxCapacity(self):
        return self.max_capacity

    def getNumElectrons(self):
        return len(self.electrons)

    def getEmptySpaces(self):
        return self.getMaxCapacity() - self.getNumElectrons()

    def isEmpty(self):
        return len(self.electrons) is 0

    def getShortForm(self):
        return "%s%s%s" % (self.getPqn(), self.getAzqn_asChar(), self.getNumElectrons())

    def getOrbitalCharge(self):
        charge = 0
        for e in self.electrons:
            charge += e.getElectronCharge()
        return charge

    def ionize(self):
        self.electrons.pop()
