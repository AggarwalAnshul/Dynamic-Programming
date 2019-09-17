"""
#M.43
Count distinct occurrences as a subsequence
Given a two strings S and T, find count of distinct occurrences of T in S as a subsequence.

Examples:

Input  : S = banana, T = ban
Output : 3
T appears in S as below three subsequences.
[ban], [ba  n], [b   an]

Input  : S = geeksforgeeks, T = ge
Output : 6
T appears in S as below three subsequences.
[ge], [     ge], [g e], [g    e] [g     e]
and [     g e]


[+]Temporal marker            : 11:03, | Monday Sept16, 19
[+]Temporal marker untethered : 10:13(R*) 11:30(DP*)  | Monday Sept16, 19
[+]Comments                   : *Recursive Solution in record time
                                *DP Solution developed within acceptable timeFrame
                                *Matter closed now.
[+]Level                      : Easy
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforgeeks.org/count-distinct-occurrences-as-a-subsequence/
"""

def findSolutionDP(s, t):
    lenS = len(s)
    lenT = len(t)
    #init
    dp = [[0]*(lenS+1) for x in range(lenT+1)]
    dp[lenT] = [1]*(lenS+1)

    for i in range(lenT-1, -1, -1):
        for j in range(lenS-1, -1, -1):
            dp[i][j] = dp[i][j+1]
            if(t[i]==s[j]):
                dp[i][j] = dp[i+1][j+1] + dp[i][j+1]
   # import PrintMatrix as pm | THE PRINTING IS OFF, ZERO ROW AND COLUMN IS AT THE LAST THIS TIME
   # pm.printss(dp, s, t)
    return dp[0][0]
def findSolution(s, t):
    lenS = len(s)
    lenT = len(t)
    if(lenT==0):
        return 1
    if(lenS == 0):
        return 0
    one = 0 #When you include this ele in subsequence
    two = findSolution(s[1:], t)  #When you exclude this ele in subsequence0
    if(t[0]==s[0]):
        one = findSolution(s[1:], t[1:])
        return one+two
    return two
    
if __name__ == "__main__":
    lis = ["banana","ban"]
    lis = ["geeksforgeeks", "ge"]

    print(findSolutionDP(lis[0], lis[1]))
    print("computing recursive solution...")
    print(findSolution(lis[0], lis[1]))
