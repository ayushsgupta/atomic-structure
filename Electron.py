# 9-22-17
# Latest update 10-1-17

class Electron:

      '''
      Attributes:
        1. pqn - principal quantum number, the energy level of the electron: 1 to 7
        2. azqn - azimuthal quantum number, which letter orbital: 0, 1, 2, 3 (corresponds to s, p , d, f)
        3. mqn - magnetic quantum number, orientation of subshell shape: -azqn to +azqn (NOT CURRENTLY)
        4. sqn - spin quantum number, electron spin: -0.5 or +0.5

      Methods:
        1.

      '''

      def __init__(self, pqn, azqn, sqn):
          if pqn in range(0, 8):
              self.pqn = pqn
          else:
              self.pqn = 1

          if azqn >= 0 and azqn <= pqn - 1:
              self.azqn = azqn
          else:
              self.azqn = 0

          '''
          if mqn >= -azqn and mqn <= azqn:
              self.mqn = mqn
          else:
              self.mqn = 0
          '''

          if sqn in [-0.5, 0.5]:
              self.sqn = sqn
          else:
              self.sqn = 0.5

          self.atomic_mass = 0
          self.charge = -1

      def __str__(self):
          return "<Electron: n = %s, l = %s, s = %s>" % (self.pqn, self.azqn, self.sqn)

      def getPqn(self):
          return self.pqn

      def getAzqn(self):
          return self.azqn

      '''
      def getMqn(self):
          return self.mqn
      '''

      def getSqn(self):
          return self.sqn

      def getAtomicMass(self):
          return self.atomic_mass

      def getElectronCharge(self):
          return self.charge
