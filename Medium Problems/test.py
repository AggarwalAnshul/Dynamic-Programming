# Python3 program to count number of 
# distinct subseqences of a given string 

MAX_CHAR = 256

def countSub(ss): 

	# create an array to store index of last 
	last = [-1 for i in range(MAX_CHAR + 1)] 
	
	# length of input string 
	n = len(ss) 
	
	# dp[i] is going to store count of 
	# discount subsequence of length of i 
	dp = [-2 for i in range(n + 1)] 
	
	# empty substring has only 
	# one subseqence 
	dp[0] = 1
	
	# Traverse through all lengths 
	# from 1 to n 
	for i in range(1, n + 1): 
		
		# number of subseqence with 
		# substring str[0...i-1] 
		dp[i] = 2 * dp[i - 1] 

		# if current character has appeared 
		# before, then remove all subseqences 
		# ending with previous occurrence. 
		if last[ord(ss[i - 1])] != -1: 
			dp[i] = dp[i] - dp[last[ord(ss[i - 1])]] 
		last[ord(ss[i - 1])] = i - 1
	
	return dp[n] 
	
# Driver code 
print(countSub("dgfg")) 

# This code is contributed 
# by mohit kumar 29 
