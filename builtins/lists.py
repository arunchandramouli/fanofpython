'''
		AIM :: To manipulate the lists container
'''

x = [100,90,80,'Alpha','Zeta','Zen',200,11.5]

# Reverse a List


def listReverse(lists):

	lens = len(lists)

	while lens:
		yield x[lens-1]
		lens -= 1


#print list(listReverse(x))

#Create a Sub-list from a list

def createSublists(lists):

	lens = len(lists)

	while lens:

		current = lists[-lens]
		
		for i in (range(lens)):

				yield current,lists[-lens+i]

		lens -= 1



for i in list(createSublists(x)): 
	print i