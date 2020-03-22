'''
Subset
Asked in:
Amazon
Microsoft
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]

[+]Temporal marker           : 18:7 Hours | Sunday 22, 2020
[+]Temporal marker untethered: 17:07 Hours | Sunday 22, 2020
[+]Comments                  : Took some time to implement the solution
                                >>Devised solution was correct and accepted
                                >> Editorial solution was using iteration
                                >>I Liked the editorial solution more, much more elegant
                                >> Implemented the editorial solution
                                >> I gain much more insight on this topic
[+]Space Complexity          : O(2^N)
[+]Time Complexity           : O(2^N)
[+]Level                     : EASY
[+]Tread Speed               : Intermittent
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

'''

#Accepted
def subset_obsolete(A):
    if len(A) == 0:
        return [[]]
    A.sort()

    def subset(lis, index):
        if index == len(lis) - 1:
            return [[lis[index]]]
        result = [[lis[index]]]
        temp = subset(lis, index + 1)
        for item in temp:
            result.append([lis[index]] + item)
        result = result + temp
        return result

    ans = subset(A, 0)
    ans.insert(0, [ ])
    return ans


# Accepted & Elegant
# @param lis: list of element
# return the lis of subsets
def subset(lis):
    lis.sort(reverse=True)
    results = [  ]
    while lis:
        item = lis.pop(0)
        temp = []
        for result in results:
            temp.append( [item] + result)
        results = [[item]] + temp + results
    return [[]] + results

if __name__ == '__main__':
    test_cases = [
        [3, 2, 1],
        [15, 20, 12, 19, 4]
    ]
    for test_case in test_cases:
        print( subset(test_case))