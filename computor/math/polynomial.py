# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    polynomial.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/08/05 13:34:00 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.math.unknown import Unknown
from computor.math.ft_sqrt import ft_sqrt
# from matplotlib import pyplot
# import numpy as np


class Polynomial:
  """Polynomial
  """
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def resolve(self):
    resolve_method = POLYNOMIAL_DEGREE_FORMULA[self.a.degree]
    resolve_method(self.a, self.b, self.c)
    # self.show()

  # def show(self):
  #   x = np.arange(-10.0, 10.0, 0.1)
  #   s1 = self.a.coef * x ** 2 + self.b.coef * x + self.c.coef
  #   pyplot.plot(x, s1)
  #   pyplot.axhline(linewidth=2, color='r')
  #   pyplot.title('Polynomial / Linear')
  #   pyplot.grid(True)
  #   pyplot.show()

  @staticmethod
  def ReducEqu(lhs, rhs):
    return Polynomial.ReduceExp([])

  @staticmethod
  def ReduceExp(*args):
    a = Unknown(0, 2)
    b = Unknown(0, 1)
    c = Unknown(0, 0)

    print("Reduced form: ")
    return Polynomial(a, b, c)

  @staticmethod
  def ResolveDefault(__reserved, _reserved, a):
    print("Polynomial degree: 0")
    if a == 0:
      print("All numbers are solution")
      return
    else:
      print("Equation can't be solved")
      return

  @staticmethod
  def ResolveLinear(_reserved, a, b):
    print("Polynomial degree: 1")
    if a == 0:
      if b == 0:
        print("All numbers are solution")
        return
      else:
        print("Equation can't be solved")
        return
    if b == 0:
      print("All numbers are solution")
      return
    print("The solution is: %.2f" % (b / a))

  @staticmethod
  def ResolveQuadratic(a, b, c):
    if a == 0:
      return Polynomial.ResolveLinear(a, b, c)

    print("Polynomial degree: 2")
    discriminant = float(b ** 2 - 4 * a * c)
    if discriminant > 0:
      print("Discriminant is strictly positive, the two solutions are:")
      print("%.2f" % ((-b + ft_sqrt(discriminant)) / (2 * a)))

      print("%.2f" % ((-b - ft_sqrt(discriminant)) / (2 * a)))

    elif discriminant == 0:
      print("Discriminant is equal to zero, the solution is:")
      print("%.2f" % (-1 * (b / (2 * a))))

    elif discriminant < 0:
      print("Discriminant is strictly negative, "
            "the two complex solutions are:")
      print("%.2f + " % ((-b) / (2 * a)), end="")
      print("i * %.2f" % ((ft_sqrt(-discriminant) / (2 * a))))

      print("%.2f - " % ((-b) / (2 * a)), end="")
      print("i * %.2f" % ((ft_sqrt(-discriminant) / (2 * a))))


POLYNOMIAL_DEGREE_FORMULA = {
  0: Polynomial.ResolveDefault,
  1: Polynomial.ResolveLinear,
  2: Polynomial.ResolveQuadratic,
}
