"""
Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new
length. Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place

For example,
Given input array A = [1,1,1,2],

Your function should return length = 3, and A is now [1,1,2].

[+]Temporal marker           : Thu, 23:4 | Feb 27, 20
[+]Temporal marker untethered: Fri, 16:54 | Feb 28, 20
[+]Comments                  : Was solving it, until golu insisted to play PUBG
                                Next day solved this problem in 10 mins max
                                matter is closed now.
[+]Space Complexity          : O(1)
[+]Time Complexity           : O(N)
[+]Level                     : EASY
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/emove-duplicates-from-sorted-array-ii
[+] Supplement Sources       : N/A
"""


def findSolution(lis):
    length = len(lis)
    flag = 0
    count = 1
    nextIndex = 1
    for index in range(1, length):
        print("index: "+str(index))
        if lis[index] != lis[index-1]:
            flag = 0
            count += 1
            lis[nextIndex] = lis[index]
            nextIndex += 1
            flag = 0
        elif lis[index] == lis[index-1]:
            if flag == 0:
                flag = 1
                lis[nextIndex] = lis[index]
                count += 1
                nextIndex += 1

    return str(count) + " >> " + str(lis)

if __name__ == "__main__":
    data = [[1,1,1,2,2,2,3,4]]
    for x in data:
        print("input: " + str(x) + " >> " + str(findSolution(x)))
    print("executiong is over...")