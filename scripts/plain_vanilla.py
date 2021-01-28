##plain_vanilla.py
#!/usr/bin/python

import sys
import re

sums = {}

for line in sys.stdin:
  line = re.sub('^\W+|\W+$', '', line) #elimina lo que no sean alfanumérico al inicio y fin de la línea
  words = re.split('\W+', line)

  for word in words:
    word = word.lower()
    sums[word] = sums.get(word, 0) + 1

print(sums)
