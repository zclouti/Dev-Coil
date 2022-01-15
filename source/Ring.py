class Ring():
    '''
    radius: position of the ring on the y axis
    zadius: position of the ring on the z axis
    y axis
	 |o
	 |oo
	 |ooooo
	 |ooooooooooo
	 |oooooooooooooooo
	 |oooooooooooooooooooooo
	 |oooooooooooooooooooooooooooo
	 |ooooooooooooooooooooooooooooooooo
	 |oooooooooooooooooooooooooooooooooooooo
	 |ooooooooooooooooooooooooooooooooooooooooooo
     -----------------------------------------------> z-axis
     where 'o' are the top right quadrant cross sectional positions of rings:
     
                |oo
                |oooo
                |ooooooo
                |oooooooooo           
     -----------------------
                |xxxxxxxxxx
                |xxxxxxx
                |xxxx
                |xx
    '''
    
    def __init__(self, i_radius: float = 0, i_zadius: float = 0):
        self.__radius = i_radius
        self.__zadius = i_zadius
        if(self.__radius == 0):
            self.__magnetic_coef = 0
            self.__length_coef = 0
        else:
            self.__magnetic_coef = (self.__radius ** 2)/(((self.__radius ** 2) + (self.__zadius ** 2)) ** 1.5)
            self.__length_coef = 1/self.__radius
        self.__total_coef = self.__magnetic_coef * self.__length_coef

    #get methods
    def getRadius(self) -> float:
        return self.__radius
    
    def getZadius(self) -> float:
        return self.__zadius
    
    def getMagneticCoef(self) -> float:
        return self.__magnetic_coef

    def getLengthCoef(self) -> float:
        return self.__length_coef
    
    def getTotalCoef(self) -> float:
        return self.__total_coef
    
    #set methods
    def setRadius(self, i_radius: float = 0) -> None:
        self.__radius = i_radius
        if(self.__radius == 0):
            self.__length_coef = 0
            self.__magnetic_coef = 0
        else:
            self.__magnetic_coef = (self.__radius ** 2)/(((self.__radius ** 2) + (self.__zadius ** 2)) ** 1.5)
            self.__length_coef = 1/self.__radius
        self.__total_coef = self.__magnetic_coef * self.__length_coef
    
    def setZadius(self, i_zadius: float = 0) -> None:
        self.__zadius = i_zadius
        self.__magnetic_coef = (self.__radius ** 2)/(((self.__radius ** 2) + (self.__zadius ** 2)) ** 1.5)
        self.__length_coef = 1/self.__radius
        self.__total_coef = self.__magnetic_coef * self.__length_coef
    
    #utility methods
    def toString(self) -> str:
        return "Radius = " + str(self.__radius) + "; Zadius = " + str(self.__zadius)
    
    def Print(self) -> None:
        print(self.toString())

    def __lt__(self, i_other_ring) -> bool:
        return self.getTotalCoef() < i_other_ring.getTotalCoef()

    def __gt__(self, i_other_ring) -> bool:
        return self.getTotalCoef() > i_other_ring.getTotalCoef()
    
    def __eq__(self, i_other_ring) -> bool:
        return self.getTotalCoef() == i_other_ring.getTotalCoef()

    def __nq__(self, i_other_ring) -> bool:
        return self.getTotalCoef != i_other_ring.getTotalCoef()


