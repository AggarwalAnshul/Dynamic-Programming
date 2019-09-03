"""
#106Different ways to sum n using numbers greater than or equal to m
Given two natural number n and m. The task is to find the number of ways in
which the numbers that are greater than or equal to m can be added to get the sum n.

Examples:

Input : n = 3, m = 1
Output : 3
Following are three different ways
to get sum n such that each term is
greater than or equal to m
1 + 1 + 1, 1 + 2, 3 

Input : n = 2, m = 1
Output : 2
Two ways are 1 + 1 and 2


[+]Temporal marker            : 18:47 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 18:58 Hours |Sept03, 2019, Tuesday
[+]Comments                   : Recognized it as a coin change varation
                                at the first glance, just implemented the soln
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/different-ways-sum-n-using-numbers-greater-equal-m/
"""

def findSolution(n, m):
    numbersToAdd = []
    for x in range(m, n+1):
        numbersToAdd.append(x)
   
    #init
    length = len(numbersToAdd)
    dp = [[0]*(length+1) for x in range(n+1)]
    dp[0] = [1]*(length+1)

    for i in range(1, n+1):
        for j in range(1, length+1):
            if(i>=numbersToAdd[j-1]):
                dp[i][j] = dp[i][j-1] + dp[i-numbersToAdd[j-1]][j]
            else:
                dp[i][j] = dp[i][j-1]
    #import PrintMatrix as pm
    #pm.printMatrix(dp)
    return dp[n][length]
    
if __name__ == "__main__":
    lisNM = [2, 1]
    lisNM = [3, 1]
    lisNM = [10, 2]
    print(findSolution(lisNM[0], lisNM[1]))
