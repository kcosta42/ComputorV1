# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    scanner.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/14 18:18:22 by kcosta           #+#    #+#              #
#    Updated: 2018/06/15 11:19:57 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Scanner:
  """Scan each character in given file

  Parameters
  ----------
  buffer: string
    Buffer to read

  Attributes
  ----------
  _cursor: number
    Cursor in buffer
  """
  def __init__(self, buffer):
    self.buffer = buffer
    self._cursor = 0

  def read(self):
    """Read one character in buffer

    Returns
    -------
    char: char
      character read
    """
    char = self.buffer[self._cursor]
    self._cursor += 1
    return char

  @property
  def cursor(self):
    return self._cursor
