"""
Subsets II
Asked in:
Amazon
Microsoft
Given a collection of integers that might contain duplicates, S, return all
 possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example :
If S = [1,2,2], the solution is:

[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]


[+]Temporal marker           : 18:04 Hours | Tuesday 24, 2020
[+]Temporal marker untethered: 18:10 Hours | Tuesday 24, 2020
[+]Comments                  : >>SOLVED IS RECORD TIME, NAH! Cause i knew the solution to similar problem
                                >> Also implemented the backtrack solution
                                >> Matter is closed now
[+]Space Complexity          : O(2^n)
[+]Time Complexity           : O(2^n)
[+]Level                     : EASY
[+]Tread Speed               : Paced
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A
"""

# Accepted
def subsetsWithDup(lis):
    import itertools as iter
    lis.sort()
    length = len(lis)
    solution = []
    for pair_length in range(1, length+1):
        for subset in iter.combinations(lis, pair_length):
            solution.append(subset)
    solution.append(())
    return sorted(list(set(solution)))

#Accepted
def subsetsWithDupNoLibraryFun(lis):
    lis.sort()
    length = len(lis)
    solution = []
    frontier = [ ([],-1) ]
    while frontier:
        subset, index = frontier.pop()
        solution.append(subset)
        for i in range(index+1, length):
            frontier.append( (subset+[lis[i]], i))
    return sorted(list(set(tuple(x) for x in solution)))


if __name__ == '__main__':
    print(subsetsWithDupNoLibraryFun([5,4]))