'''
	Use Case:  Understanding & Inspecting Modules
'''



def execute(func):

	def reporter(*args,**kargs):

		print "Sum - " , func.func_globals.__getitem__('sum')(*args,**kargs), 
		print "negate - "  , func.func_globals.__getitem__('negate')(*args,**kargs)
		prd = func(*args,**kargs)
		print "prd - ", prd
		return prd

	return reporter


