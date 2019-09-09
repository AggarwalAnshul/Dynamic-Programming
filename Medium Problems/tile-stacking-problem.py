"""
#M.18

Tile Stacking Problem
A stable tower of height n is a tower consisting of exactly n tiles of unit height stacked vertically in such a way, that no bigger tile is placed on a smaller tile. An example is shown below :

We have infinite number of tiles of sizes 1, 2, …, m. The task is calculate the number of different stable tower of height n that can be built from these tiles, with a restriction that you can use at most k tiles of each size in the tower.

Note: Two tower of height n are different if and only if there exists a height h (1 <= h <= n), such that the towers have tiles of different sizes at height h.

Examples:

Input : n = 3, m = 3, k = 1.
Output : 1
Possible sequences: { 1, 2, 3}. 
Hence answer is 1.

Input : n = 3, m = 3, k = 2.
Output : 7
{1, 1, 2}, {1, 1, 3}, {1, 2, 2},
{1, 2, 3}, {1, 3, 3}, {2, 2, 3}, 
{2, 3, 3}.

[+]Temporal marker            : N/A Hours,           | Monday Sept09, 19
[+]Temporal marker untethered : N/A About 1.5 Hours(R)  | Sunday, Sept08, 19
[+]Comments                   : Already had the apporach in my mind
                                Implementation took 15 mins max
                                All test cases passed
                                Don't feel a dynamic solution is requried
                                GFG Shows a DP Solution, However my solution has the same
                                complexity as theirs, so i'm not moving into unchartered territory unnecessarily
                                Consider the matter closed
                                Now realized branch solution is needed
                                DP Added now 
[+]Tread speed                : Relaxed
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforgeeks.org/tile-stacking-problem/
"""

def copy(lis, e):
    new = []
    for x in lis:
        new.append(x)
    new[e-1]-=1
    return new

def findSolutionDP(tiles, ranges, limits):
    new =  []
    for x in range(1, ranges+1):
        for y in range(limits):
            new.append(x)
    print(new)
    #init
    dp = [[0]*(ranges*limits) for x in range(tiles)]
    dp[0][ranges*limits-1] = 1
    for x in range(ranges*limits-2, -1, -1):
        dp[0][x] = dp[0][x+1]
        if(new[x]!=new[x+1]):
            dp[0][x]+=1

    for i in range(1, tiles):
        for j in range(ranges*limits-2, -1, -1):
            dp[i][j] = dp[i-1][j+1] + dp[i][j+1]
            if(new[j]==new[j-1]):
                dp[i][j] -= dp[i-1][j+2]

    import PrintMatrix as pm
    #pm.printss(dp)
    return dp[tiles-1][0]

    
def findSolution(tiles, lis, currTile, ranges,tab):
    #tab+="\t"
    #print(tab+" C: "+str(tiles)+" T: "+str(currTile)+" ranges:"+str(ranges))
    if(tiles<=0):
        return 1
    ret  = 0
    for x in lis:
        if(x>=currTile):
            if(ranges[x-1]>0):
                ret += findSolution(tiles-1, lis, x, copy(ranges, x),tab)
    return ret
if __name__ == "__main__":
    #lis = [tiles, ranges, limit]
    lis = [2, 3, 2]
    lis = [3, 3, 2]
    new = []
    for x in range(1, lis[1]+1):
        new.append(x)
    ranges = []
    for x in new:
        ranges.append(lis[2])
    print(findSolutionDP(lis[0], lis[1], lis[2]))
    print(findSolution(lis[0], new, 0, ranges,""))
