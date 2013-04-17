#sum = 0
#for a in range (0,1000):
#  if (a % 3 == 0):
#    sum += a
#  elif (a % 5 == 0):
#    sum += a
#print sum

sum = 0
first = 1
second = 1
temp = 0
while (second < 4000000):
  temp = first + second
  if (temp % 2 == 0):
    sum += temp
  first = second
  second = temp
print sum
