"""
#83
Count ways to build street under given constraints
There is a street of length n and as we know it has two sides. Therefore a total of 2 * n spots are available. In each of these spots either a house or an office can be built with following 2 restrictions:
1. No two offices on the same side of the street can be adjacent.
2. No two offices on different sides of the street can be exactly opposite to each other i.e. they can’t overlook each other.
There are no restrictions on building houses and each spot must either have a house or office.
Given length of the street n, find total number of ways to build the street.

Examples:

Input : 2
Output : 7
Please see below diagram for explanation.

Input : 3
Output : 17

[+]Temporal marker            : 10:09 Hours | Aug28, 2019
[+]Temporal marker untethered : 10:29 Hours | Aug28, 2019
[+]Tread speed                : Relaxed
[+]Comments                   : So glad I figured this out with absolutely no help
                                from GFG. Employed the, learned technique of breaking
                                the problem into subproblems, in this case particularly
                                the techinuqe of cutting the structure by one faction at
                                a time!!!! :D
[+]LINK : https://www.geeksforgeeks.org/ount-ways-build-street-given-constraints/

"""
#S-Complexity: O(n) | T-Complexity: O(n)
def findCountWaysBuildStreetGivenConstraints(num):
    dp = [[0]*3 for x in range(num+1)]
    dp[1] = [1,1,1]

    for x in range(2, num+1):
        dp[x][0] = dp[x-1][1] + dp[x-1][2]     #When there is an office in 1st lane
        dp[x][1] = dp[x-1][0] + dp[x-1][2]     #When there is an office in 2nd lane
        dp[x][2] = dp[x-1][0] + dp[x-1][1] + dp[x-1][2] #When there is no office in neither one

    return dp[num][0]+dp[num][1]+dp[num][2]

#S-Complexity: O(n) | T-Complexity: O(n)
def findCountWaysBuildStreetGivenConstraintsS(num):
    dp = [[0]*2 for x in range(num+1)]
    dp[1] = [2,1]

    for x in range(2, num+1):
        dp[x][0] = dp[x-1][0] + 2*(dp[x-1][1]) #When there is an office in either lane
        dp[x][1] = dp[x-1][0] + dp[x-1][1]     #When there is no office in neither lane
       
    return dp[num][0]+dp[num][1]

if __name__ == "__main__":
    num = 2
    num = 4
    num = 5
    print(findCountWaysBuildStreetGivenConstraintsS(num))

