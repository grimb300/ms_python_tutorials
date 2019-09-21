# Must import array object
from array import array

# Lists are a collection of items (anything of any type)
names = ['Susan', 'Christopher']
print(names)

# Can start with an empty list
scores = []
scores.append(98)
scores.append(99)
print(scores)
print(scores[1])

# Arrays (all elements have to be of the same type)
scores = array('d') # array of digits
scores.append(97)
scores.append(98)
print(scores)
print(scores[1])

# Common operations
print(len(names))
names.insert(0, 'Bill')
print(names)
names.sort()
print(names)

# Retrieving ranges
presenters = names[0:2] # Starting index and number of items to receive
exhibitors = names[1:3]
print(names)
print(presenters)
print(exhibitors)

# Dictionaries
person = {'first': 'Christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])