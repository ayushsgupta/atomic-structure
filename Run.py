import Constants
from Atom import Atom

cu = Atom('Cu')
print 'Atomic mass of Cu:', cu.getAtomicMass()
print 'Number of protons:', cu.getAtomicNumber()
print 'Number of electrons:', cu.getNumElectrons()
cu.ionize(2)
print 'After 2 ionizations:', cu.getSymbol()
print 'Atomic mass of Cu:', cu.getAtomicMass()
print 'Number of protons:', cu.getAtomicNumber()
print 'Number of electrons:', cu.getNumElectrons()
