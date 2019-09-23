#M.57

"""
Weighted Job Scheduling
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Example:

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50}
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3
but the profit with this schedule is 20+50+100 which is less than 250.



[+]Temporal marker            :  Mon, 10:22 | Sep 23, 19
[+]Temporal marker untethered :  Mon, 10:32 | Sep 23, 19
[+]Comments                   : *Had a clear approach in my mind
                                *Implemented in record time
                                *Solution looks good
                                *Closing the problem npw
[+]Level                      : Basic
[+]Tread spee d               : Paced
[+]LINK                       : https://www.geeksforgeeks.org/weighted-job-scheduling
"""

#S-Complexity: O(N*N) | T-Complexity: O(N*N)
# Can be optimized to O(NlogN) using binary search for the inner for loop of , won't do although can do
def findSolution(lis):
    length = len(lis)
    dp = [0]*length
    dp[0] = lis[0][2]
    ans = lis[0][2]

    for i in range(1, length):
        dp[i] = lis[i][2]
        for j in range(i):
            if(lis[j][1] <= lis[i][0]):
                dp[i] = max(dp[i], dp[j]+lis[i][2])
        #print(dp)
        ans = max(ans, dp[i])
    return ans

if __name__ == "__main__":
    #lis = [job1[start, end, perk], job2[start, end, perk], ..... , jobn[start, end, perk]]
    lis = [ [1, 2, 50 ], [3, 5, 20 ], [6, 19, 100 ], [2, 100, 200 ]]
    print(findSolution(lis))