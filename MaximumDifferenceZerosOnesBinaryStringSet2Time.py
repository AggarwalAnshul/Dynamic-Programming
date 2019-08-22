"""
Maximum difference of zeros and ones in binary string | Set 2 (O(n) time)
Given a binary string of 0s and 1s. The task is to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string. That is maximize ( number of 0s – number of 1s ) for any sub-string in the given binary string.

Examples:

Input : S = "11000010001"
Output : 6
From index 2 to index 9, there are 7
0s and 1 1s, so number of 0s - number
of 1s is 6.

Input : S = "1111"
Output : -1
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
We have discussed Dynamic Programing approach in below post :
Maximum difference of zeros and ones in binary string | Set 1.

In the post we seen an efficient method that work in O(n) time and in O(1) extra space. Idea behind that if we convert all zeros into 1 and all ones into -1.now our problem reduces to find out the maximum sum sub_array Using Kadane’s Algorithm.

Input : S = "11000010001"
     After converting '0' into 1 and
     '1' into -1 our S Look Like
      S  = -1 -1 1 1 1 1 -1 1 1 1 -1
 Now we have to find out Maximum Sum sub_array 
 that is  : 6 is that case 
    
Output : 6

[+]Temporal Marker           :  12:34 Hours | Aug22, Thursday
[+]Temporal Marker Untethered:  12:50 Hours | Aug22, Thursday
[+]Tread Speed               :   Relaxed
[+]T-Complexity              :  O(n)
[+]S-Complexity              :  O(1)
LINK: https://www.geeksforgeeks.org/maximum-difference-zeros-ones-binary-string-set-2-time/
"""

import sys

#This is a streamlined version of the following version. as pointed by
#geeksforgeeks, it swaps 1->-1 | 0->1 and finds the max sum of subarray
#using kadane's algo. This can be done in O(n) time not using more than O(1)space

#Fucntion that
#arg: 1 | returns -1
#arg: 0 | returns 1
def returnInt(char):
     if char=='1':
          return -1
     else:
          return 1
def MaximumDifferenceZerosOnesBinaryStringSet2TimeS(string):
     #Creating Modified the string
     length = len(string)             
     #start and end can be used to print the substring satisfying the constraint
     start = 0
     end = 0
     maxSum = 0
     curSum = 0
     for i in range(0, length):
          if(curSum <= 0):
               start = i
               curSum = 0
          curSum += returnInt(string[i])
          if(curSum > maxSum):
               end = i
               maxSum = curSum
     if(maxSum==0):
          return -1
     return (maxSum)

#The original devised algorithm
def MaximumDifferenceZerosOnesBinaryStringSet2Time(string):
     length = len(string)
     maxCount = -sys.maxsize-1
     
     #initializing dp 
     dp = [0]*(length)
     if(string[0]=='1'):
         dp[0] = -1
     elif(string[0]=='0'):
         dp[0] = 1
         
    #Populating dp:
     for i in range(1, length):
        #print(string[i], end=" ")
        singleValue = -1
        nextValue = 0
        if(string[i]=='0'):
            singleValue = 1
        if(string[i]=='1'):
            nextValue = dp[i-1]-1
        else:
            nextValue = dp[i-1]+1
        dp[i] = max(nextValue, singleValue)
        maxCount = max(maxCount, dp[i])
        #print(dp[i])
     return maxCount


#string = "1001000011"
string = "11000010001"
#string = "1111"
#string = "1101"
#string = "011"
print(MaximumDifferenceZerosOnesBinaryStringSet2TimeS(string))         
     

