
class Unknown:
  """Unknown variable
  
  Parameters
  ----------
  coef  : number
    Variable coefficient
  degree: number
    Variable degree
  """
  def __init__(self, coef, degree):
    self.coef = coef
    self.degree = degree

  def __add__(self, other):
    self.coef += other
    return self

  def __sub__(self, other):
    self.coef -= other
    return self

  # def __mul__(self):

  # def __div__(self):
