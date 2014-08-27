# learn read/write in python

f = open("test.txt" , "r") # open file with name of test.txt
print(f.read(1))
print(f.read())
f.close()

f = open("test.txt" , "r") 
print f.readline()
print f.readline()
f.close()

f = open("test.txt" , "r")
myList = []
for line in f:
  myList.append(line)
print myList
f.close()
