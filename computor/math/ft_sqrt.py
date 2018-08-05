# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_sqrt.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/08/05 13:36:53 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

SQRT_PRECISION = 0.01


def abs(a):
  a = -a if a < 0 else a
  return a


def f(w, g):
  return (g ** 2 - w)


def fPrime(g):
  return (2 * (g ** (2 - 1)))


def closeEnough(a, b):
  return (abs(a - b) < abs(b * SQRT_PRECISION))


def findRoot(w, g):
  newGuess = g - f(w, g) / fPrime(g)
  if closeEnough(newGuess, g):
    return newGuess
  else:
    return findRoot(w, newGuess)


def ft_sqrt(w):
  return findRoot(w, 1)
