# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/08/05 13:35:13 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.parser.lexer import Lexer
from computor.parser.token import Token, TOKEN_TYPE
from computor.math.unknown import Unknown
from computor.math.polynomial import Polynomial


class Parser:
  """Parser

  Parameters
  ----------
  buffer: string
    Buffer to read
  verbose: boolean
    Show additional information
  visual: boolean
    Show equation graph

  Attributes
  ----------
  _lexer  : object
    Lexer object for parsing the buffer
  _token  : object
    Current token read

  Exceptions
  ----------
  KeyError if unknown symbol met in buffer
  """
  def __init__(self, buffer, verbose = False, visual = False):
    self.verbose = verbose
    self.visual = visual
    self._lexer = Lexer(buffer, verbose)
    self._token = self._lexer.lexer(True)
    self._a = Unknown(0, 2)
    self._b = Unknown(0, 1)
    self._c = Unknown(0, 0)

  def parse(self):
    rhs = False

    while self._token.type != TOKEN_TYPE['EOF']:

      while ((not rhs and self._token != '=') or
             (rhs and self._token.type != TOKEN_TYPE['EOF'])):
        if self._token.type == TOKEN_TYPE['EOF']:
          self._lexer.raise_KeyError()

        elif self._token.type == TOKEN_TYPE['Unknown']:
          self.parse_unknown(1 if not rhs else -1)

        elif self._token.type == TOKEN_TYPE['Number']:
          self.parse_number(False if not rhs else True)

        elif self._token.type == TOKEN_TYPE['Symbol']:

          if self._token == '/' or self._token == '*' or self._token == '^':
            self._lexer.raise_KeyError()

          elif self._token == '-':
            self._token = self._lexer.lexer(True)
            if self._token.type != TOKEN_TYPE['Number']:
              self._lexer.raise_KeyError()
            self.parse_number(True if not rhs else False)

          elif self._token == '+':
            self._token = self._lexer.lexer(True)
            if self._token.type != TOKEN_TYPE['Number']:
              self._lexer.raise_KeyError()
            self.parse_number(False if not rhs else True)

        else:
          self._token = self._lexer.lexer(True)

      if not rhs:
        rhs = True
        self._token = self._lexer.lexer(True)

    self.print_reduced_form()

    poly = Polynomial(self._a, self._b, self._c)
    poly.resolve(self.verbose, self.visual)

  def parse_number(self, negative):
    coef = float(self._token) if not negative else -1 * float(self._token)
    self._token = self._lexer.lexer(True)

    if self._token.type == TOKEN_TYPE['Unknown']:
      return self.parse_unknown(coef)

    elif self._token.type == TOKEN_TYPE['Symbol']:
      if self._token == '*':
        self._token = self._lexer.lexer(True)
        if self._token.type != TOKEN_TYPE['Unknown']:
          self._lexer.raise_KeyError()
        return self.parse_unknown(coef)

    self._c = self._c + coef

  def parse_unknown(self, coef):
    unknown = Unknown(coef, 1)

    self._token = self._lexer.lexer(True)

    if self._token == '^':
      self._token = self._lexer.lexer(True)

      if self._token.type != TOKEN_TYPE['Number']:
        self._lexer.raise_KeyError()

      unknown.degree = float(self._token)
      if not unknown.degree.is_integer():
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer(True)

    if unknown.degree == 2:
      self._a = self._a + unknown
    elif unknown.degree == 1:
      self._b = self._b + unknown
    elif unknown.degree == 0:
      self._c = self._c + unknown
    else:
      print("The polynomial degree is stricly greater than 2, I can't solve.")
      raise Exception()

  def print_reduced_form(self):
    if self.verbose:
      print()
    print("Reduced form:", end=" ")

    if (self._a.coef != 0):
      print("{}".format(self._a), end=" + ")
    if (self._b.coef != 0):
      print("{}".format(self._b), end=" + ")

    print("{} = 0".format(self._c))
