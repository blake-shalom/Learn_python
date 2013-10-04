# Learn conditionals and other control structures


# Functions and for-loop control
def foo(q,r):
  for a in range(0,3):
    if a == 0:
      print ("if")
    elif a == 1:
      print ("elif")
    else: 
      print ("else")

foo(1,2)

# While loop


def bar(q):
  while q < 10 and q > 5:
    print q
    q += 1

bar(5)
bar(6)
bar(7)

