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
[+]Temporal marker untethered: 22:32 Hours | Monday 23, 2020
[+]Comments                  :
[+]Space Complexity          : O()
[+]Time Complexity           : O()
[+]Level                     :
[+]Tread Speed               :
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A


'''
def combinationSum(lis, target):
    dp = [[0 for y in range(len(lis)+1)] for x in range(target+1)]
    dp[0] = [1]*(len(lis)+1)
    for i in range(1, target+1):
        for j in range(1, len(lis)+1):
            if i >= lis[j-1]:
                dp[i][j] = dp[i][j-1] + dp[ i-lis[j-1]][j]
            else:
                dp[i][j] = dp[i][j-1]


    def findset(row, col, dp):
        if row < 0:
            return []
        if row == 0:
            return [ [ ] ]
        temp = []
        for index in range(1, col):
            if dp[row][index] > 0:
                for item in findset(row-lis[index-1], col, dp):
                    intermediate = sorted(item + [lis[index-1]])
                    temp.append(intermediate)
        return temp

    return findset(target, len(lis)+1, dp)


def combination(lis, target):
    def driver(index, sum, lis, target):
        if index == len(lis):
            return []
        sum += lis[index]
        if sum == target:
            return [ [] ]
        if index == len(lis):
            return []
        if sum > target:
            return []

        temp = []
        for item in driver(index, sum+lis[index], lis, target):
            temp.append([lis[index]]+item)
        for item in driver(index+1, sum + lis[index], lis, target):
            temp.append([lis[index]]+item)
        for item in driver(index+1, sum, lis, target):
            temp.append([lis[index]]+item)
        return temp
    driver(0,0, lis, target)
if __name__ == '__main__':
    test_cases = [
        [[2, 3, 6, 7],7],
        [[1, 2, 3], 4]
    ]
    for test_case in test_cases:
        print("input: "+str(test_case)+
              "\n\toutput: "+str(combination(test_case[0], test_case[1])))