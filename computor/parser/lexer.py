# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    lexer.py                                          :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:39 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 23:15:32 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.parser.scanner import Scanner
from computor.parser.token import Token, TOKEN_TYPE

WHITESPACE_CHARS = "\t\n\v\f\r "
SYMBOL_CHARS = "+-=^*/"
DECIMAL_CHAR = '.'
NUMBER_CHARS = "0123456789"
UNKNOWN_CHARS = "Xx"


class Lexer:
  """Lexer

  Parameters
  ----------
  buffer: string
    Buffer to read

  Attributes
  ----------
  _scan: object
    Scanner object for parsing the buffer
  _char: chr
    Next character read
  _token: object
    Current Token read

  Exceptions:
  -----------
  KeyError if unknown symbol met in buffer
  """
  def __init__(self, buffer):
    self._scan = Scanner(buffer)
    self._char = self._scan.read()

  def lexer(self, no_whitespace=False):
    """Lexer function

    Parameters
    ----------
    no_whitespace: boolean
      Doesn't return Whitespace token

    Returns
    -------
    _token: object
      Token

    Exceptions:
    -----------
    KeyError if unknown symbol met in buffer
    """
    if not self._char:
      self._token = Token(TOKEN_TYPE['EOF'])
    elif self._char in WHITESPACE_CHARS:
      self.whitespace_token()
    elif self._char in SYMBOL_CHARS:
      self.symbol_token()
    elif self._char in NUMBER_CHARS or self._char == DECIMAL_CHAR:
      self.number_token(self._char == DECIMAL_CHAR)
    elif self._char in UNKNOWN_CHARS:
      self.unknown_token()
    else:
      self.raise_KeyError()

    if no_whitespace and self._token.type == TOKEN_TYPE['Whitespace']:
      return self.lexer(no_whitespace)
    return self._token

  def raise_KeyError(self):
    """Exception KeyError is raised when callling this function"""
    raise KeyError(
      "Unknown symbol '{}' at index {}".format(self._token,
                                              self._scan.cursor)
    )

  def whitespace_token(self):
    """Set Whitespace Token"""
    token = Token(TOKEN_TYPE['Whitespace'])
    while self._char in WHITESPACE_CHARS:
      token = token + self._char
      self._char = self._scan.read()
    self._token = token

  def symbol_token(self):
    """Set Symbol Token"""
    token = Token(TOKEN_TYPE['Symbol'])
    token = token + self._char
    self._char = self._scan.read()
    self._token = token

  def number_token(self, has_decimal=False):
    """Set Number Token"""
    count = int(has_decimal)
    token = Token(TOKEN_TYPE["Number"])

    while self._char and (self._char in NUMBER_CHARS or self._char == DECIMAL_CHAR):

      count += int(self._char == DECIMAL_CHAR)
      if count > 1:
        self.raise_KeyError()

      token = token + self._char
      self._char = self._scan.read()

    self._token = token

  def unknown_token(self):
    """Set Unknown Token"""
    token = Token(TOKEN_TYPE["Unknown"])
    token = token + self._char
    self._char = self._scan.read()
    self._token = token
