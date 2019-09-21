"""
#M.52

Longest Zig-Zag Subsequence
The longest Zig-Zag subsequence problem is to find length of the longest subsequence of given sequence such that all elements of this are alternating.
If a sequence {x1, x2, .. xn} is alternating sequence then its element satisfy one of the following relation :

  x1 < x2 > x3 < x4 > x5 < …. xn or 
  x1 > x2 < x3 > x4 < x5 > …. xn 
Examples :

Input: arr[] = {1, 5, 4}
Output: 3
The whole arrays is of the form  x1 < x2 > x3 

Input: arr[] = {1, 4, 5}
Output: 2
All subsequences of length 2 are either of the form 
x1 < x2; or x1 > x2

Input: arr[] = {10, 22, 9, 33, 49, 50, 31, 60}
Output: 6
The subsequences {10, 22, 9, 33, 31, 60} or
{10, 22, 9, 49, 31, 60} or {10, 22, 9, 50, 31, 60}
are longest Zig-Zag of length 6.

[+]Temporal marker            : 18:45, | Saturday Sept21, 19
[+]Temporal marker untethered : 18:57  | Saturday Sept21, 19
[+]Comments                   : *Knew the approach
                                *Carefully thought it inside out
                                *Carefully implemented the solution
                                *Had 0 debuggin session                                *Problem is now closed
[+]Level                      : Basic
[+]Tread speead               : Carefully Relaxed
[+]LINK                       : https://www.geeksforgeeks.org/longest-zig-zag-subsequence/
"""

#S-Complexity: O(N) | T-Complexity: O(N*N)
def findSolution(lis):
    length  = len(lis)
    dp = [[0]*length for x in range(2)]
    dp[0][0] = 1  #increasing
    dp[1][0] = 1  #decreasing

    for i in range(1, length):
        inc = 1
        dec = 1
        for j in range(i):
            if(lis[j] > lis[i]):
                dec = max(dec, dp[0][j]+1)
            if(lis[j] < lis[i]):
                inc = max(inc, dp[1][j]+1)
        dp[0][i] = inc
        dp[1][i] = dec
    return max(dp[0][length-1], dp[1][length-1])

    print(dp)

if __name__ == "__main__":
    lis = [10, 22, 9, 33, 49, 50, 31, 60]
    lis = [1, 4, 5]
    lis = [1, 5, 4]
    lis = [1, 5, 5]
    print(findSolution(lis))

    
