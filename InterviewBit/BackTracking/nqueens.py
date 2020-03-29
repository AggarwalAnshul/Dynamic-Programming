'''

Programming Backtracking N Queens
NQueens
Asked in:
Qualcomm
Google
Amazon
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no
 two queens attack each other.

N Queens: Example 1

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens’ placement, where 'Q'
and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]


[+]Temporal marker           : 11:31 Hours | Sunday 29, 2020
[+]Temporal marker untethered: 12:00 Hours | Sunday 29, 2020
[+]Comments                  : Flashed it
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

#FLASHED IT!
#ACCEPTED
def solveNQueens(n):

    def printPattern(lis):
        ans = []
        for item in lis:
            string = ""
            for i in range(0,len(lis)):
                string += "Q" if i == item else "."
            ans.append(string)
        return ans

    def placementPossible(current_row, placementRow, index, placementValue):
        if (index == placementValue or
            index == placementValue + (current_row-placementRow) or
            index == placementValue - (current_row-placementRow)):
            return False
        return True

    frontier, solution = [ (n, [])], []
    while frontier:
        queen, placement = frontier.pop()

        if queen == 0:
            solution.append(placement)
            continue

        for index in range(n):
            flag = True
            current_row = len(placement)
            for placement_index in range(len(placement)):
                flag = flag and placementPossible(current_row, placement_index, index, placement[placement_index])
            if flag:
                frontier.append((queen-1, placement+[index]))

    return [printPattern(x) for x in reversed(solution)]

if __name__ == '__main__':
    print(solveNQueens(4))