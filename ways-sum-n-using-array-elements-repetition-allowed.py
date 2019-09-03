"""
#99
Ways to sum to N using array elements with repetition allowed
Given a set of m distinct positive integers and a value ‘N’. The problem is to count the total number of ways we can form ‘N’ by doing sum of the array elements. Repetitions and different arrangements are allowed.

Examples :

Input : arr = {1, 5, 6}, N = 7
Output : 6

Explanation:- The different ways are:
1+1+1+1+1+1+1
1+1+5
1+5+1
5+1+1
1+6
6+1

Input : arr = {12, 3, 1, 9}, N = 14
Output : 150

[+]Temporal marker            : 11:30 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 11:47 Hours | Sept03, 2019, Tuesday
[+]Comments                   : Knew the approach just implemented, took some time to remember
                                and cold press the entire execution, but figured it out on my own
                                so it's all settled now
[+]LINK                       : https://www.geeksforgeeks.org/ways-sum-n-using-array-elements-repetition-allowed/
"""

#S-Complexity: O(sumCount) | T-Complexity: O(sumCount*length of coins)
def findSolution(lis, sumCount):
    length = len(lis)
    dp = [0]*(sumCount+1)
    dp[0] = 1

    for i in range(1, sumCount+1):
        for j in range(0, length):
            if(i>=lis[j]):
                dp[i]+=dp[i-lis[j]]
    return(dp[sumCount])

if __name__ == "__main__":

    #print(findSolution([1,5,6], 7))
    print(findSolution([12, 3, 1, 9],14))
    
