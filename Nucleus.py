from Proton import Proton
from Neutron import Neutron
import Constants

class Nucleus:

    def __init__(self, element):
        self.protons = list()
        self.neutrons = list()
        self.element = element

        self.__fillProtons()
        self.__fillNeutrons()

    def __fillProtons(self):
        for p in range(0, Constants.ATOMIC_NUMBER[self.element]):
            self.protons.append(Proton())

    def __fillNeutrons(self):
        for n in range(0, (Constants.MASS_NUMBER[self.element] - Constants.ATOMIC_NUMBER[self.element])):
            self.neutrons.append(Neutron())

    def getMassNumber(self):
        return (len(self.protons) + len(self.neutrons))

    def getProtons(self):
        return self.protons

    def getNumProtons(self):
        return len(self.protons)

    def getNeutrons(self):
        return self.neutrons

    def getNumNeutrons(self):
        return len(self.neutrons)

    def getNuclearCharge(self):
        charge = 0
        for p in self.protons:
            charge += p.getProtonCharge()
        return charge
