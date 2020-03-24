"""
Programming Backtracking Combination Sum Ii
Combination Sum II
Asked in:
Microsoft
Amazon
Infosys
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C
where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example :

Given candidate set 10,1,2,7,6,1,5 and target 8,

A solution set is:

[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.


[+]Temporal marker           : 17:38 Hours | Tuesday 24, 2020
[+]Temporal marker untethered: 17:55 Hours | Tuesday 24, 2020
[+]Comments                  : >>SOLVED IS RECORD TIME, NAH! Cause i knew the solution to similar problem
[+]Space Complexity          : O(2^n)
[+]Time Complexity           : O(2^n)
[+]Level                     : MEDIUM
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""

#Accepted
def combinationSum(lis, target):
    lis.sort()
    frontier = [(0, -1, [])]
    solution = []
    while frontier:
        sum, index, subset_so_far = frontier.pop()
        if sum == target:
            solution.append(subset_so_far)
            continue
        if sum > target:
            continue
        for i in range(index + 1, len(lis)):
            frontier.append((sum + lis[i], i, subset_so_far + [lis[i]]))
    return list(set(tuple(x) for x in solution))


if __name__ == '__main__':
    print(combinationSum([10,1,2,7,6,1,5], 8))