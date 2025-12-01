from importantConstants import Constant as const

def radius(mass):
    """
    Calculates the Schwarzschild radius of a black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Schwarzschild radius in meters
    """
    return (2 * const.G * mass) / (const.c ** 2)
def surfaceA(mass):
    """
    Calculates the surface area of a Schwarzschild black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Surface area of the black hole in square meters
    """
    return (mass ** 2) * ((16 * const.PI * (const.G ** 2)) / (const.c ** 4))
def effectiveDensity(mass):
    """
    Calculates the effective density of a Schwarzschild black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Effective density of the black hole in kg/m^3
    """
    return (1 / (mass ** 2)) * ((3 * (const.c ** 6)) / (32 * const.PI * (const.G ** 3)))
def surfaceGrav(mass):
    """
    Calculates the Newtonian value of the surface gravity of the black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Surface gravity of the black hole in m/s^2
    """
    return (1 / mass) * ((const.c ** 4) / (4 * const.G))
def timeToSingularity(mass):
    """
    Calculates the time it takes to reach the singularity after reaching the event horizon.
    Args:
        mass (float): Mass of the black hole in kg
    
    Returns:
        float: Time to reach the singularity in seconds"""
    return (const.PI * const.G * mass) / (const.c ** 3)
    
def entropy(mass):#needs work
    """
    Calculates the entropy of a Schwarzschild black hole.
    Args:
        mass (float): Mass of black hole in kg
    
    Returns:
        float: Entropy of the black hole"""
    return (mass ** 2) * ((4 * const.PI * const.G) / (const.h * const.c))

def temp(mass):#needs work
    """
    Calculates the temperature of the black hole
    Args:
        mass (float): Mass of the black hole in kg
        
    Returns:
        float: Temperature of the black hole in K"""
    return (1 / mass) * ((const.h * (const.c ** 3)) / (8 * const.PI * const.Kb * const.G))

def nomialLuminosity(mass):#needs work
    """
    Calculates the luminosity of the black hole
    Args:
        mass (float): Mass of the black hole in kg
    
    Returns:
        float: Luminosity of the black hole in Watts"""
    return (1 / (mass ** 2)) * ((const.h * (const.c ** 6)) / (15360 * const.PI * (const.G ** 2)))
