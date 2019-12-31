"""
#M.46

LCS formed by consecutive segments of at least length K
Given two strings s1, s2 and K, find the length of the longest subsequence
formed by consecutive segments of at least length K.

Examples:

Input : s1 = aggayxysdfa
        s2 = aggajxaaasdfa
         k = 4
Output : 8
Explanation: aggasdfa is the longest
subsequence that can be formed by taking
consecutive segments, minimum of length 4.
Here segments are "agga" and "sdfa" which
are of length 4 which is included in making
the longest subsequence.

Input : s1 = aggasdfa
        s2 = aggajasdfaxy
         k = 5
Output : 5

Input: s1 = "aabcaaaa"
       s2 = "baaabcd"
        k = 3
Output: 4
Explanation: "aabc" is the longest subsequence that
is formed by taking segment of minimum length 3.
The segment is of length 4.


[+]Temporal marker            : 17:48, | Tuesday Sept17, 19
[+]Temporal marker untethered : 12:40(R*) 11:30(DP*)  | Tuesday Sept17, 19
[+]Comments                   : *laid for a couple of days
                                *Tried for about an hour today Fri,20
                                *One step closer
                                *Laying off for now
[+]Level                      : Hard
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/lcs-formed-consecutive-segments-least-length-k/
"""

def findSolution(one, two, k):
    len_of_one = len(one)
    len_of_two = len(two)

    dp = [[0]*(len_of_two+1) for x in range(len_of_one+1)]
    aux = [0]*(len_of_two+1)

    last_big = 0
    row = 1
    for i in range(1, len_of_one+1):
        for j in range(1, len_of_two+1):
            if(one[i-1]==two[j-1]):
                if(i==1 or j==1 or one[i-2]==two[j-2]):
                    dp[i][j] = dp[i-1][j-1]+1
                    if(dp[i][j] >= k):
                        last_big = dp[i][j]
                        row = i
                        print("last_big is initiated..."+str(last_big))
                    aux[j] = aux[j-1] + 1
                    if(aux[j] >= k):
                        last_big = aux[j]
                else:
                    dp[i][j] = 1
                    if(row!=i):
                        dp[i][j] += last_big
                    aux[j] = last_big + 1
            else:
                pass
                #dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    import PrintMatrix as pm
    pm.printss(dp, two, one)
    print(aux)

    i = len_of_one
    j = len_of_two

    ans = ""
    while(i>0 and j>0):
        if(one[i-1]==two[j-1]):
            #print(one[i-1], end="")
            ans = one[i-1] + ans
            i-=1
            j-=1
        elif(dp[i-1][j] > dp[i][j-1]):
            i-=1
        else:
            j-=1
    return ans

if __name__ == "__main__":
    lis = ["aggasdfa", "aggajasdfa", 4]
    lis = ["aggasdfa", "aggajasdfaxy", 5]
    lis = ["aggajxaaasdfa", "aggayxysdfa", 4]
    lis = ["aabcaaaa", "baaabcd", 3]
    lis = ["aggasdfa", "aggajasdfaxy", 4]

    print(findSolution(lis[0], lis[1], lis[2]))
    #print(findSolutionOb(lis[0], lis[1], lis[2]))
    #print(findSolutionR(lis[0],  lis[1], 4, 0, 0, 0, 0, 0))
    #print("LCIS: "+str(findSolutionOb(lis[0], lis[1], lis[2])))
