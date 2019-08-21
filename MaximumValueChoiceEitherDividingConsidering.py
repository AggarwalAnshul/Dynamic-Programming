"""
Maximum value with the choice of either dividing or considering as it is
We are given a number n, we need to find the maximum sum possible with the help
of following function:
F(n) = max( (F(n/2) + F(n/3) + F(n/4) + F(n/5)), n).
To calculate F(n, ) we may either have n as our result or we can further break
n into four part as in given function definition. This can be done as much time
as we can. Find the maximum possible sum you can get from a given N.
Note : 1 can not be break further so F(1) = 1 as a base case.

Temporal Marker: 14:19 Hours | Aug21, Wednesday
Temporal Marker Untethered: 14:22 Hours | Aug21, Wednesday
LINK: https://www.geeksforgeeks.org/maximum-value-choice-either-dividing-considering/
"""


def findMaximumValueChoiceEitherDividingConsidering(number):
    dp = [0]*(number+1)
    dp[1] = 1

    for i in range(2, number+1):
        a = int(i/2)
        b = int(i/3)
        c = int(i/4)
        d = int(i/5)
        computedValue = max(a, dp[a])+max(b, dp[b])+max(c, dp[c])+max(d, dp[d])
        dp[i] = max(i, computedValue)

    return dp[number]


number = 6589
print(findMaximumValueChoiceEitherDividingConsidering(number))
