"""
#89
Count ways to divide circle using N non-intersecting chords
Given a number N, find the number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.

Examples:

Input : N = 2
Output : 2
Explanation: If points are numbered 1 to 4 in 
clockwise direction, then different ways to 
draw chords are:
{(1-2), (3-4)} and {(1-4), (2-3)}


Input : N = 1
Output : 1
Explanation: Draw a chord between points 1 and 2.

[+]Temporal marker            : Didn't Tether | Wednesday, Sept04, 19
[+]Temporal marker untethered : N/A Took about an hour | Sept03, 2019, Tuesday
[+]Comments                   : Well it was laid off for a couple of days, was very hard to look
                                at the first glance, battled with today once again after completing
                                #106 prob yesterday. Tried something like kadane's algo, coin change
                                paradigm was also considered, then i drew graphics for test cases and
                                this simple logic struck me. Two chords will intersect when there are
                                odd points lying in between the endpoints of a chords. Had two loops
                                just like kadane's algo and implemented it and Voila!! after an hour
                                of implementation if finally worked like charm. Had some trouble in
                                passing the parameter input. GFG algo was working for n while mine for
                                n*2, anyways fixed it in a matter of couple of minutes.
                                TOPIC IS NOW CLOSED!!!! :D
[+]Level                      : Medium
[+]LINK                       : https://www.geeksforgeeks.org/count-ways-divide-circle-using-n-non-intersecting-chords/
"""

def findSolution(chords):
    dp = [0]*(chords+3)
    #init
    dp[0] = 1
    dp[2] = 1
    for x in range(4, chords+1,2):
        for y in range(1, x):
            diff = y-1
            if(diff%2==0):
                dp[x]+=dp[x-y-1]*dp[y-1]
    return dp[chords]

if __name__ == "__main__":
    chords = 5
    print(findSolution(chords*2))
