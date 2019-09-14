"""
#M.37
Shortest Common Supersequence
Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
Examples :

Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB"

[+]Temporal marker            : 12:40  Hours, | Thursday  Sept12, 19
[+]Temporal marker untethered : 14: 00 Hours  | Thursday  Sept12, 19
[+]Comments                   : Took a couple of hour
                                Developed the recursive algo on my own
                                Recursion looks good
                                Later saw the easier DP Approach
                                MindBlowing approach Truly!
                                FUN Fact is GFG only provides length of soln
                                My Algo provides the string too just like example
                                problem is now solved completely:D 
[+]Level                      : Medium
[+]Tread speead               : Relaxed / Paced
[+]LINK                       : https://www.geeksforg eeks.org/shortest-common-supersequence/
"""

def findSolutionDP(one, two):
    print(one, "\t", two)
    dp = [[0]*(len(two)+1) for x in range(len(one)+1)]
    for i in range(1, len(one)+1):
        for j in range(1, len(two)+1):
            if(one[i-1]==two[j-1]):
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #Printing the lcs
    i = len(one)
    j = len(two)
    lcs = ""
    import PrintMatrix as pm
    pm.printss(dp, two, one)
    while(i>0 and j>0):
        if(one[i-1]==two[j-1]):
            lcs += one[i-1]
            i-=1
            j-=1
        else:
            if(dp[i-1][j]>dp[i][j-1]):
                i-=1
            else:
                j-=1
    print("lcs: "+lcs[::-1])

    #finding the solution
    index = 0
    left = ""
    for x in reversed(one):
        if(index<len(lcs) and x==lcs[index]):
                index+=1
        else:
            left+=x

    return left[::-1]+two

   
def findSolution(one, two, x, y, cost, string):
    #print(string+" cost: "+str(cost))
    #print("x: "+str(x)+ " y: "+str(y)+ " cost: "+str(cost))
    if(x>len(one)-1 and y<len(two)):
        return [cost+len(two)-y, string+two[y:]]
    if(y>=len(two)):
        return [cost, string]
    if(one[x]==two[y]):
        a = findSolution(one, two, x+1, y+1, cost, string+one[x])
        b = findSolution(one, two, x+1, y, cost+1, string+one[x])
        if(a[0]<b[0]):
            return a
        return b
    #print("compromising...>>>")
    a = findSolution(one, two, x+1, y+1, cost+1,string+one[x]+two[y])
    c = findSolution(one, two, x, y+1, cost+1,string+two[y])
    b = findSolution(one, two, x+1, y, cost, string+one[x])
    if(a[0]<b[0] and a[0]<c[0]):
        return a
    elif(c[0]<a[0] and c[0]<b[0]):
        return c
    return b

if __name__ == "__main__":
    lis = ["geek","eke"]
    lis = ["AGGTAB", "GXTXAYB"]
    
    print(findSolutionDP(lis[0], lis[1]))
    print(findSolution(lis[0], lis[1], 0, 0, 0,""))
    """
    if(len(lis[1])>len(lis[0])):
        lis[0],lis[1] = lis[1],lis[0]
    print(findSolution(lis[0], lis[1], 0, 0, 0,""))
    """
