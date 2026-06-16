# ===== Functional Programming =====

#map, filter, zip and reduce

#map
#Executes a specified function for each item in an iterable
#Returns a list

#filter
#Returns an iterator where the items are filtered through a function to test if the item is accepted or not
#Returns a list

#zip
#Returns a zip object
#Is an iterator of tuples where the first item in each passed iterator is paired together,
#and then the second item in each passed iterator are paired together
#Returns a tuple

#reduce
#Applies a function cumulatively to the elements of an iterable and returns a single final value
#It processes elements step-by-step, combining two elements at a time until only one result remains
#Doesn't come as part of the python built-in function

def multiplica_por2(item):
    return item*2

def eh_impar(numero):
    return numero % 2 != 0

print(list(map(multiplica_por2, [1, 2, 3, 4])))

print(list(filter(eh_impar, [1, 2, 3, 4])))

x = ("Pedro","Thiago","João","Barquinho")
y = ("banana","laranja","batata","nabo","atum")
z = ("12","54","7")
print("zip: ", zip(x,y))
print("zip: ", tuple(zip(x,y)))
print("zip: ", tuple(zip(x,y,z)))
