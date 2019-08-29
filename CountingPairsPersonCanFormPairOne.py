"""
#85
Counting pairs when a person can form pair with at most one
Consider a coding competition on geeksforgeeks practice. Now their are n distinct participants taking part in the competition. A single participant can make pair with at most one other participant. We need count the number of ways in which n participants participating in the coding competition.

Examples :

Input : n = 2
Output : 2
2 shows that either both participant 
can pair themselves in one way or both 
of them can remain single.

Input : n = 3 
Output : 4
One way : Three participants remain single
Three More Ways : [(1, 2)(3)], [(1), (2,3)]
and [(1,3)(2)]

[+]Temporal marker            : N/A | Aug28, 2019
[+]Temporal marker untethered : N/A | Aug29, 2019
[+]Tread speed                : Relaxed | Tensed | Paced
[+]Comments                   : Took almost an entire day just to crack this sneaky
                                little pesky problem. Tried all approaches but none worked.
                                Just when I was about to give up,  i read this line on GFG
                                "Every participant can either pair with another participant
                                or can remain single" & it struck me with a solution.
                                I Tried the old recursive way to form the relation on the basis
                                of tree branching and magically the solution was corect, All i
                                had to do at that point of time was just to store the
                                intermediate result and sell this solution as dP which merely
                                took about 3 minutes.
                                Hence I finally came up with solution on my own!
                                
[+]LINK : https://www.geeksforgeeks.org/counting-pairs-person-can-form-pair-one/
"""
#S-Complexity: O(n) | T-Complexity: O(n)
def findCountingPairsPersonCanFormPairOne(num):
    dp = [-1]*(num+3)
    dp[0] = 1
    dp[1] = 1

    for x in range(2, num+1):
        dp[x] = (x-1)*dp[x-2] + dp[x-1]
    return dp[num]

if __name__ == "__main__":
    num = 8
    print(findCountingPairsPersonCanFormPairOne(num))
