'''
# Read input from stdin and provide input before running code

name = raw_input()
print 'Hi, %s.' % name
'''


int_number_of_elements = int(raw_input())

int_array_of_elements = raw_input().split()

'''
	Find the Element in the Array closer to zero
'''

def find_pos_neg_Array(int_array_of_elements):

	'''
		Check to make sure length of the array <= 100
	'''

	if len(int_array_of_elements) <= 100 :

		'''
			For Each Element in the Array - Determine the difference from value 0

			*** Seperating as two different array since , we could also have -ve numbers
			closer to zero!
		'''
		
		neg_Array = []
		pos_Array = []

		for each_element in int_array_of_elements:

			'''
				Add seperately to -ve and +ve arrays
			'''

			neg_Array.append(each_element) if int(each_element) < 0 else pos_Array.append(int(each_element))

				
	return pos_Array , neg_Array

'''
	Find Min value in Array
'''

def find_min_val_array(int_array_of_elements,types=None):

	
	'''
		Find min value without any builtins
	'''

	if types == "negArray":

		maxVal = int(int_array_of_elements[0])
		
		for values in int_array_of_elements:

			if int(values) > maxVal : maxVal = int(values)

		return int(maxVal)

	else :

		minVal = int_array_of_elements[0]

		for values in int_array_of_elements:

			if values < minVal : 

				minVal = values

		return minVal

'''
	Result
'''

def result():


    get_arrays_list = find_pos_neg_Array(int_array_of_elements)
	
    print "get_arrays_list " ,get_arrays_list ,"\n"

    max_array , min_array = get_arrays_list
    print "max_array , min_array ",max_array , min_array,"\n"
	
    find_max_pos_array = find_min_val_array(max_array)
    print "find_max_pos_array ",find_max_pos_array,"\n"
    
    '''
        If there would be any -ve numbers in the Array!
    '''
    
    if bool(min_array):
        
	   find_max_neg_array = find_min_val_array(min_array,types="negArray")
	
	    print "find_max_neg_array ",find_max_neg_array,"\n"

    	return find_min_val_array([find_max_pos_array,find_max_neg_array],types="negArray")
    	
    else:
        
        return find_min_val_array([find_max_pos_array])

print result()

