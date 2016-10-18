# Binary Tree

def binaryFormula(numberofNodes):    
    if numberofNodes <=1 :
        return 1

    else:
    	return facts(2*numberofNodes)/(facts(numberofNodes)*(facts(numberofNodes+1)))
 
 # (2n)!/(n!(n+1)!)


def facts(n):

	if n <= 1 : return 1	

 	for i in range(n):
 		return n * facts(n-1)

#print binaryFormula(3)


# Students Problem!

'''
	-- In Prgress - Not done yet -- Time Over
'''

def minMoves(avg):

	getLen = len(str(avg))
	dictsdata = {}

	# Get positions of 0 and 1
	for i in range(getLen):
		dictsdata.__setitem__(i,str(avg).__getitem__(i))
	return dictsdata

print minMoves(11100011001)
