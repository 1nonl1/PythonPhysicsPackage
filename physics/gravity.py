from importantConstants import Constant as const

def fOfGrav(m1, m2, r):
  """
  Calculates the force of gravity of an object
  Args:
    m1 (float): Mass of the first object in kg
    m2 (float): Mass of the second object in kg
    r (float): Distance from their centers
  Returns:
    float: Force of gravity in N
  """
  return const.G * ((m1 * m2) / (r ** 2))
