"""
Maximum path sum in a triangle.
We have given numbers in form of triangle, by starting at the top of the
triangle and moving to adjacent numbers on the row below,
find the maximum total from top to bottom.

Examples :

Input : 
   3
  7 4
 2 4 6
8 5 9 3
Output : 23
Explanation : 3 + 7 + 4 + 9 = 23 

Input :
   8
 -4 4
 2 2 6
1 1 1 1
Output : 19
Explanation : 8 + 4 + 6 + 1 = 19

Temporal maker: 13:32 Hours | Aug20, Tuesday
Temporal marker untethered: 13:47 Hours | Aug20, Tuesday
LINK: https://www.geeksforgeeks.org/maximum-path-sum-triangle/
"""

def printMatrix(dp):
    print()
    for x in dp:
        for y in x:
            print(y, end=" ")
        print()
        
def findMaximumSumPathInTriangle(triangle):
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

            
triangle = [  [3, 0, 0, 0], [7, 4, 0, 0], [2, 4, 6, 0],[8, 5, 9, 3] ]
print(findMaximumSumPathInTriangle(triangle))


