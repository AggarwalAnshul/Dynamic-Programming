#M.74

"""
Count number of binary strings without consecutive 1’s
Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.
Examples:

Input:  N = 2
Output: 3
// The 3 strings are 00, 01, 10

Input: N = 3
Output: 5
// The 5 strings are 000, 001, 010, 100, 101


[+]Temporal marker            :  Wed, 11:10                           | Sep 25, 19
[+]Temporal marker untethered :  Wed, 11:22(Obsolete) 1:33(Efficient) | Sep 25, 19
[+]Comments                   : *Devised the approach
                                *I cannot say, i might/might not have uncovered efficient solution
                                *had i not seen the word fibonacci on GFG
                                *lest I devised the more efficient solution
                                *I think i might be successful to find this link on my own
                                *Problem is now closed
[+]Level                      : Easy
[+]Tread speed                : Paced
[+]LINK                       : https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s
"""

#S-Complexity: O(1) | T-Complexity: O(N)
def findSolution(n):
    if(n==1):
        return 2
    one = 1
    two = 2
    for i in range(1, n):
        sum = one + two
        one = two
        two = sum
    return sum

#S-Complexity: O(N) | T-Complexity: O(N)
def findSolutionObsolete(n):
    dp = [[0,0] for x in range(n)]
    dp[0] = [1,1]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        dp[i][1] = dp[i-1][0]
    return dp[n-1][0]+dp[n-1][1]

if __name__ == "__main__":
    n = 2
    n = 1
    n = 3
    n = 4
    n = 1024
    print(findSolution(n), end="\n")
    print(findSolutionObsolete(n), end="\n")