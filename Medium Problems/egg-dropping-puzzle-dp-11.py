"""
#M.14

Egg Dropping Puzzle | DP-11
The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with k=36 floors.
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

…..An egg that survives a fall can be used again.
…..A broken egg must be discarded.
…..The effect of a fall is the same for all eggs.
…..If an egg breaks when dropped, then it would break if dropped from a higher floor.
…..If an egg survives a fall then it would survive a shorter fall.
…..It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg to break.

If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the least number of egg-droppings that is guaranteed to work in all cases?
The problem is not actually to find the critical floor, but merely to decide floors from which eggs should be dropped so that total number of trials are minimized.

Source: Wiki for Dynamic Programming

[+]Temporal marker            : N/A,  | Friday, Sept06, 19
[+]Temporal marker untethered : N/A, Couple of days | Sunday, Sept08, 19
[+]Comments                   : Took couple of days
                                Solution from GFG Video explanation
                                Implementation took about 10-15 minutes for both R* & DP* inclusive
                                Topic Closed
[+]Tread speed                : Relaxed
[+]Level                      : Hard
[+]LINK                       : https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
"""

import PrintMatrix as pm
import math

def findSolutionDP(floors, eggs):
     #init
     dp = [[0]*(eggs+1) for x in range(floors+1)]
     for floor in range(floors+1):
         dp[floor][0] = 0
         dp[floor][1] = floor

     for floor in range(1, floors+1):
         for egg in range(2, eggs+1):
             res = floor
             for x in range(1, floor+1):
                 res = min(res, max(dp[x-1][egg-1], dp[floor-x][egg]))
             dp[floor][egg] = res+1
     return dp[floor][egg]

#S-Complexity: O(Floors*eggs) | T-Complexity: O(Floors*eggs*Floors)
def findSolutionRDP(floors,eggs, dp):
    if(eggs==1):
        return floors
    if(floors==1 or floors==0):
        return 1
    if(dp[floors][eggs]==-1):
        res = floors
        for x in range(2, floors+1):
            temp = (max(findSolutionRDP(x-1, eggs-1, dp), findSolutionRDP(floors-x, eggs, dp)))
            res = min(res, temp)
        dp[floors][eggs] = res+1
    return dp[floors][eggs]


def findSolutionR(floors,eggs):
    if(eggs==1):
        return floors
    if(floors==1 or floors==0):
        return 1
    res = floors
    for x in range(2, floors+1):
        temp = (max(findSolutionR(x-1, eggs-1), findSolutionR(floors-x, eggs)))
        res = min(res, temp)
    return res+1

if __name__ == "__main__":
    #lis = [floor, eggs]
    lis = [1096, 2]
    dp = [[-1]*(lis[1]+1) for x in range(lis[0]+1)]
    print(findSolutionDP(lis[0], lis[1]))
    print("finding solution using recursive dynamic approach...\n>> ")
    print(findSolutionRDP(lis[0], lis[1], dp))
    print("Finding solution using pure recursive approach...\n>> ")
    print(findSolutionR(lis[0], lis[1]))
    
