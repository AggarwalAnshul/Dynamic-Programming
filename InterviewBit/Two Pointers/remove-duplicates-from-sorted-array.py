"""
Remove Duplicates from Sorted Array
Asked in:
Expedia
Microsoft
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost one and
return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,2].

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
