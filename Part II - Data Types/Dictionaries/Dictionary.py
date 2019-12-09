D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}  # Making a dictionary
print("D:", D)

D['food']  # Fetch a value from the key 'food'

D['quantity'] += 1  # Add 1 to the 'quantity' value

print(D)

D = {}  # While making a dictionary, it can start out empty
D['name'] = 'Bob'  # Then filled with created keys
D['job'] = 'dev'
D['age'] = 40

print(D)  # order scrambled, doesnt matter
print(D['name'])  # Will print 'Bob'

# You can make a dictionary using a 'keyword argument', name=value, and using
bob1 = dict(name='Bob', job='dev', age=40)  # dict(name=value)

# Or, by zipping
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print("\nbob1:\n", bob1, "\nbob2:\n", bob2)

# Nesting
nested = {'name': {'first': 'Bob', 'last': 'Smith'},
          'jobs': ['dev', 'mgr'],
          'age': 40.5}

print('\nnested:\n', nested)

nested['name'],  # Gets the whole nested dictionary
nested['name']['first'],  # Gets the value of the 'first' key in the nested dictionary
nested['jobs'][1],  # Gets the *2nd* item in the nested list 'jobs'

nested['jobs'].append('janitor')  # Editing the list works inside a dictionary
nested['jobs'].pop(0)
print(nested)

nested = 0  # Memory alloted is cleaned up automatically unlike C/C++/C#
print(nested)

# INDEXING A KEY WHICH DOENSNT EXIST WILL PRODUCE AN ERROR

D = {'a': 1, 'b': 2, 'c': 3}
print(D)  # Might not be in order, doenst matter anyway

'f' in D  # Will produce a true or false, searching key
if 'f' not in D:
    print('missing')
else:
    print('present')

D['a'] == 1  # T\F if value of 'a' is 1, true else false

v = D.get('a', 0)  # gets the value of the key 'x', if not found, gives 0
print('\n')
print(v)

v = D['a'] if 'a' in D else 0  # ^^ is the equivilent of doing this
print(v)

# To get a sorted list of keys:
Ks = list(D.keys())
print(Ks)

Ks.sort()
print(Ks)

for key in Ks:
    print(key, ':', D[key])

# Or, new way:

for key in sorted(D):
    print(key, ':', D[key])

# Watch for 'pickle' and 'shelve' modules for later

# Other core types:

###### SETS #######
V = set('spam')  # make a set out of a sequence
Z = {'h', 'a', 'm'}  # make a set with literals

print('\nSets\n',
      V, Z)
