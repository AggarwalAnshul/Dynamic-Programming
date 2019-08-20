""""
Maximum sum of a path in a Right Number Triangle
Given a right triangle of numbers, find the largest of the sum of numbers
that appear on the paths starting from the top towards the base, so that on
each path the next number is located directly below or
below-and-one-place-to-the-right.

Examples :

Input : 1
        1 2
        4 1 2
        2 3 1 1        
Output : 9
Explanation : 1 + 1 + 4 + 3

Input : 2
        4 1
        1 2 7
Output : 10
Explanation : 2 + 1 + 7

Temporal maker: 13:59 Hours | Aug20, Tuesday
Temporal marker untethered: 13:59 Hours | Aug20, Tuesday
LINK: https://www.geeksforgeeks.org/maximum-path-sum-triangle/
"""
#triangle = [[8, 0, 0, 0], [-4, 4, 0, 0], [2, 2, 6, 0], [1, 1, 1, 1]]
def printMatrix(dp):
    print()
    for x in dp:
        for y in x:
            print(y, end=" ")
        print()
        
def findMaximumSumPathInRightTriangle(triangle):
    length = len(triangle)
    dp = [[0]*length for x in range(length)]

    for i in range(length-1, -1, -1):
        for j in range(length-1, -1, -1):
            if(j<=i):
                branchBottom = 0
                branchRight = 0
                if(i+1 <= length-1):
                    branchBottom =  dp[i+1][j]
                    if(j+1 <= length-1):
                        branchRight = dp[i+1][j+1]
                dp[i][j] += triangle[i][j] + max(branchBottom, branchRight)

    return dp[0][0]


triangle = [  [1, 0, 0, 0], [1, 2, 0, 0], [4, 1, 2, 0],[2, 3, 1, 1] ]            
#triangle = [  [3, 0, 0, 0], [7, 4, 0, 0], [2, 4, 6, 0],[8, 5, 9, 3] ]
#triangle = [[8, 0, 0, 0], [-4, 4, 0, 0], [2, 2, 6, 0], [1, 1, 1, 1]]
print(findMaximumSumPathInRightTriangle(triangle))




