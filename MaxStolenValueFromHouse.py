"""
Find maximum possible stolen value from houses
There are n houses build in a line, each of which contains some value in it. A thief is going to steal the maximal value of these houses, but he can’t steal in two adjacent houses because owner of the stolen houses will tell his two neighbour left and right side. What is the maximum stolen value.
Examples:

Input  : hval[] = {6, 7, 1, 3, 8, 2, 4}
Output : 19
Thief will steal 6, 1, 8 and 4 from house.

Input  : hval[] = {5, 3, 4, 11, 2}
Output : 16
Thief will steal 5 and 11

[+]Temporal marker            : Didn't Tether+, Cleared in record time
[+]Temporal marker untethered : N/A
[+]Tread speed                : Relaxed
[+]Comments                   : Hit bulls eye in the very first attempt
[+]Link                       : https://www.geeksforgeeks.org/find-maximum-possible-stolen-value-houses/
"""

def findMaxStolenValueFromHouse(lis):
    length = len(lis)
    dp = [0]*(length+1)
    dp[0] = 0
    dp[1] = lis[0]
     
    for x in range(2, length+1):
        dp[x] = max(lis[x-1]+dp[x-2], dp[x-1])
        #print(dp)
    return dp[length]

hval = [6,7,1,3,8,2,4]
#hval = [5, 3, 4, 11, 2]
print(findMaxStolenValueFromHouse(hval))
