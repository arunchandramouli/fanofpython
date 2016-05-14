

def remove_dups(container):    
	x = set()
	for data in container:
		x.add(data)
	return x


x = ["Arun","Kumar","C","Chandramouli","Arun"]	
print remove_dups(x)



import collections 
def default_factory():
	return 'default value'
d = collections.defaultdict(default_factory, foo='bar') 

print 'd:', d
print 'foo =>', d['foo']
print 'bar =>', d['bar']