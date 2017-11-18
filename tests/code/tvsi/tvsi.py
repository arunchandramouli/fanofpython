

"""


  The following question has been taken from hackerearth challenge shared by you

  Problem Statement ::

	[Kronos] Question - 1

		You have been given an Array A of size N. The array contains integers . You need to print the number with value closest to zero . If there are multiple elements, print the number with greater value.

		Input Format:

		The first line contains a single integer N denoting the size of the array A. The next line contains N integers denoting the elements of array A.

		Output Format:

		You need to print the value of element closest to zero. If there are multiple candidiates, print the number with greater value.

		Constraints:

		1<=N<=100

		1<=| Ai |<=100
		Sample Input

		5
		0 2 3 4 5

		Sample Output

		0


"""


'''
	Find the Element in the Array closer to zero
'''

def find_pos_neg_Array(arrayInput):

	'''
		Check to make sure length of the array <= 100
	'''

	if len(arrayInput) <= 100 :

		'''
			For Each Element in the Array - Determine the difference from value 0

			*** Seperating as two different array since , we could also have -ve numbers
			closer to zero!
		'''
		
		neg_Array = []
		pos_Array = []

		for each_element in arrayInput:

			'''
				Add seperately to -ve and +ve arrays
			'''

			neg_Array.append(each_element) if each_element < 0 else pos_Array.append(each_element)

				
	return pos_Array , neg_Array


'''
	Find Min value in Array
'''

def find_min_val_array(arraylist,types=None):

	
	'''
		Find min value without any builtins
	'''

	if types == "negArray":

		maxVal = arraylist[0]

		for values in arraylist:

			if values > maxVal : maxVal = values

		return maxVal

	else :

		minVal = arraylist[0]

		for values in arraylist:

			if values < minVal : 

				minVal = values

		return minVal


 

'''
	Result
'''

def result(testArray):


	get_arrays_list = find_pos_neg_Array(testArray)

	max_array , min_array = get_arrays_list

	print max_array , min_array,"\n"

	find_max_pos_array = find_min_val_array(max_array)
	print "find_max_pos_array ",find_max_pos_array,"\n"
	find_max_neg_array = find_min_val_array(min_array,types="negArray")
	print "find_max_neg_array ",find_max_neg_array,"\n"

	return find_min_val_array([find_max_pos_array,find_max_neg_array],types="negArray")




if __name__ == "__main__":

	get_arrays = result([12,2,10,25,50,60,30,4,3,-1,-5,1,-7,0])
	print get_arrays




	


