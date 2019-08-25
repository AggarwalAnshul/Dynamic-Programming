"""
Minimum time to write characters using insert, delete and copy operation
We need to write N same characters on a screen and each time we can insert a character, delete the last character and copy and paste all written characters i.e. after copy operation count of total written character will become twice. Now we are given time for insertion, deletion and copying. We need to output minimum time to write N characters on the screen using these operations.

Examples:

Input : N = 9    
        insert time = 1    
        removal time = 2    
        copy time = 1
Output : 5
N character can be written on screen in 5 time units as shown below,
insert a character    
characters = 1  total time = 1
again insert character      
characters = 2  total time = 2
copy characters             
characters = 4  total time = 3
copy characters             
characters = 8  total time = 4
insert character           
characters = 9  total time = 5

[+]Temporal marker            : Acceptable timeFrame, Didn't Tether
[+]Temporal marker untethered : N/A
[+]Tread speed                : Relaxed
[+]Comments                   : working recurrence solution in first attempt,
                                slight hiccup of initializing dp[1], previously
                                set to dp[0]=1 --> dp[0] = iCost
[+]LINK                       : https://www.geeksforgeeks.org/minimum-time-write-characters-using-insert-delete-copy-operation/
"""

def findSolution(n, iCost, cCost, rCost):
    dp = [0]*(n+1)
    dp[1] = iCost
    for i in range(2, n+1):
        half = int(i/2)
        insert = dp[i-1]+ iCost
        copy  = dp[half] + cCost + (iCost*(i-(half*2)))
        remove = dp[half+1] + cCost + (rCost*(((half+1)*2)-i))
        dp[i] = min(insert, copy, remove)
        #print(dp)
    return dp[n]

n = 90
iCost = 4
cCost = 5
rCost = 2
print(findSolution(n, iCost, cCost, rCost))
    
