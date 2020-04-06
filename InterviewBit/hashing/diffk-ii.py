"""
/*DESC
Programming Hashing Diffk Ii
Diffk II
Asked in:  
Facebook
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Example :

Input :

A : [1 5 3]
k : 2
Output :

1
as 3 - 1 = 2

Return 0 / 1 for this problem.
*/

[+]Temporal marker            :0823 Hours | Monday 06, 2020
[+]Temporal marker Untethered :0833 Hours | Monday 06, 2020
[+]Comments                   : Solved in record time, almost flashed it
[+]Space Complexity           : O(N)
[+]Time Complexity            : O(N)
[+]Level                      : EASY
[+]Tread Speed                : PACED
[+]LINK                      : https://www.interviewbit.com/problems/diffk-ii.py
[+] Supplement Sources       : N/A

"""

# ACCEPTED


def diffPossible(lis, target):
    hashmap = {}
    for index, value in enumerate(lis):
        if value not in hashmap:
            hashmap[value] = index
        elif target == 0:
            return 1
    for index, value in enumerate(lis):
        if value - target in hashmap and hashmap[value-target] != index:
            return 1
    return 0


# Editorial Inspired
# Fully Acceptable
def diffPossible_editorial(lis, target):
    hashmap = {}
    for value in lis:
        if hashmap.get(value + target) or hashmap.get(value - target):
            return 1
        hashmap[value] = True
    return 0


if __name__ == "__main__":
    test_cases = [
        [[1, 5, 3], 2],
        [[0], 0],
        [[1, 5, 4, 1, 2], 0]
    ]
    for index in range(len(test_cases)):
        test_case = test_cases[index]
        print("input: "+str(test_case)+"\n\tOUTPUT: :" +
              str(diffPossible(test_case[0], test_case[1])) +
              "\n\tEDITORIAL: "+str(diffPossible_editorial(test_case[0], test_case[1])))
