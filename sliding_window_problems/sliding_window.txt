- lc 76

	#  Abstraction Model 1
	#  A  ....   B ....   C
	# Sliding Window maybe ? ....
	# Some length which matches based on target length. Keep running the end pointer until you find the first target combination.
	# Once you cross that character : you have to check whether that character is still contained in the next start pointer -> end pointer window.
	# Question is how do we check?
	# Maybe be some sort of Frequency Map.
	# Hmm .. lets think about it. 
	# If the end pointer is getting incremented then your map looks something like : Number of target characters encountered.
	# So in this case its going to be:
	# {'A':1 , 'B':1 , 'C':1}
	# Now target length should be 0, because you have encountered the first combination
	# So now it's time to increment the target length by 1 since the start pointer will get increamented and pass A. 
	# This means that you are looking for a future A.

	# Abstraction Model 2
	# ABBAC
	# a = -1 , b = -1, c = 0 ; t_l = 0
	# a < 0
	# a = 0, b = - 1 , c = 0
	# you wont increment the target length if something is less than 0
	# you will decrement the target length if something is greater than equal to 0