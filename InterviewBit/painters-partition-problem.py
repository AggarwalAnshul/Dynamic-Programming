"""
Given 2 integers A and B and an array of integars C of size N.

Element C[i] represents length of ith board.

You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units
of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint
contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003



Input Format

The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer array C.
Output Format

Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous
sections of board % 10000003.
Constraints

1 <=A <= 1000
1 <= B <= 10^6
1 <= C.size() <= 10^5
1 <= C[i] <= 10^6
For Example

Input 1:
    A = 2
    B = 5
    C = [1, 10]
Output 1:
    50
Explanation 1:
    Possibility 1:- same painter paints both blocks, time taken = 55units
    Possibility 2:- Painter 1 paints block 1, painter 2 paints block 2, time take = max(5, 50) = 50
    There are no other distinct ways to paint boards.
    ans = 50%10000003

Input 2:
    A = 10
    B = 1
    C = [1, 8, 11, 3]
Output 2:
    11

[+]Temporal marker           : Tue, 9:47 | Feb 04, 20
[+]Temporal marker untethered: Tue, 22:28 | Feb 04, 20
[+]Comments                  : Took about a day or to come up with a DP solution with complexity O(k*N*N)
                                * DP Solution devised on my own
                                *for the more optimized binary solution would need help
                                *for understanding this problem use:
                                    https://www.topcoder.com/community/competitive-programming/tutorials/binary-search
                                *Binary search solution took a long time to understand, implement and finally perfect.
[+]Complexity                : Binary Search : O(log(sum(N)) | DP: O(painters*boards*boards)
[+]Level                     : Medium Level
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/painters-partition-problem

"""
import sys


def isPossible(mid, painters, board):
    painter = 1
    local = 0
    for x in board:
        if local + x <= mid:
            local += x
        else:
            local = x
            painter += 1
    if painter < painters + 1:
        return True
    return False


def paints(painters, time, board):
    right = 0
    left = -sys.maxsize + 1
    for x in board:
        right += x
        left = max(left, x)
    while left < right:
        mid = (left + right) // 2
        print("mid: " + str(mid))
        if isPossible(mid, painters, board):
            print("possible")
            right = mid  # if x is possible and x-1 isn't still all x+1 to right of it would be still possible
        else:
            print("impossible")
            left = mid + 1
        print("left: " + str(left) + " right: " + str(right))
    return left


def paint(painters, time, board):
    boards = len(board)
    dp = [[0 for x in range(boards)] for y in range(painters)]
    dp[0][0] = board[0]
    for x in range(1, boards):
        dp[0][x] = dp[0][x - 1] + board[x]

    for i in range(1, painters):
        for j in range(boards):
            local_ans = sys.maxsize
            for k in range(j + 1):
                local_ans = min(local_ans, max(dp[i - 1][k], dp[0][j] - dp[0][k]))
            dp[i][j] = local_ans
    return (dp[painters - 1][boards - 1] * time) % 10000003


if __name__ == '__main__':
    # inputData = [painters, time, board[] ]
    inputData = [3, 10, [640, 435, 647, 352, 8, 90, 960, 329, 859]]
    print(paints(inputData[0], inputData[1], inputData[2]))
