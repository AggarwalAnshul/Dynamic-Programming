# A DP based Python3 program to find maximum tasks. 
# Returns the maximum among the 2 numbers 
def max1(x, y): 

	return x if(x > y) else y; 

# Returns maximum amount of task 
# that can be done till day n 
def maxTasks(high, low, n): 

	# An array task_dp that stores 
	# the maximum task done 
	task_dp = [0] * (n + 1); 

	# If n = 0, no solution exists 
	task_dp[0] = 0; 

	# If n = 1, high effort task 
	# on that day will be the solution 
	task_dp[1] = high[0]; 

	# Fill the entire array determining 
	# which task to choose on day i 
	for i in range(2, n + 1): 
		task_dp[i] = max(high[i - 1] + task_dp[i - 2], 
						low[i - 1] + task_dp[i - 1]); 
	return task_dp[n]; 

# Driver code 
n = 5; 

# This code is contributed by mits 
