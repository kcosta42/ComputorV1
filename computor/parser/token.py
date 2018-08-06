# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    token.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:46 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 00:25:43 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Token:
  """Token

  Parameters
  ----------
  type : number
    Token type

  Attributes
  ----------
  _value: string
    Token string representation
  """

  def __init__(self, type):
    self.type = type
    self._value = ''

  def __str__(self):
    return '{}'.format(self._value)

  def __add__(self, other):
    self._value = self._value + other
    return self

  def __eq__(self, other):
    return self._value == other

  def __float__(self):
    return float(self._value)

  def clone(self):
    """Return Token clone"""
    token = Token(self.type)
    token._value = self._value
    return token

TOKEN_TYPE = {
  "EOF": 0,
  "Whitespace": 1,
  "Symbol": 2,
  "Number": 3,
  "Unknown": 4,
}
