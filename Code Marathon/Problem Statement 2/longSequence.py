"""
There is an array having characters A & B. You have to find the index of ‘B’ which when replaced
gives the maximum length sequence of the continuous one.

You can only replace one ‘B’ in the sequence.
"""

# Find the index of B to replace with A to get the maximum sequence
# of continuous 1's
def longSequence(list):

	max_count = 0   		# stores maximum number of 1's (including 0)
	max_index = -1  		# stores index of 0 to be replaced

	prev_index = -1	# stores index of previous zero
	count = 0   			# stores current count of zeros

	# consider each index `i` in the list
	for i in range(len(list)):

		# if the current element is 1
		if list[i] == 1:
			count = count + 1

		else:
			# if the current element is 0
			# reset count to 1 + number of ones to the left of current 0
			count = i - prev_index

			# update `prev_zero_index` to the current index
			prev_index = i

		# update maximum count and index of 0 to be replaced if required
		if count > max_count:
			max_count = count
			max_index = prev_index

	# return index of 0 to be replaced or -1 if the list contains all 1's
	return max_index


if __name__ == '__main__':

    # list of characters
    # A = 1
    # B = 0

	list = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]

	index = longSequence(list)
	if index != -1:
		print(f"Found the B in Index no [{index}] and replace it with 1 \nto get the maximum sequence of continuous 1's")
	else:
		print("Invalid input")

    # Output:

    #Found the B in Index no [9] and replace it with 1 
    #to get the maximum sequence of continuous 1's
    