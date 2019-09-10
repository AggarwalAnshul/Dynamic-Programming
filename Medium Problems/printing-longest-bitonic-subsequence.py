"""
#M.28Printing Longest Bitonic Subsequence
The Longest Bitonic Subsequence problem is to find the longest subsequence of a given sequence such that it is first increasing and then decreasing. A sequence, sorted in increasing order is considered Bitonic with the decreasing part as empty. Similarly, decreasing order sequence is considered Bitonic with the increasing part as empty.

Examples:

Input:  [1, 11, 2, 10, 4, 5, 2, 1]
Output: [1, 2, 10, 4, 2, 1] OR [1, 11, 10, 5, 2, 1] 
	OR [1, 2, 4, 5, 2, 1]

Input:  [12, 11, 40, 5, 3, 1]
Output: [12, 11, 5, 3, 1] OR [12, 40, 5, 3, 1]

Input:  [80, 60, 30, 40, 20, 10]
Output: [80, 60, 30, 20, 10] OR [80, 60, 40, 20, 10]

[+]Temporal marker            : 15:33  Hours, | Tuesday Sept10, 19
[+]Temporal marker untethered : 15:40  Hours  | Tuesday Sept10, 19
[+]Comments                   : *Approach was clear what to do
                                *Just implemented
[+]Tread speed                : Paced
[+]Level                      : Easy
[+]LINK                       : https://www.geeksforg eeks.org/printing-longest-bitonic-subsequence/
"""
def printSeq(dp, index, lis, line, rev):
    count = dp[line][index][0]
    while(count>0):
        if(line==0):
            rev.insert(0, lis[index])
        else:
            rev.append(lis[index])
        index = dp[line][index][1]
        count-=1
    return rev
    
 
#S-Complexity: O(n) | T-Complexity: O(n) 
def findSolution(lis):
    length = len(lis)
    dp = [[[1, -1] for y in range(length)] for x in range(2)]
       
    #increasing
    index = 0
    for x in range(1, length):
        localMax = [0,-1]
        for j in range(x):
            if(lis[j]<lis[x]):
                if(localMax[0]<dp[0][j][0]):
                    localMax[0] = dp[0][j][0]
                    localMax[1] = j
        dp[0][x] = [localMax[0]+1, localMax[1]]
        if(dp[0][x][0]>dp[0][index][0]):
            index = x

    #Decreasing
    for x in range(length-2, -1, -1):
        localMax = [0,-1]
        for j in range(x+1, length, 1):
            if(lis[j]<lis[x]):
                if(localMax[0]<dp[1][j][0]):
                    localMax[0] = dp[1][j][0]
                    localMax[1] = j
        dp[1][x] = [localMax[0]+1, localMax[1]]
        if(dp[1][x][0]>dp[1][index][0]):
            index = x


    #Analyzing
    localMax = 0
    for x  in range(length):
        temp = dp[0][x][0] + dp[1][x][0]
        if(localMax < temp):
            localMax = temp
            index = x
    #printing from the index:
    rev = []
    rev = printSeq(dp, index, lis,0, rev)
    rev.pop()
    rev = printSeq(dp, index, lis,1, rev)
    print(rev)
    return localMax-1
"""
"""
if __name__ == "__main__":
    lis = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    lis = [80, 60, 30, 40, 20, 10]
    lis = [1, 11, 2, 10, 4, 5, 2, 1]
    lis = [12, 11, 40, 5, 3, 1]
   
    print(findSolution(lis))
