# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    unknown.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:15:32 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


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

  def __str__(self):
    s = "{}".format(self.coef)

    if self.degree == 1:
      return "{}x".format(s) if self.coef != 0 else ""
    if self.degree == 2:
      return "{}x²".format(s) if self.coef != 0 else ""

    return s

  def __float__(self):
    return self.coef

  def __neg__(self):
    return Unknown(float(-self.coef), self.degree)

  def __add__(self, other):
    return Unknown(float(self.coef + other), self.degree)

  def __radd__(self, other):
    return Unknown(float(other + self.coef), self.degree)

  def __sub__(self, other):
    return Unknown(float(self.coef - other), self.degree)

  def __rsub__(self, other):
    return Unknown(float(other - self.coef), self.degree)

  def __mul__(self, other):
    return Unknown(float(self.coef * other), self.degree)

  def __rmul__(self, other):
    return Unknown(float(other * self.coef), self.degree)

  def __truediv__(self, other):
    return Unknown(float(self.coef / other), self.degree)

  def __rtruediv__(self, other):
    return Unknown(float(other / self.coef), self.degree)

  def __pow__(self, other):
    return Unknown(float(self.coef ** other), self.degree)

  def __eq__(self, other):
    return self.coef == other

  def __lt__(self, other):
    return self.coef < other

  def __gt__(self, other):
    return self.coef > other
