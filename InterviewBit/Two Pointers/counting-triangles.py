"""
Programming Two Pointers Counting Triangles
Counting Triangles
You are given an array of N non-negative integers, A0, A1 ,…, AN-1.
Considering each array element Ai as the edge length of some line segment, count the number of triangles which you can form using these array values.

Notes:

You can use any value only once while forming each triangle. Order of choosing the edge lengths doesn’t matter. Any triangle formed should have a positive area.

Return answer modulo 109 + 7.

For example,

A = [1, 1, 1, 2, 2]

Return: 4


[+]Temporal marker           : Mon, 13:9 | Feb 24, 20
[+]Temporal marker untethered: Mon, 19:22 | Feb 24, 20
[+]Comments                  : Finally solved the problem.
                                Though it required a lot of brainstorming
                                Did it w/o any help whatsoever
                                With this problem i believe i got the insight of
                                TWOPOINTERS
                                Matter is closed now
                                PS: I was playing PUBG, COOKING FOOD & Logged into WFH
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N*N)
[+]Level                     : MEDIUM
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/counting-triangles
[+] Supplement Sources       : N/A
"""


# Accepted but TLE
def findSolution(lis):
    lis.sort()
    length = len(lis)
    number_of_triangles = 0
    for index in range(length):
        a = lis[index]
        right = 2
        for secondIndex in range(index + 1, length):
            b = lis[secondIndex]
            while right < length and a + b > lis[right]:
                right += 1
            number_of_triangles += right - secondIndex - 1
    return number_of_triangles % (10 ** 9 + 7)


if __name__ == "__main__":
    data = [[1, 1, 1, 2, 2],
            [4, 6, 13, 16, 20, 3, 1, 12]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
