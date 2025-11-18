#Vf = Vi + at
#Vf = sqrt(Vi^2 + 2as)
#s= Vit + ((at^2)/2)
#Vaverage = s/t

def VelAT(a, t, Vi):
  """
  Calculates the final velocity if you know the acceleration, time, and initial velocity
  Args:
    a (float): Acceleration in m/s^2
    t (float): Time in seconds
    Vi (float): Initial velocity in m/s
  Returns:
    float: Final velocity of the object
  """
  finalVelocity = Vi + (a*t)
  return finalVelocity

def VelAS(a, s, Vi): 
  """
  Calculates the final velocity if you know the acceleration, initial velocity, and displacement
  Args:
    a (float): Acceleration in m/s^2
    s (float): Displacement of object in m
    Vi (float): Initial velocity in m/s
  Returns:
    float: Final velocity of the object
  """
  finalVelocity = (Vi + (2 * (a * s))) ** 0.5
  return finalVelocity
