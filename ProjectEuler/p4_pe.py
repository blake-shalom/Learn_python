max = 0
for a in xrange(1000,100, -1):
  for b in xrange(1000, 100, -1):
    pal = a * b
    palstr = str(pal)
    half = palstr.__len__() / 2
    first = palstr[:half]
    last = palstr[half:-1]
    if (pal > max and first == last):
      max = pal
print (max)
