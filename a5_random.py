# Learn random stuff

# format numbers
print('format this number %f' % 123.45)
print('and again %.2f' % 123.45)

# and string variables
a = "abcdefghijklmnopqrstuvwxyz"
print('%.24s' % a)

# Exceptions
var1 = '1'
try:
  var1 = var1 + 1 # Shouldn't work
except:
  print(var1, " is not a number") # so execute this
print (var1)

try:
  var2 = var1 + 1 # still shouldn't work
except:
  var2 = int(var1) + 1
print (var2)


