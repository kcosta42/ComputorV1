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

from computor.parser.parser import Parser

def test_polynomial():
  print("\nE = 0")
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print("\nE = 3")
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print("\nE = 2x + 3")
  a = Unknown(0, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print("\nE = 3x² + 15x + 3")
  a = Unknown(3, 2)
  b = Unknown(15, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print("\nE = 1x²")
  a = Unknown(1, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

  print("\nE = 3x² + 2x + 3")
  a = Unknown(3, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve()

def test_parser():
  parser = Parser('X ^ 2 + 3 X + 15 = 0')
  parser.parse()
