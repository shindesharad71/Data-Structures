# Rearrange positive and negative numbers using inbuilt sort function
# https://www.geeksforgeeks.org/rearrange-positive-negative-numbers-using-inbuilt-sort-function/

def reverse(array, start, end):
	while(start < end):
		temp = array[start]
		array[start] = array[end]
		array[end] = temp
		start += 1
		end -= 1

# Rearrange the array with all negative integers
# on left and positive integers on right
# use recursion to split the array with first element
# as one half and the rest array as another and then
# merge it with head of the array in each step
def rearrange(array, start, end):
	
	# exit condition
	if(start == end):
		return

	# rearrange the array except the first
	# element in each recursive call
	rearrange(array, (start + 1), end)

	# If the first element of the array is positive,
	# then right-rotate the array by one place first
	# and then reverse the merged array.
	if(array[start] >= 0):
		reverse(array, (start + 1), end)
		reverse(array, start, end)

# Driver code
if __name__ == '__main__':
	array = [-12, -11, -13, -5, -6, 7, 5, 3, 6]
	length = len(array)
	countNegative = 0

	for i in range(length):
		if(array[i] < 0):
			countNegative += 1

	print(array)
	rearrange(array, 0, (length - 1))
	reverse(array, countNegative, (length - 1))
	print(array)
