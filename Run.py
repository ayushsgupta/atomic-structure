import Constants
from Atom import Atom

# 10-1-17
# Latest update 10-2-17

cu = Atom('Cu')
print 'Atomic mass of Cu:', cu.getAtomicMass()
print 'Number of protons:', cu.getAtomicNumber()
print 'Number of electrons:', cu.getNumElectrons()
num_ionizations = 2
cu.ionize(num_ionizations)
print 'After %d ionizations:' % (num_ionizations), cu.getSymbol()
print 'Atomic mass of %s:' % (cu.getSymbol()), cu.getAtomicMass()
print 'Number of protons:', cu.getAtomicNumber()
print 'Number of electrons:', cu.getNumElectrons()
