"""
#M.31
Count All Palindromic Subsequence in a given String
Find how many palindromic subsequence (need not necessarily be distinct) can be formed in a given string. Note that the empty string is not considered as a palindrome.
Examples:

Input : str = "abcd"
Output : 4
Explanation :- palindromic  subsequence are : "a" ,"b", "c" ,"d" 

Input : str = "aab"
Output : 4
Explanation :- palindromic subsequence are :"a", "a", "b", "aa"

Input : str = "aaaa"
Output : 15

[+]Temporal marker            : N/A  Hours, | Wednesday Sept11, 19
[+]Temporal marker untethered : N/A  Hours  | Wednesday Sept11, 19
[+]Comments                   : *Couldn't solve on my own
                                *Solution help from GFG
                                *Didn't try beyond 1 hour
                                *Gave up too early
                                *Was restricted to tabulization approach
[+]Tread speed                : Relaxed
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforg eeks.org/count-palindromic-subsequence-given-string/
"""

def findSolution(string, i, j, dp):
    if(i==j):
        return 1
    if(i>j):
        return 0
    if(dp[i][j]==-1):
        if(string[i]==string[j]):
            include = findSolution(string, i+1, j-1, dp) + 1
            exclude = (findSolution(string, i+1, j, dp) +
                       findSolution(string, i, j-1, dp) -
                       findSolution(string, i+1, j-1, dp) )
            dp[i][j] = include + exclude
        else:
            dp[i][j] =  ( findSolution(string, i+1, j, dp) +
                          findSolution(string, i, j-1, dp) -
                          findSolution(string, i+1, j-1, dp)
                         )
    return dp[i][j]
if __name__ == "__main__":
    string = "aaaa"
    string = "aab"
    string = "abibs"
    string = "abcb"
    length = len(string)
    dp = [[-1]*(length) for x in range(length)]
    print(findSolution(string, 0, len(string)-1, dp))
