# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    core.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: kcosta <kcosta@student.42.fr>             +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 21:22:03 by kcosta           #+#    #+#              #
#    Updated: 2018/06/17 22:10:59 by kcosta          ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from computor.parser.parser import Parser


def resolve(buffer, verbose, visual):
  parser = Parser(buffer, verbose, visual)
  try:
    parser.parse()
  except e:
    print(e)
