"""
#M.48
Longest Increasing Odd Even Subsequence
Given an array of size n. The problem is to find the length of the subsequence in the given array such that all the elements of the subsequence are sorted in increasing order and also they are alternately odd and even.
Note that the subsequence could start either with the odd number or with the even number.

Examples:

Input : arr[] = {5, 6, 9, 4, 7, 8}
Output : 4
{5, 6, 7, 8} is the required longest
increasing odd even subsequence.

Input : arr[] = {1, 12, 2, 22, 5, 30, 31, 14, 17, 11}
Output : 5

[+]Temporal marker            : 11:00, | Saturday Sept21, 19
[+]Temporal marker untethered : 11:24  | Saturday Sept21, 19
[+]Comments                   : *Easy peasy lemon squeezy!
[+]Level                      : Basic
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/longest-increasing-odd-even-subsequence/
"""

def findSolution(lis):
    length = len(lis)
    dp = [[0]*(length) for x in range(2)]
    #first dp row for odd elements
    #second dp row for even elements
    if(lis[0]%2!=0):
        dp[0][0] = 1
    else:
        dp[1][0] = 1
    ans = 0
    for x in range(1, length):
        localMax = 0
        curr = 0 #curr row, where this element will reside
        line = 1 #this line, where this element for search for previous alternating elements
        if(lis[x]%2==0):
            curr = 1
            line = 0
        for j in range(x):
            if(lis[j]<lis[x]):
                localMax = max(localMax, dp[line][j])
        dp[curr][x] = localMax+1
        ans = max(ans, localMax+1)
   return ans 


if __name__ == "__main__":
    lis = [5, 6, 9, 4, 7, 8]
    lis = [1, 12, 2, 22, 5, 30, 31, 14, 17, 11]
    print(findSolution(lis))
    
