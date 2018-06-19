# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_core.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:15:32 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.math.polynomial import Polynomial
from computor.math.unknown import Unknown


def test_polynomial():
  print()
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print()
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print()
  a = Unknown(0, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print()
  a = Unknown(3, 2)
  b = Unknown(15, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print()
  a = Unknown(1, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print()
  a = Unknown(3, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()
