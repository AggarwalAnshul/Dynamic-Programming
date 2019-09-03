"""
#98
Longest alternating (positive and negative) subarray starting at every index
A subarray is called alternating if any two consecutive numbers in it have opposite
signs (i.e. one of them should be negative, whereas the other should be positive).

Given an array of n integers. For each index i, we need to find the length if the
longest alternating subarray starting at i.

Examples:

Input : a[] = {1, -5, 1, -5}
Output : For index 0, {1, -5, 1, -5} = 4
             index 1, {-5, 1, -5} = 3
             index 2, {1, -5} = 2
             index 3, {-5} = 1.
      
Input :a[] = {-5, -1, -1, 2, -2, -3}
Output : index 0 = 1,
         index 1 = 1,
         index 2 = 3,
         index 3 = 2,
         index 4 = 1,
         index 5 = 1,

[+]Temporal marker            : 11:00 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 11:07 Hours | Sept03, 2019, Tuesday
[+]Comments                   : Easy peasy Lemon Squeezy!
[+]LINK                       : https://www.geeksforgeeks.org/ongest-alternating-positive-negative-subarray-starting-every-index/
"""

def findSolution(lis):
    length = len(lis)
    dp = [1]*length

    for i in range(length-2, -1, -1):
            if(lis[i]*lis[i+1]<0):
                dp[i] = dp[i+1]+1
    for element in dp:
        print(element)

if __name__ == "__main__":
    lis = [1, 2, 3, 5, 7, 11]
    lis = [ 1, 2, 6, 5, 4]
    lis = [ 1, 2, 6, 5, 4]
    lis = [-5, -1, -1, 2, -2, -3]
    lis = [1, -5, 1, -5]

    findSolution(lis)
