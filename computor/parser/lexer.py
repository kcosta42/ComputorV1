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

from expert_system.parser.scanner import Scanner
from expert_system.parser.token import Token, TOKEN_TYPE

WHITESPACE_CHARS = "\t\n\v\f\r "
SYMBOL_CHARS = "+-=^*/."
NUMBER_CHARS = "0123456789"
UNKNOWN_CHARS = "Xx"

class Lexer:
  """Lexer

  Parameters
  ----------
  filename: string
    Name of the file to be parse

  Attributes
  ----------
  _scan: object
    Scanner object for parsing the file
  _char: chr
    Next character read
  _token: object
    Current Token read

  Exceptions:
  -----------
  OSError if could not open filename
  KeyError if unknown symbol met in file
  """
  def __init__(self, filename):
    self._scan = Scanner(filename)
    self._char = self._scan.read()

  def lexer(self):
    """Lexer function

    Returns
    -------
    _token: object

    Exceptions:
    -----------
    KeyError if unknown symbol met in file
    """
    if not self._char:
      self._token = Token(TOKEN_TYPE['EOF'])
    elif self._char in WHITESPACE_CHARS:
      self.whitespace_token()
    elif self._char in SYMBOL_CHARS:
      self.symbol_token()
    elif self._char in NUMBER_CHARS:
      self.number_token()
    elif self._char in UNKNOWN_CHARS:
      self.unknown_token()
    else:
      self.raise_KeyError()

    return self._token

  def raise_KeyError(self):
    """Exception KeyError is raised when callling this function"""
    raise KeyError(
      "Unknown symbol '{}' at Ln {}, Col {}".format(self._token,
                                                    self._scan.line,
                                                    self._scan.column)
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

  def number_token(self):
    """Set Number Token"""
    token = Token(TOKEN_TYPE["Number"])
    while self._char in NUMBER_CHARS:
      token = token + self._char
      self._char = self._scan.read()
    self._token = token

  def unknown_token(self):
    """Set Unknown Token"""
    token = Token(TOKEN_TYPE["Unknown"])
    token = token + self._char
    self._char = self._scan.read()
    self._token = token
