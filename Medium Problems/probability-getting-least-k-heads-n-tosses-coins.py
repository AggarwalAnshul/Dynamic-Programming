#M.67

"""
Probability of getting at least K heads in N tosses of Coins
Given N number of coins, the task is to find probability of getting at least K number of heads after tossing all the N coins simultaneously.

Example :

Suppose we have 3 unbiased coins and we have to
find the probability of getting at least 2 heads,
so there are 23 = 8 ways to toss these
coins, i.e.,
HHH, HHT, HTH, HTT, THH, THT, TTH, TTT

Out of which there are 4 set which contain at
least 2 Heads i.e.,
HHH, HHT, HH, THH

So the probability is 4/8 or 0.5


[+]Temporal marker            :  Tue, 12:17 | Sep 24, 19
[+]Temporal marker untethered :  Tue, 14:25 | Sep 24, 19
[+]Comments                   : *Mine dp solution was termed Naive by GFG, stating it will overflow
                                *however it is correct (30 Mins)
                                *A new approach was given using logarithmic solution, that relly
                                *opened the avenues of mind, took almost 1.5 hours to understand
                                *and fully implemented
                                *Problem is closed now
[+]Level                      : Medium
[+]Tread speed                : Steady / Intermittent
[+]LINK                       : https://www.geeksforgeeks.org/probability-getting-least-k-heads-n-tosses-coins
"""
import math
def findSolution(coins, heads):
    dp = [0.0]*(coins+1)
    dp[1] = math.log(1)
    for i in range(2, coins+1):
        dp[i] = dp[i-1] + math.log(i, 2)
    temp = 0
    for i in range(heads, coins+1):
        temp += 2**(dp[coins] - dp[coins-i] - dp[i] - coins)
    return temp

def findFactorial(num, dp):
    fact = 1
    if(dp[num]==0):
        for i in range(1, num+1):
            fact *= i
        dp[num] = fact
    return dp

def findPermutation(N, r, dp):
    if(dp[N]==0):
        dp = findFactorial(N, dp)
    if(dp[r]==0):
        dp  = findFactorial(r, dp)
    if(dp[N-r]==0):
        dp = findFactorial(N-r, dp)

    #print("returning: "+str(int(dp[N]/(dp[r]*dp[N-r]))))
    return int(dp[N]/(dp[r]*dp[N-r]))

def findSolutionObsolete(coins, heads):
    dp = [0]*(coins+1)
    temp = 0
    for i in range(0, heads):
        temp  += findPermutation(coins, i, dp)
    total_combinations = int(2**coins)
    return round(1-(temp/total_combinations),5)

if __name__ == "__main__":
    lis = [3, 2]
    lis = [6, 3]
    lis = [18, 12]
    print("probability is :"+str(findSolution(lis[0], lis[1])))
    print("probability is :"+str(findSolutionObsolete(lis[0], lis[1])))



