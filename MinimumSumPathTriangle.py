"""
Minimum Sum Path in a Triangle
Given a triangular structure of numbers, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Examples :

Input : 
   2
  3 7
 8 5 6
6 1 9 3
Output : 11
Explanation : 2 + 3 + 5 + 1 = 11

Input :
   3
  6 4
 5 2 7
9 1 8 6
Output : 10
Explanation : 3 + 4 + 2 + 1 = 10

Temporal maker: 13:53 Hours | Aug20, Tuesday
Temporal marker untethered: 13:55 Hours | Aug20, Tuesday
LINK: https://www.geeksforgeeks.org/minimum-sum-path-triangle/
"""
#triangle = [[8, 0, 0, 0], [-4, 4, 0, 0], [2, 2, 6, 0], [1, 1, 1, 1]]
def printMatrix(dp):
    print()
    for x in dp:
        for y in x:
            print(y, end=" ")
        print()
        
def findMinimumSumPathInTriangle(triangle):
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
                dp[i][j] += triangle[i][j] + min(branchBottom, branchRight)

    return dp[0][0]

            
#triangle = [  [3, 0, 0, 0], [7, 4, 0, 0], [2, 4, 6, 0],[8, 5, 9, 3] ]
#triangle = [[8, 0, 0, 0], [-4, 4, 0, 0], [2, 2, 6, 0], [1, 1, 1, 1]]
triangle = [ [ 2 ],[ 3, 9 ],[ 1, 6, 7 ] ]
print(findMinimumSumPathInTriangle(triangle))


