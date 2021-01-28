#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
  line = re.sub('^\W+|\W+$', '', line) #elimina lo que no sean alfanumerico al inicio y fin de la linea
  words = re.split('\W+', line)

  for word in words:
    print(word.lower() + "\t1") #mandamos a la salida la palabra separada por un tab y un 1
