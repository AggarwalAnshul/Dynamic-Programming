"""
#105
Value of continuous floor function : F(x) = F(floor(x/2)) + x
Given an array of positive integers. For every element x of array, we need to
find the value of continuous floor function defined as F(x) = F(floor(x/2)) + x,
where F(0) = 0.

Examples :-

Input : arr[] = {6, 8}
Output : 10 15

Explanation : F(6) = 6 + F(3)
                   = 6 + 3 + F(1)
                   = 6 + 3 + 1 + F(0)
                   = 10
Similarly F(8) = 15
[+]Temporal marker            : 18:17 Hours | Sept03, 2019, Tuesday
[+]Temporal marker untethered : 18:26 Hours |Sept03, 2019, Tuesday
[+]Comments                   : Recognized it as a coin change varation with rep
                                at the first glance, just implemented the soln
                                and performed necessary modifications
[+]Level                      : Easy                               
[+]LINK                       : https://www.geeksforgeeks.org/value-continuous-floor-function-fx-ffloorx2-x/
"""
import math
def functionF(x, dp):
    if(dp[x]==-1):
        dp[x] = functionF(math.floor(x/2), dp)[0]+x
    return (dp[x], dp)

def findSolution(lis):
    answer = []
    largest = max(lis)
    dp = [-1]*(largest+1)
    dp[0] = 0

    for x in lis:
        answer.append(functionF(x, dp)[0])
        dp = functionF(x, dp)[1]
    return answer

if __name__ == "__main__":
    lis = [6, 8]
    print(findSolution(lis))
