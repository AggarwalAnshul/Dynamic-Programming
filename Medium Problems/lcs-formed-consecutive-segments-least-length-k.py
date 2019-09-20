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

def printLCSOp(dp, one, two, k):
    i = 1
    j = 1
    lcs = ""
    count = 0
    ans = 0
    print("K: " +str(k))
    while(i<len(dp) and j<len(dp[0])):
        if(one[i-1]==two[j-1]):
            lcs = lcs+one[i-1]
            count+=1
            i+=1
            j+=1
        
def printLCS(dp, one, two, k):
    i = len(dp)-1
    j = len(dp[0])-1
    lcs = ""
    count = 0
    ans = 0
    print("K: "+str(k))
    while(i>0 and j>0):
        if(one[i-1]==two[j-1]):
            lcs = one[i-1]+lcs
            count+=1
            #print(one[i-1], end="\t")
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            if(count>=k):
                ans+=count
                count = 0
            i-=1
        else:
           if(count>=k):
               ans += count
               count = 0
           j-=1
        print("i: "+str(i)+" j: "+str(j)+" count: "+str(count)+" ans: "+str(ans))
    if(count>=k):
        ans+=count-1
    print("Ans: "+str(ans))
    print("LCS is: " + str(lcs))
    return lcs

def findSolutionR(one, two, i, j, k, count, last, ans):
    if(count==k):
        ans += count
        count = 0
    if(last==0):
        count = 0
    if(i<len(one) and  j<len(two)):
        return ans
    if(one[i]==two[j]):
        return max(findSolutionR(one, two, i+1, j+1, k,  count+1, 1, ans),
                   findSolutionR(one, two, i, j+1,k, count, 0, ans),
                   findSolutionR(one, two, i+1, j, k, count, 0, ans))
    else:
        return max(findSolutionR(one, two, i, j+1, k,count, 0, ans),
                   findSolutionR(one, two, i+1, j, k,count, 0, ans))
    
    
def findSolution(one, two, k):
    lenOne = len(one)
    lenTwo = len(two)
    count = 0
    dp = [[0]*(lenOne+1) for x in range(lenTwo+2)]
    #extra row at the bottom to count for the longest cosecutive chain of subsequence

    for i in range(1, lenTwo+1):
        for j in range(1, lenOne+1):
            if(two[i-1]==one[j-1]):
                if(i>1 and j>1 and one[j-2]!=two[i-2]):
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]+1
            #count for the chain
            if(dp[i][j]<k and dp[i-1][j-1]>=k):
                count+=dp[i-1][j-1]
                print("increasing the count to: "+str(count)+ " at i: "+str(i)+" j: "+str(j))
    #iterating for the final row
    for j in range(1, lenOne+1):
        if(dp[lenTwo+1][j]<k and dp[lenTwo+1-1][j-1]>=k):
            count+=dp[lenTwo+1-1][j-1]
    import PrintMatrix as pm
    pm.printss(dp, one, two+" ")
    print("The count is: "+str(count))





    
def findSolutionOb(one, two, k):
    lenOne = len(one)
    lenTwo = len(two)
    dp = [[0]*(lenOne+1) for x in range(lenTwo+1)]
    count = 0
    for i in range(1, lenTwo+1):
        for j in range(1, lenOne+1):
            if(one[j-1]==two[i-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                """
            if(one[j-1]==two[i-1]):
                if(j-2>=0 and i-2>=0 and two[i-2]!=one[j-2]):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1]+1
                    dp[i-1][j-1] = 0
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                """
    import PrintMatrix as pm
    pm.printss(dp, one, two)
    print("the count is: "+str(count))
    printLCS(dp, two, one, k)
if __name__ == "__main__":
    lis = ["aggasdfa", "aggajasdfaxy", 5]
    lis = ["aggajxaaasdfa", "aggayxysdfa", 4]
    lis = ["aggasdfa", "aggajasdfaxy", 4]
    lis = ["aabcaaaa", "baaabcd", 3]
    lis = ["aggasdfa", "aggajasdfa", 4]
    print(findSolutionOb(lis[0], lis[1], lis[2]))
    print(findSolutionR(lis[0],  lis[1], 4, 0, 0, 0, 0, 0))
    #print("LCIS: "+str(findSolutionOb(lis[0], lis[1], lis[2])))
