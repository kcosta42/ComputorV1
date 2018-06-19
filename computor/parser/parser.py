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

  def parse(self):
    self._token = self._lexer.lexer()
    print(self._token)
