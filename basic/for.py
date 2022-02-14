mylist = [1,3,5]
mytuple = (1, 2, 'skip a few', 99, 100)
myset = {'a', 'b', 'z'}
mystring = 'abracadabra'
mydict = {'a': 96, 'b': 97, 'c': 98}

for i in mylist:
  print(i)
  
for i in mytuple:
  print(i)
  
for i in myset:
  print(i)
  
for character in mystring:
  print(character)
  
for key in mydict:
  print(key)
  
for key, value in mydict.items():
  print(key, value)
  
for i in range(10):
  j = 10 * i + 1
  print(j, end=' ')