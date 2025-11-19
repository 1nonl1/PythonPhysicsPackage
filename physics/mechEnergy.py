def kE(m, v):
    """
    Calculates kinetic energy of an object
    Args:
        m (float): Mass in kg
        v (float): Velocity in m/s
    Returns:
        float: The kinetic energy of an object in Joules
    """
    return (m * (v ** 2))

def pE(m, g, h):
    """
    Calculates the potential energy of an object
    Args:
        m (float): Mass in kg
        g (float): Force of gravity in m/s^2
        h (float): Height of the object in m
    Returns:
        float: Potential energy of an object in Joules
    """
    return (m * g * h)

def springConstant(F, s):
    """
    Calculates the spring constant
    Args:
        F (float): Force applied in N
        s (float): Displacement of spring from equilibrium in m
    Returns:
        float: Value of the Spring constant
    """
def elasticPE(k, s):
    """
    Calculates the potential energy in a spring
    Args:
        k (float): Spring constant
        s (float): Displacement the spring is stretched or compressed from equilibrium
    Returns:
        float: Potential energy of a string
    """
    return (k * (s ** 2))

def mE(m, v, g, h):
    """
    Calculates the mechanical energy of an object
    Args:
        m (float): Mass in kg
        g (float): Force of gravity in m/s^2
        h (float): Height of the object in m
        v (float): Velocity of object in m/s
    Returns:
        float: Mechanical Energy of an object in Joules
    """
    return (kE(m, v) + pE(m, g, h))