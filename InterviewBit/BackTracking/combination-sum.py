'''
Programming Backtracking Combination Sum
Combination Sum
Asked in:
Facebook
Amazon
Adobe
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where
the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi
AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example,
Given candidate set 2,3,6,7 and target 7,
A solution set is:

[2, 2, 3]
[7]
 Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING COMBINATIONS.
Example : itertools.combinations in python.


[+]Temporal marker           : 22:32 Hours | Monday 23, 2020
[+]Temporal marker untethered: 11:12 Hours | Monday 24, 2020
[+]Comments                  : Actually I did solve the problem yesterday night but I wasn't too happy with solution
                                >> Today mornign the solution was an improvement
                                >> took me about 20 mins or so
                                >> Editorial was an eye opener
                                >> they anyways used sort and set fucntion hence bringin my solution to same level
                                >> Anyways, understood the editorial solution inside out.
                                >> MAtter is closed now
[+]Space Complexity          : O(2^n)
[+]Time Complexity           : O(2^n)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A


'''

#Accepetd but can be optimized further
def combinationSum(lis, target):
    def driver(index, sum, lis, target):
        if sum == target:
            return [[]]
        if sum > target:
            return []
        if index == len(lis):
            return []
        temp = []
        for item in driver(index, sum+lis[index], lis, target):
            temp.append([lis[index]]+item)
        for item in driver(index+1, sum+lis[index], lis, target):
            temp.append([lis[index]] + item)
        for item in driver(index+1, sum, lis, target):
            temp.append([] + item)
        return temp
    ans = []
    for x in sorted(driver(0, 0, lis, target)):
        if not ans or ans[-1]!= x:
            ans.append(x)
    return ans

#OUT of scope, using library function
def quick(lis, target):
    import itertools as iter
    ans = []
    length = len(lis)
    for pair in range(1, length+1):
        for item in iter.combinations_with_replacement(lis, pair):
            if sum(item) == target:
                ans.append(item)
    return sorted(ans)

def combination_experimental(lis, target):
    lis = list(set(lis))
    lis.sort(reverse=True)
    frontier = [(0, [])]
    solution = []
    while frontier:
        sum, subset_so_far = frontier.pop()
        if sum == target:
            solution.append(subset_so_far)
            continue
        if sum > target:
            continue
        for candidate in lis:
            if not subset_so_far or candidate >= subset_so_far[-1]:
                frontier.append( (sum + candidate,
                                  subset_so_far + [candidate]))
    return solution




if __name__ == '__main__':
    test_cases = [
        [[2, 3, 6, 7],7],
        [[1, 2, 3], 4]
    ]
    for test_case in test_cases:
        print("input: "+str(test_case)+
              "\n\toutput: "+str(combination_experimental(test_case[0], test_case[1])))