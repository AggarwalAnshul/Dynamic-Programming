"""
#91
Remove array end element to maximize the sum of product
Given an array of N positive integers. We are allowed to remove element from
either of the two ends i.e from the left side or right side of the array. Each
time we remove an element, score is increased by
value of element * (number of element already removed + 1).
The task is to find the maximum score that can be obtained by removing all the element.

Examples:

Input : arr[] = { 1, 3, 1, 5, 2 }.
Output : 43
Remove 1 from left side (score = 1*1 = 1)
then remove 2, score = 1 + 2*2 = 5
then remove 3, score = 5 + 3*3 = 14
then remove 1, score = 14 + 1*4 = 18
then remove 5, score = 18 + 5*5 = 43.

Input :  arr[] = { 1, 2 }
Output : 5.

[+]Temporal marker            : 15:31 Hours | Sept02, 2019, Monday
[+]Temporal marker untethered : 10:54 Hours | Sept02, 2019, Monday
[+]Comments                   : *Recursive solution produced in record time
                                *DP Solution not satisfactory in GFG
                                *Some erros in DP Solution, laid down for now
                                UPDATE:
                                *DP Solution devised
                                *Works in accordance to recursive solution
                                *Had the same approach to execute it initially,
                                *After layoff, had a comprehensive look at the GFG DP Solution
                                *Problem is now CLOSED! :D
[+]LINK                       : https://www.geeksforgeeks.org/remove-array-end-element-maximize-sum-product/
"""

def findSolutionDp(lis, count, start, end, dp):
    if(start==end):
        return (count+1)*lis[start]
    if(dp[start][end] == -1):
        branchOne = lis[start]*(count+1) + findSolutionDp(lis, count+1, start+1, end, dp)
        branchTwo = lis[end]*(count+1) + findSolutionDp(lis, count+1, start, end-1, dp)
        dp[start][end] = max(branchOne, branchTwo)
    return dp[start][end]

def findSolutionR(lis, count, start, end, sumCount):
    #print("start: "+str(start)+" end: "+str(end)+" : sum" + str(sumCount))
    if(start>end):
        return sumCount
    left = 0
    right = 0
    if(start+1<len(lis)):
        left = findSolutionR(lis, count+1, start+1, end, sumCount+(lis[start]*(count+1)))
    if(end-1>=0):
        right = findSolutionR(lis, count+1, start, end-1, sumCount+(lis[end]*(count+1)))
    return max(left, right)

if __name__ == "__main__":
    lis = [2, 2]
    lis = [3, 3]
    lis = [10, 18]
    lis = [1,2]
    lis = [1,3,1,5,2]
    lis = [1, 3, 1,8,54,7,5,778,10,18, 5, 2 ]
    dp = [[-1] *(len(lis)) for x in range(len(lis))]
    print(findSolutionR(lis, 0, 0, len(lis)-1, 0))
    print(findSolutionDp(lis, 0, 0, len(lis)-1, dp))
