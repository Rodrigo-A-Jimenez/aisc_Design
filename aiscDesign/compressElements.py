from aiscpy import SelectByCriteria, Shape
from .constants import E, pi

__K = 12 #in/ft
def effective_Slenderness(Lc, rmin):
    return (__K*Lc/rmin)

def Cc(Fy):
    return ((2*(pi**2)*E)/Fy)**0.5

def critical_Stress(Fy, effectiveSlenderness):
    Kl_r = effectiveSlenderness
    Cc_ = Cc(Fy)
    if Kl_r >= Cc_:
        Fa = (12*(pi**2)*E)/(23*Kl_r**2)
        return round(Fa, 2)
    else:
        Fa = ((1-((Kl_r**2)/(2*Cc_**2)))*Fy)/((5/3)+((3*Kl_r)/(8*Cc_)-((Kl_r**3)/(8*Cc_**3))))
        return round(Fa,2)
    


class CompressDesign():
    def __init__(self, shape: Shape, compress, Lc, Fy) -> None:
        self.__shape = shape
        self.__compress = compress
        self.__Lc = Lc
        self.__Fy = Fy
        
        self.__A = self.__shape.query.toDict()['A']
        self.__rx = self.__shape.query.toDict()['rx']
        self.__ry = self.__shape.query.toDict()['ry']
        self.__rmin = min(self.__rx, self.__ry)
        
        self.__Kl_c = effective_Slenderness(self.__Lc, self.__rmin)
        self.__Fa = critical_Stress(self.__Fy, self.__Kl_c)
        self.__fa = compress/self.__A
        
    def status(self):
        if self.__Fa >= self.__fa:
            return 'OK'
        else:
            return 'NOT OK'
    @property
    def Kl_c(self):
        return self.__Kl_c
    
    @property
    def Fa(self):
        return self.__Fa
    
    @property
    def fa(self):
        return self.__fa
    
    @property
    def A(self):
        return self.__A
    
    @property
    def rmin(self):
        return self.__rmin
    