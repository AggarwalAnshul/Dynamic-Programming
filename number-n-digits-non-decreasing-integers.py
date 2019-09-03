"""
#101
Number of n-digits non-decreasing integers
Given an integer n > 0, which denotes the number of digits, the task to find total number of n-digit positive integers which are non-decreasing in nature.
A non-decreasing integer is a one in which all the digits from left to right are in non-decreasing form. ex: 1234, 1135, ..etc.
Note :Leading zeros also count in non-decreasing integers such as 0000, 0001, 0023, etc are also non-decreasing integers of 4-digits.

Examples :

Input : n = 1
Output : 10
Numbers are 0, 1, 2, ...9.

Input : n = 2
Output : 55

Input : n = 4
Output : 715

There is only one obstacle in the middle.
[+]Temporal marker            : Didn't Tether N/A | Sept03, 2019, Tuesday
[+]Temporal marker untethered : Didn't Tether N/A | Sept03, 2019, Tuesday
[+]Comments                   : Took about an hour unitl i found the pattern in 2D dp grid
                                Took about half an hour in implementation, idk for some
                                strange reasons was confused in 0Indexing... Pfff!
                                Anyways done without 0 help!
[+]LINK                       : https://www.geeksforgeeks.org/number-n-digits-non-decreasing-integers/
"""
import PrintMatrix as pm
def findSolution(n):
    #init
    dp = [[0]*(10+1) for x in range(n+1)]
    for x in range(10+1):
        dp[0][x] = 1

    for i in range(1, n+1):
        for j in range(1, 10+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #pm.printMatrix(dp)
    return dp[n][10]

if __name__ == "__main__":
    n = 5
    print(findSolution(n))
