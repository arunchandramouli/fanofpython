'''
	Use Case:  Understanding the usage of default dicts

'''

from collections import defaultdict

# s is a simple container with key,value pairs
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# forming a defaultdict as a list
d = defaultdict(list)

x = defaultdict() # Forming an empty default dict.


dicts = {} # A normal dictionary

for k , v in s:
	d[k].append(v)
	dicts[k]= v

'''
  The difference between normal dicts and default dicts is that while we add values to defaultdict "d[k].append(v)",
  the o/p will show as key as yellow and value as (1,3) since yellow appears twice with such values.

  While we add to the normal dictionary, it gets shows as "yellow:3", since 3 is the latest value on iteration in order
'''
print d	, '  ',dicts, ' ', type(d), ' ', type(dicts)

'''
	Output ::

	defaultdict(<type 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})    {'blue': 4, 'red': 1, 'yellow': 3}   

	<type 'collections.defaultdict'>   <type 'dict'>

'''


'''
	Accessing Elements inside a defaultdict and a dict
'''

print d.__getitem__('blue') # returns [2,4]
print dicts.__getitem__('blue') # returns 4


# Adding items to a defaultdict as a list

d = {} #  normal dict
f = {}
for k , v in s:

	d.setdefault(k,[]).append(v) # converting as a default dict and adding a value
	f.setdefault(k,{})[v] = v # defaultdict as a dict


print d , ' ',f

'''
	Output ::

	{'blue': [2, 4], 'red': [1], 'yellow': [1, 3]}   {'blue': {2: 2, 4: 4}, 'red': {1: 1}, 'yellow': {1: 1, 3: 3}}
'''	



