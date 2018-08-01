# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    parser.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:15:32 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.parser.lexer import Lexer
from computor.parser.token import Token, TOKEN_TYPE
from computor.math.unknown import Unknown

class Parser:
  """Parser

  Parameters
  ----------
  buffer: string
    Buffer to read

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
  def __init__(self, buffer):
    self._lexer = Lexer(buffer)
    self._token = self._lexer.lexer(True)
    self._args = []
    self._a = Unknown(0, 2)
    self._b = Unknown(0, 1)
    self._c = Unknown(0, 0)

  def parse(self):
    rhs = False

    while self._token.type != TOKEN_TYPE['EOF']:

      while (not rhs and self._token != '=') or (rhs and self._token.type != TOKEN_TYPE['EOF']):

        if self._token.type == TOKEN_TYPE['EOF']:
          self._lexer.raise_KeyError()

        elif self._token.type == TOKEN_TYPE['Unknown']:
          self.parse_unknown(0)

        elif self._token.type == TOKEN_TYPE['Number']:
          self.parse_number(False)

        elif self._token.type == TOKEN_TYPE['Symbol']:

          if self._token == '/' or self._token == '*' or self._token == '^':
            self._lexer.raise_KeyError()

          elif self._token == '-':
            self._token = self._lexer.lexer(True)
            if self._token.type != TOKEN_TYPE['Number']:
              self._lexer.raise_KeyError()
            self.parse_number(True)

          elif self._token == '+':
            self._token = self._lexer.lexer(True)
            if self._token.type != TOKEN_TYPE['Number']:
              self._lexer.raise_KeyError()
            self.parse_number(False)

        self._token = self._lexer.lexer(True)

      if not rhs:
        print("=", end=" ")
        rhs = True
        self._token = self._lexer.lexer(True)

    print()

  def parse_number(self, negative):
    coef = float(self._token) if not negative else -1 * float(self._token)
    self._token = self._lexer.lexer(True)

    if self._token.type == TOKEN_TYPE['Unknown']:
      self.parse_unknown(coef)

    elif self._token.type == TOKEN_TYPE['Symbol']:
      if self._token != '*':
        self._lexer.raise_KeyError()

      self._token = self._lexer.lexer(True)
      if self._token.type != TOKEN_TYPE['Unknown']:
        self._lexer.raise_KeyError()
      self.parse_unknown(coef)

  def parse_unknown(self, coef):
    unknown = Unknown(coef, 0)
