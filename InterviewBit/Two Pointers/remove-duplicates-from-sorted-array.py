"""

[+]Temporal marker           : Thu, 23:01 | Feb 27, 20
[+]Temporal marker untethered: Thu, 23:10 | Feb 27, 20
[+]Comments                  : EASY Question | Wrong Problem Statement
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : PACED
[+]LINK                      : https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array
[+] Supplement Sources       : N/A
"""


def findSolution(lis):
    index = 1
    length = len(lis)
    count = 1
    nextIndex = 1
    for index in range(1, length):
        if lis[index] != lis[index - 1]:
            lis[nextIndex] = lis[index]
            nextIndex += 1
            count += 1
    return count


if __name__ == "__main__":
    data = []
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
