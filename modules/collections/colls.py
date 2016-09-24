'''
	Use Case:  Understanding the usage of default dicts

'''

from collections import defaultdict,OrderedDict

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
print '\n\n ', ' Defaultdicts ','\n\n '
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



print '\n\n ', ' Ordereddicts ','\n\n '

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 4}

# Creating an OrderedDict
newOrderedDict = OrderedDict(d)
print newOrderedDict, ' ',newOrderedDict.__class__
newOrderedDict['state'] = 'Newyork'
newOrderedDict['state2'] = 'Alaska'
print newOrderedDict, ' ',newOrderedDict.__class__

print '\n\n', '*'*15,'\n\n'
print ' Sorting an OrderedDict'
print '\n\n', '*'*15,'\n\n'
print sorted(newOrderedDict.items(),key = lambda x:x[0]) # By Key
print sorted(newOrderedDict.items(),key = lambda x:x[1]) # By Value

print '\n\n', '*'*15,'\n\n'
print ' Iterating an OrderedDict and an Ordinary dict'
'''
	An Ordinary Dict produces value in an arbitary manner while it's being iterated, meanwhile an OrderedDict provides value in an insertion order
'''
print '\n\n', '*'*15,'\n\n'
print ' Iterating an Ordinary dict'
print '\n\n', '*'*15,'\n\n'

for k,v in d.items():
	print k,v

'''
   Output ::

    orange 4
	pear 1
	banana 3
	apple 4
'''

print '\n\n', '*'*15,'\n\n'
print ' Iterating an OrderedDict - Remembers the insertion order!'
print '\n\n', '*'*15,'\n\n'

# Creating an OrderedDict
newOrderedDict = OrderedDict()

{'banana': 3, 'apple': 4, 'pear': 1, 'orange': 4}

newOrderedDict['banana'] = 3
newOrderedDict['apple'] = 4
newOrderedDict['pear'] = 1
newOrderedDict['orange'] = 4

for k,v in newOrderedDict.items():
	print k,v

'''

   Output::

    banana 3
	apple 4
	pear 1
	orange 4
'''