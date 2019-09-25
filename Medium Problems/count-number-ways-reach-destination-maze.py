# M.72

"""
Count number of ways to reach destination in a Maze
Given a maze with obstacles, count number of paths to reach rightmost-bottommost cell from topmost-leftmost cell. A cell in given maze has value -1 if it is a blockage or dead end, else 0.

From a given cell, we are allowed to move to cells (i+1, j) and (i, j+1) only.

Examples:

Input: maze[R][C] =  {{0,  0, 0, 0},
                      {0, -1, 0, 0},
                      {-1, 0, 0, 0},
                      {0,  0, 0, 0}};
Output: 4
There are four possible paths as shown in
below diagram.
blockage


[+]Temporal marker            :  Wed, 9:21 | Sep 25, 19
[+]Temporal marker untethered :  Wed, 9:27 | Sep 25, 19
[+]Comments                   : *Knew the  approach
                                *Just implemented
                                *Solution devised in record time
                                *Problem is now closed
[+]Level                      : Easy
[+]Tread speed                : Paced
[+]LINK                       : https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze
"""


def findSolution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * (cols + 1) for x in range(rows + 1)]
    dp[0][1] = 1

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if (matrix[i - 1][j - 1] != -1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[rows][cols]


if __name__ == "__main__":
    matrix = [[0, 0, 0, 0],
              [0, -1, 0, 0],
              [0, 0, -1, 0],
              [0, 0, 0, 0]]
    print(findSolution(matrix))
