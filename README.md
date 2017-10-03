# atomic-structure

## Objectives
To model atomic structure in Python. Eventually, will be expanded to ions, ionization, formation of ionic and covalent compounds, and chemical reactions.

### Current Status
Basic atomic structure, ions, and ionization are complete.

## Organization
### Electron
Forms the basis for modeling atomic structure that is not the nucleus. Has principal, azimuthal, and spin quantum numbers.

### Orbital
Structure used to contain electrons, imports Electron class. Comes in s, p, d, and f varieties. Maximum number of electrons depends on the type of orbital. Currently, different classes for the different types that all inherit from a general Orbital class are not implemented.

### Proton
Positively charged nucleic particle. Mass of 1.

### Neutron
Nucleic particle with no charge. Mass of 1.

### Nucleus
Contains a list of protons and a list of neutrons. More for organization than anything else.

### Atom
The master file. Imports  everything mentioned above, whether directly or indirectly. It has a nucleus as well as orbitals filled with electrons. Initialization is done by giving the chemical symbol, and the electronic configuration is determined from a dictionary in the Constants file, as is the atomic number and atomic mass.

### Constants
Contains all the useful numbers and conversions needed to make everything else work smoothly.

### Run.py
Run the damn program already!
