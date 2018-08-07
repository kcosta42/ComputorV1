# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    test_core.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/08/05 13:38:44 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.math.polynomial import Polynomial
from computor.math.unknown import Unknown

from computor.parser.parser import Parser


def test_polynomial():
  print("\n0 = 0")
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)

  print("\n3 = 0")
  a = Unknown(0, 2)
  b = Unknown(0, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)

  print("\n2x + 3 = 0")
  a = Unknown(0, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)

  print("\n3x² + 15x + 3 = 0")
  a = Unknown(3, 2)
  b = Unknown(15, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)

  print("\n1x² = 0")
  a = Unknown(1, 2)
  b = Unknown(0, 1)
  c = Unknown(0, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)

  print("\n3x² + 2x + 3 = 0")
  a = Unknown(3, 2)
  b = Unknown(2, 1)
  c = Unknown(3, 0)
  poly = Polynomial(a, b, c)
  poly.resolve(False, False)


def test_parser():
  parser = Parser('X ^ 2 + 3 X + 15 = 2X ^ 2 + 4 * X - 10', True)
  parser.parse()

  print()
  parser = Parser('X ^ 2 + 3 X + 15 = X ^ 2 + 4 * X - 10', True)
  parser.parse()

  print()
  parser = Parser('5 * X^0 = 5 * X^0', True)
  parser.parse()

  print()
  parser = Parser('4 * X^0 = 8 * X^0', True)
  parser.parse()

  print()
  parser = Parser('5 * X^0 = 4 * X^0 + 7 * X^1', True)
  parser.parse()

  print()
  parser = Parser('5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1', True)
  parser.parse()

  print()
  parser = Parser('6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1', True)
  parser.parse()

  print()
  parser = Parser('5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1', True)
  parser.parse()

  print()
  try:
    parser = Parser('1 * X^3 = 0', True)
    parser.parse()
  except:
    pass

  print()
  parser = Parser('4x = 0', True)
  parser.parse()

  print()
  parser = Parser('X = 0', True)
  parser.parse()

  print()
  parser = Parser('4 * X = 0', True)
  parser.parse()

  print()
  parser = Parser('1 X ^ 2 + 2 X ^ 2 + X + 15 + 3 X ^ 2 + 5 X + 30 = 0', True)
  parser.parse()
