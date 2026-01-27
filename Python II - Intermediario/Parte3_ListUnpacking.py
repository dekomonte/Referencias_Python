#==========#Data Structure==========

#List unpacking
a,b,c = [1,2,3]
print(a)
print(b)
print(c)

a,b,c, *outros = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(outros)

a,b,c, *outros, d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(outros)
print(d)
