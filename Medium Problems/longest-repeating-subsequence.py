"""
#M.41
Longest Repeating Subsequence
Given a string, find length of the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.
longest-repeating-subsequence

Examples:

Input: str = "abc"
Output: 0
There is no repeating subsequence

Input: str = "aab"
Output: 1
The two subssequence are 'a'(first) and 'a'(second). 
Note that 'b' cannot be considered as part of subsequence 
as it would be at same index in both.

Input: str = "aabb"
Output: 2

Input: str = "axxxy"
Output: 2

[+]Temporal marker            : 13:50, | Sunday, Sept15, 19
[+]Temporal marker untethered : 13:58  | Sunday, Sept15, 19
[+]Comments                   : *Took a couple of hour
                                *Developed the DP(not so optimized) Algo on my own
                                *Algo looks good
                                *More optimized elegant DP Solution from GFG
                                *Uses the approach  that i discarded/not pursued enough
                                during brainstorming
                                *DPO Solution is vaguely understandable
                                *Problem is now closed
[+]Level                      : Medium
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/longest-repeating-subsequence/
"""
#S-Complexity: O(N*N) | T-Complexity: O(N*N)
def findSolution(string):
    length = len(string)
    dp = [[0]*(length+1) for x in range(length+1)]

    for i in range(1, length+1):
        for j in range(1, length+1):
            if(string[i-1]==string[j-1] and i!=j):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[length][length]

if __name__ == "__main__":
    string = "aabb"
    string = "axxxy"
    string = "abc"
    string = "aab"

    print(findSolution(string))
