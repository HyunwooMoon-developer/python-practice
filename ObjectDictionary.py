#Dictionary object {}

cabinet = {3 : 'DOG' , 100 : 'CAT'}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5]) error and end
print(cabinet.get(5))
print(cabinet.get(5, 'able'))

print(3 in cabinet) # True
print(8 in cabinet) # False

cabinet[8] = 'TURTLE'
print(cabinet)

cabinet[8] = 'TIGER'
print(cabinet)

del cabinet[8]
print(cabinet)

# key
print(cabinet.keys())

# value
print(cabinet.values())

# key and values
print(cabinet.items())

#close cabinet
cabinet.clear()
print(cabinet)