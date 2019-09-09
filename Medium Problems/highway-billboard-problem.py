"""
#M.20
Highway Billboard Problem
Consider a highway of M miles. The task is to place billboards on the highway such
that revenue is maximized. The possible sites for billboards are given by number
x1 < x2 < ….. < xn-1 < xn, specifying positions in miles measured from one end
of the road. If we place a billboard at position xi, we receive a revenue of
ri > 0. There is a restriction that no two billboards can be placed within t
miles or less than it.

Note : All possible sites from x1 to xn are in range from 0 to M as need to place
billboards on a highway of M miles.

Examples:

Input : M = 20
        x[]       = {6, 7, 12, 13, 14}
        revenue[] = {5, 6, 5,  3,  1}
        t = 5
Output: 10
By placing two billboards at 6 miles and 12
miles will produce the maximum revenue of 10.

Input : M = 15
        x[] = {6, 9, 12, 14}
        revenue[] = {5, 6, 3, 7}
        t = 2
Output : 18  

[+]Temporal marker            : 15:00 Hours, | Monday Sept09, 19
[+]Temporal marker untethered : 15:20 Hours  | Monday Sept09, 19
[+]Comments                   : implemented sort of kadane's algorithm 
[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/highway-billboard-problem/
"""

#S-Complexity: O(m) | T-Complexity: O(mile*mile)+
def findSolution(mile, revenue, limit):
    dp = [0]*len(mile)
    dp[0] = revenue[0]
    answer = 0

    for x in range(1, len(mile)):
        localMax = revenue[x]
        for y in range(x):
            localMax = max(localMax, dp[y])
            if(mile[y]+limit<mile[x]):
                localMax = max(localMax, dp[y]+revenue[x])
        dp[x] = localMax
        answer = max(answer, dp[x])
        
    print(dp)
    return answer

if __name__ == "__main__":
    #lis = [tiles, ranges, limit]
    lis = [[6, 7, 12, 13, 14], [5, 6, 5, 3, 1], 5]  
    lis = [[6, 9, 12, 14], [5, 6, 3, 7], 2]
    print(findSolution(lis[0], lis[1], lis[2]))
    
