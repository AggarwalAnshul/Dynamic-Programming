"""
#100
Unique paths in a Grid with Obstacles
Given a grid of size m * n, let us assume you are starting at (1, 1) and your goal is to
reach (m, n). At any instance, if you are on (x, y), you can either go to (x, y + 1) or
(x + 1, y).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space are marked as 1 and 0 respectively in the grid.

Examples:

Input: [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
Output : 2
There is only one obstacle in the middle.
[+]Temporal marker            : 12:02 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 11:23 Hours | Sept03, 2019, Tuesday
[+]Comments                   : Knew the approach just implemented, took some time to remember
                                and cold press the entire execution, but figured it out on my own
                                so it's all settled now
[+]LINK                       : https://www.geeksforgeeks.org/unique-paths-in-a-grid-with-obstacles/
"""

#S-Complexity: O(sumCount) | T-Complexity: O(sumCount*length of coins)
def findSolution(maze):
    rows = len(maze)
    cols = len(maze[0])
    dp = [[0]*(cols) for x in range(rows)]

    #init
    for x in range(cols):
        if(maze[0][x]!=1):
            dp[0][x] = 1
        else:
            break
    for x in range(1, rows):
        if(maze[x][0]!=1):
            dp[x][0] = 1
        else:
            break

    for i in range(1, rows):
        for j in range(1, cols):
            if(maze[i][j]!=1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[rows-1][cols-1]

if __name__ == "__main__":
    maze = [[0,0,0,0],[0,1,0,1],[0,0,0,0],[0,0,0,0]]
    maze = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(findSolution(maze))
    
