"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P.......A........H.......N
..A..P....L....S....I...I....G
....Y.........I........R
And then read line by line: PAHNAPLSIIGYIR
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
**Example 2 : **
ABCD, 2 can be written as

A....C
...B....D
and hence the answer would be ACBD.

[+]Temporal marker           : Wed, 17:9 | Feb 19, 20
[+]Temporal marker untethered: Wed, 17:24 | Feb 19, 20
[+]Comments                  : Knew the approach
                                Matter is closed now
[+]Space Complexity          : O(N*R)
[+]Time Complexity           : O(N*R)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/zigzag-string
[+] Supplement Sources       : N/A
"""


def findSolution(string, rows):
    length = len(string)
    dp = [[None for x in range(length)] for y in range(rows)]

    dir = 0  # 1 is up | 0 is down
    index = 0
    i, j = 0, 0
    while index < length:
        if rows == 1:
            dir = 2
        elif i == 0:
            dir = 0
        elif i == rows - 1:
            dir = 1
        dp[i][j] = string[index]
        index += 1
        j += 1
        if dir == 0:
            i += 1
        elif dir ==1:
            i -= 1


    ans = ""
    for i in range(rows):
        for j in range(length):
            if dp[i][j] != None:
                ans += dp[i][j]
    return ans


if __name__ == "__main__":
    data = [["Paypalishiring", 1],["",8]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x[0], x[1])))
