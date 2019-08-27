"""
Find number of solutions of a linear equation of n variables
Given a linear equation of n variables, find number of non-negative integer solutions of it. For example,let the given equation be “x + 2y = 5”, solutions of this equation are “x = 1, y = 2”, “x = 5, y = 0” and “x = 1. It may be assumed that all coefficients in given equation are positive integers.

Example :

Input:  coeff[] = {1, 2}, rhs = 5
Output: 3
The equation "x + 2y = 5" has 3 solutions.
(x=3,y=1), (x=1,y=2), (x=5,y=0)

Input:  coeff[] = {2, 2, 3}, rhs = 4
Output: 3
The equation "2x + 2y + 3z = 4"  has 3 solutions.
(x=0,y=2,z=0), (x=2,y=0,z=0), (x=1,y=1,z=0)

[+]Temporal marker            : 13:03 Hours | Aug27, 2019
[+]Temporal marker untethered : 13:20 Hours | Aug27, 2019
[+]Tread speed                : Relaxed
[+]Comments                   : Couldn't crack the solution, took help from GFG
                                From GFG disqous it was revealed that it's similary to coin
                                change problem, once it was tought, it seemed obvious and the
                                solution was implemented pretty quickly as coin change was still
                                fresh in my memory and i knew the concept
[+]LINK : https://www.geeksforgeeks.org/find-number-of-solutions-of-a-linear-equation-of-n-variables/
"""
def findNumberOfSolutionsOfALinearEquationOfNVariables(coeff, rhs):
    dp = [[0]*(len(coeff)+1) for x in range(rhs+1)]
    maxCount = 0
    
    #init
    for x in range(0, len(coeff)+1):
        dp[0][x] = 1
        
    for i in range(1, rhs+1):
        for j in range(1, len(coeff)+1):
            if(i<coeff[j-1]):
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j], dp[i-coeff[j-1]][j]+dp[i][j-1])
            maxCount = max(maxCount, dp[i][j])
    return maxCount

coeff = [2,2,3]
rhs = 4
#coeff = [1,2]
#rhs = 5
print(findNumberOfSolutionsOfALinearEquationOfNVariables(coeff,rhs))
